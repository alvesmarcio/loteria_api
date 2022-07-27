from rest_framework import serializers, status
from results.models import Result
from rest_framework.views import Response

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = "__all__"

    def create(self, validated_data):
        result, _ = Result.objects.get_or_create(**validated_data)
        return result
    
    def update(self, instance: Result, validated_data: dict):
        non_updatable = {'concurso'}
        
        for key, value in validated_data.items():
            if key in non_updatable:
                continue

            setattr(instance, key, value)
            instance.save()
            
        return instance