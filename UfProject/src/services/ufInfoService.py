from src.utils.response import ApiResponse
from src.utils.ufApi import InfoUf
import pandas as pd

class UfService:
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    
    def __init__(self):
        self.infoUfApi = InfoUf()
    
    def getYearMonthVariations(self, year):
        try:
        
            json_data = self.infoUfApi.InfoApi(year)
            
            df = pd.DataFrame(json_data['serie'])
            
            df['fecha'] = pd.to_datetime(df['fecha'])
            
            best = df['valor'].idxmax()
            worst = df['valor'].idxmin()
            
            # Filtrar las filas
            best_row = df.loc[best]
            worst_row = df.loc[worst]
            
            df = df.sort_values('fecha')
            df['mes'] = df['fecha'].dt.month
            
            variaciones = df.groupby(['mes']).agg(
                inicio=('valor', 'first'),
                fin=('valor', 'last')
            ).reset_index()
            
            variaciones['variacion'] = variaciones['fin'] - variaciones['inicio']
            variaciones['mes'] = variaciones['mes'].apply(lambda x: self.meses[x-1])	

            return {
                'data': variaciones[['mes', 'variacion']],
                'best_day': best_row.to_dict(),  # Convertir fila a diccionario
                'worst_day': worst_row.to_dict(),  # Convertir fila a diccionario
                'success': True
            }
        
        except Exception as e:
            return {'success': False, 'data': str(e)}