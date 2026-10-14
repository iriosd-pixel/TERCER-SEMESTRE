class ModeloBase:
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
    def __init__(self, id_registro, nombre, apellido, email):
        super().__init__(id_registro)
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def a_diccionario(self):
        datos = super().a_diccionario()
        datos.update({"nombre": self.nombre, "apellido": self.apellido, "email": self.email})
        return datos

    def etiqueta(self):
        return self.nombre_completo()


class Empleado(Persona):
    def __init__(self, id_registro, nombre, apellido, email, cargo):
        super().__init__(id_registro, nombre, apellido, email)
        self.cargo = cargo

    def a_diccionario(self):
        datos = super().a_diccionario()
        datos["cargo"] = self.cargo
        return datos

    def etiqueta(self):
        return f"{super().etiqueta()} · {self.cargo}"
