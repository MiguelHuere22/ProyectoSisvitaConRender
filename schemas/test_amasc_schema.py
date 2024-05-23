from utils.ma import ma
from marshmallow import fields


class TestAmascSchema(ma.Schema):
    id_Amasc = fields.Integer()
    nombre = fields.String()
    id_Area = fields.Integer()
    Numero_preguntas = fields.Integer()
    descripcion = fields.String()

test_amasc_schema = TestAmascSchema()
tests_amasc_schema = TestAmascSchema(many=True)

