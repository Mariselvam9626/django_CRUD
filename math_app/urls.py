from django.urls import path
from .views import MultiplicationTableAPIView

urlpatterns = [

    path('multiplication-table/',MultiplicationTableAPIView.as_view()),
]