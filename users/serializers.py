from dataclasses import fields
from rest_framework import serializers
from user_numbers.serializers import UserNumbersSerializer

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

        read_only_fields=["id", "created_at"]
    
    user_numbers = UserNumbersSerializer(many=True, read_only=True)
    
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")