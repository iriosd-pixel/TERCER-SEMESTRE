from abc import ABC, abstractmethod
import math
import os

from models import Departamento, Empleado, Nomina
from shared.json_manager import GestorJSON


CARPETA_DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


class CrudBase(ABC):
    """Define las siete operaciones de todo controlador."""

    @abstractmethod
    def leer(self):
        pass

    @abstractmethod
    def obtener(self, id_registro):
        pass

    @abstractmethod
    def buscar(self, texto):
        pass

    @abstractmethod
    def siguiente(self):
        pass

    @abstractmethod
    def crear(self, datos):
        pass

    @abstractmethod
    def actualizar(self, id_registro, datos):
        pass

    @abstractmethod
    def eliminar(self, id_registro):
        pass


# ---------------------------------------------------------------------
# Controlador de departamentos
# ---------------------------------------------------------------------
class DepartamentoController(CrudBase):
    CAMPOS = {"nombre"}

    def __init__(self, archivo=None, empleados=None):
        if archivo is None:
            archivo = os.path.join(CARPETA_DATA, "departamentos.json")
        self.gestor = GestorJSON(archivo)
        self.lista = []
        self.empleados = empleados
        for datos in self.gestor.leer():
            self.lista.append(Departamento.desde_diccionario(datos))

    def conectar_empleados(self, empleados):
        self.empleados = empleados

    def guardar(self):
        datos = []
        for departamento in self.lista:
            datos.append(departamento.a_diccionario())
        return self.gestor.guardar(datos)

    def validar(self, datos, id_actual=None):
        if "nombre" in datos and str(datos["nombre"]).strip() == "":
            return "El nombre es obligatorio"
        if id_actual is None and str(datos.get("nombre", "")).strip() == "":
            return "El nombre es obligatorio"

        nombre = " ".join(str(datos.get("nombre", "")).split()).casefold()
        for departamento in self.lista:
            nombre_guardado = " ".join(departamento.nombre.split()).casefold()
            if departamento.id != id_actual and nombre_guardado == nombre:
                return "Ya existe ese departamento"
        return None

    def leer(self):
        return self.lista

    def obtener(self, id_registro):
        for departamento in self.lista:
            if departamento.id == id_registro:
                return departamento
        return None

    def buscar(self, texto):
        termino = str(texto).strip().casefold()
        encontrados = []
        if termino == "":
            return encontrados
        for departamento in self.lista:
            if termino in departamento.nombre.casefold():
                encontrados.append(departamento)
        return encontrados

    def siguiente(self):
        mayor = 0
        for departamento in self.lista:
            if departamento.id > mayor:
                mayor = departamento.id
        return mayor + 1

    def crear(self, datos):
        desconocidos = set(datos) - self.CAMPOS
        if desconocidos:
            return False, f"Campos no válidos: {', '.join(sorted(desconocidos))}"
        error = self.validar(datos)
        if error:
            return False, error

        nombre = " ".join(str(datos["nombre"]).split()).title()
        departamento = Departamento(self.siguiente(), nombre)
        self.lista.append(departamento)
        if not self.guardar():
            self.lista.remove(departamento)
            return False, "No se pudo guardar el departamento"
        return True, f"Departamento creado: {departamento.etiqueta()}"

    def actualizar(self, id_registro, datos):
        departamento = self.obtener(id_registro)
        if departamento is None:
            return False, "No existe el departamento"
        if not datos:
            return False, "No se indicaron cambios"
        desconocidos = set(datos) - self.CAMPOS
        if desconocidos:
            return False, f"Campos no válidos: {', '.join(sorted(desconocidos))}"
        error = self.validar(datos, id_registro)
        if error:
            return False, error

        nombre_anterior = departamento.nombre
        departamento.nombre = " ".join(str(datos["nombre"]).split()).title()
        if not self.guardar():
            departamento.nombre = nombre_anterior
            return False, "No se pudo guardar el departamento"
        return True, f"Departamento {id_registro} actualizado"

    def eliminar(self, id_registro):
        departamento = self.obtener(id_registro)
        if departamento is None:
            return False, "No existe el departamento"
        if self.empleados is None:
            return False, "Conecte EmpleadoController antes de eliminar departamentos"

        for empleado in self.empleados.leer():
            if empleado.departamento_id == id_registro:
                return False, "No se elimina: el departamento tiene empleados"

        posicion = self.lista.index(departamento)
        self.lista.remove(departamento)
        if not self.guardar():
            self.lista.insert(posicion, departamento)
            return False, "No se pudo guardar la eliminación"
        return True, f"Departamento {id_registro} eliminado"


# ---------------------------------------------------------------------
# Controlador de empleados
# ---------------------------------------------------------------------
class EmpleadoController(CrudBase):
    CAMPOS = {"nombre", "apellido", "email", "departamento_id"}

    def __init__(self, departamentos, archivo=None, nominas=None):
        if archivo is None:
            archivo = os.path.join(CARPETA_DATA, "empleados.json")
        self.departamentos = departamentos
        self.nominas = nominas
        self.gestor = GestorJSON(archivo)
        self.lista = []
        for datos in self.gestor.leer():
            self.lista.append(Empleado.desde_diccionario(datos))

    def conectar_nominas(self, nominas):
        self.nominas = nominas

    def guardar(self):
        datos = []
        for empleado in self.lista:
            datos.append(empleado.a_diccionario())
        return self.gestor.guardar(datos)

    def validar(self, datos, id_actual=None):
        obligatorios = ("nombre", "apellido", "email", "departamento_id")
        for campo in obligatorios:
            if id_actual is None or campo in datos:
                if str(datos.get(campo, "")).strip() == "":
                    return f"El campo {campo} es obligatorio"

        if "departamento_id" in datos:
            try:
                departamento_id = int(datos["departamento_id"])
            except (TypeError, ValueError):
                return "El ID del departamento debe ser entero"
            if self.departamentos.obtener(departamento_id) is None:
                return "No existe ese departamento"

        if "email" in datos:
            email = str(datos["email"]).strip().casefold()
            for empleado in self.lista:
                if empleado.id != id_actual and empleado.email.casefold() == email:
                    return "Ese email ya está registrado"
        return None

    def leer(self):
        return self.lista

    def obtener(self, id_registro):
        for empleado in self.lista:
            if empleado.id == id_registro:
                return empleado
        return None

    def buscar(self, texto):
        termino = str(texto).strip().casefold()
        encontrados = []
        if termino == "":
            return encontrados
        for empleado in self.lista:
            campos = (empleado.nombre, empleado.apellido, empleado.email)
            for campo in campos:
                if termino in campo.casefold():
                    encontrados.append(empleado)
                    break
        return encontrados

    def siguiente(self):
        mayor = 0
        for empleado in self.lista:
            if empleado.id > mayor:
                mayor = empleado.id
        return mayor + 1

    def crear(self, datos):
        desconocidos = set(datos) - self.CAMPOS
        if desconocidos:
            return False, f"Campos no válidos: {', '.join(sorted(desconocidos))}"
        error = self.validar(datos)
        if error:
            return False, error

        empleado = Empleado(
            self.siguiente(),
            str(datos["nombre"]).strip().title(),
            str(datos["apellido"]).strip().title(),
            str(datos["email"]).strip().lower(),
            int(datos["departamento_id"]),
        )
        self.lista.append(empleado)
        if not self.guardar():
            self.lista.remove(empleado)
            return False, "No se pudo guardar el empleado"
        return True, f"Empleado creado: {empleado.etiqueta()}"

    def actualizar(self, id_registro, datos):
        empleado = self.obtener(id_registro)
        if empleado is None:
            return False, "No existe el empleado"
        if not datos:
            return False, "No se indicaron cambios"
        desconocidos = set(datos) - self.CAMPOS
        if desconocidos:
            return False, f"Campos no válidos: {', '.join(sorted(desconocidos))}"
        error = self.validar(datos, id_registro)
        if error:
            return False, error

        anteriores = {}
        for campo, valor in datos.items():
            anteriores[campo] = getattr(empleado, campo)
            if campo == "departamento_id":
                valor = int(valor)
            elif campo == "email":
                valor = str(valor).strip().lower()
            else:
                valor = str(valor).strip().title()
            setattr(empleado, campo, valor)

        if not self.guardar():
            for campo, valor in anteriores.items():
                setattr(empleado, campo, valor)
            return False, "No se pudo guardar la actualización"
        return True, f"Empleado {id_registro} actualizado"

    def eliminar(self, id_registro):
        empleado = self.obtener(id_registro)
        if empleado is None:
            return False, "No existe el empleado"
        if self.nominas is None:
            return False, "Conecte NominaController antes de eliminar empleados"

        for nomina in self.nominas.leer():
            if nomina.empleado_id == id_registro:
                return False, "No se elimina: el empleado tiene nóminas"

        posicion = self.lista.index(empleado)
        self.lista.remove(empleado)
        if not self.guardar():
            self.lista.insert(posicion, empleado)
            return False, "No se pudo guardar la eliminación"
        return True, f"Empleado {id_registro} eliminado"


# ---------------------------------------------------------------------
# Controlador de nóminas
# ---------------------------------------------------------------------
class NominaController(CrudBase):
    CAMPOS = {"empleado_id", "periodo", "sueldo_base", "bonificacion", "descuento"}

    def __init__(self, empleados, archivo=None):
        if archivo is None:
            archivo = os.path.join(CARPETA_DATA, "nominas.json")
        self.empleados = empleados
        self.gestor = GestorJSON(archivo)
        self.lista = []
        for datos in self.gestor.leer():
            self.lista.append(Nomina.desde_diccionario(datos))

    def guardar(self):
        datos = []
        for nomina in self.lista:
            datos.append(nomina.a_diccionario())
        return self.gestor.guardar(datos)

    def validar_montos(self, datos, actual=None):
        montos = {}
        nombres = ("sueldo_base", "bonificacion", "descuento")
        for campo in nombres:
            if campo in datos:
                valor_entrada = datos[campo]
            elif actual is not None:
                valor_entrada = getattr(actual, campo)
            else:
                valor_entrada = None

            if valor_entrada is None:
                return None, f"El campo {campo} es obligatorio"
            try:
                valor = float(valor_entrada)
            except (TypeError, ValueError):
                return None, f"El campo {campo} debe ser numérico"
            if not math.isfinite(valor) or valor < 0 or valor > 1000000000:
                return None, f"El campo {campo} está fuera del rango permitido"
            montos[campo] = valor
        return montos, None

    def validar(self, datos, id_actual=None):
        actual = None
        if id_actual is not None:
            actual = self.obtener(id_actual)
        obligatorios = ("empleado_id", "periodo")
        for campo in obligatorios:
            if campo in datos and str(datos[campo]).strip() == "":
                return f"El campo {campo} es obligatorio"
            if actual is None and campo not in datos:
                return f"El campo {campo} es obligatorio"

        empleado_id = datos.get("empleado_id")
        if empleado_id is None and actual is not None:
            empleado_id = actual.empleado_id
        try:
            empleado_id = int(empleado_id)
        except (TypeError, ValueError):
            return "El ID del empleado debe ser entero"
        if self.empleados.obtener(empleado_id) is None:
            return "No existe ese empleado"

        periodo = datos.get("periodo")
        if periodo is None and actual is not None:
            periodo = actual.periodo
        periodo = " ".join(str(periodo).split())
        if periodo == "":
            return "El periodo es obligatorio"

        montos, error = self.validar_montos(datos, actual)
        if error:
            return error
        pago_neto = montos["sueldo_base"] + montos["bonificacion"] - montos["descuento"]
        if pago_neto < 0:
            return "El pago neto no puede ser negativo"

        for nomina in self.lista:
            if (nomina.id != id_actual
                    and nomina.empleado_id == empleado_id
                    and nomina.periodo.casefold() == periodo.casefold()):
                return "Ya existe una nómina de ese empleado en ese periodo"
        return None

    def leer(self):
        return self.lista

    def obtener(self, id_registro):
        for nomina in self.lista:
            if nomina.id == id_registro:
                return nomina
        return None

    def buscar(self, texto):
        termino = str(texto).strip().casefold()
        encontrados = []
        if termino == "":
            return encontrados
        for nomina in self.lista:
            if termino in nomina.etiqueta().casefold():
                encontrados.append(nomina)
        return encontrados

    def siguiente(self):
        mayor = 0
        for nomina in self.lista:
            if nomina.id > mayor:
                mayor = nomina.id
        return mayor + 1

    def crear(self, datos):
        desconocidos = set(datos) - self.CAMPOS
        if desconocidos:
            return False, f"Campos no válidos: {', '.join(sorted(desconocidos))}"
        error = self.validar(datos)
        if error:
            return False, error
        montos, _error = self.validar_montos(datos)
        periodo = " ".join(str(datos["periodo"]).split())

        nomina = Nomina(
            self.siguiente(),
            int(datos["empleado_id"]),
            periodo,
            montos["sueldo_base"],
            montos["bonificacion"],
            montos["descuento"],
        )
        self.lista.append(nomina)
        if not self.guardar():
            self.lista.remove(nomina)
            return False, "No se pudo guardar la nómina"
        return True, f"Nómina creada: {nomina.etiqueta()}"

    def actualizar(self, id_registro, datos):
        nomina = self.obtener(id_registro)
        if nomina is None:
            return False, "No existe la nómina"
        if not datos:
            return False, "No se indicaron cambios"
        desconocidos = set(datos) - self.CAMPOS
        if desconocidos:
            return False, f"Campos no válidos: {', '.join(sorted(desconocidos))}"
        error = self.validar(datos, id_registro)
        if error:
            return False, error

        anteriores = {}
        for campo, valor in datos.items():
            anteriores[campo] = getattr(nomina, campo)
            if campo == "empleado_id":
                valor = int(valor)
            elif campo == "periodo":
                valor = " ".join(str(valor).split())
            else:
                valor = float(valor)
            setattr(nomina, campo, valor)

        if not self.guardar():
            for campo, valor in anteriores.items():
                setattr(nomina, campo, valor)
            return False, "No se pudo guardar la actualización"
        return True, f"Nómina {id_registro} actualizada"

    def eliminar(self, id_registro):
        nomina = self.obtener(id_registro)
        if nomina is None:
            return False, "No existe la nómina"
        posicion = self.lista.index(nomina)
        self.lista.remove(nomina)
        if not self.guardar():
            self.lista.insert(posicion, nomina)
            return False, "No se pudo guardar la eliminación"
        return True, f"Nómina {id_registro} eliminada"
