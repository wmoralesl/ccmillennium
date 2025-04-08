from django.urls import path
from .views import PrivateView

app_name = 'private'

urlpatterns = [
   path('', PrivateView.as_view(), name='home'),
]