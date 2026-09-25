"""Capa de lógica de negocio para clientes.

Este archivo concentra la lógica que se encarga de interactuar con los datos.
No se ocupa de imprimir en consola ni de dibujar el menú; su objetivo es:
- validar la información que llega del usuario,
- buscar datos en el archivo JSON,
- crear, actualizar y borrar clientes,
- y devolver respuestas que luego la capa visual puede mostrar.
"""

from models import Cliente, CAMPOS_CLIENTE
from shared.json_manager import GestorJSON
from shared.herramientas import es_email_valido

# Este objeto gestiona la persistencia de los clientes en el archivo JSON.
# De esta forma, todas las operaciones del CRUD leen y escriben a través del mismo punto.
gestor = GestorJSON("data/clientes.json")

# Estas tuplas definen reglas del sistema.
# CAMPOS_OBLIGATORIOS indica qué campos no pueden quedar vacíos.
# CAMPOS_BUSCABLES indica en qué campos se debe buscar al hacer filtros.
CAMPOS_OBLIGATORIOS = ("nombre", "apellido", "email")
CAMPOS_BUSCABLES = ("nombre", "apellido", "email", "telefono", "ciudad")


# ================================================================
# Bloque de funciones auxiliares
# ================================================================

def emails_registrados(excepto_id=None):
    """Devuelve todos los emails ya registrados en formato normalizado.

    Se usa como comprobación rápida para evitar duplicados. Si se pasa un id,
    se excluye ese cliente concreto para permitir editar su propio email sin que
    el sistema lo considere repetido.
    """
    return {
        registro["email"].lower()
        for registro in gestor.leer()
        if registro["id"] != excepto_id
    }


def siguiente_id():
    """Calcula el siguiente id disponible para un nuevo cliente.

    Se revisan todos los ids existentes y se toma el mayor, sumando 1. Si no
    hay clientes aún, devuelve 1 como primer identificador.
    """
    ids = [registro["id"] for registro in gestor.leer()]
    return max(ids) + 1 if ids else 1


# ================================================================
# CREATE: crear un cliente
# ================================================================

def crear_cliente(datos):
    """Crea un cliente si los datos son válidos y no hay duplicados.

    La función recibe un diccionario con los campos del cliente, normaliza los
    valores, valida correo y campos obligatorios, y luego guarda el registro en
    el archivo JSON.
    """
    try:
        # 1) Normalización: convertimos cada dato a texto y eliminamos espacios al
        # principio y al final, porque en entradas de consola suele quedar basura.
        valores = {campo: str(datos.get(campo, "")).strip() for campo in CAMPOS_CLIENTE}

        # 2) Validación de campos obligatorios.
        faltantes = [campo for campo in CAMPOS_OBLIGATORIOS if not valores[campo]]
        if faltantes:
            return False, f"Faltan campos obligatorios: {', '.join(faltantes)}"

        # 3) Validación del email con una regla simple: debe contener un @,
        # un nombre antes y un dominio válido después. Si no cumple, se rechaza.
        if not es_email_valido(valores["email"]):
            return False, f"El email '{valores['email']}' no tiene un formato válido"

        # 4) Evitar duplicados: si el email ya está registrado, no se permite crear
        # otro cliente con ese mismo correo.
        if valores["email"].lower() in emails_registrados():
            return False, "Ese email ya está registrado"

        # 5) Construimos el objeto Cliente a partir del diccionario.
        #    El operador ** desempaqueta el diccionario en argumentos del constructor.
        cliente = Cliente(siguiente_id(), **valores)

        # 6) Leemos la lista de clientes actuales y añadimos el nuevo registro.
        registros = gestor.leer()
        registros.append(cliente.a_diccionario())

        # 7) Guardamos la lista completa en el archivo JSON.
        if not gestor.guardar(registros):
            return False, "No se pudo escribir el archivo"

        return True, f"Cliente {cliente.obtener_nombre_completo()} creado con id {cliente.id}"

    except Exception as error:
        # Cualquier fallo inesperado se captura aquí para evitar que el programa
        # termine de forma abrupta y para informar al usuario del problema.
        return False, f"Error inesperado: {error}"


# ================================================================
# READ: leer clientes
# ================================================================

def obtener_todos():
    """Devuelve todos los clientes convertidos en objetos Cliente."""
    registros = gestor.leer()
    return [Cliente.desde_diccionario(registro) for registro in registros]


def obtener_por_id(id_cliente):
    """Busca un cliente exacto por su id y devuelve el objeto si existe."""
    for cliente in obtener_todos():
        if cliente.id == id_cliente:
            return cliente
    return None


# ================================================================
# SEARCH: buscar clientes
# ================================================================

def buscar_clientes(termino):
    """Busca clientes por coincidencia parcial en varios campos.

    El texto puede ser un nombre, apellido, email, teléfono o ciudad. Si coincide
    en cualquiera de esos campos, se devuelve ese cliente.
    """
    termino = termino.strip().lower()
    if not termino:
        return []

    encontrados = []
    for registro in gestor.leer():
        for campo in CAMPOS_BUSCABLES:
            # Se compara si el texto buscado aparece dentro del valor del campo.
            if termino in str(registro.get(campo, "")).lower():
                encontrados.append(Cliente.desde_diccionario(registro))
                break
    return encontrados


# ================================================================
# UPDATE: actualizar un cliente
# ================================================================

def actualizar_cliente(id_cliente, cambios):
    """Actualiza los datos de un cliente existente.

    El diccionario cambios solo incluye los campos que el usuario quiere cambiar.
    Esto ayuda a modificar únicamente lo necesario y no sobrescribir todo el registro.
    """
    try:
        # 1) Revisamos si el usuario envió nombres de campo no válidos.
        desconocidos = set(cambios) - set(CAMPOS_CLIENTE)
        if desconocidos:
            return False, f"Campos no válidos: {', '.join(sorted(desconocidos))}"

        # 2) Si el diccionario viene vacío, no hay cambios que aplicar.
        if not cambios:
            return False, "No se indicó ningún cambio"

        # 3) Si se desea cambiar el email, se valida y se verifica que no lo use otro cliente.
        if "email" in cambios:
            if not es_email_valido(cambios["email"]):
                return False, "El email no tiene un formato válido"
            if cambios["email"].lower() in emails_registrados(excepto_id=id_cliente):
                return False, "Ese email ya lo usa otro cliente"

        # 4) Leemos todos los registros y buscamos la posición del cliente indicado.
        registros = gestor.leer()
        posicion = None
        for indice, registro in enumerate(registros):
            if registro["id"] == id_cliente:
                posicion = indice
                break

        if posicion is None:
            return False, f"No existe un cliente con id {id_cliente}"

        # 5) Actualizamos solo el registro encontrado y luego se guarda la lista entera.
        registros[posicion].update(cambios)
        gestor.guardar(registros)
        return True, f"Cliente {id_cliente} actualizado ({len(cambios)} campo/s)"

    except Exception as error:
        return False, f"Error inesperado: {error}"


# ================================================================
# DELETE: eliminar un cliente
# ================================================================

def eliminar_cliente(id_cliente):
    """Elimina un cliente por su id.

    En vez de modificar el registro en su sitio, se crea una nueva lista que
    excluye al cliente indicado, y luego se guarda esa lista definitiva.
    """
    registros = gestor.leer()

    # nueva_lista consiste en todos los clientes que no tienen ese id.
    quedan = [registro for registro in registros if registro["id"] != id_cliente]

    if len(quedan) == len(registros):
        return False, f"No existe un cliente con id {id_cliente}"

    gestor.guardar(quedan)
    return True, f"Cliente {id_cliente} eliminado"


# ================================================================
# ESTADÍSTICAS: resumen del sistema
# ================================================================

def estadisticas():
    """Devuelve un resumen con ciudades, dominios y clientes sin teléfono.

    Este resumen ayuda a tener una vista rápida del estado del archivo.
    """
    registros = gestor.leer()

    # set elimina duplicados; por eso sirve para saber ciudades distintas y dominios distintos.
    ciudades = {r.get("ciudad", "").title() for r in registros if r.get("ciudad")}
    dominios = {r["email"].split("@")[1].lower() for r in registros if "@" in r["email"]}
    sin_telefono = [r["nombre"] for r in registros if not r.get("telefono")]

    return {
        "total": len(registros),
        "ciudades": sorted(ciudades),
        "dominios": sorted(dominios),
        "sin_telefono": sin_telefono,
    }