from rest_framework import serializers
from results.models import Result


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = "__all__"

    def create(self, validated_data):
        result, _ = Result.objects.get_or_create(**validated_data)
        return result