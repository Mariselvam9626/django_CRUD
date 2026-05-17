from django.urls import path
from .views import calculator_api



urlpatterns = [
    path('calculate/', calculator_api),
    
    ]