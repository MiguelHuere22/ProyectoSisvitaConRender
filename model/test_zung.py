from utils.db import db
from dataclasses import dataclass

@dataclass
class TestZung(db.Model):
    id_zung: int = db.Column(db.Integer, primary_key=True)
    nombre: str = db.Column(db.String(255), nullable=False)
    numero_preguntas: int = db.Column(db.Integer, nullable=False)
    descripcion: str = db.Column(db.Text, nullable=True)
    test_id = db.Column(db.Integer, db.ForeignKey('test.id_test'))

    def __init__(self, nombre, numero_preguntas, descripcion=None):
        self.nombre = nombre
        self.numero_preguntas = numero_preguntas
        self.descripcion = descripcion

