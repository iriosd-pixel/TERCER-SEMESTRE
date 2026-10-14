import json, os

class GestorJSON:
    def __init__(self, ruta): self.ruta = ruta; os.makedirs(os.path.dirname(ruta), exist_ok=True)
    def leer(self):
        try:
            with open(self.ruta, encoding="utf-8") as archivo:
                datos = json.load(archivo)
            return datos if isinstance(datos, list) else []
        except FileNotFoundError: return []
        except (OSError, json.JSONDecodeError): return []
    def guardar(self, datos):
        try:
            with open(self.ruta, "w", encoding="utf-8") as archivo: json.dump(datos, archivo, ensure_ascii=False, indent=2)
            return True
        except (OSError, TypeError): return False
