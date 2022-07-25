from rest_framework import serializers
from user_numbers.models import UserNumbersModel
from users.models import User


class UserNumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNumbersModel
        fields = "__all__"
        read_only_fields = ["id", "user"]

    def create(self, validated_data):
        user = validated_data.pop("user")
        user = User.objects.filter(id=user.id).first()
        return UserNumbersModel.objects.create(**validated_data, user=user)

    def validate_numbers(self, value):
        numbers = [number for number in value.split(", ")]
        for number in numbers:
            if not number.isdigit():
                raise serializers.ValidationError("Numbers must be digits")
            if int(number.strip()) < 1 or int(number.strip()) > 60:
                raise serializers.ValidationError("Numbers must be between 01 and 60")
        return value
