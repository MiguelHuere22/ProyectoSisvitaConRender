from flask import Blueprint, jsonify
from model.test_zung import TestZung
from utils.db import db
from schemas.test_zung_schema import  tests_zung_schema

test_zung_bp = Blueprint('test_zung_bp', __name__)

@test_zung_bp.route('/test_zung/v1', methods=['GET'])
def getMensaje():
    result = {"data": 'Hola, Test Zung'}
    return jsonify(result)

# -------------------------------------------------------------

@test_zung_bp.route('/test_zung/v1/listar', methods=['GET'])
def getTestZung():
    tests_zung = TestZung.query.all()
    result = {
        "data": tests_zung_schema.dump(tests_zung),
        "status_code": 200,
        "msg": "Se recuperó la lista de Tests Zung sin inconvenientes"
    }
    return jsonify(result), 200
