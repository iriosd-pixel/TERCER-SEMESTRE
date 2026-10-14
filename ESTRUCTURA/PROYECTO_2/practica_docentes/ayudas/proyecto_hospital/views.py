from abc import ABC, abstractmethod
from datetime import date, time
import os
from models import Paciente, Medico, Cita
from shared.json_manager import GestorJSON

BASE = os.path.dirname(os.path.abspath(__file__))


class CrudBase(ABC):
    @abstractmethod
    def leer(self): pass
    @abstractmethod
    def obtener(self, id_registro): pass
    @abstractmethod
    def buscar(self, texto): pass
    @abstractmethod
    def siguiente(self): pass
    @abstractmethod
    def crear(self, datos): pass
    @abstractmethod
    def actualizar(self, id_registro, datos): pass
    @abstractmethod
    def eliminar(self, id_registro): pass


class ControladorBase(CrudBase):
    CAMPOS = set(); MODELO = None; ARCHIVO = ""
    def __init__(self, archivo=None):
        if archivo is None: archivo = os.path.join(BASE, "data", self.ARCHIVO)
        self.gestor = GestorJSON(archivo); self.lista = []
        for fila in self.gestor.leer(): self.lista.append(self.MODELO.desde_diccionario(fila))
    def guardar(self):
        filas = []
        for obj in self.lista: filas.append(obj.a_diccionario())
        return self.gestor.guardar(filas)
    def leer(self): return self.lista
    def obtener(self, id_registro):
        for obj in self.lista:
            if obj.id == id_registro: return obj
        return None
    def buscar(self, texto):
        texto = str(texto).strip().lower(); resultados = []
        for obj in self.lista:
            if texto and texto in obj.etiqueta().lower(): resultados.append(obj)
        return resultados
    def siguiente(self):
        mayor = 0
        for obj in self.lista:
            if obj.id > mayor: mayor = obj.id
        return mayor + 1
    def construir(self, datos, id_registro): raise NotImplementedError
    def validar(self, datos, id_actual=None): return None
    def crear(self, datos):
        desconocidos = set(datos) - self.CAMPOS
        if desconocidos: return False, f"Campos inválidos: {sorted(desconocidos)}"
        error = self.validar(datos)
        if error: return False, error
        obj = self.construir(datos, self.siguiente()); self.lista.append(obj)
        if not self.guardar(): self.lista.remove(obj); return False, "Falló el guardado; lista restaurada"
        return True, f"Creado: {obj.etiqueta()}"
    def actualizar(self, id_registro, datos):
        obj = self.obtener(id_registro)
        if obj is None: return False, "No existe el registro"
        if not datos: return False, "No se indicaron cambios"
        desconocidos = set(datos) - self.CAMPOS
        if desconocidos: return False, f"Campos inválidos: {sorted(desconocidos)}"
        error = self.validar(datos, id_registro)
        if error: return False, error
        anterior = obj.a_diccionario()
        for campo, valor in datos.items(): setattr(obj, campo, self.normalizar(campo, valor))
        if not self.guardar():
            restaurado = self.MODELO.desde_diccionario(anterior); obj.__dict__.update(restaurado.__dict__)
            return False, "Falló el guardado; cambios restaurados"
        return True, f"Actualizado: {id_registro}"
    def normalizar(self, campo, valor): return str(valor).strip().title()
    def eliminar(self, id_registro):
        obj = self.obtener(id_registro)
        if obj is None: return False, "No existe el registro"
        posicion = self.lista.index(obj); self.lista.remove(obj)
        if not self.guardar(): self.lista.insert(posicion, obj); return False, "Falló el guardado; registro restaurado"
        return True, f"Eliminado: {id_registro}"


class PacienteController(ControladorBase):
    MODELO, ARCHIVO = Paciente, "pacientes.json"; CAMPOS = {"nombre", "apellido", "email", "telefono"}
    def construir(self, d, i): return Paciente(i, d["nombre"].strip().title(), d["apellido"].strip().title(), d["email"].strip().lower(), d["telefono"].strip())
    def validar(self, d, id_actual=None):
        for c in self.CAMPOS:
            if (id_actual is None or c in d) and not str(d.get(c, "")).strip(): return f"{c} obligatorio"
        return None
    def normalizar(self, c, v): return str(v).strip().lower() if c == "email" else str(v).strip().title()
    def eliminar(self, id_registro):
        for cita in self.citas.leer():
            if cita.paciente_id == id_registro:
                return False, "No se elimina: el paciente tiene citas"
        return super().eliminar(id_registro)


class MedicoController(ControladorBase):
    MODELO, ARCHIVO = Medico, "medicos.json"; CAMPOS = {"nombre", "apellido", "email", "especialidad"}
    def construir(self, d, i): return Medico(i, d["nombre"].strip().title(), d["apellido"].strip().title(), d["email"].strip().lower(), d["especialidad"].strip().title())
    def validar(self, d, id_actual=None):
        for c in self.CAMPOS:
            if (id_actual is None or c in d) and not str(d.get(c, "")).strip(): return f"{c} obligatorio"
        return None
    def normalizar(self, c, v): return str(v).strip().lower() if c == "email" else str(v).strip().title()
    def eliminar(self, id_registro):
        for cita in self.citas.leer():
            if cita.medico_id == id_registro:
                return False, "No se elimina: el médico tiene citas"
        return super().eliminar(id_registro)


class CitaController(ControladorBase):
    MODELO, ARCHIVO = Cita, "citas.json"; CAMPOS = {"paciente_id", "medico_id", "fecha", "hora"}
    def __init__(self, pacientes, medicos, archivo=None): self.pacientes = pacientes; self.medicos = medicos; super().__init__(archivo)
    def construir(self, d, i): return Cita(i, int(d["paciente_id"]), int(d["medico_id"]), d["fecha"], d["hora"])
    def validar(self, d, id_actual=None):
        actual = self.obtener(id_actual) if id_actual is not None else None
        paciente_id = d.get("paciente_id", actual.paciente_id if actual else None)
        medico_id = d.get("medico_id", actual.medico_id if actual else None)
        fecha = str(d.get("fecha", actual.fecha if actual else "")).strip()
        hora = str(d.get("hora", actual.hora if actual else "")).strip()
        try: paciente_id = int(paciente_id); medico_id = int(medico_id)
        except (TypeError, ValueError): return "Los IDs deben ser enteros"
        if self.pacientes.obtener(paciente_id) is None: return "No existe el paciente"
        if self.medicos.obtener(medico_id) is None: return "No existe el médico"
        try: date.fromisoformat(fecha); time.fromisoformat(hora)
        except ValueError: return "Use fecha YYYY-MM-DD y hora HH:MM válida"
        for cita in self.lista:
            if cita.id == id_actual: continue
            mismo_horario = cita.fecha == fecha and cita.hora == hora
            if mismo_horario and cita.medico_id == medico_id: return "El médico ya tiene una cita en ese horario"
            if mismo_horario and cita.paciente_id == paciente_id: return "El paciente ya tiene una cita en ese horario"
        return None
    def normalizar(self, campo, valor): return int(valor) if campo in ("paciente_id", "medico_id") else str(valor).strip()
