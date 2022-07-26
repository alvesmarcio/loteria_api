from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.views import APIView, Request, Response, status

from results.models import Result
from results.permissions import AdminPermission, ListOrAdminCreatePermission
from results.serializers import ResultSerializer
from results.utils import GetResultsFromAPI

import requests
import json


class CreateView(CreateAPIView):
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


class GetListResultsView(APIView):
    def get(self, _: Request):
        results = Result.objects.all()
        serialized = ResultSerializer(results, many=True)
        
        if len(serialized.data) == 0:
            url = "https://loteriascaixa-api.herokuapp.com/api/mega-sena"
            response = requests.get(url)
            results = json.loads(response.text)        

            for result in results:
                result = GetResultsFromAPI.get_results(self, result)

                serialized_result = ResultSerializer(data=result)
                serialized_result.is_valid(raise_exception=True)
                serialized_result.save()
        
            results = Result.objects.all()
            serialized = ResultSerializer(results, many=True)     
            

        return Response(serialized.data ,status.HTTP_200_OK)