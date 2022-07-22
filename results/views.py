from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated

from results.models import Result
from results.permissions import AdminPermission
from results.serializers import ResultSerializer


class ListRetrieveView(ListAPIView, RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class CreateUpdateDestroyView(CreateAPIView, UpdateAPIView, DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AdminPermission]

    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    def perform_update(self, serializer):
        serializer.save(concurso=self.kwargs.get("pk"))

    def perform_destroy(self, instance):
        instance.delete()

    def perform_create(self, serializer):
        serializer.save(concurso=self.kwargs.get("pk"))
