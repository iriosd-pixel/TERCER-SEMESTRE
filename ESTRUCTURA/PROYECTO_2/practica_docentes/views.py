from abc import ABC, abstractmethod
import os

from models import Docente
from shared.herramientas import es_email_valido
from shared.json_manager import GestorJSON


CARPETA_DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


class CrudBase(ABC):
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


class DocenteController(CrudBase):
    def __init__(self, archivo=None):
        if archivo is None:
            archivo = os.path.join(CARPETA_DATA, "docente.json")

        self.gestor = GestorJSON(archivo)
        self.lista = []

        for datos in self.gestor.leer():
            self.lista.append(Docente.desde_diccionario(datos))

    def guardar(self):
        datos = []

        for docente in self.lista:
            datos.append(docente.a_diccionario())

        return self.gestor.guardar(datos)

    def validar(self, datos, id_actual=None):
        obligatorios = ("nombre", "apellido", "email", "especialidad")

        for campo in obligatorios:
            if id_actual is None or campo in datos:
                if str(datos.get(campo, "")).strip() == "":
                    return f"El campo {campo} es obligatorio"

        if "email" in datos:
            email = str(datos["email"]).strip().lower()

            if not es_email_valido(email):
                return f"Email inválido: '{email}'"

            # CONJUNTO: guarda emails normalizados para evitar duplicados.
            emails_usados = set()

            for docente in self.lista:
                if docente.id != id_actual:
                    emails_usados.add(docente.email.strip().lower())

            if email in emails_usados:
                return "Ese email ya está registrado"

        return None

    def leer(self):
        return self.lista

    def obtener(self, id_registro):
        # CONJUNTO: reúne los IDs registrados para comprobar la pertenencia.
        ids = set()

        for docente in self.lista:
            ids.add(docente.id)

        if id_registro not in ids:
            return None

        for docente in self.lista:
            if docente.id == id_registro:
                return docente

        return None

    def buscar(self, texto):
        texto = str(texto).strip().lower()
        encontrados = []

        if texto == "":
            return encontrados

        for docente in self.lista:
            # TUPLA: reúne los campos que se revisan en la búsqueda.
            campos = (
                docente.nombre,
                docente.apellido,
                docente.email,
                docente.especialidad,
            )

            for campo in campos:
                if texto in str(campo).lower():
                    encontrados.append(docente)
                    break

        return encontrados

    def siguiente(self):
        mayor = 0

        for docente in self.lista:
            if docente.id > mayor:
                mayor = docente.id

        return mayor + 1

    def crear(self, datos):
        error = self.validar(datos)

        if error:
            return False, error

        docente = Docente(
            self.siguiente(),
            str(datos["nombre"]).strip().title(),
            str(datos["apellido"]).strip().title(),
            str(datos["email"]).strip().lower(),
            str(datos["especialidad"]).strip().title(),
        )
        self.lista.append(docente)

        if not self.guardar():
            self.lista.remove(docente)
            return False, "No se pudo guardar el docente"

        # TUPLA: devuelve el éxito y el mensaje del resultado.
        return True, f"Docente creado: {docente.etiqueta()}"

    def actualizar(self, id_registro, datos):
        docente = self.obtener(id_registro)

        if docente is None:
            return False, "No existe el docente"

        if not datos:
            return False, "No se indicó ningún cambio"

        # CONJUNTO: identifica campos que no se pueden modificar.
        permitidos = {"nombre", "apellido", "email", "especialidad"}
        desconocidos = set(datos) - permitidos

        if desconocidos:
            return False, f"Campos no válidos: {', '.join(sorted(desconocidos))}"

        error = self.validar(datos, docente.id)

        if error:
            return False, error

        anteriores = {}

        for campo, valor in datos.items():
            anteriores[campo] = getattr(docente, campo)
            valor = str(valor).strip()

            if campo in ("nombre", "apellido", "especialidad"):
                valor = valor.title()
            elif campo == "email":
                valor = valor.lower()

            setattr(docente, campo, valor)

        if not self.guardar():
            for campo, valor in anteriores.items():
                setattr(docente, campo, valor)

            return False, "No se pudo actualizar el docente"

        # TUPLA: devuelve el éxito y el mensaje del resultado.
        return True, f"Docente {docente.id} actualizado"

    def eliminar(self, id_registro):
        docente = self.obtener(id_registro)

        if docente is None:
            return False, "No existe el docente"

        posicion = self.lista.index(docente)
        self.lista.remove(docente)

        if not self.guardar():
            self.lista.insert(posicion, docente)
            return False, "No se pudo eliminar el docente"

        # TUPLA: devuelve el éxito y el mensaje del resultado.
        return True, f"Docente {docente.id} eliminado"

    def especialidades(self):
        # CONJUNTO: conserva cada especialidad una sola vez.
        especialidades = set()

        for docente in self.lista:
            if docente.especialidad:
                especialidades.add(docente.especialidad)

        return sorted(especialidades)
