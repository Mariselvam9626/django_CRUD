from django.urls import path
from .views import FoodCaloriesAPIView

urlpatterns = [
    path('food-api/', FoodCaloriesAPIView.as_view()),
]