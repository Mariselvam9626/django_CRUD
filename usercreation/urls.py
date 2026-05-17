from django.urls import path
from .views import UserCreate
from .views import LoginView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [    
    path('usercreate/',UserCreate.as_view()),      #POST, GET
    path('users/<int:id>/', UserCreate.as_view()), # PATCH, DELETE

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]