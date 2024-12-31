import json
import requests
 
class InfoUf:
    
    def InfoApi(self, year):
        # En este caso hacemos la solicitud para el caso de consulta de un indicador en un año determinado
        url = f'https://mindicador.cl/api/uf/{year}'
        response = requests.get(url)
        data = json.loads(response.text.encode("utf-8"))
        return data