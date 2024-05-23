from utils.ma import ma
from model.area import Area
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class AreaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Area
        load_instance = True

area_schema = AreaSchema()
areas_schema = AreaSchema(many=True)
