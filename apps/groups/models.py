from django.db import models
from django.conf import settings

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        limit_choices_to={'role': 'teacher'},
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    year = models.PositiveIntegerField()
    in_person = models.BooleanField(default=True)
    start_date = models.DateField()
    end_date = models.DateField()
    schedule = models.TimeField()  # Start time of the group
    hours_count = models.PositiveIntegerField()
    is_visible = models.BooleanField(default=True)
    course = models.ForeignKey(
        'courses.Course',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} ({self.year})'