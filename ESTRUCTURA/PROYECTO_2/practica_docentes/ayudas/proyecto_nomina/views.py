from abc import ABC, abstractmethod
import math, os
from models import Empleado, Departamento, Nomina
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
    CAMPOS = set()
    MODELO = None
    ARCHIVO = ""
    def __init__(self, archivo=None):
        if archivo is None: archivo = os.path.join(BASE, "data", self.ARCHIVO)
        self.gestor = GestorJSON(archivo); self.lista = []
        for fila in self.gestor.leer(): self.lista.append(self.MODELO.desde_diccionario(fila))
    def guardar(self):
        filas = []
        for objeto in self.lista: filas.append(objeto.a_diccionario())
        return self.gestor.guardar(filas)
    def leer(self): return self.lista
    def obtener(self, id_registro):
        for objeto in self.lista:
            if objeto.id == id_registro: return objeto
        return None
    def buscar(self, texto):
        termino = str(texto).lower().strip(); encontrados = []
        for objeto in self.lista:
            if termino and termino in objeto.etiqueta().lower(): encontrados.append(objeto)
        return encontrados
    def siguiente(self):
        mayor = 0
        for objeto in self.lista:
            if objeto.id > mayor: mayor = objeto.id
        return mayor + 1
    def construir(self, datos, id_registro): raise NotImplementedError
    def validar(self, datos, id_actual=None): return None
    def crear(self, datos):
        desconocidos = set(datos) - self.CAMPOS
        if desconocidos: return False, f"Campos inválidos: {sorted(desconocidos)}"
        error = self.validar(datos)
        if error: return False, error
        objeto = self.construir(datos, self.siguiente()); self.lista.append(objeto)
        if not self.guardar(): self.lista.remove(objeto); return False, "Fallo al guardar; se revirtió la lista"
        return True, f"Creado: {objeto.etiqueta()}"
    def actualizar(self, id_registro, datos):
        objeto = self.obtener(id_registro)
        if objeto is None: return False, "No existe el registro"
        if not datos: return False, "No se indicaron cambios"
        desconocidos = set(datos) - self.CAMPOS
        if desconocidos: return False, f"Campos inválidos: {sorted(desconocidos)}"
        error = self.validar(datos, id_registro)
        if error: return False, error
        anterior = objeto.a_diccionario()
        for campo, valor in datos.items(): setattr(objeto, campo, self.normalizar(campo, valor))
        if not self.guardar():
            restaurado = self.MODELO.desde_diccionario(anterior); objeto.__dict__.update(restaurado.__dict__)
            return False, "Fallo al guardar; se revirtieron los cambios en memoria"
        return True, f"Actualizado: {id_registro}"
    def normalizar(self, campo, valor): return valor
    def eliminar(self, id_registro):
        objeto = self.obtener(id_registro)
        if objeto is None: return False, "No existe el registro"
        posicion = self.lista.index(objeto); self.lista.remove(objeto)
        if not self.guardar(): self.lista.insert(posicion, objeto); return False, "Fallo al guardar; se restauró la lista"
        return True, f"Eliminado: {id_registro}"


class DepartamentoController(ControladorBase):
    MODELO, ARCHIVO, CAMPOS = Departamento, "departamentos.json", {"nombre"}
    def construir(self, datos, id_registro): return Departamento(id_registro, datos["nombre"].strip().title())
    def validar(self, datos, id_actual=None):
        if "nombre" in datos and not datos["nombre"].strip(): return "Nombre obligatorio"
        nombre = str(datos.get("nombre", "")).strip().lower()
        for d in self.lista:
            if d.id != id_actual and nombre and d.nombre.lower() == nombre: return "Departamento repetido"
        if id_actual is None and not nombre: return "Nombre obligatorio"
        return None
    def eliminar(self, id_registro):
        for empleado in self.empleados.leer():
            if empleado.departamento_id == id_registro:
                return False, "No se elimina: departamento asignado a empleados"
        return super().eliminar(id_registro)


class EmpleadoController(ControladorBase):
    MODELO, ARCHIVO = Empleado, "empleados.json"
    CAMPOS = {"nombre", "apellido", "email", "departamento_id"}
    def __init__(self, departamentos, archivo=None): self.departamentos = departamentos; super().__init__(archivo)
    def construir(self, d, i): return Empleado(i, d["nombre"].strip().title(), d["apellido"].strip().title(), d["email"].strip().lower(), int(d["departamento_id"]))
    def validar(self, d, id_actual=None):
        for c in ("nombre", "apellido", "email", "departamento_id"):
            if (id_actual is None or c in d) and not str(d.get(c, "")).strip(): return f"{c} obligatorio"
        if "departamento_id" in d:
            try: departamento_id = int(d["departamento_id"])
            except (TypeError, ValueError): return "departamento_id debe ser entero"
            if self.departamentos.obtener(departamento_id) is None: return "No existe el departamento"
        return None
    def normalizar(self, campo, valor): return int(valor) if campo == "departamento_id" else str(valor).strip().lower() if campo == "email" else str(valor).strip().title()
    def eliminar(self, id_registro):
        for nomina in self.nominas.leer():
            if nomina.empleado_id == id_registro:
                return False, "No se elimina: empleado tiene nóminas"
        return super().eliminar(id_registro)


class NominaController(ControladorBase):
    MODELO, ARCHIVO = Nomina, "nominas.json"
    CAMPOS = {"empleado_id", "periodo", "sueldo_base", "bonificacion", "descuento"}
    def __init__(self, empleados, archivo=None): self.empleados = empleados; super().__init__(archivo)
    def convertir_montos(self, d, requeridos):
        montos = {}
        for campo in ("sueldo_base", "bonificacion", "descuento"):
            if campo in d or campo in requeridos:
                try: valor = float(d.get(campo, 0))
                except (TypeError, ValueError): return None, f"{campo} debe ser numérico"
                if not math.isfinite(valor) or valor < 0 or valor > 1000000000: return None, f"{campo} debe ser finito y estar entre 0 y 1000000000"
                montos[campo] = valor
        return montos, None
    def validar(self, d, id_actual=None):
        for c in ("empleado_id", "periodo", "sueldo_base", "bonificacion", "descuento"):
            if (id_actual is None or c in d) and not str(d.get(c, "")).strip(): return f"{c} obligatorio"
        if "empleado_id" in d:
            try: empleado_id = int(d["empleado_id"])
            except (TypeError, ValueError): return "empleado_id debe ser entero"
            if self.empleados.obtener(empleado_id) is None: return "No existe el empleado"
        montos, error = self.convertir_montos(d, self.CAMPOS if id_actual is None else set())
        if error: return error
        empleado_id = int(d.get("empleado_id", self.obtener(id_actual).empleado_id if id_actual else 0))
        periodo = str(d.get("periodo", self.obtener(id_actual).periodo if id_actual else "")).strip()
        for n in self.lista:
            if n.id != id_actual and n.empleado_id == empleado_id and n.periodo == periodo: return "Ya existe nómina de ese empleado en ese periodo"
        actual = self.obtener(id_actual) if id_actual is not None else None
        sueldo = montos.get("sueldo_base", actual.sueldo_base if actual else 0)
        bono = montos.get("bonificacion", actual.bonificacion if actual else 0)
        descuento = montos.get("descuento", actual.descuento if actual else 0)
        if sueldo + bono - descuento < 0: return "El pago neto no puede ser negativo"
        return None
    def construir(self, d, i): return Nomina(i, int(d["empleado_id"]), d["periodo"].strip(), float(d["sueldo_base"]), float(d["bonificacion"]), float(d["descuento"]))
    def normalizar(self, campo, valor): return int(valor) if campo == "empleado_id" else str(valor).strip() if campo == "periodo" else float(valor)

# Inyectamos referencias después de instanciar controladores en main.py.
