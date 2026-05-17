from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class MultiplicationTableAPIView(APIView):

    def post(self, request):

        number = request.data.get("number")

        if not number:

            return Response(
                {"error": "Number is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        number = int(number)

        table = []

        for i in range(1, 11):

            result = number * i

            table.append(
                f"{number} x {i} = {result}"
            )

        return Response({
            "number": number,
            "multiplication_table": table
        })