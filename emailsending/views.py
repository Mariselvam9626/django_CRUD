from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView



class EmailSending(APIView):

    def post(self,request):
        
        email=request.data.get("email") 
        subject=request.data.get("subject")
        message=request.data.get("message")
 
        if not email or not subject or not message:
            return Response("All fields are required")

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email]   
        )
        return  Response("Email sent successfully")

