from flask import Blueprint, request, jsonify
from model.estudiante import Estudiante
from utils.db import db
from schemas.estudiante_schema import estudiantes_schema

estudiantes = Blueprint('estudiantes', __name__)

@estudiantes.route('/estudiantes/v1', methods=['GET'])
def getMensaje():
    result = {"data": 'Hola, estudiantes'}
    return jsonify(result)

# -------------------------------------------------------------

@estudiantes.route('/estudiantes/v1/listar', methods=['GET'])
def getEstudiantes():
    estudiantes = Estudiante.query.all()
    result = {
        "data": estudiantes_schema.dump(estudiantes),
        "status_code": 200,
        "msg": "Se recuperaron los estudiantes sin inconvenientes"
    }
    return jsonify(result), 200

# -------------------------------------------------------------

@estudiantes.route('/estudiantes/v1/agregar', methods=['POST'])
def agregarEstudiante():
    data = request.json
    nuevo_estudiante = Estudiante(
        nombre=data['nombre'],
        apellido=data['apellido'],
        sexo=data.get('sexo'),
        correo=data.get('correo'),
        telefono=data.get('telefono')
    )
    db.session.add(nuevo_estudiante)
    db.session.commit()
    return estudiante_schema.jsonify(nuevo_estudiante), 201

# -------------------------------------------------------------

@estudiantes.route('/estudiantes/v1/actualizar/<int:id>', methods=['PUT'])
def actualizarEstudiante(id):
    data = request.json
    estudiante = Estudiante.query.get_or_404(id)
    estudiante.nombre = data.get('nombre', estudiante.nombre)
    estudiante.apellido = data.get('apellido', estudiante.apellido)
    estudiante.sexo = data.get('sexo', estudiante.sexo)
    estudiante.correo = data.get('correo', estudiante.correo)
    estudiante.telefono = data.get('telefono', estudiante.telefono)
    db.session.commit()
    return estudiante_schema.jsonify(estudiante), 200

# -------------------------------------------------------------

@estudiantes.route('/estudiantes/v1/eliminar/<int:id>', methods=['DELETE'])
def eliminarEstudiante(id):
    estudiante = Estudiante.query.get_or_404(id)
    db.session.delete(estudiante)
    db.session.commit()
    return jsonify({
        "status_code": 200,
        "msg": "Estudiante eliminado exitosamente"
    }), 200

# -------------------------------------------------------------
