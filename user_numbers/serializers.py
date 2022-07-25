from rest_framework import serializers
from user_numbers.models import UserNumbersModel


class UserNumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNumbersModel
        fields = "__all__"
        read_only_fields = ["id"]

    def validate_numbers(self, value):
        for number in value.split(","):
            if not number.isdigit():
                raise serializers.ValidationError("Numbers must be digits")
            if int(number.strip()) < 1 or int(number.strip) > 60:
                raise serializers.ValidationError("Numbers must be between 01 and 60")
        return value
