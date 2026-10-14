# ---------------------------------------------------------------------
# Modelo base y datos de persona
# ---------------------------------------------------------------------
class ModeloBase:
    """Guarda el identificador común de cada registro."""

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
    """Datos comunes de las personas del ejercicio."""

    def __init__(self, id_registro, nombre, apellido, email):
        super().__init__(id_registro)
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def a_diccionario(self):
        datos = super().a_diccionario()
        datos["nombre"] = self.nombre
        datos["apellido"] = self.apellido
        datos["email"] = self.email
        return datos

    def etiqueta(self):
        return f"{self.nombre} {self.apellido} · {self.email}"


class Empleado(Persona):
    """Persona asignada a un departamento."""

    def __init__(self, id_registro, nombre, apellido, email, departamento_id):
        super().__init__(id_registro, nombre, apellido, email)
        self.departamento_id = int(departamento_id)

    def a_diccionario(self):
        datos = super().a_diccionario()
        datos["departamento_id"] = self.departamento_id
        return datos

    def etiqueta(self):
        return f"{super().etiqueta()} · departamento {self.departamento_id}"


# ---------------------------------------------------------------------
# Entidades de la organización
# ---------------------------------------------------------------------
class Departamento(ModeloBase):
    def __init__(self, id_registro, nombre):
        super().__init__(id_registro)
        self.nombre = nombre

    def a_diccionario(self):
        datos = super().a_diccionario()
        datos["nombre"] = self.nombre
        return datos

    def etiqueta(self):
        return self.nombre


# ---------------------------------------------------------------------
# Registro y cálculo de nómina
# ---------------------------------------------------------------------
class Nomina(ModeloBase):
    def __init__(self, id_registro, empleado_id, periodo, sueldo_base, bonificacion, descuento):
        super().__init__(id_registro)
        self.empleado_id = int(empleado_id)
        self.periodo = periodo
        self.sueldo_base = float(sueldo_base)
        self.bonificacion = float(bonificacion)
        self.descuento = float(descuento)

    def pago_neto(self):
        return round(self.sueldo_base + self.bonificacion - self.descuento, 2)

    def a_diccionario(self):
        datos = super().a_diccionario()
        datos["empleado_id"] = self.empleado_id
        datos["periodo"] = self.periodo
        datos["sueldo_base"] = self.sueldo_base
        datos["bonificacion"] = self.bonificacion
        datos["descuento"] = self.descuento
        return datos

    def etiqueta(self):
        return f"{self.periodo} · empleado {self.empleado_id} · neto {self.pago_neto():.2f}"
