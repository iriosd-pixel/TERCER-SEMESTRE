"""Modelo de estudiantes: datos, materias y calificaciones."""

# TUPLA: contiene los campos que se solicitan al crear un estudiante.
# El ID se genera automáticamente en el controlador.
CAMPOS_ESTUDIANTE = ("nombre", "apellido", "email", "carnet")


class Estudiante:
    """Representa un estudiante, sus materias y sus notas."""

    def __init__(
        self, id_estudiante, nombre, apellido,
        email, carnet, notas=None, materias=None
    ):
        """Inicializa los datos del estudiante."""
        self.id = id_estudiante
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.carnet = carnet

        # DICCIONARIO DE LISTAS:
        # cada materia tiene una lista de calificaciones.
        # Ejemplo: {"Matemática": [18, 19], "Inglés": [17]}
        self.notas = notas if notas is not None else {}

        # CONJUNTO: guarda las materias sin repetir.
        self.materias = set(materias) if materias is not None else set()

    def obtener_nombre_completo(self):
        """Devuelve el nombre y apellido juntos."""
        return f"{self.nombre} {self.apellido}"

    def inscribir_materia(self, materia):
        """Agrega una materia sin duplicarla."""
        self.materias.add(materia)

    def agregar_nota(self, materia, nota):
        """Registra una nota y también inscribe la materia.

        El controlador valida la nota antes de llamar a este método.
        """
        self.inscribir_materia(materia)

        # Si la materia todavía no existe, crea una lista vacía.
        # Después agrega la nota a esa lista.
        self.notas.setdefault(materia, []).append(nota)

    def obtener_promedio(self):
        """Calcula el promedio de todas las notas del estudiante."""
        todas = []

        for lista_notas in self.notas.values():
            todas.extend(lista_notas)

        # Si no hay notas, evita dividir entre cero.
        if not todas:
            return 0

        return round(sum(todas) / len(todas), 2)

    def materias_en_comun(self, otro_estudiante):
        """Devuelve las materias que comparten dos estudiantes."""
        return self.materias & otro_estudiante.materias

    def a_diccionario(self):
        """Convierte los datos del estudiante a un diccionario."""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "carnet": self.carnet,
            "notas": self.notas,

            # JSON no admite conjuntos.
            # sorted convierte las materias en una lista ordenada.
            "materias": sorted(self.materias),
        }

    @classmethod
    def desde_diccionario(cls, datos):
        """Crea un estudiante a partir de los datos guardados."""
        return cls(
            id_estudiante=datos["id"],
            nombre=datos["nombre"],
            apellido=datos["apellido"],
            email=datos["email"],
            carnet=datos["carnet"],
            notas=datos.get("notas", {}),
            materias=datos.get("materias", []),
        )

    def __str__(self):
        """Devuelve un resumen del estudiante como texto."""
        return (
            f"[{self.carnet}] "
            f"{self.obtener_nombre_completo()} - "
            f"Promedio: {self.obtener_promedio():.2f}"
        )