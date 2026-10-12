import os
from datetime import date

from models import Estudiante, Materia, Matricula
from shared.json_manager import GestorJSON
from shared.herramientas import es_email_valido


CARPETA = os.path.join(os.path.dirname(__file__), "data")
gestor_estudiantes = GestorJSON(os.path.join(CARPETA, "estudiantes.json"))
gestor_materias = GestorJSON(os.path.join(CARPETA, "materias.json"))
gestor_matriculas = GestorJSON(os.path.join(CARPETA, "matriculas.json"))

# =====================================================================
# FUCNIONES GENERICAS: sirven paar cuaqluier entidad
# =====================================================================
def leer_objetos(gestor, clase):
    objetos=[]
    for registro in gestor.leer():
        objeto=clase.desde_diccionario(registro)
        objetos.append(objeto)
    return objetos
    

def obtener_por_id(gestor, clase, id_registro):
    for objeto in leer_objetos(gestor, clase):
        if objeto.id== id_registro:
            return objeto
    return None

def buscar(gestor, clase, texto, campos):
    texto= str(texto).strip().lower()
    encontrados=[]
    
    if texto =="":
        return encontrados
    for objeto in leer_objetos(gestor, clase):
        # TUPLA: campos contiene los nombres fijos de los atributos buscables.
        for campo in campos:
            valor= str(getattr(objeto, campo)).lower() 
            if texto in valor:
                encontrados.append(objeto)
                break
    return encontrados     

def siguiente_id(gestor):
    registros=gestor.leer()
    mayor=0
    
    for registro in registros:
        if registro["id"]>mayor:
            mayor=registro["id"]
    
    return mayor+1

def  guardar_nuevo(gestor, objeto):
    resgistros= gestor.leer()
    resgistros.append(objeto.a_diccionario())
    return gestor.guardar(resgistros)

def reemplazar(gestor, objeto):
    registros=gestor.leer()
    
    for indice, registro in enumerate(registros):
        if registro["id"]==objeto.id:
            registros[indice]=objeto.a_diccionario()
            return gestor.guardar(registros)
    
    return False

def eliminar(gestor, id_registro):
    registros=gestor.leer()
    restantes=[]
    
    for registro in registros:
        if registro["id"]!= id_registro:
            restantes.append(registro)
    
    if len(restantes)==len(registros):
        return False
    
    return gestor.guardar(restantes)

def ids_registrados(gestor):
    # CONJUNTO: permite comprobar si un id existe y evita repetidos.
    ids=set()
    
    for registo in gestor.leer():
        ids.add(registo["id"])
        
    return ids

def indice_por_id(objetos):
    # DICCIONARIO ÍNDICE: permite acceder directamente a un objeto por su id.
    indice={}
    for objeto in objetos:
        indice[objeto.id]=objeto
        
    return indice

# =====================================================================
# ESTUDIANTES
# =====================================================================
"""VALIDACIONES"""
def carnets_registrados(excepto_id=None):
    # CONJUNTO: permite comprobar si otro estudiante ya usa un carnet.
    carnets= set()
    for registro in gestor_estudiantes.leer():
        if registro["id"]!= excepto_id:
            carnets.add(registro["carnet"].strip().upper())
            
    return carnets

def validar_estudiante(datos, id_actual=None):
    obligatorios=("nombre", "apellido", "email", "carnet")
    
    for campo in obligatorios:
        if id_actual is None or campo in datos:
            if str(datos.get(campo, "")).strip()=="":
                return f"El campo {campo} es obligatorio"
            
    if "email" in datos:
            email = str(datos["email"]).strip().lower()

            if not es_email_valido(email):
                return f"Email inválido: '{email}'"

            # CONJUNTO: permite comprobar si otro estudiante usa ese email.
            emails_usados = set()

            for registro in gestor_estudiantes.leer():
                if registro["id"] != id_actual:
                    emails_usados.add(registro["email"].strip().lower())

            if email in emails_usados:
                return "Ese email ya está registrado"

    if "carnet" in datos:
            carnet = str(datos["carnet"]).strip().upper()

            if carnet in carnets_registrados(id_actual):
                return "Ese carnet ya está registrado"

    return None
"""" FUNCIONES DE ESTUDIANTE"""
def crear_estudiante(datos):
    error=validar_estudiante(datos)
    if error:
    # TUPLA: devuelve el resultado y el motivo del error.
        return False, error
    
    estudiante=Estudiante(
        siguiente_id(gestor_estudiantes),
        str(datos["Nombre"]).strip().title(),
        str(datos["apellido"]).strip().title(),
        str(datos["email"]).strip().lower(),
        str(datos["carnet"]).strip().upper(),
        str(datos.get("carrera", "")).strip().title()
    )
    
    if not guardar_nuevo(gestor_estudiantes, estudiante):
        return False, "No se pudo guardar el estudiante"
    # TUPLA: devuelve el resultado y un mensaje de confirmación.
    return True, f"Estudiante creado: {estudiante.etiqueta()}"

def obtener_estudiantes():
    return leer_objetos(gestor_estudiantes,Estudiante)

def obtener_estudiante(id_estudiante):
    return obtener_por_id(gestor_estudiantes, Estudiante, id_estudiante)

def buscar_estudiantes(termino):
    # TUPLA: define los campos fijos que se revisan en la búsqueda.
    campos = ("nombre", "apellido", "email", "carnet", "carrera")
    return buscar(gestor_estudiantes, Estudiante, termino,campos)

def actualizar_estudiante(id_estudiante, cambios):
    estudiante=obtener_estudiante(id_estudiante)
    
    if estudiante is None:
        return False, "no existe el estudiante"
    
    if not cambios:
        return False, "No se indico ningun cambio"
    # CONJUNTO: identifica los campos que no se permiten modificar.
    permitidos={"nombre", "apellido", "email", "carnet", "carrera"}
    desconocidos= set(cambios)-permitidos
    
    if desconocidos:
        return False, f"Campos no válidos: {', '.join(sorted(desconocidos))}"
    
    error= validar_estudiante(cambios, estudiante.id)
    
    if error:
        return False, error
    for campo, valor in cambios.items():
            valor = str(valor).strip()

            if campo in ("nombre", "apellido", "carrera"):
                valor = valor.title()
            elif campo == "email":
                valor = valor.lower()
            elif campo == "carnet":
                valor = valor.upper()

            setattr(estudiante, campo, valor)

    if not reemplazar(gestor_estudiantes, estudiante):
        return False, "No se pudo actualizar el estudiante"

        # TUPLA: devuelve el resultado y un mensaje de confirmación.
    return True, f"Estudiante {estudiante.id} actualizado"    

def eliminar_estudiante(id_estudiante):
    estudiante=obtener_estudiante(id_estudiante)
    
    if estudiante is None:
        return False, "NO existe el estudiante"
    
    if not eliminar(gestor_estudiantes, estudiante.id):
        return False, "no se pudo eliminar el estudiante"
    return True, f"Estudiante {estudiante.id} eliminado"






# ==============================================================
#  MATERIA
# =====================================================================
"""VALIDACIONES"""
def codigos_registrados(excepto_id=None):
    # CONJUNTO: reúne los códigos usados para detectar duplicados.
    codigos = set()

    for registro in gestor_materias.leer():
        if registro["id"] != excepto_id:
            codigos.add(registro["codigo"].strip().upper())

    return codigos

def validar_materia(datos, id_actual=None):
    for campo in ("nombre", "codigo"):
        if id_actual is None or campo in datos:
            if str(datos.get(campo, "")).strip() == "":
                return f"El campo {campo} es obligatorio"

    if "codigo" in datos:
        codigo = str(datos["codigo"]).strip().upper()

        if codigo in codigos_registrados(id_actual):
            return "Ese código ya está registrado"

    if id_actual is None or "creditos" in datos:
        try:
            creditos = int(str(datos.get("creditos", 0)).strip())
        except (TypeError, ValueError):
            return "Los créditos deben ser un número entero"

        if not 1 <= creditos <= 10:
            return "Los créditos deben estar entre 1 y 10"

    if id_actual is None or "cupos" in datos:
        try:
            cupos = int(str(datos.get("cupos", 0)).strip())
        except (TypeError, ValueError):
            return "Los cupos deben ser un número entero"

        if not 0 <= cupos <= Materia.CUPOS_MAXIMOS:
            return f"Los cupos deben estar entre 0 y {Materia.CUPOS_MAXIMOS}"

    return None
"""FUNCIONES DE CLASE"""
def crear_materia(datos):
    error = validar_materia(datos)

    if error:
        return False, error

    materia = Materia(
        siguiente_id(gestor_materias),
        str(datos["nombre"]).strip().title(),
        str(datos["codigo"]).strip().upper(),
        int(str(datos["creditos"]).strip()),
        int(str(datos.get("cupos", 0)).strip())
    )

    if not guardar_nuevo(gestor_materias, materia):
        return False, "No se pudo guardar la materia"

    # TUPLA: devuelve el resultado y un mensaje de confirmación.
    return True, f"Materia creada: {materia.etiqueta()}"

def obtener_materias():
    return leer_objetos(gestor_materias, Materia)

def obtener_materia(id_materia):
    return obtener_por_id(gestor_materias, Materia, id_materia)

def buscar_materias(termino):
    campos=("nombre", "codigo")
    
    return buscar( gestor_materias, Materia, termino, campos)

def actualizar_materia(id_materia, cambios):
    materia = obtener_materia(id_materia)

    if materia is None:
        return False, "No existe la materia"

    if not cambios:
        return False, "No se indicó ningún cambio"

    # CONJUNTO: identifica campos que no se permiten modificar.
    permitidos = {"nombre", "codigo", "creditos", "cupos"}
    desconocidos = set(cambios) - permitidos

    if desconocidos:
        return False, f"Campos no válidos: {', '.join(sorted(desconocidos))}"

    error = validar_materia(cambios, materia.id)

    if error:
        return False, error

    for campo, valor in cambios.items():
        if campo == "nombre":
            valor = str(valor).strip().title()
        elif campo == "codigo":
            valor = str(valor).strip().upper()
        else:
            valor = int(str(valor).strip())

        setattr(materia, campo, valor)

    if not reemplazar(gestor_materias, materia):
        return False, "No se pudo actualizar la materia"

    # TUPLA: devuelve el resultado y un mensaje de confirmación.
    return True, f"Materia {materia.id} actualizada"

def eliminar_materia(id_materia):
    materia = obtener_materia(id_materia)

    if materia is None:
        return False, "No existe la materia"

    if not eliminar(gestor_materias, materia.id):
        return False, "No se pudo eliminar la materia"

    # TUPLA: devuelve el resultado y un mensaje de confirmación.
    return True, f"Materia {materia.id} eliminada"

def materias_sin_cupo():
    sin_cupo=[]
    
    for materia in obtener_materias():
        if not materia.hay_cupo():
            sin_cupo.append(materia)
    
    return sin_cupo






# =====================================================================
# CONTROLADOR DE VENTAS
# =====================================================================
"""VALIDACIONES"""
def validar_matricula(datos):
    try:
        estudiante_id = int(datos.get("estudiante_id", 0))
        materia_id = int(datos.get("materia_id", 0))
    except (TypeError, ValueError):
        return "Los IDs deben ser números enteros"

    periodo = str(datos.get("periodo", "")).strip()
    nota = datos.get("nota", 0)

    if periodo == "":
        return "El periodo es obligatorio"

    if not Materia.es_nota_valida(nota):
        return "La nota debe estar entre 0 y 20"

    # CONJUNTO: permite comprobar si el estudiante está registrado.
    if estudiante_id not in ids_registrados(gestor_estudiantes):
        return "No existe el estudiante"

    # CONJUNTO: permite comprobar si la materia está registrada.
    if materia_id not in ids_registrados(gestor_materias):
        return "No existe la materia"

    materia = obtener_materia(materia_id)

    if not materia.hay_cupo():
        return "La materia no tiene cupos disponibles"

    for registro in gestor_matriculas.leer():
        if (registro["estudiante_id"] == estudiante_id
            and registro["materia_id"] == materia_id
            and registro["periodo"] == periodo):
            return "El estudiante ya está matriculado en esa materia y periodo"

    return None

"""FUNCIONES DE MATRICULA"""
def crear_matricula(datos):
    error = validar_matricula(datos)

    if error:
        return False, error

    materia = obtener_materia(int(datos["materia_id"]))

    matricula = Matricula(
        siguiente_id(gestor_matriculas),
        int(datos["estudiante_id"]),
        materia.id,
        str(datos["periodo"]).strip(),
        float(datos.get("nota", 0))
    )

    materia.ocupar_cupo()

    if not reemplazar(gestor_materias, materia):
        return False, "No se pudieron guardar los cupos"

    if not guardar_nuevo(gestor_matriculas, matricula):
        materia.liberar_cupo()
        reemplazar(gestor_materias, materia)
        return False, "No se pudo guardar la matrícula"

    # TUPLA: devuelve el resultado y un mensaje de confirmación.
    return True, f"Matrícula {matricula.id} creada"

def obtener_matriculas():
    return leer_objetos(gestor_matriculas, Matricula)

def obtener_matricula(id_matricula):
    return obtener_por_id(gestor_matriculas, Matricula, id_matricula)

def registrar_nota(id_matricula, nota):
    matricula=obtener_matricula(id_matricula)
    
    if matricula is None:
        return False, "No existe la matricula"
    
    if not Materia.es_nota_valida(nota):
        return False, "La nota debe estar entre 0 y 20"
    
    matricula.nota=float(nota)
    
    if not reemplazar(gestor_matriculas, matricula):
        return False, "No se pudo guardar la nota"
    # TUPLA: devuelve el resultado y un mensaje de confirmación.
    return True, f"Nota registrada: {matricula.nota} · {matricula.estado()}"

def retirar_matricula(id_matricula):
    matricula = obtener_matricula(id_matricula)

    if matricula is None:
        return False, "No existe la matrícula"

    materia = obtener_materia(matricula.materia_id)

    if materia is None:
        return False, "No existe la materia de esa matrícula"

    if not eliminar(gestor_matriculas, matricula.id):
        return False, "No se pudo retirar la matrícula"

    materia.liberar_cupo()

    if not reemplazar(gestor_materias, materia):
        guardar_nuevo(gestor_matriculas, matricula)
        return False, "No se pudo guardar la devolución del cupo"

    # TUPLA: devuelve el resultado y un mensaje de confirmación.
    return True, "Matrícula retirada y cupo devuelto"

def certificado(id_matricula):
    matricula = obtener_matricula(id_matricula)

    if matricula is None:
        return None

    # DICCIONARIOS ÍNDICE: permiten acceder a cada objeto por su id.
    estudiantes = indice_por_id(obtener_estudiantes())
    materias = indice_por_id(obtener_materias())

    estudiante = estudiantes.get(matricula.estudiante_id)
    materia = materias.get(matricula.materia_id)

    if estudiante is None or materia is None:
        return "No se puede generar el certificado: faltan datos"

    return (
        f"CERTIFICADO DE MATRÍCULA #{matricula.id}\n"
        f"Estudiante: {estudiante.nombre_completo()}\n"
        f"Carnet: {estudiante.carnet}\n"
        f"Materia: {materia.nombre} ({materia.codigo})\n"
        f"Periodo: {matricula.periodo}\n"
        f"Fecha: {matricula.fecha}\n"
        f"Nota: {matricula.nota:.1f}\n"
        f"Estado: {matricula.estado()}"
    )

def matriculas_por_estudiante():
    agrupadas={}
    
    for matricula in obtener_matriculas():
        lista= agrupadas.setdefault(matricula.estudiante_id, [])
        lista.append(matricula)
        
    return agrupadas

def promedio_de_estudiante(id_estudiante):
    agrupadas = matriculas_por_estudiante()
    matriculas = agrupadas.get(id_estudiante, [])

    if not matriculas:
        return None

    suma = 0

    for matricula in matriculas:
        suma += matricula.nota

    return round(suma / len(matriculas), 2)