from utils.db import db
from dataclasses import dataclass

@dataclass
class Pregunta(db.Model):
    id_pregunta: int = db.Column(db.Integer, primary_key=True)
    texto: str = db.Column(db.Text, nullable=False)
    id_area: int = db.Column(db.Integer, db.ForeignKey('area.id_area'), nullable=False)
    id_test: int = db.Column(db.Integer, db.ForeignKey('test.id_test'), nullable=False)

    area = db.relationship('Area', back_populates='preguntas')
    test = db.relationship('Test', back_populates='preguntas')

    def __init__(self, texto, id_area, id_test):
        self.texto = texto
        self.id_area = id_area
        self.id_test = id_test


