from rest_framework import generics
from rest_framework.views import APIView, Response, Request, status
from rest_framework.authtoken.models import  Token
from django.contrib.auth import authenticate


from users.models import User
from users.serializers import LoginSerializer, UserSerializer

class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserIdView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    lookup_field = "user_id"
    
class UserIdDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    lookup_field = "user_id"
    
class LoginView(APIView):
    def post(self, request: Request):
        serialized = LoginSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        
        user: User = authenticate(**serialized.validated_data)
        
        if not user:
            return Response({"detail": "invalid email or password"}, status.HTTP_401_UNAUTHORIZED)
          
        token, _ = Token.objects.get_or_create(user=user)
        
        return Response({"token": token.key}, status.HTTP_200_OK)
    
class UserIdNumber(APIView):
    def get(self, request: Request, user_id:int):
        return Response(status.HTTP_200_OK)