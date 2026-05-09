from flask import Blueprint, request, jsonify
from services.diseases_service import get_top_5_diseases_by_state, get_top_5_diseases_by_city

disease_bp = Blueprint('disease_bp', __name__)

@disease_bp.route('/top-diseases/state', methods=['POST'])
def top_diseases_state():
    data = request.get_json()
    state_name = data.get('state')
    if not state_name:
        return jsonify({"error": "State name is required"}), 400
    result = get_top_5_diseases_by_state(state_name)
    return jsonify(result)

@disease_bp.route('/top-diseases/city', methods=['POST'])
def top_diseases_city():
    data = request.get_json()
    city_name = data.get('city')
    if not city_name:
        return jsonify({"error": "City name is required"}), 400
    result = get_top_5_diseases_by_city(city_name)
    return jsonify(result)
