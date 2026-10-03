import json

# TUPLAS: nombres fijos de los campos.
# El id se genera automáticamente.
CAMPOS_CLIENTE = (
    "nombre", "apellido", "email",
    "telefono", "ciudad", "direccion"
)

CAMPOS_ESTUDIANTE = ("nombre", "apellido", "email", "carnet")


class Cliente:
    """Representa los datos de un cliente."""

    def __init__(
        self, id_cliente, nombre, apellido,
        email, telefono, ciudad, direccion
    ):
        self.id = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.ciudad = ciudad
        self.direccion = direccion

    def obtener_nombre_completo(self):
        """Devuelve el nombre y apellido juntos."""
        return f"{self.nombre} {self.apellido}"

    def a_diccionario(self):
        """Convierte el cliente en un diccionario."""
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
        """Crea un cliente a partir de un diccionario."""
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
        """Convierte los datos a texto JSON."""
        return json.dumps(
            self.a_diccionario(),
            ensure_ascii=False
        )

    def __str__(self):
        """Devuelve un texto que representa al cliente."""
        return (
            f"[{self.id}] "
            f"{self.obtener_nombre_completo()} - {self.email}"
        )


class Estudiante:
    """Representa un estudiante, sus materias y sus notas."""

    def __init__(
        self, id_estudiante, nombre, apellido,
        email, carnet, notas=None, materias=None
    ):
        self.id = id_estudiante
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.carnet = carnet

        # DICCIONARIO DE LISTAS:
        # cada materia tiene una lista de calificaciones.
        # Ejemplo: {"Matemática": [18, 19], "Inglés": [17]}
        self.notas = notas if notas else {}

        # CONJUNTO: guarda materias sin repetir.
        self.materias = set(materias) if materias else set()

    def obtener_nombre_completo(self):
        """Devuelve el nombre y apellido juntos."""
        return f"{self.nombre} {self.apellido}"

    def inscribir_materia(self, materia):
        """Agrega una materia al conjunto, sin duplicarla."""
        self.materias.add(materia)

    def agregar_nota(self, materia, nota):
        """Agrega una nota y registra la materia.

        El controlador debe validar la nota antes
        de llamar a este método.
        """
        self.inscribir_materia(materia)

        # Si la materia no existe en el diccionario,
        # setdefault crea una lista vacía.
        # append agrega la nota a esa lista.
        self.notas.setdefault(materia, []).append(nota)

    def obtener_promedio(self):
        """Devuelve el promedio general o 0 si no hay notas."""

        # LISTA: reúne las notas de todas las materias.
        todas = []

        for lista_notas in self.notas.values():
            todas.extend(lista_notas)

        # Evita dividir entre cero.
        if not todas:
            return 0

        # Devuelve únicamente el promedio.
        return round(sum(todas) / len(todas), 2)

    def materias_en_comun(self, otro_estudiante):
        """Devuelve las materias que ambos estudiantes comparten."""

        # INTERSECCIÓN de conjuntos.
        return self.materias & otro_estudiante.materias

    def a_diccionario(self):
        """Convierte el estudiante a un diccionario para JSON."""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "carnet": self.carnet,
            "notas": self.notas,

            # JSON no admite conjuntos.
            # sorted convierte el conjunto en una lista ordenada.
            "materias": sorted(self.materias),
        }

    @classmethod
    def desde_diccionario(cls, datos):
        """Reconstruye un estudiante desde un diccionario."""
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
        """Devuelve un resumen del estudiante."""
        return (
            f"[{self.carnet}] "
            f"{self.obtener_nombre_completo()} - "
            f"Promedio: {self.obtener_promedio()}"
        )


# Estas pruebas se ejecutan únicamente al ejecutar models.py.
# Al importar este archivo desde otro módulo, no se ejecutan.
if __name__ == "__main__":
    est1 = Estudiante(
        1, "Ana", "Pérez", "ana@unemi.edu.ec", "EST2026001"
    )

    est2 = Estudiante(
        2, "Luis", "Mora", "luis@unemi.edu.ec", "EST2026002"
    )

    print("--- Nombre completo ---")
    print(est1.obtener_nombre_completo())
    print(est2.obtener_nombre_completo())

    print("\n--- Promedio sin notas: debe ser 0 ---")
    print(est1.obtener_promedio())

    print("\n--- Inscribir una materia repetida ---")
    est1.inscribir_materia("Física")
    est1.inscribir_materia("Física")
    print(sorted(est1.materias))

    print("\n--- Agregar notas ---")
    est1.agregar_nota("Matemática", 18)
    est1.agregar_nota("Matemática", 19)
    est1.agregar_nota("Inglés", 17)

    est2.agregar_nota("Matemática", 15)
    est2.agregar_nota("Programación", 20)

    print("Notas de Ana:", est1.notas)
    print("Notas de Luis:", est2.notas)

    print("\n--- Promedios ---")
    print("Ana:", est1.obtener_promedio())    # 18.0
    print("Luis:", est2.obtener_promedio())   # 17.5

    print("\n--- Materias en común ---")
    print(sorted(est1.materias_en_comun(est2)))

    print("\n--- Convertir a diccionario ---")
    datos = est1.a_diccionario()
    print(datos)

    print("\n--- Reconstruir desde un diccionario ---")
    copia = Estudiante.desde_diccionario(datos)
    print(copia)
    print("¿Mismas notas?", copia.notas == est1.notas)
    print("¿Mismas materias?", copia.materias == est1.materias)

    print("\n--- Resumen de cada estudiante ---")
    print(est1)
    print(est2)