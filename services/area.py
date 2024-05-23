from flask import Blueprint, request, jsonify
from model.area import Area
from utils.db import db
from schemas.area_schema import area_schema, areas_schema

areas = Blueprint('areas', __name__)

@areas.route('/areas/v1', methods=['GET'])
def getMensaje():
    result = {"data": 'Hola, Areas'}
    return jsonify(result)

@areas.route('/areas/v1/listar', methods=['GET'])
def getAreas():
    areas = Area.query.all()
    result = {
        "data": areas_schema.dump(areas),
        "status_code": 200,
        "msg": "Se recuperó la lista de Áreas sin inconvenientes"
    }
    return jsonify(result), 200

@areas.route('/areas/v1/agregar', methods=['POST'])
def agregarArea():
    data = request.json
    nueva_area = Area(nombre=data['nombre'])
    db.session.add(nueva_area)
    db.session.commit()
    return area_schema.jsonify(nueva_area), 201

@areas.route('/areas/v1/actualizar/<int:id>', methods=['PUT'])
def actualizarArea(id):
    data = request.json
    area = Area.query.get_or_404(id)
    area.nombre = data.get('nombre', area.nombre)
    db.session.commit()
    return area_schema.jsonify(area), 200

@areas.route('/areas/v1/eliminar/<int:id>', methods=['DELETE'])
def eliminarArea(id):
    area = Area.query.get_or_404(id)
    db.session.delete(area)
    db.session.commit()
    return jsonify({
        "status_code": 200,
        "msg": "Área eliminada exitosamente"
    }), 200
