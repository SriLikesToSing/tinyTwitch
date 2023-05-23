from django.urls import path
from . import views

urlpatterns = [
    path('testChat/', views.home, name='home')
]









