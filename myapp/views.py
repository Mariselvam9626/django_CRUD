from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated


class StudentView(APIView):    #Its  for authentication class

    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "JWT Working"})

    
class Student_Crud(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):     # This method used to Get the Data From API

        # print(request)
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data)
            
    def post(self,request):       # Updating New Data

        serializer = StudentSerializer(data = request.data,many=True)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request):     # Update all fields
        
        student_id = request.GET.get("ids")
        student = Student.objects.get(id = student_id)
        serializer = StudentSerializer(student,data = request.data)
        
        if serializer.is_valid():      # checks datatype required fields max length
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status =  status.HTTP_400_BAD_REQUEST)
 
 # status= is used to send an HTTP status code in API responses.
    
    def delete(self,request,ids):   #its used to deleted the data completely that ID
        
        student = Student.objects.get(id = ids)
        student.delete()
        return Response({"Message":"Deleted Successfully"})
    