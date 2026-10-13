from shared.herramientas import (
    confirmar,
    imprimir_error,
    imprimir_exito,
    imprimir_info,
    imprimir_titulo,
)
from views import DocenteController


docentes = DocenteController()


def pausa():
    input("\nPresiona Enter para continuar...")


def mostrar_resultado(exito, mensaje):
    if exito:
        imprimir_exito(mensaje)
    else:
        imprimir_error(mensaje)


def pedir_entero(etiqueta):
    while True:
        try:
            return int(input(etiqueta))
        except ValueError:
            imprimir_error("Escribe un número entero")


def mostrar_lista(objetos):
    if not objetos:
        imprimir_info("No hay registros para mostrar")
        return

    for objeto in objetos:
        print(objeto)


def mostrar_detalle(objeto):
    if objeto is None:
        imprimir_error("No existe el registro")
        return

    for campo, valor in objeto.a_diccionario().items():
        print(f"{campo}: {valor}")


def pedir_cambios(objeto, campos):
    cambios = {}
    imprimir_info("Deja vacío un campo para conservar su valor")

    for campo in campos:
        actual = getattr(objeto, campo)
        nuevo = input(f"{campo} [{actual}]: ").strip()

        if nuevo:
            cambios[campo] = nuevo

    return cambios


def crear_docente():
    imprimir_titulo("CREAR DOCENTE")
    datos = {
        "nombre": input("Nombre: "),
        "apellido": input("Apellido: "),
        "email": input("Email: "),
        "especialidad": input("Especialidad: "),
    }
    exito, mensaje = docentes.crear(datos)
    mostrar_resultado(exito, mensaje)
    pausa()


def listar_docentes():
    imprimir_titulo("LISTA DE DOCENTES")
    lista = docentes.leer()
    mostrar_lista(lista)
    pausa()


def buscar_docentes():
    imprimir_titulo("BUSCAR DOCENTES")
    termino = input("Texto a buscar: ")
    encontrados = docentes.buscar(termino)
    mostrar_lista(encontrados)
    pausa()


def ver_docente():
    imprimir_titulo("VER DOCENTE")
    id_docente = pedir_entero("ID del docente: ")
    docente = docentes.obtener(id_docente)
    mostrar_detalle(docente)
    pausa()


def actualizar_docente():
    imprimir_titulo("ACTUALIZAR DOCENTE")
    id_docente = pedir_entero("ID del docente: ")
    docente = docentes.obtener(id_docente)

    if docente is None:
        imprimir_error("No existe el docente")
    else:
        cambios = pedir_cambios(
            docente, ("nombre", "apellido", "email", "especialidad")
        )
        exito, mensaje = docentes.actualizar(id_docente, cambios)
        mostrar_resultado(exito, mensaje)

    pausa()


def eliminar_docente():
    imprimir_titulo("ELIMINAR DOCENTE")
    id_docente = pedir_entero("ID del docente: ")
    docente = docentes.obtener(id_docente)

    if docente is None:
        imprimir_error("No existe el docente")
    else:
        mostrar_detalle(docente)

        if confirmar("¿Deseas eliminar este docente?"):
            exito, mensaje = docentes.eliminar(id_docente)
            mostrar_resultado(exito, mensaje)
        else:
            imprimir_info("Eliminación cancelada")

    pausa()


def ejecutar_menu(titulo, opciones):
    while True:
        imprimir_titulo(titulo)

        for numero, (descripcion, _) in opciones.items():
            print(f"{numero}. {descripcion}")

        print("0. Salir")
        opcion = input("\nElige una opción: ").strip()

        if opcion == "0":
            return

        accion = opciones.get(opcion)

        if accion is None:
            imprimir_error("Opción no válida")
            pausa()
        else:
            accion[1]()


def menu_docentes():
    opciones = {
        "1": ("Crear docente", crear_docente),
        "2": ("Listar docentes", listar_docentes),
        "3": ("Buscar docentes", buscar_docentes),
        "4": ("Ver docente por ID", ver_docente),
        "5": ("Actualizar docente", actualizar_docente),
        "6": ("Eliminar docente", eliminar_docente),
    }
    ejecutar_menu("DOCENTES", opciones)


if __name__ == "__main__":
    menu_docentes()
