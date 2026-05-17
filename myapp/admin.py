from django.contrib import admin
from .models import Student   #import only model name here

admin.site.register(Student)   

# we can pass the data from api and admin page.
# after creating admin page create super user for Username,Password.
