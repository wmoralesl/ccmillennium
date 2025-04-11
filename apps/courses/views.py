from django.shortcuts import render
from django.views.generic import ListView, CreateView
from courses.models import Course
from courses.forms import CourseCreateForm
from django.urls import reverse, reverse_lazy

# Create your views here.

class CourseListView(ListView):
    model = Course
    template_name = 'courses/list_courses.html'
    context_object_name = 'courses'

class CourseCreateView(CreateView):
    model = Course
    form_class = CourseCreateForm
    template_name = 'courses/form_course.html'
    success_url = reverse_lazy('courses:list')