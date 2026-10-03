





































""" models"""
"""Modelo del sistema de empleados."""

CAMPOS_EMPLEADO = (
    "nombre",
    "apellido",
    "email",
    "codigo",
    "cargo",
    "salario",
)


class Empleado:
    """Representa los datos de un empleado."""

    def __init__(
        self, id_empleado, nombre, apellido,
        email, codigo, cargo, salario
    ):
        self.id = id_empleado
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.codigo = codigo
        self.cargo = cargo
        self.salario = salario

    def obtener_nombre_completo(self):
        """Une nombre y apellido."""
        return f"{self.nombre} {self.apellido}"

    def a_diccionario(self):
        """Convierte el empleado en un diccionario."""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "codigo": self.codigo,
            "cargo": self.cargo,
            "salario": self.salario,
        }

    @classmethod
    def desde_diccionario(cls, datos):
        """Construye un empleado a partir de un diccionario."""
        return cls(
            datos["id"],
            datos["nombre"],
            datos["apellido"],
            datos["email"],
            datos["codigo"],
            datos["cargo"],
            datos["salario"],
        )

    def __str__(self):
        """Devuelve un resumen del empleado."""
        return (
            f"[{self.codigo}] {self.obtener_nombre_completo()} "
            f"- {self.cargo} - Salario: ${self.salario:.2f}"
        )
        
        
        

""" views"""
"""Controlador del sistema de empleados."""

import math
from pathlib import Path

from models import Empleado, CAMPOS_EMPLEADO
from shared.json_manager import GestorJSON
from shared.herramientas import es_email_valido


# Ubica data dentro de este proyecto, aunque se ejecute
# el programa desde otra carpeta.
CARPETA_PROYECTO = Path(__file__).resolve().parent
gestor = GestorJSON(CARPETA_PROYECTO / "data" / "empleados.json")

# TUPLAS: configuración fija.
CAMPOS_OBLIGATORIOS = CAMPOS_EMPLEADO

CAMPOS_BUSCABLES = (
    "nombre", "apellido", "email", "codigo", "cargo"
)


def codigos_registrados(excepto_id=None):
    """Devuelve los códigos usados por otros empleados."""

    # CONJUNTO: permite comprobar códigos duplicados.
    return {
        registro["codigo"].strip().upper()
        for registro in gestor.leer()
        if registro["id"] != excepto_id
    }


def siguiente_id():
    """Calcula un id a partir de los registros existentes."""

    # LISTA: reúne los identificadores actuales.
    ids = [registro["id"] for registro in gestor.leer()]
    return max(ids) + 1 if ids else 1


def validar_datos(datos, excepto_id=None):
    """Valida los datos completos de un empleado.

    Devuelve (True, diccionario limpio) o (False, mensaje).
    """
    # DICCIONARIO: relaciona cada campo con su valor limpio.
    valores = {
        campo: (
            "" if datos.get(campo) is None
            else str(datos[campo]).strip()
        )
        for campo in CAMPOS_EMPLEADO
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

    valores["codigo"] = valores["codigo"].upper()

    if valores["codigo"] in codigos_registrados(excepto_id):
        return False, "Ese código ya lo usa otro empleado"

    try:
        salario = float(valores["salario"])
    except ValueError:
        return False, "El salario debe ser un número"

    if not math.isfinite(salario) or salario < 0:
        return False, "El salario debe ser un número finito no negativo"

    valores["salario"] = round(salario, 2)

    # TUPLA: indica éxito y entrega los datos validados.
    return True, valores


def crear_empleado(datos):
    """Valida y guarda un empleado nuevo."""
    exito, resultado = validar_datos(datos)

    if not exito:
        return False, resultado

    empleado = Empleado(siguiente_id(), **resultado)

    registros = gestor.leer()
    registros.append(empleado.a_diccionario())

    if not gestor.guardar(registros):
        return False, "No se pudo guardar el empleado"

    return (
        True,
        f"Empleado {empleado.obtener_nombre_completo()} "
        f"creado con id {empleado.id}"
    )


def obtener_todos():
    """Devuelve una lista de objetos Empleado."""
    return [
        Empleado.desde_diccionario(registro)
        for registro in gestor.leer()
    ]


def obtener_por_id(id_empleado):
    """Devuelve el empleado o None si no existe."""
    for empleado in obtener_todos():
        if empleado.id == id_empleado:
            return empleado

    return None


def buscar_empleados(termino):
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
                    Empleado.desde_diccionario(registro)
                )
                break

    return encontrados


def actualizar_empleado(id_empleado, cambios):
    """Actualiza los campos indicados después de validarlos."""
    desconocidos = set(cambios) - set(CAMPOS_EMPLEADO)

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
        if registro["id"] == id_empleado:
            posicion = indice
            break

    if posicion is None:
        return False, f"No existe un empleado con id {id_empleado}"

    # Combina los datos actuales con los cambios solicitados.
    datos = registros[posicion].copy()
    datos.update(cambios)

    exito, resultado = validar_datos(
        datos, excepto_id=id_empleado
    )

    if not exito:
        return False, resultado

    empleado = Empleado(id_empleado, **resultado)
    registros[posicion] = empleado.a_diccionario()

    if not gestor.guardar(registros):
        return False, "No se pudieron guardar los cambios"

    return (
        True,
        f"Empleado {id_empleado} actualizado "
        f"({len(cambios)} campo/s)"
    )


def eliminar_empleado(id_empleado):
    """Elimina al empleado indicado."""
    registros = gestor.leer()

    # Crea otra lista sin modificar la que estamos recorriendo.
    quedan = [
        registro
        for registro in registros
        if registro["id"] != id_empleado
    ]

    if len(quedan) == len(registros):
        return False, f"No existe un empleado con id {id_empleado}"

    if not gestor.guardar(quedan):
        return False, "No se pudo guardar la eliminación"

    return True, f"Empleado {id_empleado} eliminado"


""" main"""
"""Vista del sistema de empleados."""

from models import CAMPOS_EMPLEADO

from shared.herramientas import (
    imprimir_titulo,
    imprimir_exito,
    imprimir_error,
    imprimir_info,
    confirmar,
)

from views import (
    crear_empleado,
    obtener_todos,
    obtener_por_id,
    buscar_empleados,
    actualizar_empleado,
    eliminar_empleado,
)


def pausa():
    """Espera hasta que el usuario presione Enter."""
    input("\nPresione Enter para continuar...")


def mostrar_resultado(exito, mensaje):
    """Muestra el resultado de una operación."""
    if exito:
        imprimir_exito(mensaje)
    else:
        imprimir_error(mensaje)


def pedir_id():
    """Convierte el id ingresado a entero o devuelve None."""
    try:
        return int(input("Id del empleado: "))
    except ValueError:
        imprimir_error("El id debe ser un número entero")
        return None


def mostrar_tabla(empleados):
    """Presenta los empleados en columnas."""
    print(
        f"{'ID':<5}"
        f"{'NOMBRE':<25}"
        f"{'CÓDIGO':<15}"
        f"{'CARGO':<20}"
        f"{'SALARIO':>12}  "
        f"{'EMAIL':<30}"
    )
    print("-" * 109)

    for empleado in empleados:
        print(
            f"{empleado.id:<5}"
            f"{empleado.obtener_nombre_completo():<25}"
            f"{empleado.codigo:<15}"
            f"{empleado.cargo:<20}"
            f"{empleado.salario:>12.2f}  "
            f"{empleado.email:<30}"
        )

    print("-" * 109)
    imprimir_info(f"Total: {len(empleados)} empleado(s)")


def opcion_crear():
    """Solicita los datos de un nuevo empleado."""
    imprimir_titulo("CREAR EMPLEADO")

    datos = {}

    for campo in CAMPOS_EMPLEADO:
        etiqueta = campo.capitalize()

        if campo == "salario":
            etiqueta = "Salario (ejemplo: 650.50)"

        datos[campo] = input(f"{etiqueta}: ")

    exito, mensaje = crear_empleado(datos)
    mostrar_resultado(exito, mensaje)
    pausa()


def opcion_ver_todos():
    """Muestra los empleados registrados."""
    imprimir_titulo("LISTA DE EMPLEADOS")
    empleados = obtener_todos()

    if not empleados:
        imprimir_info("Todavía no hay empleados registrados.")
    else:
        mostrar_tabla(empleados)

    pausa()


def opcion_buscar():
    """Solicita un término y muestra las coincidencias."""
    imprimir_titulo("BUSCAR EMPLEADO")

    termino = input("Nombre, apellido, email, código o cargo: ")
    encontrados = buscar_empleados(termino)

    if not encontrados:
        imprimir_info(
            f"Ningún empleado coincide con '{termino}'."
        )
    else:
        mostrar_tabla(encontrados)

    pausa()


def opcion_ver_por_id():
    """Muestra los datos de un empleado específico."""
    imprimir_titulo("VER EMPLEADO POR ID")
    id_empleado = pedir_id()

    if id_empleado is None:
        pausa()
        return

    empleado = obtener_por_id(id_empleado)

    if empleado is None:
        imprimir_error(
            f"No existe un empleado con id {id_empleado}"
        )
    else:
        for clave, valor in empleado.a_diccionario().items():
            if clave == "salario":
                valor = f"${valor:.2f}"

            print(f"  {clave.capitalize():<12}: {valor}")

    pausa()


def opcion_actualizar():
    """Solicita los campos que se desean modificar."""
    imprimir_titulo("ACTUALIZAR EMPLEADO")
    id_empleado = pedir_id()

    if id_empleado is None:
        pausa()
        return

    empleado = obtener_por_id(id_empleado)

    if empleado is None:
        imprimir_error(
            f"No existe un empleado con id {id_empleado}"
        )
        pausa()
        return

    imprimir_info(
        f"Editando a {empleado.obtener_nombre_completo()}"
    )
    print("Deje en blanco los campos que quiera conservar.\n")

    cambios = {}

    for campo in CAMPOS_EMPLEADO:
        actual = getattr(empleado, campo)
        nuevo = input(
            f"{campo.capitalize()} [{actual}]: "
        ).strip()

        if nuevo:
            cambios[campo] = nuevo

    exito, mensaje = actualizar_empleado(
        id_empleado, cambios
    )
    mostrar_resultado(exito, mensaje)
    pausa()


def opcion_eliminar():
    """Pide confirmación antes de eliminar."""
    imprimir_titulo("ELIMINAR EMPLEADO")
    id_empleado = pedir_id()

    if id_empleado is None:
        pausa()
        return

    empleado = obtener_por_id(id_empleado)

    if empleado is None:
        imprimir_error(
            f"No existe un empleado con id {id_empleado}"
        )
        pausa()
        return

    imprimir_info(f"Se eliminará: {empleado}")

    if confirmar("¿Confirma la eliminación?"):
        exito, mensaje = eliminar_empleado(id_empleado)
        mostrar_resultado(exito, mensaje)
    else:
        imprimir_info("Operación cancelada")

    pausa()


def salir():
    """Indica que se debe terminar el programa."""
    imprimir_info("¡Hasta luego!")
    return "salir"


# DICCIONARIO con TUPLAS: texto del menú y función asociada.
OPCIONES = {
    "1": ("Crear empleado", opcion_crear),
    "2": ("Ver todos", opcion_ver_todos),
    "3": ("Buscar", opcion_buscar),
    "4": ("Ver por id", opcion_ver_por_id),
    "5": ("Actualizar", opcion_actualizar),
    "6": ("Eliminar", opcion_eliminar),
    "0": ("Salir", salir),
}


def mostrar_menu():
    """Muestra todas las opciones."""
    imprimir_titulo("SISTEMA DE GESTIÓN DE EMPLEADOS")

    for tecla, (texto, _funcion) in OPCIONES.items():
        print(f"  {tecla}. {texto}")

    print()


def main():
    """Repite el menú hasta seleccionar salir."""
    while True:
        mostrar_menu()
        tecla = input("Seleccione una opción: ").strip()

        if tecla not in OPCIONES:
            imprimir_error("Opción no válida")
            pausa()
            continue

        _texto, funcion = OPCIONES[tecla]

        if funcion() == "salir":
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
        
        
        
        
""" json manager"""
"""Lectura y escritura de listas de diccionarios en JSON."""

import json
import os


class GestorJSON:
    """Administra un archivo JSON."""

    def __init__(self, ruta):
        self.ruta = ruta
        carpeta = os.path.dirname(ruta)

        if carpeta and not os.path.exists(carpeta):
            os.makedirs(carpeta)

    def leer(self):
        """Devuelve los registros o una lista vacía."""
        if not os.path.exists(self.ruta):
            return []

        try:
            with open(
                self.ruta, "r", encoding="utf-8"
            ) as archivo:
                datos = json.load(archivo)

            return datos if isinstance(datos, list) else []

        except (json.JSONDecodeError, OSError):
            return []

    def guardar(self, datos):
        """Guarda los datos y devuelve True o False."""
        try:
            with open(
                self.ruta, "w", encoding="utf-8"
            ) as archivo:
                json.dump(
                    datos,
                    archivo,
                    ensure_ascii=False,
                    indent=2,
                )

            return True

        except (TypeError, OSError):
            return False
        
        
        
         
         
         
         
         
         
         
         
         
""" herramientas"""
"""Herramientas para la interfaz de consola."""

import os


COLORES = {
    "ROJO": "\033[91m",
    "VERDE": "\033[92m",
    "AZUL": "\033[94m",
    "AMARILLO": "\033[93m",
    "CYAN": "\033[96m",
    "BLANCO": "\033[97m",
    "RESET": "\033[0m",
}

RESPUESTAS_SI = ("si", "sí", "s", "yes", "y")


def limpiar_pantalla():
    """Limpia la consola."""
    os.system("clear" if os.name == "posix" else "cls")


def imprimir_color(texto, color):
    """Muestra un texto con el color indicado."""
    codigo = COLORES.get(color, COLORES["BLANCO"])
    print(f"{codigo}{texto}{COLORES['RESET']}")


def imprimir_titulo(texto):
    """Limpia la pantalla y muestra un título."""
    limpiar_pantalla()
    imprimir_color("=" * 60, "AZUL")
    print(f"  {texto}".center(60))
    imprimir_color("=" * 60, "AZUL")
    print()


def imprimir_exito(mensaje):
    imprimir_color(f"✓ {mensaje}", "VERDE")


def imprimir_error(mensaje):
    imprimir_color(f"✗ {mensaje}", "ROJO")


def imprimir_info(mensaje):
    imprimir_color(f"ℹ {mensaje}", "CYAN")


def confirmar(pregunta):
    """Devuelve True si el usuario acepta."""
    respuesta = input(
        f"{pregunta} (si/no): "
    ).strip().lower()

    return respuesta in RESPUESTAS_SI


def es_email_valido(texto):
    """Realiza una comprobación básica del email."""
    texto = texto.strip()

    if texto.count("@") != 1:
        return False

    usuario, dominio = texto.split("@")

    return (
        len(usuario) > 0
        and "." in dominio
        and not dominio.endswith(".")
    )
    
    
    
    
    
    
       
       
       
