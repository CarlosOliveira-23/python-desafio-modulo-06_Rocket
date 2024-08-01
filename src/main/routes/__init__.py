from flask import Flask
from src.routes.calculators import calculators_bp
from src.routes.calculator_4 import calculator_4_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(calculators_bp)
    app.register_blueprint(calculator_4_bp)
    return app

