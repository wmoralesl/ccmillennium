from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from courses.models import Course, Module
from courses.forms import CourseCreateForm
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json
from django.http import JsonResponse
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

class CourseEditView(UpdateView):
    model = Course
    form_class = CourseCreateForm
    template_name = 'courses/form_course.html'

    def get_success_url(self):
        return reverse('courses:view', kwargs={'pk': self.object.id})

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail_course.html'
    context_object_name = 'course'

# Modulos

# @csrf_exempt  # para pruebas, mejor usa CSRF token en producción
def actualizar_nombre_modulo(request, modulo_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        nuevo_nombre = data.get('nombre')
        if not nuevo_nombre:
            return JsonResponse({'error': 'El nombre es obligatorio'}, status=400)

        modulo = get_object_or_404(Module, id=modulo_id)
        print(modulo)
        modulo.name = nuevo_nombre
        print(modulo.name)
        modulo.save()

        return JsonResponse({'mensaje': 'Nombre actualizado correctamente'})
    else:
        
        return JsonResponse({'error': 'Método no permitido'}, status=405)