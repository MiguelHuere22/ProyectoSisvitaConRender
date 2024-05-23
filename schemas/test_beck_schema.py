from utils.ma import ma
from marshmallow import fields

class TestBeckSchema(ma.Schema):
    id_Beck = fields.Integer()
    nombre = fields.String()
    Numero_preguntas = fields.Integer()
    descripcion = fields.String()

test_beck_schema = TestBeckSchema()
tests_beck_schema = TestBeckSchema(many=True)

