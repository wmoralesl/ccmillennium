from django.urls import path
from .views import PaymentsListView

app_name = 'payments'

urlpatterns = [
    path('', PaymentsListView.as_view(), name='list')
]