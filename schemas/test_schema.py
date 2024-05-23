from utils.ma import ma
from marshmallow import fields
from schemas.test_amasc_schema import TestAmascSchema
from schemas.test_beck_schema import TestBeckSchema
from schemas.test_zung_schema import TestZungSchema

class TestSchema(ma.Schema):
    id_Test = fields.Integer()
    id_Tipo_Test = fields.Integer()
    tipo_test = fields.String()
    test_amasc = fields.Nested(TestAmascSchema, many=False, only=('id_Amasc', 'nombre'))
    test_beck = fields.Nested(TestBeckSchema, many=False, only=('id_Beck', 'nombre'))
    test_zung = fields.Nested(TestZungSchema, many=False, only=('id_Zung', 'nombre'))

test_schema = TestSchema()
tests_schema = TestSchema(many=True)
