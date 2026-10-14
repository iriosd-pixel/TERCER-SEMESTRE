from abc import ABC, abstractmethod
import os
from models import Empleado
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


class EmpleadoController(CrudBase):
    CAMPOS = {"nombre", "apellido", "email", "cargo"}

    def __init__(self, archivo=None):
        if archivo is None:
            archivo = os.path.join(BASE, "data", "empleados.json")
        self.gestor = GestorJSON(archivo)
        self.lista = []
        for fila in self.gestor.leer():
            self.lista.append(Empleado.desde_diccionario(fila))

    def guardar(self):
        datos = []
        for empleado in self.lista:
            datos.append(empleado.a_diccionario())
        return self.gestor.guardar(datos)

    def validar(self, datos, id_actual=None):
        for campo in self.CAMPOS:
            if campo in datos and str(datos[campo]).strip() == "":
                return f"{campo} es obligatorio"
        if id_actual is None:
            for campo in self.CAMPOS:
                if str(datos.get(campo, "")).strip() == "":
                    return f"{campo} es obligatorio"
        if "email" in datos:
            email = str(datos["email"]).strip().lower()
            for empleado in self.lista:
                if empleado.id != id_actual and empleado.email.lower() == email:
                    return "Ese email ya está registrado"
        return None

    def leer(self): return self.lista

    def obtener(self, id_registro):
        for empleado in self.lista:
            if empleado.id == id_registro: return empleado
        return None

    def buscar(self, texto):
        termino = str(texto).strip().lower()
        resultados = []
        for empleado in self.lista:
            if termino and (termino in empleado.nombre.lower() or termino in empleado.apellido.lower() or termino in empleado.email.lower() or termino in empleado.cargo.lower()):
                resultados.append(empleado)
        return resultados

    def siguiente(self):
        mayor = 0
        for empleado in self.lista:
            if empleado.id > mayor: mayor = empleado.id
        return mayor + 1

    def crear(self, datos):
        desconocidos = set(datos) - self.CAMPOS
        if desconocidos: return False, f"Campos no válidos: {', '.join(sorted(desconocidos))}"
        error = self.validar(datos)
        if error: return False, error
        empleado = Empleado(self.siguiente(), str(datos["nombre"]).strip().title(), str(datos["apellido"]).strip().title(), str(datos["email"]).strip().lower(), str(datos["cargo"]).strip().title())
        self.lista.append(empleado)
        if not self.guardar():
            self.lista.remove(empleado)
            return False, "No se pudo guardar el empleado"
        return True, f"Empleado creado: {empleado.etiqueta()}"

    def actualizar(self, id_registro, datos):
        empleado = self.obtener(id_registro)
        if empleado is None: return False, "No existe el empleado"
        if not datos: return False, "No se indicaron cambios"
        desconocidos = set(datos) - self.CAMPOS
        if desconocidos: return False, f"Campos no válidos: {', '.join(sorted(desconocidos))}"
        error = self.validar(datos, id_registro)
        if error: return False, error
        anteriores = {}
        for campo, valor in datos.items():
            anteriores[campo] = getattr(empleado, campo)
            valor = str(valor).strip()
            if campo != "email": valor = valor.title()
            else: valor = valor.lower()
            setattr(empleado, campo, valor)
        if not self.guardar():
            for campo, valor in anteriores.items(): setattr(empleado, campo, valor)
            return False, "No se pudo guardar la actualización"
        return True, f"Empleado {id_registro} actualizado"

    def eliminar(self, id_registro):
        empleado = self.obtener(id_registro)
        if empleado is None: return False, "No existe el empleado"
        posicion = self.lista.index(empleado)
        self.lista.remove(empleado)
        if not self.guardar():
            self.lista.insert(posicion, empleado)
            return False, "No se pudo guardar la eliminación"
        return True, f"Empleado {id_registro} eliminado"
