from utils.ma import ma
from marshmallow import fields

class EstudianteSchema(ma.Schema):
    id_estudiante = fields.Integer()
    nombre = fields.String()
    apellido = fields.String()
    sexo = fields.String()
    correo = fields.String()
    telefono = fields.String()

estudiante_schema = EstudianteSchema()
estudiantes_schema = EstudianteSchema(many=True)
