from utils.ma import ma
from marshmallow import fields

class TestZungSchema(ma.Schema):
    id_Zung = fields.Integer()
    nombre = fields.String()
    Numero_preguntas = fields.Integer()
    descripcion = fields.String()

test_zung_schema = TestZungSchema()
tests_zung_schema = TestZungSchema(many=True)

