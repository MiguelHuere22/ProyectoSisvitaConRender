from flask import Blueprint, request, jsonify
from model.test import Test
from utils.db import db
from schemas.test_schema import tests_schema

tests = Blueprint('tests', __name__)

@tests.route('/tests/v1', methods=['GET'])
def getMensaje():
    result = {
        "data": "Hola, tests"
    }
    return jsonify(result)

@tests.route('/tests/v1/listar', methods=['GET'])
def getTests():
    tests = Test.query.all()
    result = {
        "data": tests_schema.dump(tests),
        "status_code": 200,
        "msg": "Se recuperaron los tipos de tests sin inconvenientes"
    }
    return jsonify(result), 200

@tests.route('/tests/v1/agregar', methods=['POST'])
def agregarTest():
    data = request.json
    nuevo_test = Test(
        id_tipo_test=data['id_tipo_test'],
        tipo_test=data['tipo_test']
    )
    db.session.add(nuevo_test)
    db.session.commit()
    return test_schema.jsonify(nuevo_test), 201

@tests.route('/tests/v1/actualizar/<int:id>', methods=['PUT'])
def actualizarTest(id):
    data = request.json
    test = Test.query.get_or_404(id)
    test.id_tipo_test = data.get('id_tipo_test', test.id_tipo_test)
    test.tipo_test = data.get('tipo_test', test.tipo_test)
    db.session.commit()
    return test_schema.jsonify(test), 200

@tests.route('/tests/v1/eliminar/<int:id>', methods=['DELETE'])
def eliminarTest(id):
    test = Test.query.get_or_404(id)
    db.session.delete(test)
    db.session.commit()
    return jsonify({
        "status_code": 200,
        "msg": "Test eliminado exitosamente"
    }), 200
