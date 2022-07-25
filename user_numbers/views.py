from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response, Request, status

from user_numbers.models import UserNumbersModel
from user_numbers.serializers import UserNumbersSerializer


class UserNumberIdView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, _: Request, id: str):
        try:
            numbers = get_object_or_404(UserNumbersModel, pk=id)
            serialized = UserNumbersSerializer(numbers)

            return Response(serialized.data, status.HTTP_200_OK)

        except Http404:
            return Response({"detail": "Numbers not found"}, status.HTTP_404_NOT_FOUND)


class UserNumberView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        serialized = UserNumbersSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.save()

        return Response(serialized.data, status.HTTP_201_CREATED)
