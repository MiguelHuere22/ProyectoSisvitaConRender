from flask import Blueprint, jsonify
from model.test_amasc import TestAMASC
from utils.db import db
from schemas.test_amasc_schema import tests_amasc_schema

test_amasc_bp = Blueprint('test_amasc_bp', __name__)

@test_amasc_bp.route('/test_amasc/v1', methods=['GET'])
def getMensaje():
    result = {"data": 'Hola, Test AMASC'}
    return jsonify(result)

# -------------------------------------------------------------

@test_amasc_bp.route('/test_amasc/v1/listar', methods=['GET'])
def getTestAMASC():
    tests_amasc = TestAMASC.query.all()
    result = {
        "data": tests_amasc_schema.dump(tests_amasc),
        "status_code": 200,
        "msg": "Se recuperó la lista de Tests AMASC sin inconvenientes"
    }
    return jsonify(result), 200

