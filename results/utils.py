class GetResultsFromAPI:
    def get_results(self, result):        
        concurso = result["concurso"]
        day, month, year = result["data"].split("/")
        data = year + "-" + month + "-" + day
        bola1, bola2, bola3, bola4, bola5, bola6 = [
            int(bola) for bola in result["dezenas"]
        ]
        info = {
            "concurso": concurso,
            "data": data,
            "bola1": bola1,
            "bola2": bola2,
            "bola3": bola3,
            "bola4": bola4,
            "bola5": bola5,
            "bola6": bola6,

        }
                        
        return info

