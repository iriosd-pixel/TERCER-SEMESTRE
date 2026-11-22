"""Vista del sistema de estudiantes.

Muestra el menú, solicita datos y presenta los resultados.
Las operaciones y validaciones del negocio están en views.py.
"""

from models import CAMPOS_ESTUDIANTE

from shared.herramientas import (
    imprimir_titulo,
    imprimir_exito,
    imprimir_error,
    imprimir_info,
    confirmar,
)

from views import (
    crear_estudiante,
    obtener_todos,
    obtener_por_id,
    buscar_estudiantes,
    actualizar_estudiante,
    eliminar_estudiante,
    agregar_nota,
    materias_ofertadas,
    estudiantes_en_comun,
)


# -------------------- UTILIDADES --------------------

def pausa():
    """Espera hasta que el usuario presione Enter."""
    input("\nPresione Enter para continuar...")


def mostrar_tabla(estudiantes):
    """Muestra los estudiantes en columnas."""
    print(
        f"{'ID':<5}"
        f"{'NOMBRE':<30}"
        f"{'CARNET':<18}"
        f"{'EMAIL':<30}"
    )
    print("-" * 83)

    for estudiante in estudiantes:
        print(
            f"{estudiante.id:<5}"
            f"{estudiante.obtener_nombre_completo():<30}"
            f"{estudiante.carnet:<18}"
            f"{estudiante.email:<30}"
        )

    print("-" * 83)
    imprimir_info(f"Total: {len(estudiantes)} estudiante(s)")


# -------------------- CREAR --------------------

def opcion_crear():
    """Solicita los datos de un nuevo estudiante."""
    imprimir_titulo("CREAR NUEVO ESTUDIANTE")

    # DICCIONARIO: guarda cada campo con su valor.
    datos = {}

    # Recorre la TUPLA de campos definida en models.py.
    for campo in CAMPOS_ESTUDIANTE:
        datos[campo] = input(f"{campo.capitalize()}: ")

    exito, mensaje = crear_estudiante(datos)

    if exito:
        imprimir_exito(mensaje)
    else:
        imprimir_error(mensaje)

    pausa()


# -------------------- VER TODOS --------------------

def opcion_ver_todos():
    """Solicita y muestra la lista de estudiantes."""
    imprimir_titulo("LISTA DE ESTUDIANTES")

    estudiantes = obtener_todos()

    if not estudiantes:
        imprimir_info(
            "Todavía no hay estudiantes. "
            "Use la opción 1 para crear el primero."
        )
    else:
        mostrar_tabla(estudiantes)

    pausa()


# -------------------- BUSCAR --------------------

def opcion_buscar():
    """Solicita un texto para buscar estudiantes."""
    imprimir_titulo("BUSCAR ESTUDIANTE")

    termino = input("Nombre, apellido, email o carnet: ")
    encontrados = buscar_estudiantes(termino)

    if not encontrados:
        imprimir_info(
            f"Ningún estudiante coincide con '{termino}'."
        )
    else:
        mostrar_tabla(encontrados)

    pausa()


# -------------------- VER POR ID --------------------

def opcion_ver_por_id():
    """Muestra los datos de un estudiante por su id."""
    imprimir_titulo("VER ESTUDIANTE POR ID")

    try:
        id_estudiante = int(input("Id del estudiante: "))
    except ValueError:
        imprimir_error("El id debe ser un número entero")
        pausa()
        return

    estudiante = obtener_por_id(id_estudiante)

    if estudiante is None:
        imprimir_error(
            f"No existe un estudiante con id {id_estudiante}"
        )
    else:
        for clave, valor in estudiante.a_diccionario().items():
            print(f"  {clave.capitalize():<12}: {valor}")

    pausa()


# -------------------- ACTUALIZAR --------------------

def opcion_actualizar():
    """Solicita cambios en los datos de un estudiante."""
    imprimir_titulo("ACTUALIZAR ESTUDIANTE")

    try:
        id_estudiante = int(input("Id del estudiante: "))
    except ValueError:
        imprimir_error("El id debe ser un número entero")
        pausa()
        return

    estudiante = obtener_por_id(id_estudiante)

    if estudiante is None:
        imprimir_error(
            f"No existe un estudiante con id {id_estudiante}"
        )
        pausa()
        return

    imprimir_info(
        f"Editando a {estudiante.obtener_nombre_completo()}"
    )
    print("Deje en blanco el campo que no quiera cambiar.\n")

    # Incluye únicamente los campos que el usuario modifica.
    cambios = {}

    for campo in CAMPOS_ESTUDIANTE:
        actual = getattr(estudiante, campo)
        nuevo = input(
            f"{campo.capitalize()} [{actual}]: "
        ).strip()

        if nuevo:
            cambios[campo] = nuevo

    exito, mensaje = actualizar_estudiante(
        id_estudiante, cambios
    )

    if exito:
        imprimir_exito(mensaje)
    else:
        imprimir_error(mensaje)

    pausa()


# -------------------- ELIMINAR --------------------

def opcion_eliminar():
    """Pide confirmación y solicita eliminar un estudiante."""
    imprimir_titulo("ELIMINAR ESTUDIANTE")

    try:
        id_estudiante = int(input("Id del estudiante: "))
    except ValueError:
        imprimir_error("El id debe ser un número entero")
        pausa()
        return

    estudiante = obtener_por_id(id_estudiante)

    if estudiante is None:
        imprimir_error(
            f"No existe un estudiante con id {id_estudiante}"
        )
        pausa()
        return

    imprimir_info(
        f"Se eliminará: {estudiante.obtener_nombre_completo()} "
        f"({estudiante.carnet})"
    )

    if confirmar("¿Confirma la eliminación?"):
        exito, mensaje = eliminar_estudiante(id_estudiante)

        if exito:
            imprimir_exito(mensaje)
        else:
            imprimir_error(mensaje)
    else:
        imprimir_info("Operación cancelada")

    pausa()


# -------------------- AGREGAR NOTA --------------------

def opcion_agregar_nota():
    """Solicita el estudiante, la materia y la nota."""
    imprimir_titulo("AGREGAR NOTA")

    try:
        id_estudiante = int(input("Id del estudiante: "))
    except ValueError:
        imprimir_error("El id debe ser un número entero")
        pausa()
        return

    materia = input("Materia: ")
    nota = input("Nota entre 0 y 20: ")

    # El controlador convierte y valida la nota,
    # comprueba el id y guarda los cambios.
    exito, mensaje = agregar_nota(
        id_estudiante, materia, nota
    )

    if exito:
        imprimir_exito(mensaje)
    else:
        imprimir_error(mensaje)

    pausa()


# -------------------- VER PROMEDIO --------------------

def opcion_ver_promedio():
    """Muestra el promedio calculado por el modelo."""
    imprimir_titulo("VER PROMEDIO")

    try:
        id_estudiante = int(input("Id del estudiante: "))
    except ValueError:
        imprimir_error("El id debe ser un número entero")
        pausa()
        return

    estudiante = obtener_por_id(id_estudiante)

    if estudiante is None:
        imprimir_error(
            f"No existe un estudiante con id {id_estudiante}"
        )
    else:
        print(
            f"Estudiante: {estudiante.obtener_nombre_completo()}"
        )
        print(f"Carnet: {estudiante.carnet}")
        print(f"Promedio: {estudiante.obtener_promedio():.2f}")

    pausa()


# -------------------- MATERIAS EN COMÚN --------------------

def opcion_materias_en_comun():
    """Solicita dos estudiantes y muestra sus materias comunes."""
    imprimir_titulo("MATERIAS EN COMÚN")

    try:
        id_a = int(input("Id del primer estudiante: "))
        id_b = int(input("Id del segundo estudiante: "))
    except ValueError:
        imprimir_error("Los ids deben ser números enteros")
        pausa()
        return

    # El controlador devuelve:
    # (True, conjunto de materias) o (False, mensaje de error).
    exito, resultado = estudiantes_en_comun(id_a, id_b)

    if not exito:
        imprimir_error(resultado)
    elif not resultado:
        imprimir_info("Los estudiantes no comparten materias.")
    else:
        print("Materias que comparten:")

        for materia in sorted(resultado):
            print(f"  - {materia}")

    pausa()


# -------------------- MATERIAS OFERTADAS --------------------

def opcion_materias_ofertadas():
    """Muestra todas las materias registradas, sin repetir."""
    imprimir_titulo("MATERIAS OFERTADAS")

    materias = materias_ofertadas()

    if not materias:
        imprimir_info("Todavía no hay materias registradas.")
    else:
        for materia in sorted(materias):
            print(f"  - {materia}")

        imprimir_info(f"Total: {len(materias)} materia(s)")

    pausa()


# -------------------- SALIR --------------------

def salir():
    """Devuelve la señal para terminar el menú."""
    imprimir_info("¡Hasta luego!")
    return "salir"


# DICCIONARIO:
# cada tecla se relaciona con una TUPLA de texto y función.
OPCIONES = {
    "1": ("Crear estudiante", opcion_crear),
    "2": ("Ver todos", opcion_ver_todos),
    "3": ("Buscar", opcion_buscar),
    "4": ("Ver por id", opcion_ver_por_id),
    "5": ("Actualizar", opcion_actualizar),
    "6": ("Eliminar", opcion_eliminar),
    "7": ("Agregar nota", opcion_agregar_nota),
    "8": ("Ver promedio", opcion_ver_promedio),
    "9": ("Materias en común", opcion_materias_en_comun),
    "10": ("Materias ofertadas", opcion_materias_ofertadas),
    "0": ("Salir", salir),
}


def mostrar_menu():
    """Muestra las opciones disponibles."""
    imprimir_titulo("SISTEMA DE GESTIÓN DE ESTUDIANTES")

    for tecla, (texto, _funcion) in OPCIONES.items():
        print(f"  {tecla}. {texto}")

    print()


def main():
    """Repite el menú hasta que el usuario elija salir."""
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