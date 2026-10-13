from abc import ABC, abstractmethod

from models import Estudiante, Materia, Matricula
from shared.json_manager import GestorJSON
from shared.herramientas import es_email_valido


# =====================================================================
# CLASE BASE ABSTRACTA
# =====================================================================
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


# =====================================================================
# CONTROLADOR DE ESTUDIANTES
# =====================================================================
class EstudianteController(CrudBase):

    def __init__(self, archivo="data/estudiantes.json"):
        self.gestor = GestorJSON(archivo)
        self.lista = []

        for datos in self.gestor.leer():
            self.lista.append(Estudiante.desde_diccionario(datos))

    def guardar(self):
        datos = []

        for estudiante in self.lista:
            datos.append(estudiante.a_diccionario())

        return self.gestor.guardar(datos)

    def validar(self, datos, id_actual=None):
        obligatorios = ("nombre", "apellido", "email", "carnet")

        for campo in obligatorios:
            if id_actual is None or campo in datos:
                if str(datos.get(campo, "")).strip() == "":
                    return f"El campo {campo} es obligatorio"

        if "email" in datos:
            email = str(datos["email"]).strip().lower()

            if not es_email_valido(email):
                return f"Email inválido: '{email}'"

            # CONJUNTO: permite detectar emails repetidos.
            emails_usados = set()

            for estudiante in self.lista:
                if estudiante.id != id_actual:
                    emails_usados.add(estudiante.email.strip().lower())

            if email in emails_usados:
                return "Ese email ya está registrado"

        if "carnet" in datos:
            carnet = str(datos["carnet"]).strip().upper()

            # CONJUNTO: permite detectar carnets repetidos.
            carnets_usados = set()

            for estudiante in self.lista:
                if estudiante.id != id_actual:
                    carnets_usados.add(estudiante.carnet.strip().upper())

            if carnet in carnets_usados:
                return "Ese carnet ya está registrado"

        return None

    def leer(self):
        return self.lista

    def obtener(self, id_registro):
        # CONJUNTO: permite comprobar si el id está registrado.
        ids = set()

        for estudiante in self.lista:
            ids.add(estudiante.id)

        if id_registro not in ids:
            return None

        for estudiante in self.lista:
            if estudiante.id == id_registro:
                return estudiante

        return None

    def buscar(self, texto):
        texto = str(texto).strip().lower()
        encontrados = []

        if texto == "":
            return encontrados

        for estudiante in self.lista:
            # TUPLA: reúne los campos que se revisan en la búsqueda.
            campos = (
                estudiante.nombre,
                estudiante.apellido,
                estudiante.email,
                estudiante.carnet,
                estudiante.carrera
            )

            for campo in campos:
                if texto in str(campo).lower():
                    encontrados.append(estudiante)
                    break

        return encontrados

    def siguiente(self):
        mayor = 0

        for estudiante in self.lista:
            if estudiante.id > mayor:
                mayor = estudiante.id

        return mayor + 1

    def crear(self, datos):
        error = self.validar(datos)

        if error:
            return False, error

        estudiante = Estudiante(
            self.siguiente(),
            str(datos["nombre"]).strip().title(),
            str(datos["apellido"]).strip().title(),
            str(datos["email"]).strip().lower(),
            str(datos["carnet"]).strip().upper(),
            str(datos.get("carrera", "")).strip().title()
        )

        self.lista.append(estudiante)

        if not self.guardar():
            self.lista.remove(estudiante)
            return False, "No se pudo guardar el estudiante"

        # TUPLA: comunica el resultado y su mensaje.
        return True, f"Estudiante creado: {estudiante.etiqueta()}"

    def actualizar(self, id_registro, datos):
        estudiante = self.obtener(id_registro)

        if estudiante is None:
            return False, "No existe el estudiante"

        if not datos:
            return False, "No se indicó ningún cambio"

        # CONJUNTO: identifica campos que no se permiten modificar.
        permitidos = {"nombre", "apellido", "email", "carnet", "carrera"}
        desconocidos = set(datos) - permitidos

        if desconocidos:
            return False, f"Campos no válidos: {', '.join(sorted(desconocidos))}"

        error = self.validar(datos, estudiante.id)

        if error:
            return False, error

        anteriores = {}

        for campo, valor in datos.items():
            anteriores[campo] = getattr(estudiante, campo)
            valor = str(valor).strip()

            if campo in ("nombre", "apellido", "carrera"):
                valor = valor.title()
            elif campo == "email":
                valor = valor.lower()
            elif campo == "carnet":
                valor = valor.upper()

            setattr(estudiante, campo, valor)

        if not self.guardar():
            for campo, valor in anteriores.items():
                setattr(estudiante, campo, valor)

            return False, "No se pudo actualizar el estudiante"

        return True, f"Estudiante {estudiante.id} actualizado"

    def eliminar(self, id_registro):
        estudiante = self.obtener(id_registro)

        if estudiante is None:
            return False, "No existe el estudiante"

        posicion = self.lista.index(estudiante)
        self.lista.remove(estudiante)

        if not self.guardar():
            self.lista.insert(posicion, estudiante)
            return False, "No se pudo eliminar el estudiante"

        return True, f"Estudiante {estudiante.id} eliminado"

    def carreras(self):
        # CONJUNTO: reúne las carreras sin repetirlas.
        carreras = set()

        for estudiante in self.lista:
            if estudiante.carrera:
                carreras.add(estudiante.carrera)

        return sorted(carreras)


# =====================================================================
# CONTROLADOR DE MATERIAS
# =====================================================================
class MateriaController(CrudBase):

    def __init__(self, archivo="data/materias.json"):
        self.gestor = GestorJSON(archivo)
        self.lista = []

        for datos in self.gestor.leer():
            self.lista.append(Materia.desde_diccionario(datos))

    def guardar(self):
        datos = []

        for materia in self.lista:
            datos.append(materia.a_diccionario())

        return self.gestor.guardar(datos)

    def validar(self, datos, id_actual=None):
        for campo in ("nombre", "codigo"):
            if id_actual is None or campo in datos:
                if str(datos.get(campo, "")).strip() == "":
                    return f"El campo {campo} es obligatorio"

        if "codigo" in datos:
            codigo = str(datos["codigo"]).strip().upper()

            # CONJUNTO: permite detectar códigos repetidos.
            codigos_usados = set()

            for materia in self.lista:
                if materia.id != id_actual:
                    codigos_usados.add(str(materia.codigo).strip().upper())

            if codigo in codigos_usados:
                return "Ese código ya está registrado"

        if id_actual is None or "creditos" in datos:
            try:
                creditos = int(str(datos.get("creditos", 0)).strip())
            except (TypeError, ValueError):
                return "Los créditos deben ser un número entero"

            if not 1 <= creditos <= 10:
                return "Los créditos deben estar entre 1 y 10"

        if id_actual is None or "cupos" in datos:
            try:
                cupos = int(str(datos.get("cupos", 0)).strip())
            except (TypeError, ValueError):
                return "Los cupos deben ser un número entero"

            if not 0 <= cupos <= Materia.CUPOS_MAXIMOS:
                return f"Los cupos deben estar entre 0 y {Materia.CUPOS_MAXIMOS}"

        return None

    def leer(self):
        return self.lista

    def obtener(self, id_registro):
        # CONJUNTO: permite comprobar si el id está registrado.
        ids = set()

        for materia in self.lista:
            ids.add(materia.id)

        if id_registro not in ids:
            return None

        for materia in self.lista:
            if materia.id == id_registro:
                return materia

        return None

    def buscar(self, texto):
        texto = str(texto).strip().lower()
        encontrados = []

        if texto == "":
            return encontrados

        for materia in self.lista:
            # TUPLA: reúne los campos que se revisan en la búsqueda.
            campos = (materia.nombre, materia.codigo)

            for campo in campos:
                if texto in str(campo).lower():
                    encontrados.append(materia)
                    break

        return encontrados

    def siguiente(self):
        mayor = 0

        for materia in self.lista:
            if materia.id > mayor:
                mayor = materia.id

        return mayor + 1

    def crear(self, datos):
        error = self.validar(datos)

        if error:
            return False, error

        materia = Materia(
            self.siguiente(),
            str(datos["nombre"]).strip().title(),
            str(datos["codigo"]).strip().upper(),
            int(str(datos["creditos"]).strip()),
            int(str(datos.get("cupos", 0)).strip())
        )

        self.lista.append(materia)

        if not self.guardar():
            self.lista.remove(materia)
            return False, "No se pudo guardar la materia"

        # TUPLA: comunica el resultado y su mensaje.
        return True, f"Materia creada: {materia.etiqueta()}"

    def actualizar(self, id_registro, datos):
        materia = self.obtener(id_registro)

        if materia is None:
            return False, "No existe la materia"

        if not datos:
            return False, "No se indicó ningún cambio"

        # CONJUNTO: identifica campos que no se permiten modificar.
        permitidos = {"nombre", "codigo", "creditos", "cupos"}
        desconocidos = set(datos) - permitidos

        if desconocidos:
            return False, f"Campos no válidos: {', '.join(sorted(desconocidos))}"

        error = self.validar(datos, materia.id)

        if error:
            return False, error

        anteriores = {}

        for campo, valor in datos.items():
            anteriores[campo] = getattr(materia, campo)

            if campo == "nombre":
                valor = str(valor).strip().title()
            elif campo == "codigo":
                valor = str(valor).strip().upper()
            else:
                valor = int(str(valor).strip())

            setattr(materia, campo, valor)

        if not self.guardar():
            for campo, valor in anteriores.items():
                setattr(materia, campo, valor)

            return False, "No se pudo actualizar la materia"

        return True, f"Materia {materia.id} actualizada"

    def eliminar(self, id_registro):
        materia = self.obtener(id_registro)

        if materia is None:
            return False, "No existe la materia"

        posicion = self.lista.index(materia)
        self.lista.remove(materia)

        if not self.guardar():
            self.lista.insert(posicion, materia)
            return False, "No se pudo eliminar la materia"

        return True, f"Materia {materia.id} eliminada"

    def materias_sin_cupo(self):
        sin_cupo = []

        for materia in self.lista:
            if not materia.hay_cupo():
                sin_cupo.append(materia)

        return sin_cupo


# =====================================================================
# CONTROLADOR DE MATRÍCULAS
# =====================================================================
class MatriculaController(CrudBase):

    def __init__(
        self,
        estudiantes,
        materias,
        archivo="data/matriculas.json"
    ):
        # Recibe los mismos controladores que utiliza main.py.
        self.estudiantes = estudiantes
        self.materias = materias
        self.gestor = GestorJSON(archivo)
        self.lista = []

        for datos in self.gestor.leer():
            self.lista.append(Matricula.desde_diccionario(datos))

    def guardar(self):
        datos = []

        for matricula in self.lista:
            datos.append(matricula.a_diccionario())

        return self.gestor.guardar(datos)

    def validar(self, datos):
        try:
            estudiante_id = int(str(datos.get("estudiante_id", 0)).strip())
            materia_id = int(str(datos.get("materia_id", 0)).strip())
        except (TypeError, ValueError):
            return "Los IDs deben ser números enteros"

        periodo = str(datos.get("periodo", "")).strip()
        nota = datos.get("nota", 0)

        if periodo == "":
            return "El periodo es obligatorio"

        if not Materia.es_nota_valida(nota):
            return "La nota debe estar entre 0 y 20"

        # CONJUNTO: permite comprobar que el estudiante exista.
        ids_estudiantes = set()

        for estudiante in self.estudiantes.leer():
            ids_estudiantes.add(estudiante.id)

        if estudiante_id not in ids_estudiantes:
            return "No existe el estudiante"

        # CONJUNTO: permite comprobar que la materia exista.
        ids_materias = set()

        for materia in self.materias.leer():
            ids_materias.add(materia.id)

        if materia_id not in ids_materias:
            return "No existe la materia"

        materia = self.materias.obtener(materia_id)

        if not materia.hay_cupo():
            return "La materia no tiene cupos disponibles"

        for matricula in self.lista:
            if (
                matricula.estudiante_id == estudiante_id
                and matricula.materia_id == materia_id
                and matricula.periodo == periodo
            ):
                return "El estudiante ya está matriculado en esa materia y periodo"

        return None

    def leer(self):
        return self.lista

    def obtener(self, id_registro):
        for matricula in self.lista:
            if matricula.id == id_registro:
                return matricula

        return None

    def buscar(self, texto):
        texto = str(texto).strip().lower()
        encontradas = []

        if texto == "":
            return encontradas

        for matricula in self.lista:
            # TUPLA: reúne los campos que se revisan en la búsqueda.
            campos = (matricula.periodo, matricula.fecha)

            for campo in campos:
                if texto in str(campo).lower():
                    encontradas.append(matricula)
                    break

        return encontradas

    def siguiente(self):
        mayor = 0

        for matricula in self.lista:
            if matricula.id > mayor:
                mayor = matricula.id

        return mayor + 1

    def crear(self, datos):
        error = self.validar(datos)

        if error:
            return False, error

        materia_id = int(str(datos["materia_id"]).strip())
        materia = self.materias.obtener(materia_id)

        matricula = Matricula(
            self.siguiente(),
            int(str(datos["estudiante_id"]).strip()),
            materia.id,
            str(datos["periodo"]).strip(),
            float(datos.get("nota", 0))
        )

        cupos_anteriores = materia.cupos
        materia.ocupar_cupo()

        if not self.materias.guardar():
            materia.cupos = cupos_anteriores
            return False, "No se pudieron guardar los cupos"

        self.lista.append(matricula)

        if not self.guardar():
            self.lista.remove(matricula)
            materia.cupos = cupos_anteriores

            if not self.materias.guardar():
                return False, "No se guardó la matrícula ni se pudo restaurar el cupo"

            return False, "No se pudo guardar la matrícula"

        # TUPLA: comunica el resultado y su mensaje.
        return True, f"Matrícula {matricula.id} creada"

    def actualizar(self, id_registro, datos):
        # Implementa el método obligatorio; solo permite cambiar la nota.
        if not datos:
            return False, "No se indicó ningún cambio"

        desconocidos = set(datos) - {"nota"}

        if desconocidos:
            return False, "Solo se puede actualizar la nota"

        return self.registrar_nota(id_registro, datos["nota"])

    def eliminar(self, id_registro):
        matricula = self.obtener(id_registro)

        if matricula is None:
            return False, "No existe la matrícula"

        materia = self.materias.obtener(matricula.materia_id)

        if materia is None:
            return False, "No existe la materia de esa matrícula"

        cupos_anteriores = materia.cupos
        materia.liberar_cupo()

        if not self.materias.guardar():
            materia.cupos = cupos_anteriores
            return False, "No se pudo guardar la devolución del cupo"

        posicion = self.lista.index(matricula)
        self.lista.remove(matricula)

        if not self.guardar():
            self.lista.insert(posicion, matricula)
            materia.cupos = cupos_anteriores

            if not self.materias.guardar():
                return False, "No se retiró la matrícula ni se pudo restaurar el cupo"

            return False, "No se pudo retirar la matrícula"

        return True, "Matrícula retirada y cupo devuelto"

    def registrar_nota(self, id_matricula, nota):
        matricula = self.obtener(id_matricula)

        if matricula is None:
            return False, "No existe la matrícula"

        if not Materia.es_nota_valida(nota):
            return False, "La nota debe estar entre 0 y 20"

        anterior = matricula.nota
        matricula.nota = float(nota)

        if not self.guardar():
            matricula.nota = anterior
            return False, "No se pudo guardar la nota"

        return True, f"Nota registrada: {matricula.nota} · {matricula.estado()}"

    def retirar_matricula(self, id_matricula):
        return self.eliminar(id_matricula)

    def certificado(self, id_matricula):
        matricula = self.obtener(id_matricula)

        if matricula is None:
            return None

        # DICCIONARIOS ÍNDICE: permiten acceder a los objetos por su id.
        estudiantes = {}
        materias = {}

        for estudiante in self.estudiantes.leer():
            estudiantes[estudiante.id] = estudiante

        for materia in self.materias.leer():
            materias[materia.id] = materia

        estudiante = estudiantes.get(matricula.estudiante_id)
        materia = materias.get(matricula.materia_id)

        if estudiante is None or materia is None:
            return "No se puede generar el certificado: faltan datos"

        return (
            f"CERTIFICADO DE MATRÍCULA #{matricula.id}\n"
            f"Estudiante: {estudiante.nombre_completo()}\n"
            f"Carnet: {estudiante.carnet}\n"
            f"Materia: {materia.nombre} ({materia.codigo})"
            f" · {materia.creditos} créditos\n"
            f"Periodo: {matricula.periodo}\n"
            f"Fecha: {matricula.fecha}\n"
            f"Nota: {matricula.nota:.1f}\n"
            f"Estado: {matricula.estado()}"
        )

    def matriculas_por_estudiante(self):
        # DICCIONARIO DE LISTAS: agrupa las matrículas de cada estudiante.
        agrupadas = {}

        for matricula in self.lista:
            lista = agrupadas.setdefault(matricula.estudiante_id, [])
            lista.append(matricula)

        return agrupadas

    def promedio_de_estudiante(self, id_estudiante):
        agrupadas = self.matriculas_por_estudiante()
        matriculas = agrupadas.get(id_estudiante, [])

        if not matriculas:
            return None

        suma = 0

        for matricula in matriculas:
            suma += matricula.nota

        return round(suma / len(matriculas), 2)