from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'



# ModelSerializer automatically converts Django model data into JSON and 
# validates incoming data. 
# JSON → Python object
# Python object → JSON
