from django.shortcuts import render
from django.views.generic import ListView
from courses.models import Course
# Create your views here.

class CourseListView(ListView):
    model = Course
    template_name = 'courses/list_courses.html'
    context_object_name = 'courses'