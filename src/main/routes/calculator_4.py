from flask import Blueprint, request, jsonify
from src.calculators.calculator_4 import Calculator4
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

calculator_4_bp = Blueprint('calculator_4', __name__)


@calculator_4_bp.route('/calculator_4', methods=['POST'])
def calculate_average():
    data = request.get_json()
    if not data or 'numbers' not in data:
        raise HttpUnprocessableEntityError("Lista de números não fornecida ou mal formatada!")

    calculator = Calculator4()
    result = calculator.calculate_average(data['numbers'])
    return jsonify(result)
