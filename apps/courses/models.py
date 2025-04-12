from django.db import models

# Create your models here.
class Course(models.Model):
    banner = models.ImageField(upload_to='courses', null=True, blank=True)
    name = models.CharField(max_length=255)
    
    # Tarifas y pagos
    monthly_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Tarifa mensual del curso.")
    total_payments = models.PositiveIntegerField(null=True, blank=True, help_text="Número total de pagos mensuales.")
    enrollment_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Tarifa única de inscripción.")
    
    # Estado y visibilidad
    is_visible = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()
    
    class Meta:
        app_label = 'courses'

class Module(models.Model):
    name = models.CharField(max_length=256)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='module')

    def __str__(self):
        return f'{self.course.name} - {self.name}'
