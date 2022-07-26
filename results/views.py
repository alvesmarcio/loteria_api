from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.views import APIView, Request
from rest_framework.pagination import PageNumberPagination

from results.models import Result
from results.permissions import AdminPermission, ListOrAdminPermission
from results.serializers import ResultSerializer
from results.utils import GetResultsFromAPI

import requests
import json


class CreateView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ListOrAdminPermission]

    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class RetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ListOrAdminPermission]

    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    lookup_field = "concurso"


class GetListResultsView(APIView, PageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AdminPermission]

    def get(self, request: Request):
        results = Result.objects.all()
        serialized = ResultSerializer(results, many=True)

        url = "https://loteriascaixa-api.herokuapp.com/api/mega-sena"
        response = requests.get(url)
        results_ms = json.loads(response.text)

        if len(serialized.data) != len(results_ms):

            for result in results_ms:
                result = GetResultsFromAPI.get_results(self, result)

                serialized_result = ResultSerializer(data=result)
                serialized_result.is_valid(raise_exception=True)
                serialized_result.save()

            results = Result.objects.all()

        pagination = self.paginate_queryset(
            queryset=results, request=request, view=self
        )
        serialized = ResultSerializer(pagination, many=True)

        return self.get_paginated_response(serialized.data)
