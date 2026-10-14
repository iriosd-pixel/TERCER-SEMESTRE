from views import PacienteController, MedicoController, CitaController
from shared.herramientas import confirmar


# Los mismos controladores sirven para validar las relaciones de las citas.
pacientes = PacienteController()
medicos = MedicoController()
citas = CitaController(pacientes, medicos)
pacientes.conectar_citas(citas)
medicos.conectar_citas(citas)


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
# Pantallas de pacientes
# ---------------------------------------------------------------------
def crear_paciente():
    datos = {
        "nombre": input("Nombre: "),
        "apellido": input("Apellido: "),
        "email": input("Email: "),
        "telefono": input("Teléfono: "),
    }
    exito, mensaje = pacientes.crear(datos)
    mostrar_resultado(exito, mensaje)
    pausa()


def listar_pacientes():
    mostrar_lista(pacientes.leer(), "Todavía no hay pacientes.")
    pausa()


def buscar_paciente():
    texto = input("Nombre, apellido, email o teléfono: ")
    mostrar_lista(pacientes.buscar(texto), "Sin coincidencias.")
    pausa()


def ver_paciente():
    id_registro = pedir_entero("ID: ")
    paciente = None
    if id_registro is not None:
        paciente = pacientes.obtener(id_registro)
    if paciente is None:
        print("No encontrado")
    else:
        print(paciente.a_diccionario())
    pausa()


def actualizar_paciente():
    id_registro = pedir_entero("ID: ")
    paciente = None
    if id_registro is not None:
        paciente = pacientes.obtener(id_registro)
    if paciente is None:
        print("No encontrado")
        return pausa()
    campos = ("nombre", "apellido", "email", "telefono")
    cambios = pedir_cambios(paciente, campos)
    exito, mensaje = pacientes.actualizar(id_registro, cambios)
    mostrar_resultado(exito, mensaje)
    pausa()


def eliminar_paciente():
    id_registro = pedir_entero("ID: ")
    paciente = None
    if id_registro is not None:
        paciente = pacientes.obtener(id_registro)
    if paciente is None:
        print("No encontrado")
    elif confirmar(f"¿Eliminar {paciente.etiqueta()}?"):
        exito, mensaje = pacientes.eliminar(id_registro)
        mostrar_resultado(exito, mensaje)
    else:
        print("Operación cancelada")
    pausa()


# ---------------------------------------------------------------------
# Pantallas de médicos
# ---------------------------------------------------------------------
def crear_medico():
    datos = {
        "nombre": input("Nombre: "),
        "apellido": input("Apellido: "),
        "email": input("Email: "),
        "especialidad": input("Especialidad: "),
    }
    exito, mensaje = medicos.crear(datos)
    mostrar_resultado(exito, mensaje)
    pausa()


def listar_medicos():
    mostrar_lista(medicos.leer(), "Todavía no hay médicos.")
    pausa()


def buscar_medico():
    texto = input("Nombre, apellido, email o especialidad: ")
    mostrar_lista(medicos.buscar(texto), "Sin coincidencias.")
    pausa()


def ver_medico():
    id_registro = pedir_entero("ID: ")
    medico = None
    if id_registro is not None:
        medico = medicos.obtener(id_registro)
    if medico is None:
        print("No encontrado")
    else:
        print(medico.a_diccionario())
    pausa()


def actualizar_medico():
    id_registro = pedir_entero("ID: ")
    medico = None
    if id_registro is not None:
        medico = medicos.obtener(id_registro)
    if medico is None:
        print("No encontrado")
        return pausa()
    campos = ("nombre", "apellido", "email", "especialidad")
    cambios = pedir_cambios(medico, campos)
    exito, mensaje = medicos.actualizar(id_registro, cambios)
    mostrar_resultado(exito, mensaje)
    pausa()


def eliminar_medico():
    id_registro = pedir_entero("ID: ")
    medico = None
    if id_registro is not None:
        medico = medicos.obtener(id_registro)
    if medico is None:
        print("No encontrado")
    elif confirmar(f"¿Eliminar {medico.etiqueta()}?"):
        exito, mensaje = medicos.eliminar(id_registro)
        mostrar_resultado(exito, mensaje)
    else:
        print("Operación cancelada")
    pausa()


# ---------------------------------------------------------------------
# Pantallas de citas
# ---------------------------------------------------------------------
def crear_cita():
    print("Pacientes disponibles:")
    mostrar_lista(pacientes.leer())
    print("Médicos disponibles:")
    mostrar_lista(medicos.leer())
    datos = {
        "paciente_id": input("ID del paciente: "),
        "medico_id": input("ID del médico: "),
        "fecha": input("Fecha (AAAA-MM-DD): "),
        "hora": input("Hora (HH:MM): "),
    }
    exito, mensaje = citas.crear(datos)
    mostrar_resultado(exito, mensaje)
    pausa()


def listar_citas():
    mostrar_lista(citas.leer(), "Todavía no hay citas.")
    pausa()


def buscar_cita():
    texto = input("Fecha o número de paciente/médico: ")
    mostrar_lista(citas.buscar(texto), "Sin coincidencias.")
    pausa()


def ver_cita():
    id_registro = pedir_entero("ID: ")
    cita = None
    if id_registro is not None:
        cita = citas.obtener(id_registro)
    if cita is None:
        print("No encontrado")
    else:
        print(cita.a_diccionario())
    pausa()


def actualizar_cita():
    id_registro = pedir_entero("ID: ")
    cita = None
    if id_registro is not None:
        cita = citas.obtener(id_registro)
    if cita is None:
        print("No encontrado")
        return pausa()
    campos = ("paciente_id", "medico_id", "fecha", "hora")
    cambios = pedir_cambios(cita, campos)
    exito, mensaje = citas.actualizar(id_registro, cambios)
    mostrar_resultado(exito, mensaje)
    pausa()


def eliminar_cita():
    id_registro = pedir_entero("ID: ")
    cita = None
    if id_registro is not None:
        cita = citas.obtener(id_registro)
    if cita is None:
        print("No encontrado")
    elif confirmar(f"¿Eliminar cita {id_registro}?"):
        exito, mensaje = citas.eliminar(id_registro)
        mostrar_resultado(exito, mensaje)
    else:
        print("Operación cancelada")
    pausa()


MENU_PACIENTES = {
    "1": ("Crear", crear_paciente),
    "2": ("Listar", listar_pacientes),
    "3": ("Buscar", buscar_paciente),
    "4": ("Ver por ID", ver_paciente),
    "5": ("Actualizar", actualizar_paciente),
    "6": ("Eliminar", eliminar_paciente),
    "0": ("Volver", None),
}
MENU_MEDICOS = {
    "1": ("Crear", crear_medico),
    "2": ("Listar", listar_medicos),
    "3": ("Buscar", buscar_medico),
    "4": ("Ver por ID", ver_medico),
    "5": ("Actualizar", actualizar_medico),
    "6": ("Eliminar", eliminar_medico),
    "0": ("Volver", None),
}
MENU_CITAS = {
    "1": ("Crear", crear_cita),
    "2": ("Listar", listar_citas),
    "3": ("Buscar", buscar_cita),
    "4": ("Ver por ID", ver_cita),
    "5": ("Actualizar", actualizar_cita),
    "6": ("Eliminar", eliminar_cita),
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
        print("\nSISTEMA DE HOSPITAL")
        print("  1. Pacientes")
        print("  2. Médicos")
        print("  3. Citas")
        print("  0. Salir")
        opcion = input("Opción: ").strip()
        if opcion == "1":
            ejecutar_menu("PACIENTES", MENU_PACIENTES)
        elif opcion == "2":
            ejecutar_menu("MÉDICOS", MENU_MEDICOS)
        elif opcion == "3":
            ejecutar_menu("CITAS", MENU_CITAS)
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
