from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from courses.models import Course, Module
from courses.forms import CourseCreateForm
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, redirect
import json
from django.http import JsonResponse
from django.contrib import messages

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

    def form_valid(self, form):
        messages.success(self.request,'Se ha creado el curso correctamente')
        return super().form_valid(form)
    
class CourseEditView(UpdateView):
    model = Course
    form_class = CourseCreateForm
    template_name = 'courses/form_course.html'

    def get_success_url(self):
        messages.success(self.request, 'Se ha actualizado el curso correctamente')
        return reverse('courses:view', kwargs={'pk': self.object.id})
    
    

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail_course.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        path = self.request.path
        mipath = '/'.join(path.rstrip('/').split('/')[:-2]) + '/'
        context['mipath'] = mipath # Para hacer el fetch al api-url correcta
        return context

# Modulos

# @csrf_exempt  # para pruebas, mejor usa CSRF token en producción
def updateModule(request, module_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        nuevo_nombre = data.get('nombre')
        if not nuevo_nombre:
            return JsonResponse({'error': 'El nombre es obligatorio'}, status=400)

        modulo = get_object_or_404(Module, id=module_id)
        modulo.name = nuevo_nombre
        modulo.save()

        return JsonResponse({'mensaje': 'Nombre actualizado correctamente'})
    else:
        
        return JsonResponse({'error': 'Método no permitido'}, status=405)

def createModule(request, course_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        courser = get_object_or_404(Course, id=course_id)
        print(data)
        print(courser)
        Module.objects.create(name=data.get('name'), course=courser)
        messages.success(request, f"Modulo creado correctamente")
        return JsonResponse({'mensaje': 'Modulo creado correctamente'})
        # return redirect('courses:view', pk = course_id)

def deleteModule(request, course_id, module_id):
    if request.method == 'POST':
        module = get_object_or_404(Module, pk=module_id)
        module.delete()
        return redirect('courses:view', pk = course_id)
        

