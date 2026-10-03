"""Módulo de persistencia JSON para el proyecto.

Este archivo abstrae la parte de lectura y escritura del disco. Gracias a él,
la lógica de negocios no tiene que manejar directamente archivos ni JSON.
La idea es separar responsabilidades: una parte sabe cómo guardar datos y otra
sabe cómo usarlos.
"""

import json
import os

# En este archivo no se usa *args, pero la idea se entiende con esta pista:
# *args reúne argumentos extra en una tupla. Si una función necesitara varios
# valores sin saber cuántos llegarán, se usaría así:
# def guardar(*args):
#     print(args)
#
# También aquí se ve el uso de return porque los métodos `.leer()` y `.guardar()`
# devuelven resultados al código que los llama.


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
            # Si no existe el archivo, devuelve [] para que el programa siga funcionando.
            return []

        try:
            with open(self.ruta, "r", encoding="utf-8") as archivo:
                # json.load() lee el contenido JSON y lo transforma a Python.
                datos = json.load(archivo)

            # Aseguramos que la lectura siempre sea una lista, porque el programa
            # espera trabajar con una colección de registros.
            # Cuando la carga funciona correctamente, se devuelve la lista leída.
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
            # return True significa que la escritura se realizó correctamente.
            return True
        except (TypeError, OSError):
            # TypeError aparece cuando se intenta guardar algo que JSON no puede
            # serializar, por ejemplo un set o un dato incompatible.
            # Si falla, devolvemos False para que el programa sepa que no se guardó.
            return False