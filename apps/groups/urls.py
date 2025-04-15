
from django.urls import path
from groups.views import GroupListView

app_name = 'groups'
urlpatterns = [
    path('', GroupListView.as_view(), name ='list')
]