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
    lookup_field = "concurso"
