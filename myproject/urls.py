"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (    # It is for Jwt Authentication
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),                                        # Admin Site 
    path('student/',include('myapp.urls')),                                 # App Site
    path('api/token/login/', TokenObtainPairView.as_view()),                # Login
    path('api/token/refresh/', TokenRefreshView.as_view()),                 # Refresh token
    path('', include('sentiment_analyzer.urls')),                           # sentiment_analyzer    
    path('calories/',include('calorie_finder.urls')),                       # calorie_finder
    path('maths/',include('math_app.urls')),                                # math_app
    path('calculator/',include('calculator.urls')),                         # calulator
    path('email/',include('emailsending.urls')),                            # Email sending
    # path('usercreation/',include('usercreation.urls')),                   # Usercreation
    path('orm/',include('orm_practice.urls')), 
    ]
