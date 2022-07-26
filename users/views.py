from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView, Response, Request, status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.contrib.auth import authenticate

from users.models import User
from users.permissions import IsAdminOrUser, UserPermission
from users.serializers import LoginSerializer, UserSerializer

# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi

class UserView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermission]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserIdView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    # @swagger_auto_schema()  
    def post(self, request: Request):

        serialized = LoginSerializer(data=request)
        serialized.is_valid(raise_exception=True)

        user: User = authenticate(**serialized.validated_data)

        if not user:
            return Response(
                {"detail": "invalid username or password"}, status.HTTP_401_UNAUTHORIZED
            )

        token, _ = Token.objects.get_or_create(user=user)

        return Response({"token": token.key}, status.HTTP_200_OK)
