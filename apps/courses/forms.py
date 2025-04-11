from django import forms
from courses.models import Course

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'monthly_fee', 'total_payments', 'enrollment_fee', 'photo']
