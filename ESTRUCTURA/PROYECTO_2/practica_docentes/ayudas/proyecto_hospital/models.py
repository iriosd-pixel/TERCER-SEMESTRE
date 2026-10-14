class ModeloBase:
    def __init__(self, id_registro): self.id = int(id_registro)
    @classmethod
    def desde_diccionario(cls, datos):
        datos = dict(datos); id_registro = datos.pop("id"); return cls(id_registro, **datos)
    def a_diccionario(self): return {"id": self.id}
    def etiqueta(self): return f"registro {self.id}"
    def __str__(self): return f"[{self.id}] {self.etiqueta()}"


class Persona(ModeloBase):
    def __init__(self, id_registro, nombre, apellido, email):
        super().__init__(id_registro); self.nombre = nombre; self.apellido = apellido; self.email = email
    def a_diccionario(self):
        datos = super().a_diccionario(); datos.update({"nombre": self.nombre, "apellido": self.apellido, "email": self.email}); return datos
    def etiqueta(self): return f"{self.nombre} {self.apellido} · {self.email}"


class Paciente(Persona):
    def __init__(self, id_registro, nombre, apellido, email, telefono):
        super().__init__(id_registro, nombre, apellido, email); self.telefono = telefono
    def a_diccionario(self):
        datos = super().a_diccionario(); datos["telefono"] = self.telefono; return datos


class Medico(Persona):
    def __init__(self, id_registro, nombre, apellido, email, especialidad):
        super().__init__(id_registro, nombre, apellido, email); self.especialidad = especialidad
    def a_diccionario(self):
        datos = super().a_diccionario(); datos["especialidad"] = self.especialidad; return datos


class Cita(ModeloBase):
    def __init__(self, id_registro, paciente_id, medico_id, fecha, hora):
        super().__init__(id_registro); self.paciente_id = int(paciente_id); self.medico_id = int(medico_id); self.fecha = fecha; self.hora = hora
    def a_diccionario(self):
        datos = super().a_diccionario(); datos.update({"paciente_id": self.paciente_id, "medico_id": self.medico_id, "fecha": self.fecha, "hora": self.hora}); return datos
    def etiqueta(self): return f"{self.fecha} {self.hora} · paciente {self.paciente_id} · médico {self.medico_id}"
