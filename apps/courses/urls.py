from django.urls import path
from .views import CourseListView

app_name = 'courses'

urlpatterns = [
    path('', CourseListView.as_view(), name='list'),
]