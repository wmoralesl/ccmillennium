from django.urls import path
from .views import CourseListView, CourseCreateView, CourseEditView, CourseDetailView, actualizar_nombre_modulo

app_name = 'courses'

urlpatterns = [
    path('', CourseListView.as_view(), name='list'),
    path('create/', CourseCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', CourseEditView.as_view(), name='edit'),
    path('view/<int:pk>/', CourseDetailView.as_view(), name='view'),
    path('modulo/<int:modulo_id>/actualizar-nombre/', actualizar_nombre_modulo, name='actualizar_nombre_modulo'),

]