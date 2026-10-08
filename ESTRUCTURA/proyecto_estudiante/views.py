"""Controlador del sistema de estudiantes.

Valida datos y realiza las operaciones sobre el archivo JSON.
Devuelve resultados para que main.py los muestre.
"""

from pathlib import Path

from models import Estudiante, CAMPOS_ESTUDIANTE
from shared.json_manager import GestorJSON
from shared.herramientas import es_email_valido


# Guarda los estudiantes junto al proyecto, sin depender del directorio
# desde el que se inicia Python (por ejemplo, la raíz abierta en VS Code).
gestor = GestorJSON(
    Path(__file__).resolve().parent / "data" / "estudiantes.json"
)

# TUPLAS: definen campos fijos de configuración.
CAMPOS_OBLIGATORIOS = ("nombre", "apellido", "email", "carnet")
CAMPOS_BUSCABLES = ("nombre", "apellido", "email", "carnet")


# -------------------- AYUDAS INTERNAS --------------------

def carnets_registrados(excepto_id=None):
    """Devuelve un conjunto con los carnets registrados."""

    # CONJUNTO: permite comprobar si un carnet ya está usado.
    # Se excluye el estudiante que se está actualizando.
    return {
        registro["carnet"].strip().upper()
        for registro in gestor.leer()
        if registro["id"] != excepto_id
    }


def siguiente_id():
    """Calcula el siguiente id a partir de los registros actuales."""

    # LISTA: reúne los ids existentes.
    ids = [registro["id"] for registro in gestor.leer()]

    return max(ids) + 1 if ids else 1


# -------------------- CREAR --------------------

def crear_estudiante(datos):
    """Valida y guarda un estudiante nuevo.

    Devuelve una TUPLA: (exito, mensaje).
    """
    try:
        # DICCIONARIO: reúne los campos y limpia sus valores.
        valores = {
            campo: str(datos.get(campo, "")).strip()
            for campo in CAMPOS_ESTUDIANTE
        }

        faltantes = [
            campo
            for campo in CAMPOS_OBLIGATORIOS
            if not valores[campo]
        ]

        if faltantes:
            return (
                False,
                f"Faltan campos obligatorios: {', '.join(faltantes)}"
            )

        if not es_email_valido(valores["email"]):
            return False, "El email no tiene un formato válido"

        # Normaliza el carnet para comparar y guardar.
        valores["carnet"] = valores["carnet"].upper()

        if valores["carnet"] in carnets_registrados():
            return False, "Ese carnet ya está registrado"

        estudiante = Estudiante(siguiente_id(), **valores)

        registros = gestor.leer()
        registros.append(estudiante.a_diccionario())

        if not gestor.guardar(registros):
            return False, "No se pudo guardar el estudiante"

        return (
            True,
            f"Estudiante {estudiante.obtener_nombre_completo()} "
            f"creado con id {estudiante.id}"
        )

    except Exception as error:
        return False, f"Error inesperado: {error}"


# -------------------- LEER --------------------

def obtener_todos():
    """Devuelve una lista de objetos Estudiante."""

    return [
        Estudiante.desde_diccionario(registro)
        for registro in gestor.leer()
    ]


def obtener_por_id(id_estudiante):
    """Devuelve un estudiante o None si no existe."""

    for estudiante in obtener_todos():
        if estudiante.id == id_estudiante:
            return estudiante

    return None


# -------------------- BUSCAR --------------------

def buscar_estudiantes(termino):
    """Busca coincidencias parciales en los campos configurados."""

    termino = termino.strip().lower()

    if not termino:
        return []

    encontrados = []

    for registro in gestor.leer():
        for campo in CAMPOS_BUSCABLES:
            texto = str(registro.get(campo, "")).lower()

            if termino in texto:
                encontrados.append(
                    Estudiante.desde_diccionario(registro)
                )

                # Evita agregar dos veces al mismo estudiante.
                break

    return encontrados


# -------------------- ACTUALIZAR --------------------

def actualizar_estudiante(id_estudiante, cambios):
    """Actualiza únicamente los campos personales permitidos."""

    try:
        # DIFERENCIA DE CONJUNTOS:
        # identifica campos que no están permitidos.
        desconocidos = set(cambios) - set(CAMPOS_ESTUDIANTE)

        if desconocidos:
            return (
                False,
                f"Campos no válidos: {', '.join(sorted(desconocidos))}"
            )

        if not cambios:
            return False, "No se indicó ningún cambio"

        registros = gestor.leer()
        posicion = None

        for indice, registro in enumerate(registros):
            if registro["id"] == id_estudiante:
                posicion = indice
                break

        if posicion is None:
            return (
                False,
                f"No existe un estudiante con id {id_estudiante}"
            )

        # Crea otro diccionario con los valores limpios.
        cambios = {
            campo: str(valor).strip()
            for campo, valor in cambios.items()
        }

        # Impide vaciar un campo obligatorio.
        vacios = [
            campo
            for campo in CAMPOS_OBLIGATORIOS
            if campo in cambios and not cambios[campo]
        ]

        if vacios:
            return (
                False,
                f"No pueden quedar vacíos: {', '.join(vacios)}"
            )

        if "email" in cambios:
            if not es_email_valido(cambios["email"]):
                return False, "El email no tiene un formato válido"

        if "carnet" in cambios:
            cambios["carnet"] = cambios["carnet"].upper()

            usados = carnets_registrados(
                excepto_id=id_estudiante
            )

            if cambios["carnet"] in usados:
                return False, "Ese carnet ya lo usa otro estudiante"

        # Modifica solo los campos recibidos.
        # Las notas y materias permanecen en el registro.
        registros[posicion].update(cambios)

        if not gestor.guardar(registros):
            return False, "No se pudieron guardar los cambios"

        return (
            True,
            f"Estudiante {id_estudiante} actualizado "
            f"({len(cambios)} campo/s)"
        )

    except Exception as error:
        return False, f"Error inesperado: {error}"


# -------------------- ELIMINAR --------------------

def eliminar_estudiante(id_estudiante):
    """Elimina el registro del estudiante indicado."""

    registros = gestor.leer()

    # LISTA nueva con todos excepto el estudiante que se elimina.
    quedan = [
        registro
        for registro in registros
        if registro["id"] != id_estudiante
    ]

    if len(quedan) == len(registros):
        return (
            False,
            f"No existe un estudiante con id {id_estudiante}"
        )

    if not gestor.guardar(quedan):
        return False, "No se pudo guardar la eliminación"

    return True, f"Estudiante {id_estudiante} eliminado"


# -------------------- AGREGAR NOTA --------------------

def agregar_nota(id_estudiante, materia, nota):
    """Valida una nota entre 0 y 20 y la guarda."""

    # input() entrega texto: aquí lo convertimos a número.
    try:
        nota = float(nota)
    except (ValueError, TypeError):
        return False, "La nota debe ser un número"

    if not (0 <= nota <= 20):
        return False, "La nota debe estar entre 0 y 20"

    # Unifica espacios y mayúsculas para registrar las materias.
    materia = " ".join(materia.split()).title()

    if not materia:
        return False, "El nombre de la materia es obligatorio"

    registros = gestor.leer()

    for indice, registro in enumerate(registros):
        if registro["id"] == id_estudiante:
            estudiante = Estudiante.desde_diccionario(registro)

            # El modelo agrega la nota e inscribe la materia.
            estudiante.agregar_nota(materia, nota)

            # Convierte el objeto nuevamente a diccionario.
            registros[indice] = estudiante.a_diccionario()

            if not gestor.guardar(registros):
                return False, "No se pudo guardar la nota"

            return (
                True,
                f"Nota {nota:g} de {materia} agregada a "
                f"{estudiante.obtener_nombre_completo()}"
            )

    return (
        False,
        f"No existe un estudiante con id {id_estudiante}"
    )


# -------------------- MATERIAS OFERTADAS --------------------

def materias_ofertadas():
    """Devuelve todas las materias inscritas, sin repetir."""

    # CONJUNTO: reúne las materias de todos los estudiantes.
    materias = set()

    for estudiante in obtener_todos():
        materias.update(estudiante.materias)

    return materias


# -------------------- MATERIAS EN COMÚN --------------------

def estudiantes_en_comun(id_a, id_b):
    """Devuelve (True, conjunto) o (False, mensaje de error)."""

    estudiante_a = obtener_por_id(id_a)

    if estudiante_a is None:
        return False, f"No existe un estudiante con id {id_a}"

    estudiante_b = obtener_por_id(id_b)

    if estudiante_b is None:
        return False, f"No existe un estudiante con id {id_b}"

    # El método del modelo utiliza la intersección: conjunto A & B.
    comunes = estudiante_a.materias_en_comun(estudiante_b)

    return True, comunes