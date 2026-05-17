from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import CalculatorSerializer
from .models import Calculator


@api_view(['POST'])
def calculator_api(request):

    serializer = CalculatorSerializer(data=request.data)

    if serializer.is_valid():

        num1 = serializer.validated_data['num1']
        num2 = serializer.validated_data['num2']
        operation = serializer.validated_data['operation']

        if operation == "add":
            result = num1 + num2

        elif operation == "sub":
            result = num1 - num2

        elif operation == "mul":
            result = num1 * num2

        elif operation == "div":

            if num2 == 0:
                return Response(
                    {"error": "Cannot divide by zero"},
                    status=400
                )

            result = num1 / num2

        else:
            return Response(
                {"error": "Invalid operation"},
                status=400
            )

        # Save to database
        Calculator.objects.create(
            num1=num1,
            num2=num2,
            operation=operation,
            result=result
        )

        return Response(
            {
                "num1": num1,
                "num2": num2,
                "operation": operation,
                "result": result
            }
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )