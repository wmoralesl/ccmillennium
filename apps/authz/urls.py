from django.urls import path
from .views import LoginView, link_logout

app_name = 'auth'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', link_logout, name='logout'),

]
