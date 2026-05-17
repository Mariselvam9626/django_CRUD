from .models import Students
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import StudentSerializer
from rest_framework import status


class Orm_Practice(APIView):

    def get(self,request):
        # data = {}
            
        students = Students.objects.all()
        # students = Students.objects.order_by("age")
        # students = Students.objects.filter(age=21)
        # students = Students.objects.values()

        serializer =  StudentSerializer(students,many=True)
        return Response({"Total members":students.count(),"Data ":serializer.data}) 
    
    def post(self,request): 
       
        serializer = StudentSerializer(data = request.data,many=True)
        # students = Students.objects.create(
        #             name="Mariselvam",
        #             age=21,
        #             salary=70000
        #             )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    