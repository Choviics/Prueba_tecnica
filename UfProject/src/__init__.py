from flask import Flask, request
from flask_cors import CORS

# Routes
from .routes import indexRoutes, ufApiResRoutes

app = Flask(__name__)

CORS(app, supports_credentials=True)

@app.before_request
def handle_options_request():
    if request.method == 'OPTIONS':
        response = app.response_class()
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
        response.headers.add('Access-Control-Allow-Methods', 'GET, OPTIONS')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response, 204


def init_app(config):
    # Configuration
    app.config.from_object(config)

    # Blueprints
    app.register_blueprint(indexRoutes.main, url_prefix='/')
    app.register_blueprint(ufApiResRoutes.main, url_prefix='/uf')

    return app