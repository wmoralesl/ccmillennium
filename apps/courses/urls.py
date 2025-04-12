from django.urls import path
from .views import CourseListView, CourseCreateView, CourseEditView, CourseDetailView, updateModule, createModule

app_name = 'courses'

urlpatterns = [
    path('', CourseListView.as_view(), name='list'),
    path('create/', CourseCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', CourseEditView.as_view(), name='edit'),
    path('view/<int:pk>/', CourseDetailView.as_view(), name='view'),
    path('module/<int:module_id>/update/', updateModule, name='update-module'),
    path('module/<int:course_id>/create/', createModule, name='create-module'),


]