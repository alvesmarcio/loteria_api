from results.models import Result
from results.serializers import ResultSerializer

import requests
import json


class GetResultsFromAPI:
    url = "https://loteriascaixa-api.herokuapp.com/api/mega-sena"

    def get_results(self):
        response = requests.get(self.url)
        results = json.loads(response.text)

        for result in results:
            concurso = result["concurso"]
            day, month, year = result["data"].split("/")
            date = year + "-" + month + "-" + day
            bola1, bola2, bola3, bola4, bola5, bola6 = [
                int(bola) for bola in result["dezenas"]
            ]

            data = {concurso, date, bola1, bola2, bola3, bola4, bola5, bola6}
            serialized = ResultSerializer(**data)
            Result.objects.create(**serialized.data)


GetResultsFromAPI.get_results()
