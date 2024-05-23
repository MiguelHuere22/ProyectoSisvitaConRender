from flask import Blueprint, jsonify
from model.test_beck import TestBeck
from utils.db import db
from schemas.test_beck_schema import tests_beck_schema

test_beck_bp = Blueprint('test_beck_bp', __name__)

@test_beck_bp.route('/test_beck/v1', methods=['GET'])
def getMensaje():
    result = {"data": 'Hola, Test Beck'}
    return jsonify(result)

# -------------------------------------------------------------

@test_beck_bp.route('/test_beck/v1/listar', methods=['GET'])
def getTestBeck():
    tests_beck = TestBeck.query.all()
    result = {
        "data": tests_beck_schema.dump(tests_beck),
        "status_code": 200,
        "msg": "Se recuperó la lista de Tests Beck sin inconvenientes"
    }
    return jsonify(result), 200
