"""Funciones auxiliares para la interfaz de consola.

Este archivo no maneja clientes ni archivos JSON. Su trabajo es brindar
herramientas visuales y de validación para que el resto del programa pueda
mostrar mensajes bonitos, limpiar la pantalla y comprobar entradas del usuario.
"""

import os

# Los códigos ANSI permiten cambiar el color del texto en la terminal.
# Cada clave del diccionario representa un color y su valor es el código que la
# consola interpreta para pintar el texto.
COLORES = {
    "ROJO": "\033[91m",
    "VERDE": "\033[92m",
    "AZUL": "\033[94m",
    "AMARILLO": "\033[93m",
    "CYAN": "\033[96m",
    "BLANCO": "\033[97m",
    "RESET": "\033[0m",
}

# Esta tupla define qué palabras se consideran una respuesta afirmativa en el
# programa. Por ejemplo, si el usuario escribe 'si', 's' o 'y', la opción se
# interpreta como aceptar una acción.
RESPUESTAS_SI = ("si", "sí", "s", "yes", "y")


def limpiar_pantalla():
    """Limpia la terminal para que cada menú se vea limpio y ordenado.

    En sistemas Unix se usa 'clear'; en Windows se usa 'cls'. El código detecta
    el sistema operativo y elige el comando correcto.
    """
    os.system("clear" if os.name == "posix" else "cls")


def imprimir_color(texto, color):
    """Imprime un mensaje con un color determinado usando códigos ANSI."""
    codigo = COLORES.get(color, COLORES["BLANCO"])
    print(f"{codigo}{texto}{COLORES['RESET']}")


def imprimir_titulo(texto):
    """Muestra un encabezado visual para cada pantalla del programa.

    Se usa para que cada sección del menú se vea más clara y ordenada visualmente.
    """
    limpiar_pantalla()
    imprimir_color("=" * 60, "AZUL")
    print(f"  {texto}".center(60))
    imprimir_color("=" * 60, "AZUL")
    print()


def imprimir_exito(mensaje):
    """Muestra mensajes de éxito en verde.

    Se usa cuando una operación como crear, editar o eliminar termina bien.
    """
    imprimir_color(f"✓ {mensaje}", "VERDE")


def imprimir_error(mensaje):
    """Muestra mensajes de error en rojo.

    Se usa en caso de datos inválidos, campos vacíos o elementos inexistentes.
    """
    imprimir_color(f"✗ {mensaje}", "ROJO")


def imprimir_info(mensaje):
    """Muestra mensajes informativos en color cian.

    Sirve para avisos generales, como "todavía no hay clientes" o "operación cancelada".
    """
    imprimir_color(f"ℹ {mensaje}", "CYAN")


def confirmar(pregunta):
    """Pregunta al usuario si confirma una acción importante.

    Devuelve True si la respuesta es afirmativa y False en caso contrario.
    Esto se usa antes de borrar un cliente para evitar eliminaciones accidentales.
    """
    respuesta = input(f"{pregunta} (si/no): ").strip().lower()
    return respuesta in RESPUESTAS_SI


def es_email_valido(texto):
    """Valida el formato de un email con una condición básica.

    La regla que se usa aquí es sencilla:
    - debe haber exactamente un @,
    - debe existir texto antes y después,
    - el dominio no puede terminar en un punto.
    """
    texto = texto.strip()
    if texto.count("@") != 1:
        return False

    usuario, dominio = texto.split("@")
    return len(usuario) > 0 and "." in dominio and not dominio.endswith(".")