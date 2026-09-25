"""Archivo principal del proyecto.

Este archivo es el punto de entrada de la aplicación. Aquí se arma el menú
principal, se capturan las opciones del usuario y se llaman a las funciones
que ya están definidas en el resto de archivos. Es la parte del programa
que hace que el usuario pueda interactuar con la lógica del sistema.
"""

# Importamos los campos del cliente desde el modelo para reutilizar su estructura.
# Eso hace que si cambiamos el orden o los nombres de los datos del cliente,
# el menú de creación también se adapte automáticamente.
from models import CAMPOS_CLIENTE

# Importamos funciones de ayuda para mostrar mensajes con formato visual.
from shared.herramientas import (
    imprimir_titulo,
    imprimir_exito,
    imprimir_error,
    imprimir_info,
    confirmar,
)

# Importamos las operaciones reales del sistema: crear, leer, buscar,
# editar, eliminar y generar estadísticas.
from views import (
    crear_cliente,
    obtener_todos,
    obtener_por_id,
    buscar_clientes,
    actualizar_cliente,
    eliminar_cliente,
    estadisticas,
)


# ---------------------------------------------------------------------
# Bloque de utilidades para la interfaz visual del programa
# ---------------------------------------------------------------------

def pausa():
    """Detiene la ejecución unos segundos hasta que el usuario presione Enter.

    Esta función sirve para que el usuario tenga tiempo de leer cada pantalla
    y no se sienta que la aplicación se mueve demasiado rápido.
    """
    input("\nPresione Enter para continuar...")


def mostrar_tabla(clientes):
    """Muestra una tabla con los clientes en formato legible para consola.

    Se usa en las opciones de listar clientes y buscar clientes para imprimir
    todos los registros en columnas ordenadas.
    """
    print(f"{'ID':<5}{'NOMBRE':<25}{'EMAIL':<28}{'CIUDAD':<15}{'TELÉFONO':<12}")
    print("-" * 85)

    for cliente in clientes:
        # Cada fila representa un cliente y se presenta con espacios para alinear
        # los datos y que la tabla se vea ordenada.
        print(
            f"{cliente.id:<5}{cliente.obtener_nombre_completo():<25}"
            f"{cliente.email:<28}{cliente.ciudad:<15}{cliente.telefono:<12}"
        )

    print("-" * 85)
    imprimir_info(f"Total: {len(clientes)} cliente(s)")


# ---------------------------------------------------------------------
# Opción 1: crear un nuevo cliente
# ---------------------------------------------------------------------
def opcion_crear():
    """Recoge los datos del usuario y los envía a la lógica de creación.

    El formulario se crea dinámicamente recorriendo CAMPOS_CLIENTE, así que
    si cambias el modelo de datos, este bloque sigue funcionando sin modificar
    la estructura del menú.
    """
    imprimir_titulo("CREAR NUEVO CLIENTE")

    datos = {}
    for campo in CAMPOS_CLIENTE:
        # Se pide cada valor con el nombre del campo. Ejemplo: nombre, apellido,
        # email, etc. Lo guardamos en un diccionario para construir luego el cliente.
        datos[campo] = input(f"{campo.capitalize()}: ")

    exito, mensaje = crear_cliente(datos)
    if exito:
        imprimir_exito(mensaje)
    else:
        imprimir_error(mensaje)
    pausa()


# ---------------------------------------------------------------------
# Opción 2: mostrar todos los clientes
# ---------------------------------------------------------------------
def opcion_ver_todos():
    """Solicita la lista completa de clientes y la imprime en pantalla."""
    imprimir_titulo("LISTA DE CLIENTES")
    clientes = obtener_todos()

    if not clientes:
        imprimir_info("Todavía no hay clientes. Use la opción 1 para crear el primero.")
    else:
        mostrar_tabla(clientes)

    pausa()


# ---------------------------------------------------------------------
# Opción 3: buscar clientes por un texto
# ---------------------------------------------------------------------
def opcion_buscar():
    """Busca clientes por nombre, email, teléfono o ciudad.

    El término puede ser parcial. Por ejemplo, si escribes "madrid" mostrará
    todos los clientes que tengan esa ciudad en su registro.
    """
    imprimir_titulo("BUSCAR CLIENTE")
    termino = input("Nombre, email, teléfono o ciudad: ")
    encontrados = buscar_clientes(termino)

    if not encontrados:
        imprimir_info(f"Ningún cliente coincide con '{termino}'.")
    else:
        mostrar_tabla(encontrados)

    pausa()


# ---------------------------------------------------------------------
# Opción 4: mostrar un cliente por su id
# ---------------------------------------------------------------------
def opcion_ver_por_id():
    """Busca un cliente concreto usando su identificador único."""
    imprimir_titulo("VER CLIENTE POR ID")

    try:
        # El id es un número entero, así que se convierte con int().
        id_cliente = int(input("Id del cliente: "))
    except ValueError:
        imprimir_error("El id debe ser un número entero")
        return pausa()

    cliente = obtener_por_id(id_cliente)
    if not cliente:
        imprimir_error(f"No existe un cliente con id {id_cliente}")
    else:
        # Se recorre el diccionario del cliente para sacar cada atributo y mostrarlo
        # con su clave. Por ejemplo: nombre, email, ciudad, direccion, etc.
        for clave, valor in cliente.a_diccionario().items():
            print(f"  {clave.capitalize():<12}: {valor}")

    pausa()


# ---------------------------------------------------------------------
# Opción 5: actualizar datos de un cliente existente
# ---------------------------------------------------------------------
def opcion_actualizar():
    """Permite editar la información de un cliente que ya existe.

    El usuario escribe solo los campos que quiere cambiar y deja en blanco los
    que no desea tocar. Esto evita perder información por accident.
    """
    imprimir_titulo("ACTUALIZAR CLIENTE")

    try:
        id_cliente = int(input("Id del cliente: "))
    except ValueError:
        imprimir_error("El id debe ser un número entero")
        return pausa()

    cliente = obtener_por_id(id_cliente)
    if not cliente:
        imprimir_error(f"No existe un cliente con id {id_cliente}")
        return pausa()

    imprimir_info(f"Editando a {cliente.obtener_nombre_completo()}")
    print("Deje en blanco el campo que no quiera cambiar.\n")

    cambios = {}
    for campo in CAMPOS_CLIENTE:
        # Leemos el valor actual para mostrárselo al usuario como referencia.
        actual = getattr(cliente, campo)
        nuevo = input(f"{campo.capitalize()} [{actual}]: ").strip()

        # Solo guardamos el campo si han escrito algo nuevo.
        if nuevo:
            cambios[campo] = nuevo

    exito, mensaje = actualizar_cliente(id_cliente, cambios)
    if exito:
        imprimir_exito(mensaje)
    else:
        imprimir_error(mensaje)

    pausa()


# ---------------------------------------------------------------------
# Opción 6: eliminar un cliente
# ---------------------------------------------------------------------
def opcion_eliminar():
    """Elimina una persona del sistema después de pedir confirmación.

    Es importante confirmar porque una eliminación es irreversible en esta
    práctica y el usuario debe aceptar la acción de forma explícita.
    """
    imprimir_titulo("ELIMINAR CLIENTE")

    try:
        id_cliente = int(input("Id del cliente: "))
    except ValueError:
        imprimir_error("El id debe ser un número entero")
        return pausa()

    cliente = obtener_por_id(id_cliente)
    if not cliente:
        imprimir_error(f"No existe un cliente con id {id_cliente}")
        return pausa()

    imprimir_info(f"Se eliminará: {cliente}")

    if confirmar("¿Confirma la eliminación?"):
        exito, mensaje = eliminar_cliente(id_cliente)
        if exito:
            imprimir_exito(mensaje)
        else:
            imprimir_error(mensaje)
    else:
        imprimir_info("Operación cancelada")

    pausa()


# ---------------------------------------------------------------------
# Opción 7: visualizar estadísticas del sistema
# ---------------------------------------------------------------------
def opcion_estadisticas():
    """Muestra un resumen del estado actual de los datos almacenados."""
    imprimir_titulo("ESTADÍSTICAS")
    datos = estadisticas()

    print(f"  Clientes registrados : {datos['total']}")
    print(f"  Ciudades distintas   : {len(datos['ciudades'])} -> {', '.join(datos['ciudades'])}")
    print(f"  Dominios de email    : {', '.join(datos['dominios'])}")
    print(f"  Sin teléfono         : {len(datos['sin_telefono'])}")
    pausa()


# ---------------------------------------------------------------------
# Acción de salida del menú
# ---------------------------------------------------------------------
def salir():
    """Finaliza el ciclo principal de la aplicación."""
    imprimir_info("¡Hasta luego! 👋")
    return "salir"


# El diccionario relacona cada tecla del menú con su texto y su función.
# De esta manera, cuando el usuario escribe "1", se ejecuta opcion_crear();
# cuando escribe "2", se ejecuta opcion_ver_todos(), y así sucesivamente.
OPCIONES = {
    "1": ("Crear cliente", opcion_crear),
    "2": ("Ver todos", opcion_ver_todos),
    "3": ("Buscar", opcion_buscar),
    "4": ("Ver por id", opcion_ver_por_id),
    "5": ("Actualizar", opcion_actualizar),
    "6": ("Eliminar", opcion_eliminar),
    "7": ("Estadísticas", opcion_estadisticas),
    "0": ("Salir", salir),
}


def mostrar_menu():
    """Imprime la pantalla de inicio con todas las opciones disponibles.

    Esta función se llama repetidamente dentro del bucle principal, por eso
    el programa siempre vuelve a mostrar el menú después de cada acción.
    """
    imprimir_titulo("SISTEMA DE GESTIÓN DE CLIENTES")
    for tecla, (texto, _funcion) in OPCIONES.items():
        print(f"  {tecla}. {texto}")
    print()


def main():
    """Bucle principal del programa.

    Aquí se repite el proceso:
    1. mostrar el menú,
    2. leer la opción del usuario,
    3. ejecutar la acción,
    4. volver a empezar hasta que el usuario salga.
    """
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


# Este bloque se ejecuta solo cuando el archivo se abre directamente con Python.
# Si el archivo se importa desde otro archivo, no se ejecuta automáticamente.
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")