class ModeloBase:
    """Base para los registros del proyecto de práctica."""

    def __init__(self, id_registro):
        self.id = int(id_registro)

    @classmethod
    def desde_diccionario(cls, datos):
        datos = dict(datos)
        id_registro = datos.pop("id")
        return cls(id_registro, **datos)

    def a_diccionario(self):
        return {"id": self.id}

    def etiqueta(self):
        return f"registro {self.id}"

    def __str__(self):
        return f"[{self.id}] {self.etiqueta()}"


class Persona(ModeloBase):
    """Datos que comparten las personas."""

    def __init__(self, id_registro, nombre, apellido, email):
        super().__init__(id_registro)
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def a_diccionario(self):
        datos = super().a_diccionario()
        datos["nombre"] = self.nombre
        datos["apellido"] = self.apellido
        datos["email"] = self.email
        return datos

    def etiqueta(self):
        return self.nombre_completo()


class Docente(Persona):
    """Persona con una especialidad docente."""

    def __init__(self, id_registro, nombre, apellido, email, especialidad=""):
        super().__init__(id_registro, nombre, apellido, email)
        self.especialidad = especialidad

    def a_diccionario(self):
        datos = super().a_diccionario()
        datos["especialidad"] = self.especialidad
        return datos

    def etiqueta(self):
        return f"{super().etiqueta()} · {self.especialidad}"
