from django.urls import path
from .views import Orm_Practice

urlpatterns = [
    path('orm_practice/',Orm_Practice.as_view())
]