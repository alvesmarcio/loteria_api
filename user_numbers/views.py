from rest_framework.views import APIView, Response, Request, status

from user_numbers.models import UserNumbersModel
from user_numbers.serializers import UserNumbersSerializer


class UserNumberView(APIView):
    def get(self, request: Request, id: str):

        numbers = UserNumbersModel.objects.all()

        serialized = UserNumbersSerializer(numbers, many=True)

        return Response(serialized.data, status.HTTP_200_OK)

    def post(self, requrest: Request):
        ...
