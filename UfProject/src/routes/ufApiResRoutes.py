from flask import Blueprint, jsonify, request
from src.utils.response import ApiResponse
from src.services.ufInfoService import UfService
import json

main = Blueprint('uf_blueprint', __name__)

ufService = UfService()

year_variations_cache = {}

@main.route('/', methods=['GET'])
def getUfInfo():
    try:
        year = int(request.args.get('year'))
        
        if year in year_variations_cache:
            combined_data = {
                'months': json.loads(year_variations_cache[year]['data'].to_json(orient='records')),
                'best_day': year_variations_cache[year]['best_day'],
                'worst_day': year_variations_cache[year]['worst_day']
            }
            return ApiResponse(
                True, 
                combined_data, 
                'Uf obtenida con exito', 
                200
            )
        
        if not year or not (1977 <= year <= 2024):
            return ApiResponse(False, None, 'El año no es valido', 400)
        
        result = ufService.getYearMonthVariations(year)
        
        if not result['success']:
            return ApiResponse(False, None, result['data'], 404)
        
        year_variations_cache[year] = {}
        year_variations_cache[year]['data'] = result['data']
        year_variations_cache[year]['best_day'] = result['best_day']
        year_variations_cache[year]['worst_day'] = result['worst_day']
        
        combined_data = {
            'months': json.loads(result['data'].to_json(orient='records')),
            'best_day': result['best_day'],
            'worst_day': result['worst_day']
        }
                           
        return ApiResponse(True, 
                           combined_data,
                           'Uf obtenida con exito', 
                           200
                        )
    
    except Exception as e:
        return ApiResponse(False, None, str(e), 500)
    
@main.route('/asc', methods=['GET'])
def orderByAsc():
    try:
        year = int(request.args.get('year'))
        
        if not year or not (1977 <= year <= 2024):
            return ApiResponse(False, None, 'El año no es valido', 400)
        
        if year not in year_variations_cache:
            return ApiResponse(False, None, 'No se ha consultado el año', 404)
        
        data = year_variations_cache[year]['data']
        
        sorted_data = data[data['variacion']>0].sort_values(by='variacion', ascending=True)
        
        combined_data = {
                'months': json.loads(sorted_data.to_json(orient='records')),
                'best_day': year_variations_cache[year]['best_day'],
                'worst_day': year_variations_cache[year]['worst_day']
            }
        
        return ApiResponse(True, 
                           combined_data, 
                           'Uf ordenada de forma ascendente', 
                           200
                        )
    
    except Exception as e:
        return ApiResponse(False, None, str(e), 500)
    
@main.route('/desc', methods=['GET'])
def orderByDesc():
    try:
        year = int(request.args.get('year'))
        
        if not year or not (1977 <= year <= 2024):
            return ApiResponse(False, None, 'El año no es valido', 400)
        
        if year not in year_variations_cache:
            return ApiResponse(False, None, 'No se ha consultado el año', 404)
        
        data = year_variations_cache[year]['data']
        
        sorted_data = data[data['variacion']<0].sort_values(by='variacion', ascending=False)
        
        combined_data = {
                'months': json.loads(sorted_data.to_json(orient='records')),
                'best_day': year_variations_cache[year]['best_day'],
                'worst_day': year_variations_cache[year]['worst_day']
            }
        
        return ApiResponse(True, 
                           combined_data, 
                           'Uf ordenada de forma descendente', 
                           200
                        )
    
    except Exception as e:
        return ApiResponse(False, None, str(e), 500)
    
@main.route('/noavg', methods=['GET'])
def orderByDont():
    try:
        year = int(request.args.get('year'))
        
        if not year or not (1977 <= year <= 2024):
            return ApiResponse(False, None, 'El año no es valido', 400)
        
        if year not in year_variations_cache:
            return ApiResponse(False, None, 'No se ha consultado el año', 404)
        
        data = year_variations_cache[year]['data']
        
        sorted_data = data[data['variacion']==0].sort_values(by='mes')
        
        combined_data = {
                'months': json.loads(sorted_data.to_json(orient='records')),
                'best_day': year_variations_cache[year]['best_day'],
                'worst_day': year_variations_cache[year]['worst_day']
            }

        return ApiResponse(True, 
                           combined_data, 
                           'Uf que no tuvieron variacion', 
                           200
                        )
    
    except Exception as e:
        return ApiResponse(False, None, str(e), 500)