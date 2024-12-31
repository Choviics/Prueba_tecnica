from flask import jsonify

def ApiResponse(success: bool, data, message: str, status: int):
    return jsonify({
        'success': success,
        'data': data,
        'message': message
    }), status