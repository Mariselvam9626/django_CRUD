from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import User
from django.contrib.auth.hashers import make_password



class UserCreate(APIView):                    #Creating class
    
    permission_classes = [IsAuthenticated]     #only login users are allowed

    
    def post(self,request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")
        location = request.data.get("location")

        if not username or not password:
            return Response({"error": "Username and Password required"}, status=status.HTTP_400_BAD_REQUEST)

        #   it is check for user exists
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
 

        # create user 
        user = User.objects.create_user(
            username=username, 
            email=email,
            password=password,
            location=location
        )

        return Response({
            "message": "User created successfully",
            "username": user.username,
            "email": user.email,
            "location": user.location
        }, status=status.HTTP_201_CREATED)
    
    def get(self,request):

        users = User.objects.all().values("id","username","email","location")
        return Response(users,status = status.HTTP_200_OK)
    
    def patch(self,request,id):
        
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({"error ": "User not found"},status=status.HTTP_404_NOT_FOUND)      
        
        username = request.data.get("username")
        email = request.data.get("email")

        if username :
            user.username = username
        if email :
            user.email = email

        user.save()        

        return Response({"message": "User updated successfully"}, status=status.HTTP_200_OK)
    
    def delete(self,request,id):
        
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({"error ": "User not found"},status=status.HTTP_404_NOT_FOUND)      
        
        user.delete()        
        
        return Response({"message": "User Deleted successfully"}, status=status.HTTP_200_OK)
 
 

from rest_framework_simplejwt.views import TokenObtainPairView

class LoginView(TokenObtainPairView):
    pass

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

class LogoutView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"message": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)  