from django.urls import path
from . import views

urlpatterns = [
    path('template/', views.template, name='template')
]
