from utils.ma import ma
from marshmallow import fields
from schemas.area_schema import AreaSchema
from schemas.test_schema import TestSchema

class PreguntaSchema(ma.Schema):
    id_pregunta = fields.Integer()
    texto = fields.String()
    id_area = fields.Integer()
    id_test = fields.Integer()
    area = fields.Nested(AreaSchema, many=False, only=("id_area", "nombre"))
    test = fields.Nested(TestSchema, many=False, only=("id_test", "tipo_test"))

pregunta_schema = PreguntaSchema()
preguntas_schema = PreguntaSchema(many=True)
