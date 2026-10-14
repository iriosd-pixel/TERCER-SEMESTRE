from views import EmpleadoController
from shared.herramientas import confirmar


empleados = EmpleadoController()


def pausa():
    input("\nPresione Enter para continuar...")


def pedir_entero(etiqueta):
    try:
        return int(input(etiqueta))
    except ValueError:
        return None


def mostrar_resultado(exito, mensaje):
    if exito:
        print(f"[OK] {mensaje}")
    else:
        print(f"[ERROR] {mensaje}")


def mostrar_lista(objetos, vacio="No hay empleados."):
    if not objetos:
        print(vacio)
        return
    for empleado in objetos:
        print(f"  {empleado}")
    print(f"Total: {len(objetos)}")


def pedir_cambios(empleado, campos):
    cambios = {}
    for campo in campos:
        valor_actual = getattr(empleado, campo)
        valor_nuevo = input(f"{campo} [{valor_actual}] (vacío conserva): ").strip()
        if valor_nuevo:
            cambios[campo] = valor_nuevo
    return cambios


def crear_empleado():
    datos = {
        "nombre": input("Nombre: "),
        "apellido": input("Apellido: "),
        "email": input("Email: "),
        "cargo": input("Cargo: "),
    }
    exito, mensaje = empleados.crear(datos)
    mostrar_resultado(exito, mensaje)
    pausa()


def listar_empleados():
    mostrar_lista(empleados.leer())
    pausa()


def buscar_empleado():
    texto = input("Nombre, apellido, email o cargo: ")
    encontrados = empleados.buscar(texto)
    mostrar_lista(encontrados, "Sin coincidencias.")
    pausa()


def ver_empleado():
    id_registro = pedir_entero("ID: ")
    empleado = None
    if id_registro is not None:
        empleado = empleados.obtener(id_registro)
    if empleado is None:
        print("No encontrado")
    else:
        print(empleado.a_diccionario())
    pausa()


def actualizar_empleado():
    id_registro = pedir_entero("ID: ")
    empleado = None
    if id_registro is not None:
        empleado = empleados.obtener(id_registro)
    if empleado is None:
        print("No encontrado")
        return pausa()
    campos = ("nombre", "apellido", "email", "cargo")
    cambios = pedir_cambios(empleado, campos)
    exito, mensaje = empleados.actualizar(id_registro, cambios)
    mostrar_resultado(exito, mensaje)
    pausa()


def eliminar_empleado():
    id_registro = pedir_entero("ID: ")
    empleado = None
    if id_registro is not None:
        empleado = empleados.obtener(id_registro)
    if empleado is None:
        print("No encontrado")
    elif confirmar(f"¿Eliminar {empleado.etiqueta()}?"):
        exito, mensaje = empleados.eliminar(id_registro)
        mostrar_resultado(exito, mensaje)
    else:
        print("Operación cancelada")
    pausa()


MENU_EMPLEADOS = {
    "1": ("Crear empleado", crear_empleado),
    "2": ("Listar empleados", listar_empleados),
    "3": ("Buscar empleado", buscar_empleado),
    "4": ("Ver por ID", ver_empleado),
    "5": ("Actualizar empleado", actualizar_empleado),
    "6": ("Eliminar empleado", eliminar_empleado),
    "0": ("Volver", None),
}


def ejecutar_menu(titulo, opciones):
    while True:
        print(f"\n{titulo}")
        for tecla, (texto, _funcion) in opciones.items():
            print(f"  {tecla}. {texto}")
        tecla = input("Opción: ").strip()
        if tecla not in opciones:
            print("Opción no válida")
            pausa()
            continue
        _texto, funcion = opciones[tecla]
        if funcion is None:
            break
        funcion()


def main():
    ejecutar_menu("EMPLEADOS", MENU_EMPLEADOS)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
