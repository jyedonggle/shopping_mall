from django.urls import path
from . import views

app_name = 'climey'

urlpatterns = [
    path('', views.index, name = 'index')
]