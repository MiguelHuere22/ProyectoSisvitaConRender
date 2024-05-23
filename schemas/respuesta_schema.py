from utils.ma import ma
from marshmallow import fields
from schemas.pregunta_schema import PreguntaSchema
from schemas.estudiante_schema import EstudianteSchema

class RespuestaSchema(ma.Schema):
    id_respuesta = fields.Integer()
    respuesta_usuario = fields.String()
    pregunta_id = fields.Integer()
    id_estudiante = fields.Integer()
    pregunta = fields.Nested(PreguntaSchema, many=False, only=("id_pregunta", "texto"))
    estudiante = fields.Nested(EstudianteSchema, many=False, only=("id_estudiante", "nombre", "apellido"))

respuesta_schema = RespuestaSchema()
respuestas_schema = RespuestaSchema(many=True)
