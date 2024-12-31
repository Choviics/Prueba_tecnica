from flask import Blueprint, jsonify, request
import logging
from src.utils.response import ApiResponse

main = Blueprint('index_blueprint', __name__)

logging.basicConfig(level=logging.INFO)

@main.route('/', methods=['GET'])
def index():
    
    logging.info(f'Received {request.method} request at / with data: {request.data}')
    
    return ApiResponse(True, None, 'Pagina de inicio', 200)