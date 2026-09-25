"""Modelos del proyecto.

Este archivo define las estructuras fundamentales de la aplicación. Un modelo es
la representación de una entidad del negocio (cliente, estudiante, etc.) para que
el resto del código pueda trabajar con objetos y no solo con diccionarios crudos.
"""

import json

# Esta tupla representa el orden de los datos que tendrá cada cliente.
# Se usa como referencia central para que todas las partes del programa conozcan
# qué campos existen y en qué orden se deben pedir o mostrar.
CAMPOS_CLIENTE = ("nombre", "apellido", "email", "telefono", "ciudad", "direccion")


class Cliente:
    """Representa a un cliente con sus datos personales y de contacto.

    Cada objeto Cliente contiene la información que queremos guardar y luego
    consultar. Más adelante, esos objetos se convierten en diccionarios que
    se escriben en JSON para persistir la información.
    """

    def __init__(self, id_cliente, nombre, apellido, email, telefono, ciudad, direccion):
        # id_cliente identifica al cliente dentro del archivo JSON.
        # Es importante separarlo del nombre de parámetro 'id' de Python.
        self.id = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.ciudad = ciudad
        self.direccion = direccion

    def obtener_nombre_completo(self):
        """Devuelve el nombre completo juntando nombre y apellido."""
        return f"{self.nombre} {self.apellido}"

    def a_diccionario(self):
        """Convierte el objeto Cliente a un diccionario listo para guardar en JSON.

        Esto es útil porque el archivo JSON no puede guardar directamente un objeto
        de Python. Por eso transformamos el objeto al formato más simple: diccionario.
        """
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "telefono": self.telefono,
            "ciudad": self.ciudad,
            "direccion": self.direccion,
        }

    @classmethod
    def desde_diccionario(cls, datos):
        """Crea un objeto Cliente a partir de un diccionario leido desde JSON.

        Este método se usa cuando el programa vuelve a cargar los datos desde disco
        y necesita reconstruir objetos Cliente a partir de los registros guardados.
        """
        return cls(
            datos["id"],
            datos["nombre"],
            datos["apellido"],
            datos["email"],
            datos["telefono"],
            datos.get("ciudad", ""),
            datos.get("direccion", ""),
        )

    def a_json(self):
        """Serializa el cliente a texto JSON para poder guardarlo o imprimirlo."""
        return json.dumps(self.a_diccionario(), ensure_ascii=False)

    def __str__(self):
        """Retorna una representación breve del cliente para mostrar en consola."""
        return f"[{self.id}] {self.obtener_nombre_completo()} - {self.email}"


class Estudiante:
    """Modelo extra para practicar colecciones como listas, diccionarios y conjuntos.

    No está ligado directamente al CRUD de clientes, pero se usa para entender
    cómo manejar diferentes tipos de datos en Python: listas, diccionarios y sets.
    """

    def __init__(self, id_estudiante, nombre, apellido, email, carnet, notas=None, materias=None):
        self.id = id_estudiante
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.carnet = carnet

        # notas es un diccionario donde cada clave es una materia y cada valor es una
        # lista con todas las notas que ha obtenido en esa materia.
        self.notas = notas if notas else {}

        # materias es un conjunto, por eso no se repite ninguna materia.
        self.materias = set(materias) if materias else set()

    def obtener_nombre_completo(self):
        """Devuelve el nombre del estudiante completo."""
        return f"{self.nombre} {self.apellido}"

    def inscribir_materia(self, materia):
        """Añade una materia al estudiante evitando duplicados."""
        self.materias.add(materia)

    def agregar_nota(self, materia, nota):
        """Guarda una nota para una materia concreta.

        Primero asegura que la materia exista en el conjunto y luego añade la nota
        a la lista correspondiente dentro del diccionario de notas.
        """
        self.inscribir_materia(materia)
        self.notas.setdefault(materia, []).append(nota)

    def obtener_promedio(self):
        """Calcula el promedio general de todas las notas del estudiante."""
        todas = []
        for lista_notas in self.notas.values():
            todas.extend(lista_notas)

        if not todas:
            return 0

        return round(sum(todas) / len(todas), 2)

    def materias_en_comun(self, otro_estudiante):
        """Devuelve las materias que comparten dos estudiantes.

        Esto se hace con la intersección de conjuntos, que es una operación muy útil
        cuando necesitas comparar datos sin duplicados.
        """
        return self.materias & otro_estudiante.materias

    def a_diccionario(self):
        """Convierte el estudiante a un diccionario compatible con JSON."""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "carnet": self.carnet,
            "notas": self.notas,
            "materias": sorted(self.materias),
        }

    @classmethod
    def desde_diccionario(cls, datos):
        """Recupera un objeto Estudiante desde un diccionario guardado en JSON."""
        return cls(
            datos["id"],
            datos["nombre"],
            datos["apellido"],
            datos["email"],
            datos["carnet"],
            notas=datos.get("notas", {}),
            materias=set(datos.get("materias", [])),
        )

    def __str__(self):
        """Devuelve un resumen legible del estudiante y su promedio."""
        return f"[{self.carnet}] {self.obtener_nombre_completo()} - Promedio: {self.obtener_promedio()}"