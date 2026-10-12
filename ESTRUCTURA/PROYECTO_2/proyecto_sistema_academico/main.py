import views

from shared.herramientas import(
    imprimir_titulo,
    imprimir_exito,
    imprimir_error,
    imprimir_info,
    confirmar
)
def mostrar_resultado(exito, mensaje):
    if exito:
        imprimir_exito(mensaje)
    else:
        imprimir_error(mensaje)
        
def pedir_entero(etiqueta):
    while True:
        try:
            numero = int(input(etiqueta))
            return numero
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

    datos = objeto.a_diccionario()

    for campo, valor in datos.items():
        print(f"{campo}: {valor}")
        
def pedir_cambios(objeto, campos):
    cambios = {}

    imprimir_info("Deja vacío un campo para conservar su valor")

    for campo in campos:
        actual = getattr(objeto, campo)
        nuevo = input(f"{campo} [{actual}]: ").strip()

        if nuevo != "":
            cambios[campo] = nuevo

    return cambios

def crear_estudiante():
    imprimir_titulo("CREAR ESTUDIANTE")

    datos = {
        "nombre": input("Nombre: "),
        "apellido": input("Apellido: "),
        "email": input("Email: "),
        "carnet": input("Carnet: "),
        "carrera": input("Carrera: ")
    }

    exito, mensaje = views.crear_estudiante(datos)
    mostrar_resultado(exito, mensaje)
    pausa()

def pausa():
    input("\nPresiona Enter para continuar...")
    
def listar_estudiantes():
    imprimir_titulo("LISTA DE ESTUDIANTES")

    estudiantes = views.obtener_estudiantes()
    mostrar_lista(estudiantes)

    pausa()
    
def buscar_estudiante():
    imprimir_titulo("BUSCAR ESTUDIANTES")

    termino = input("Texto a buscar: ")
    encontrados = views.buscar_estudiantes(termino)

    mostrar_lista(encontrados)
    pausa()
    
def ver_estudiante():
    imprimir_titulo("VER ESTUDIANTE")

    id_estudiante = pedir_entero("ID del estudiante: ")
    estudiante = views.obtener_estudiante(id_estudiante)

    mostrar_detalle(estudiante)
    pausa()
    
def actualizar_estudiante():
    imprimir_titulo("ACTUALIZAR ESTUDIANTE")

    id_estudiante = pedir_entero("ID del estudiante: ")
    estudiante = views.obtener_estudiante(id_estudiante)

    if estudiante is None:
        imprimir_error("No existe el estudiante")
    else:
        campos = ("nombre", "apellido", "email", "carnet", "carrera")
        cambios = pedir_cambios(estudiante, campos)

        exito, mensaje = views.actualizar_estudiante(
            id_estudiante, cambios
        )
        mostrar_resultado(exito, mensaje)

    pausa()
    
def eliminar_estudiante():
    imprimir_titulo("ELIMINAR ESTUDIANTE")

    id_estudiante = pedir_entero("ID del estudiante: ")
    estudiante = views.obtener_estudiante(id_estudiante)

    if estudiante is None:
        imprimir_error("No existe el estudiante")
    else:
        mostrar_detalle(estudiante)

        if confirmar("¿Deseas eliminar este estudiante?"):
            exito, mensaje = views.eliminar_estudiante(id_estudiante)
            mostrar_resultado(exito, mensaje)
        else:
            imprimir_info("Eliminación cancelada")

    pausa()

def crear_materia():
    imprimir_titulo("CREAR MATERIA")

    datos = {
        "nombre": input("Nombre: "),
        "codigo": input("Código: "),
        "creditos": input("Créditos (1 a 10): "),
        "cupos": input("Cupos (0 a 30): ")
    }

    exito, mensaje = views.crear_materia(datos)
    mostrar_resultado(exito, mensaje)
    pausa()
    
def listar_materias():
    imprimir_titulo("LISTA DE MATERIAS")

    materias = views.obtener_materias()
    mostrar_lista(materias)

    pausa()

def buscar_materia():
    imprimir_titulo("BUSCAR MATERIAS")

    termino = input("Nombre o código: ")
    materias = views.buscar_materias(termino)
    mostrar_lista(materias)

    pausa()


def ver_materia():
    imprimir_titulo("VER MATERIA")

    id_materia = pedir_entero("ID de la materia: ")
    materia = views.obtener_materia(id_materia)
    mostrar_detalle(materia)

    pausa()


def actualizar_materia():
    imprimir_titulo("ACTUALIZAR MATERIA")

    id_materia = pedir_entero("ID de la materia: ")
    materia = views.obtener_materia(id_materia)

    if materia is None:
        imprimir_error("No existe la materia")
    else:
        campos = ("nombre", "codigo", "creditos", "cupos")
        cambios = pedir_cambios(materia, campos)

        exito, mensaje = views.actualizar_materia(id_materia, cambios)
        mostrar_resultado(exito, mensaje)

    pausa()


def eliminar_materia():
    imprimir_titulo("ELIMINAR MATERIA")

    id_materia = pedir_entero("ID de la materia: ")
    materia = views.obtener_materia(id_materia)

    if materia is None:
        imprimir_error("No existe la materia")
    else:
        mostrar_detalle(materia)

        if confirmar("¿Deseas eliminar esta materia?"):
            exito, mensaje = views.eliminar_materia(id_materia)
            mostrar_resultado(exito, mensaje)
        else:
            imprimir_info("Eliminación cancelada")

    pausa()


def mostrar_materias_sin_cupo():
    imprimir_titulo("MATERIAS SIN CUPO")

    materias = views.materias_sin_cupo()
    mostrar_lista(materias)

    pausa()


# =====================================================================
# MATRÍCULAS
# =====================================================================
def crear_matricula():
    imprimir_titulo("CREAR MATRÍCULA")

    datos = {
        "estudiante_id": pedir_entero("ID del estudiante: "),
        "materia_id": pedir_entero("ID de la materia: "),
        "periodo": input("Periodo: "),
        "nota": input("Nota inicial (0 a 20): ")
    }

    exito, mensaje = views.crear_matricula(datos)
    mostrar_resultado(exito, mensaje)

    pausa()


def listar_matriculas():
    imprimir_titulo("LISTA DE MATRÍCULAS")

    matriculas = views.obtener_matriculas()
    mostrar_lista(matriculas)

    pausa()


def registrar_nota():
    imprimir_titulo("REGISTRAR NOTA")

    id_matricula = pedir_entero("ID de la matrícula: ")
    nota = input("Nueva nota (0 a 20): ")

    exito, mensaje = views.registrar_nota(id_matricula, nota)
    mostrar_resultado(exito, mensaje)

    pausa()


def ver_certificado():
    imprimir_titulo("CERTIFICADO")

    id_matricula = pedir_entero("ID de la matrícula: ")
    texto = views.certificado(id_matricula)

    if texto is None:
        imprimir_error("No existe la matrícula")
    else:
        print(texto)

    pausa()


def retirar_matricula():
    imprimir_titulo("RETIRAR MATRÍCULA")

    id_matricula = pedir_entero("ID de la matrícula: ")
    matricula = views.obtener_matricula(id_matricula)

    if matricula is None:
        imprimir_error("No existe la matrícula")
    else:
        mostrar_detalle(matricula)

        if confirmar("¿Deseas retirar esta matrícula?"):
            exito, mensaje = views.retirar_matricula(id_matricula)
            mostrar_resultado(exito, mensaje)
        else:
            imprimir_info("Retiro cancelado")

    pausa()


def mostrar_matriculas_por_estudiante():
    imprimir_titulo("MATRÍCULAS POR ESTUDIANTE")

    agrupadas = views.matriculas_por_estudiante()

    if not agrupadas:
        imprimir_info("No hay matrículas registradas")
    else:
        for id_estudiante, matriculas in agrupadas.items():
            print(f"\nEstudiante con ID {id_estudiante}:")
            mostrar_lista(matriculas)

    pausa()


def mostrar_promedio():
    imprimir_titulo("PROMEDIO DEL ESTUDIANTE")

    id_estudiante = pedir_entero("ID del estudiante: ")
    estudiante = views.obtener_estudiante(id_estudiante)

    if estudiante is None:
        imprimir_error("No existe el estudiante")
    else:
        promedio = views.promedio_de_estudiante(id_estudiante)

        if promedio is None:
            imprimir_info("El estudiante no tiene matrículas")
        else:
            print(f"Estudiante: {estudiante.nombre_completo()}")
            print(f"Promedio: {promedio:.2f}")

    pausa()


# =====================================================================
# RESUMEN
# =====================================================================
def mostrar_resumen():
    imprimir_titulo("RESUMEN ACADÉMICO")

    resumen = views.resumen_academico()

    print(f"Total de estudiantes: {resumen['estudiantes']}")

    print("\nCarreras:")
    if resumen["carreras"]:
        for carrera in resumen["carreras"]:
            print(f"- {carrera}")
    else:
        imprimir_info("No hay carreras registradas")

    print("\nMaterias sin cupo:")
    mostrar_lista(resumen["materias_sin_cupo"])

    print(
        f"\nMatrículas aprobadas: "
        f"{resumen['matriculas_aprobadas']}"
    )

    pausa()


# =====================================================================
# MENÚ REUTILIZABLE
# =====================================================================
def ejecutar_menu(titulo, opciones):
    while True:
        imprimir_titulo(titulo)

        for numero, datos in opciones.items():
            descripcion, accion = datos
            print(f"{numero}. {descripcion}")

        print("0. Salir / volver")

        opcion = input("\nElige una opción: ").strip()

        if opcion == "0":
            return

        if opcion in opciones:
            descripcion, accion = opciones[opcion]
            accion()
        else:
            imprimir_error("Opción inválida")
            pausa()


# =====================================================================
# SUBMENÚS
# =====================================================================
def menu_estudiantes():
    opciones = {
        "1": ("Crear estudiante", crear_estudiante),
        "2": ("Listar estudiantes", listar_estudiantes),
        "3": ("Buscar estudiantes", buscar_estudiante),
        "4": ("Ver estudiante por ID", ver_estudiante),
        "5": ("Actualizar estudiante", actualizar_estudiante),
        "6": ("Eliminar estudiante", eliminar_estudiante)
    }

    ejecutar_menu("ESTUDIANTES", opciones)


def menu_materias():
    opciones = {
        "1": ("Crear materia", crear_materia),
        "2": ("Listar materias", listar_materias),
        "3": ("Buscar materias", buscar_materia),
        "4": ("Ver materia por ID", ver_materia),
        "5": ("Actualizar materia", actualizar_materia),
        "6": ("Eliminar materia", eliminar_materia),
        "7": ("Materias sin cupo", mostrar_materias_sin_cupo)
    }

    ejecutar_menu("MATERIAS", opciones)


def menu_matriculas():
    opciones = {
        "1": ("Crear matrícula", crear_matricula),
        "2": ("Listar matrículas", listar_matriculas),
        "3": ("Registrar nota", registrar_nota),
        "4": ("Ver certificado", ver_certificado),
        "5": ("Retirar matrícula", retirar_matricula),
        "6": (
            "Matrículas por estudiante",
            mostrar_matriculas_por_estudiante
        ),
        "7": ("Promedio del estudiante", mostrar_promedio)
    }

    ejecutar_menu("MATRÍCULAS", opciones)


# =====================================================================
# MENÚ PRINCIPAL
# =====================================================================
def main():
    opciones = {
        "1": ("Estudiantes", menu_estudiantes),
        "2": ("Materias", menu_materias),
        "3": ("Matrículas", menu_matriculas),
        "4": ("Resumen académico", mostrar_resumen)
    }

    ejecutar_menu("SISTEMA ACADÉMICO", opciones)


if __name__ == "__main__":
    main()