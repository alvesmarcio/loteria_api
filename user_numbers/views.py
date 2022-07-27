from django.http import Http404
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import RetrieveUpdateAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Request, Response, status

from user_numbers.models import UserNumbersModel
from user_numbers.serializers import UserNumbersSerializer
from user_numbers.utils import lucky


class UserNumberCreateView(GenericAPIView):
    serializer_class = UserNumbersSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        serialized = UserNumbersSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.save(user=request.user)

        return Response(serialized.data, status.HTTP_201_CREATED)

    def get(self, request: Request):
        try:
            adjacent = bool(request.query_params.get("adjacent", False))
            column = bool(request.query_params.get("column", False))
            spread = bool(request.query_params.get("spread", False))

            user_favorite_numbers = UserNumbersModel.objects.filter(
                user=request.user
            ).first()

            user_favorite_numbers_serialized = UserNumbersSerializer(
                user_favorite_numbers
            )
            # print(user_favorite_numbers_serialized.data["numbers"], "<<<<<<<<<<<<<<<<<<<<<<<<<,")
            if len(user_favorite_numbers_serialized.data["numbers"]) == 0:
                numbers = set()    
            else:
                numbers = {
                    int(number)
                    for number in user_favorite_numbers_serialized.data["numbers"].split(
                        ", "
                    )
                }
            draw_numbers = lucky(numbers, adjacent, column, spread)

            return Response(draw_numbers, status.HTTP_200_OK)

        except Http404:
            return Response({"detail": "Numbers not found"}, status.HTTP_404_NOT_FOUND)


class UserNumberIdView(RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = UserNumbersModel.objects.all()
    serializer_class = UserNumbersSerializer
    lookup_field = "id"
