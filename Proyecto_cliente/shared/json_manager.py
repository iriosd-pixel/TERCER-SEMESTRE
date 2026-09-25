"""Módulo de persistencia JSON para el proyecto.

Este archivo abstrae la parte de lectura y escritura del disco. Gracias a él,
la lógica de negocios no tiene que manejar directamente archivos ni JSON.
La idea es separar responsabilidades: una parte sabe cómo guardar datos y otra
sabe cómo usarlos.
"""

import json
import os


class GestorJSON:
    """Se encarga de leer y guardar listas de diccionarios en un archivo JSON."""

    def __init__(self, ruta):
        """Recibe la ruta del archivo y crea la carpeta si hace falta."""
        self.ruta = ruta
        carpeta = os.path.dirname(ruta)

        # Si la ruta incluye una carpeta y esta no existe, la creamos para evitar
        # errores al intentar guardar la información.
        if carpeta and not os.path.exists(carpeta):
            os.makedirs(carpeta)

    def leer(self):
        """Devuelve la lista guardada en el JSON, o [] si no existe o está corrupto."""
        if not os.path.exists(self.ruta):
            return []

        try:
            with open(self.ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

            # Aseguramos que la lectura siempre sea una lista, porque el programa
            # espera trabajar con una colección de registros.
            return datos if isinstance(datos, list) else []
        except (json.JSONDecodeError, OSError):
            # Si el archivo está vacío o dañado, se devuelve una lista vacía para
            # evitar que el programa falle por completo.
            return []

    def guardar(self, datos):
        """Escribe la lista de diccionarios en el archivo JSON indicado."""
        try:
            with open(self.ruta, "w", encoding="utf-8") as archivo:
                # indent=2 deja el JSON ordenado y fácil de leer en un editor.
                json.dump(datos, archivo, ensure_ascii=False, indent=2)
            return True
        except (TypeError, OSError):
            # TypeError aparece cuando se intenta guardar algo que JSON no puede
            # serializar, por ejemplo un set o un dato incompatible.
            return False