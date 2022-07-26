from rest_framework import serializers
from user_numbers.serializers import UserNumbersSerializer

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "last_login",
            "is_superuser",
            "first_name",
            "last_name",
            "is_staff",
            "is_active",
            "groups",
            "user_permissions",
            "date_joined",
        ]
        extra_kwargs = {"password": {"write_only": True}}
        read_only_fields = ["id", "created_at"]

    user_numbers = UserNumbersSerializer(read_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
