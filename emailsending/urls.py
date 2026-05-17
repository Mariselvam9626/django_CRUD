from django.urls import path
from .views import EmailSending

urlpatterns= [
    path('emailsending/', EmailSending.as_view(), name="EmailSending"),
    

]