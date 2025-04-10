from django.db import models
from django.contrib.auth.models import AbstractUser
from .until import user_directory_path, generate_unique_username, validate_image

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Estudiante'),
        ('teacher', 'Maestro'),
        ('admin', 'Administrador'),
    )
    GENDER_CHOICES = (
        ('none', 'No especifica'),
        ('male', 'Hombre'),
        ('female', 'Mujer'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    second_last_name = models.CharField(max_length=255, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    dpi = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to=user_directory_path, null=True, blank=True, validators=[validate_image])  # Aquí se agrega el campo de imagen
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='none')
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    password = models.CharField(max_length=128, blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'second_last_name', 'role']

    def save(self, *args, **kwargs):
        # Obtener la instancia anterior antes de guardar
        try:
            old_user = User.objects.get(pk=self.pk)
        except User.DoesNotExist:
            old_user = None

        if not self.username:
            self.username = generate_unique_username(self)
        
        # Asignar el username como contraseña si no hay una contraseña establecida
        if not self.password:
            self.set_password(self.username)


        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name} {self.second_last_name}'
    
    def __str__(self):
        return f'**** {self.username} ***** {self.id} - {self.first_name} {self.last_name} {self.second_last_name}'
    
    class Meta:
        app_label = 'users'