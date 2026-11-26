import json
import os

from app.models.doce import Doce

DB_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "db")


class DataRecord():
    """Banco de dados JSON para o recurso Doces"""

    def __init__(self):
        self.__doces = []  # banco (json)
        self.read()

    def read(self):
        with open(os.path.join(DB_DIR, "doces.json"), "r", encoding="utf-8") as arquivo_json:
            doce_data = json.load(arquivo_json)
            self.__doces = [Doce(**data) for data in doce_data]

    def todos(self):
        return list(self.__doces)

    def buscar(self, doce_id):
        for d in self.__doces:
            if d.id == doce_id:
                return d
        return None

    def por_ids(self, ids):
        return [d for d in (self.buscar(i) for i in ids) if d]
