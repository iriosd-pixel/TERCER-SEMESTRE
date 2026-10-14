from views import DepartamentoController, EmpleadoController, NominaController
from shared.herramientas import confirmar


# Los controladores compartidos permiten comprobar las relaciones.
departamentos = DepartamentoController()
empleados = EmpleadoController(departamentos)
nominas = NominaController(empleados)
departamentos.conectar_empleados(empleados)
empleados.conectar_nominas(nominas)


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


def mostrar_lista(objetos, vacio="No hay registros."):
    if not objetos:
        print(vacio)
        return
    for objeto in objetos:
        print(f"  {objeto}")
    print(f"Total: {len(objetos)}")


def pedir_cambios(objeto, campos):
    cambios = {}
    for campo in campos:
        valor_actual = getattr(objeto, campo)
        valor_nuevo = input(f"{campo} [{valor_actual}] (vacío conserva): ").strip()
        if valor_nuevo:
            cambios[campo] = valor_nuevo
    return cambios


# ---------------------------------------------------------------------
# Pantallas de departamentos
# ---------------------------------------------------------------------
def crear_departamento():
    datos = {"nombre": input("Nombre: ")}
    exito, mensaje = departamentos.crear(datos)
    mostrar_resultado(exito, mensaje)
    pausa()


def listar_departamentos():
    mostrar_lista(departamentos.leer(), "Todavía no hay departamentos.")
    pausa()


def buscar_departamento():
    texto = input("Nombre: ")
    mostrar_lista(departamentos.buscar(texto), "Sin coincidencias.")
    pausa()


def ver_departamento():
    id_registro = pedir_entero("ID: ")
    departamento = None
    if id_registro is not None:
        departamento = departamentos.obtener(id_registro)
    if departamento is None:
        print("No encontrado")
    else:
        print(departamento.a_diccionario())
    pausa()


def actualizar_departamento():
    id_registro = pedir_entero("ID: ")
    departamento = None
    if id_registro is not None:
        departamento = departamentos.obtener(id_registro)
    if departamento is None:
        print("No encontrado")
        return pausa()
    cambios = pedir_cambios(departamento, ("nombre",))
    exito, mensaje = departamentos.actualizar(id_registro, cambios)
    mostrar_resultado(exito, mensaje)
    pausa()


def eliminar_departamento():
    id_registro = pedir_entero("ID: ")
    departamento = None
    if id_registro is not None:
        departamento = departamentos.obtener(id_registro)
    if departamento is None:
        print("No encontrado")
    elif confirmar(f"¿Eliminar {departamento.etiqueta()}?"):
        exito, mensaje = departamentos.eliminar(id_registro)
        mostrar_resultado(exito, mensaje)
    else:
        print("Operación cancelada")
    pausa()


# ---------------------------------------------------------------------
# Pantallas de empleados
# ---------------------------------------------------------------------
def crear_empleado():
    mostrar_lista(departamentos.leer(), "Cree un departamento primero.")
    datos = {
        "nombre": input("Nombre: "),
        "apellido": input("Apellido: "),
        "email": input("Email: "),
        "departamento_id": input("ID del departamento: "),
    }
    exito, mensaje = empleados.crear(datos)
    mostrar_resultado(exito, mensaje)
    pausa()


def listar_empleados():
    mostrar_lista(empleados.leer(), "Todavía no hay empleados.")
    pausa()


def buscar_empleado():
    texto = input("Nombre, apellido o email: ")
    mostrar_lista(empleados.buscar(texto), "Sin coincidencias.")
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
    campos = ("nombre", "apellido", "email", "departamento_id")
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


# ---------------------------------------------------------------------
# Pantallas de nóminas
# ---------------------------------------------------------------------
def crear_nomina():
    mostrar_lista(empleados.leer(), "Cree un empleado primero.")
    datos = {
        "empleado_id": input("ID del empleado: "),
        "periodo": input("Periodo: "),
        "sueldo_base": input("Sueldo base: "),
        "bonificacion": input("Bonificación: "),
        "descuento": input("Descuento: "),
    }
    exito, mensaje = nominas.crear(datos)
    mostrar_resultado(exito, mensaje)
    pausa()


def listar_nominas():
    mostrar_lista(nominas.leer(), "Todavía no hay nóminas.")
    pausa()


def buscar_nomina():
    texto = input("Periodo o ID empleado: ")
    mostrar_lista(nominas.buscar(texto), "Sin coincidencias.")
    pausa()


def ver_nomina():
    id_registro = pedir_entero("ID: ")
    nomina = None
    if id_registro is not None:
        nomina = nominas.obtener(id_registro)
    if nomina is None:
        print("No encontrado")
    else:
        print(nomina.a_diccionario())
        print(f"Pago neto: {nomina.pago_neto():.2f}")
    pausa()


def actualizar_nomina():
    id_registro = pedir_entero("ID: ")
    nomina = None
    if id_registro is not None:
        nomina = nominas.obtener(id_registro)
    if nomina is None:
        print("No encontrado")
        return pausa()
    campos = ("empleado_id", "periodo", "sueldo_base", "bonificacion", "descuento")
    cambios = pedir_cambios(nomina, campos)
    exito, mensaje = nominas.actualizar(id_registro, cambios)
    mostrar_resultado(exito, mensaje)
    pausa()


def eliminar_nomina():
    id_registro = pedir_entero("ID: ")
    nomina = None
    if id_registro is not None:
        nomina = nominas.obtener(id_registro)
    if nomina is None:
        print("No encontrado")
    elif confirmar(f"¿Eliminar nómina {id_registro}?"):
        exito, mensaje = nominas.eliminar(id_registro)
        mostrar_resultado(exito, mensaje)
    else:
        print("Operación cancelada")
    pausa()


MENU_DEPARTAMENTOS = {
    "1": ("Crear", crear_departamento),
    "2": ("Listar", listar_departamentos),
    "3": ("Buscar", buscar_departamento),
    "4": ("Ver por ID", ver_departamento),
    "5": ("Actualizar", actualizar_departamento),
    "6": ("Eliminar", eliminar_departamento),
    "0": ("Volver", None),
}

MENU_EMPLEADOS = {
    "1": ("Crear", crear_empleado),
    "2": ("Listar", listar_empleados),
    "3": ("Buscar", buscar_empleado),
    "4": ("Ver por ID", ver_empleado),
    "5": ("Actualizar", actualizar_empleado),
    "6": ("Eliminar", eliminar_empleado),
    "0": ("Volver", None),
}

MENU_NOMINAS = {
    "1": ("Crear", crear_nomina),
    "2": ("Listar", listar_nominas),
    "3": ("Buscar", buscar_nomina),
    "4": ("Ver por ID", ver_nomina),
    "5": ("Actualizar", actualizar_nomina),
    "6": ("Eliminar", eliminar_nomina),
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
    while True:
        print("\nSISTEMA DE NÓMINA")
        print("  1. Departamentos")
        print("  2. Empleados")
        print("  3. Nóminas")
        print("  0. Salir")
        opcion = input("Opción: ").strip()
        if opcion == "1":
            ejecutar_menu("DEPARTAMENTOS", MENU_DEPARTAMENTOS)
        elif opcion == "2":
            ejecutar_menu("EMPLEADOS", MENU_EMPLEADOS)
        elif opcion == "3":
            ejecutar_menu("NÓMINAS", MENU_NOMINAS)
        elif opcion == "0":
            break
        else:
            print("Opción no válida")
            pausa()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
