from flask import Blueprint, request, jsonify
from model.pregunta import Pregunta
from utils.db import db
from schemas.pregunta_schema import preguntas_schema

preguntas = Blueprint('preguntas', __name__)

@preguntas.route('/preguntas/v1', methods=['GET'])
def getMensaje():
    result = {"data": 'Hola, Preguntas'}
    return jsonify(result)

# -------------------------------------------------------------

@preguntas.route('/preguntas/v1/listar', methods=['GET'])
def getPreguntas():
    preguntas = Pregunta.query.all()
    result = {
        "data": preguntas_schema.dump(preguntas),
        "status_code": 200,
        "msg": "Se recuperó la lista de Preguntas sin inconvenientes"
    }
    return jsonify(result), 200

# -------------------------------------------------------------

@preguntas.route('/preguntas/v1/agregar', methods=['POST'])
def agregarPregunta():
    data = request.json
    nueva_pregunta = Pregunta(
        texto=data['texto'],
        id_area=data['id_area'],
        id_test=data['id_test']
    )
    db.session.add(nueva_pregunta)
    db.session.commit()
    return pregunta_schema.jsonify(nueva_pregunta), 201

# -------------------------------------------------------------

@preguntas.route('/preguntas/v1/actualizar/<int:id>', methods=['PUT'])
def actualizarPregunta(id):
    data = request.json
    pregunta = Pregunta.query.get_or_404(id)
    pregunta.texto = data.get('texto', pregunta.texto)
    pregunta.id_area = data.get('id_area', pregunta.id_area)
    pregunta.id_test = data.get('id_test', pregunta.id_test)
    db.session.commit()
    return pregunta_schema.jsonify(pregunta), 200

# -------------------------------------------------------------

@preguntas.route('/preguntas/v1/eliminar/<int:id>', methods=['DELETE'])
def eliminarPregunta(id):
    pregunta = Pregunta.query.get_or_404(id)
    db.session.delete(pregunta)
    db.session.commit()
    return jsonify({
        "status_code": 200,
        "msg": "Pregunta eliminada exitosamente"
    }), 200

# -------------------------------------------------------------
