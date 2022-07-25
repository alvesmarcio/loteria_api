from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from results.models import Result
from results.permissions import AdminPermission, ListOrAdminCreatePermission
from results.serializers import ResultSerializer


class ListCreateView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ListOrAdminCreatePermission]

    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class RetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
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
