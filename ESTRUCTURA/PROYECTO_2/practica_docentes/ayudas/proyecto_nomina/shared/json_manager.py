import json
import os


class GestorJSON:
    """Lee y guarda listas de diccionarios en un archivo JSON."""

    def __init__(self, ruta):
        self.ruta = ruta
        carpeta = os.path.dirname(ruta)
        if carpeta:
            os.makedirs(carpeta, exist_ok=True)

    def leer(self):
        try:
            with open(self.ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
            if isinstance(datos, list):
                return datos
            return []
        except FileNotFoundError:
            return []
        except (OSError, json.JSONDecodeError):
            return []

    def guardar(self, datos):
        try:
            with open(self.ruta, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, ensure_ascii=False, indent=2)
            return True
        except (OSError, TypeError):
            return False
