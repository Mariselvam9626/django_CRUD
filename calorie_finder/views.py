from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

class FoodCaloriesAPIView(APIView):

    def post(self, request):

        food = request.data.get("food")

        if not food:
            return Response(
                {"error": "Food name is required"},
                status = status.HTTP_400_BAD_REQUEST
            )

        api_key = "55Fjio4U1paTWGPtrPCFig==KbM9mVw3qOR33ouP"

        api_url = f"https://api.api-ninjas.com/v1/nutrition?query={food}"

        api_request = requests.get(
            api_url,
            headers={"X-Api-Key": api_key}
        )

        if api_request.status_code == 200:

            api_data = api_request.json()
            # print(api_data)

            if api_data == []:
                return Response(
                    {"message": "This is not a valid food"},
                    status=status.HTTP_404_NOT_FOUND
                )

            parsed_data = api_data[0]

            return Response({
                "food_name": food.capitalize(),
                "calories": parsed_data.get("calories"),
                "protein_g": parsed_data.get("protein_g"),
                "fat_total_g": parsed_data.get("fat_total_g"),
                "carbohydrates_total_g": parsed_data.get("carbohydrates_total_g"),
                "fiber_g": parsed_data.get("fiber_g"),
                "sugar_g": parsed_data.get("sugar_g"),
                "sodium_mg": parsed_data.get("sodium_mg"),
                "potassium_mg": parsed_data.get("potassium_mg"),
                "serving_size_g": parsed_data.get("serving_size_g"),
            })

        return Response(
            {
                "error": "API request failed",
                "status_code": api_request.status_code,
                "details": api_request.text
            },
            status=status.HTTP_400_BAD_REQUEST
        )

        