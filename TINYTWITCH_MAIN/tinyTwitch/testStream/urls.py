from django.urls import path
from . import views

urlpatterns = [
        path('testStream/', views.testStream, name='testStream')
        
       ]
















