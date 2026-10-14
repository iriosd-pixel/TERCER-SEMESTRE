from abc import ABC, abstractmethod
from datetime import date, time
import os

from models import Cita, Medico, Paciente
from shared.json_manager import GestorJSON


CARPETA_DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


class CrudBase(ABC):
    """Define las siete operaciones del controlador."""

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
# Controlador de pacientes
# ---------------------------------------------------------------------
class PacienteController(CrudBase):
    CAMPOS = {"nombre", "apellido", "email", "telefono"}

    def __init__(self, archivo=None, citas=None):
        if archivo is None:
            archivo = os.path.join(CARPETA_DATA, "pacientes.json")
        self.gestor = GestorJSON(archivo)
        self.lista = []
        self.citas = citas
        for datos in self.gestor.leer():
            self.lista.append(Paciente.desde_diccionario(datos))

    def conectar_citas(self, citas):
        self.citas = citas

    def guardar(self):
        datos = []
        for paciente in self.lista:
            datos.append(paciente.a_diccionario())
        return self.gestor.guardar(datos)

    def validar(self, datos, id_actual=None):
        for campo in self.CAMPOS:
            if campo in datos and str(datos[campo]).strip() == "":
                return f"El campo {campo} es obligatorio"
        if id_actual is None:
            for campo in self.CAMPOS:
                if str(datos.get(campo, "")).strip() == "":
                    return f"El campo {campo} es obligatorio"
        return None

    def leer(self):
        return self.lista

    def obtener(self, id_registro):
        for paciente in self.lista:
            if paciente.id == id_registro:
                return paciente
        return None

    def buscar(self, texto):
        termino = str(texto).strip().casefold()
        encontrados = []
        if termino == "":
            return encontrados
        for paciente in self.lista:
            campos = (paciente.nombre, paciente.apellido, paciente.email, paciente.telefono)
            for campo in campos:
                if termino in str(campo).casefold():
                    encontrados.append(paciente)
                    break
        return encontrados

    def siguiente(self):
        mayor = 0
        for paciente in self.lista:
            if paciente.id > mayor:
                mayor = paciente.id
        return mayor + 1

    def crear(self, datos):
        desconocidos = set(datos) - self.CAMPOS
        if desconocidos:
            return False, f"Campos no válidos: {', '.join(sorted(desconocidos))}"
        error = self.validar(datos)
        if error:
            return False, error

        paciente = Paciente(
            self.siguiente(),
            str(datos["nombre"]).strip().title(),
            str(datos["apellido"]).strip().title(),
            str(datos["email"]).strip().lower(),
            str(datos["telefono"]).strip(),
        )
        self.lista.append(paciente)
        if not self.guardar():
            self.lista.remove(paciente)
            return False, "No se pudo guardar el paciente"
        return True, f"Paciente creado: {paciente.etiqueta()}"

    def actualizar(self, id_registro, datos):
        paciente = self.obtener(id_registro)
        if paciente is None:
            return False, "No existe el paciente"
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
            anteriores[campo] = getattr(paciente, campo)
            valor = str(valor).strip()
            if campo == "email":
                valor = valor.lower()
            elif campo != "telefono":
                valor = valor.title()
            setattr(paciente, campo, valor)
        if not self.guardar():
            for campo, valor in anteriores.items():
                setattr(paciente, campo, valor)
            return False, "No se pudo guardar la actualización"
        return True, f"Paciente {id_registro} actualizado"

    def eliminar(self, id_registro):
        paciente = self.obtener(id_registro)
        if paciente is None:
            return False, "No existe el paciente"
        if self.citas is None:
            return False, "Conecte CitaController antes de eliminar pacientes"
        for cita in self.citas.leer():
            if cita.paciente_id == id_registro:
                return False, "No se elimina: el paciente tiene citas"

        posicion = self.lista.index(paciente)
        self.lista.remove(paciente)
        if not self.guardar():
            self.lista.insert(posicion, paciente)
            return False, "No se pudo guardar la eliminación"
        return True, f"Paciente {id_registro} eliminado"


# ---------------------------------------------------------------------
# Controlador de médicos
# ---------------------------------------------------------------------
class MedicoController(CrudBase):
    CAMPOS = {"nombre", "apellido", "email", "especialidad"}

    def __init__(self, archivo=None, citas=None):
        if archivo is None:
            archivo = os.path.join(CARPETA_DATA, "medicos.json")
        self.gestor = GestorJSON(archivo)
        self.lista = []
        self.citas = citas
        for datos in self.gestor.leer():
            self.lista.append(Medico.desde_diccionario(datos))

    def conectar_citas(self, citas):
        self.citas = citas

    def guardar(self):
        datos = []
        for medico in self.lista:
            datos.append(medico.a_diccionario())
        return self.gestor.guardar(datos)

    def validar(self, datos, id_actual=None):
        for campo in self.CAMPOS:
            if campo in datos and str(datos[campo]).strip() == "":
                return f"El campo {campo} es obligatorio"
        if id_actual is None:
            for campo in self.CAMPOS:
                if str(datos.get(campo, "")).strip() == "":
                    return f"El campo {campo} es obligatorio"
        return None

    def leer(self):
        return self.lista

    def obtener(self, id_registro):
        for medico in self.lista:
            if medico.id == id_registro:
                return medico
        return None

    def buscar(self, texto):
        termino = str(texto).strip().casefold()
        encontrados = []
        if termino == "":
            return encontrados
        for medico in self.lista:
            campos = (medico.nombre, medico.apellido, medico.email, medico.especialidad)
            for campo in campos:
                if termino in str(campo).casefold():
                    encontrados.append(medico)
                    break
        return encontrados

    def siguiente(self):
        mayor = 0
        for medico in self.lista:
            if medico.id > mayor:
                mayor = medico.id
        return mayor + 1

    def crear(self, datos):
        desconocidos = set(datos) - self.CAMPOS
        if desconocidos:
            return False, f"Campos no válidos: {', '.join(sorted(desconocidos))}"
        error = self.validar(datos)
        if error:
            return False, error

        medico = Medico(
            self.siguiente(),
            str(datos["nombre"]).strip().title(),
            str(datos["apellido"]).strip().title(),
            str(datos["email"]).strip().lower(),
            str(datos["especialidad"]).strip().title(),
        )
        self.lista.append(medico)
        if not self.guardar():
            self.lista.remove(medico)
            return False, "No se pudo guardar el médico"
        return True, f"Médico creado: {medico.etiqueta()}"

    def actualizar(self, id_registro, datos):
        medico = self.obtener(id_registro)
        if medico is None:
            return False, "No existe el médico"
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
            anteriores[campo] = getattr(medico, campo)
            valor = str(valor).strip()
            if campo == "email":
                valor = valor.lower()
            else:
                valor = valor.title()
            setattr(medico, campo, valor)
        if not self.guardar():
            for campo, valor in anteriores.items():
                setattr(medico, campo, valor)
            return False, "No se pudo guardar la actualización"
        return True, f"Médico {id_registro} actualizado"

    def eliminar(self, id_registro):
        medico = self.obtener(id_registro)
        if medico is None:
            return False, "No existe el médico"
        if self.citas is None:
            return False, "Conecte CitaController antes de eliminar médicos"
        for cita in self.citas.leer():
            if cita.medico_id == id_registro:
                return False, "No se elimina: el médico tiene citas"

        posicion = self.lista.index(medico)
        self.lista.remove(medico)
        if not self.guardar():
            self.lista.insert(posicion, medico)
            return False, "No se pudo guardar la eliminación"
        return True, f"Médico {id_registro} eliminado"


# ---------------------------------------------------------------------
# Controlador de citas
# ---------------------------------------------------------------------
class CitaController(CrudBase):
    CAMPOS = {"paciente_id", "medico_id", "fecha", "hora"}

    def __init__(self, pacientes, medicos, archivo=None):
        if archivo is None:
            archivo = os.path.join(CARPETA_DATA, "citas.json")
        self.pacientes = pacientes
        self.medicos = medicos
        self.gestor = GestorJSON(archivo)
        self.lista = []
        for datos in self.gestor.leer():
            cita = Cita.desde_diccionario(datos)
            fecha, hora, error = self.normalizar_fecha_hora(cita.fecha, cita.hora)
            if error:
                raise ValueError(f"La cita {cita.id} tiene fecha u hora inválida")
            cita.fecha = fecha
            cita.hora = hora
            self.lista.append(cita)

    def guardar(self):
        datos = []
        for cita in self.lista:
            datos.append(cita.a_diccionario())
        return self.gestor.guardar(datos)

    def normalizar_fecha_hora(self, fecha, hora):
        try:
            fecha_normalizada = date.fromisoformat(str(fecha).strip()).isoformat()
            hora_objeto = time.fromisoformat(str(hora).strip())
        except (TypeError, ValueError):
            return None, None, "Use fecha YYYY-MM-DD y una hora válida"

        if hora_objeto.second == 0 and hora_objeto.microsecond == 0:
            hora_normalizada = hora_objeto.isoformat(timespec="minutes")
        else:
            hora_normalizada = hora_objeto.isoformat()
        return fecha_normalizada, hora_normalizada, None

    def validar(self, datos, id_actual=None):
        actual = None
        if id_actual is not None:
            actual = self.obtener(id_actual)
        paciente_id = datos.get("paciente_id")
        medico_id = datos.get("medico_id")
        fecha = datos.get("fecha")
        hora = datos.get("hora")

        if actual is not None:
            if paciente_id is None:
                paciente_id = actual.paciente_id
            if medico_id is None:
                medico_id = actual.medico_id
            if fecha is None:
                fecha = actual.fecha
            if hora is None:
                hora = actual.hora

        try:
            paciente_id = int(paciente_id)
            medico_id = int(medico_id)
        except (TypeError, ValueError):
            return "Los IDs de paciente y médico deben ser enteros"
        if self.pacientes.obtener(paciente_id) is None:
            return "No existe ese paciente"
        if self.medicos.obtener(medico_id) is None:
            return "No existe ese médico"

        fecha, hora, error = self.normalizar_fecha_hora(fecha, hora)
        if error:
            return error
        for cita in self.lista:
            if cita.id == id_actual:
                continue
            mismo_horario = cita.fecha == fecha and cita.hora == hora
            if mismo_horario and cita.medico_id == medico_id:
                return "El médico ya tiene una cita en ese horario"
            if mismo_horario and cita.paciente_id == paciente_id:
                return "El paciente ya tiene una cita en ese horario"
        return None

    def leer(self):
        return self.lista

    def obtener(self, id_registro):
        for cita in self.lista:
            if cita.id == id_registro:
                return cita
        return None

    def buscar(self, texto):
        termino = str(texto).strip().casefold()
        encontrados = []
        if termino == "":
            return encontrados
        for cita in self.lista:
            if termino in cita.etiqueta().casefold():
                encontrados.append(cita)
        return encontrados

    def siguiente(self):
        mayor = 0
        for cita in self.lista:
            if cita.id > mayor:
                mayor = cita.id
        return mayor + 1

    def crear(self, datos):
        desconocidos = set(datos) - self.CAMPOS
        if desconocidos:
            return False, f"Campos no válidos: {', '.join(sorted(desconocidos))}"
        for campo in self.CAMPOS:
            if campo not in datos or str(datos[campo]).strip() == "":
                return False, f"El campo {campo} es obligatorio"
        error = self.validar(datos)
        if error:
            return False, error

        fecha, hora, _error = self.normalizar_fecha_hora(datos["fecha"], datos["hora"])
        cita = Cita(
            self.siguiente(),
            int(datos["paciente_id"]),
            int(datos["medico_id"]),
            fecha,
            hora,
        )
        self.lista.append(cita)
        if not self.guardar():
            self.lista.remove(cita)
            return False, "No se pudo guardar la cita"
        return True, f"Cita creada: {cita.etiqueta()}"

    def actualizar(self, id_registro, datos):
        cita = self.obtener(id_registro)
        if cita is None:
            return False, "No existe la cita"
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
            anteriores[campo] = getattr(cita, campo)
            if campo in ("paciente_id", "medico_id"):
                valor = int(valor)
            setattr(cita, campo, valor)
        cita.fecha, cita.hora, _error = self.normalizar_fecha_hora(cita.fecha, cita.hora)

        if not self.guardar():
            for campo, valor in anteriores.items():
                setattr(cita, campo, valor)
            return False, "No se pudo guardar la actualización"
        return True, f"Cita {id_registro} actualizada"

    def eliminar(self, id_registro):
        cita = self.obtener(id_registro)
        if cita is None:
            return False, "No existe la cita"
        posicion = self.lista.index(cita)
        self.lista.remove(cita)
        if not self.guardar():
            self.lista.insert(posicion, cita)
            return False, "No se pudo guardar la eliminación"
        return True, f"Cita {id_registro} eliminada"
