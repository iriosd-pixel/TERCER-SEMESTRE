# NOTA: este archivo NO define una clase. Es un MÓDULO con funciones sueltas que
# hacen el CRUD de clientes (Crear, Leer, Actualizar, Eliminar) + búsqueda.
# Aunque se llama "views", en MVC cumple el papel de CONTROLADOR: tiene la lógica
# y las validaciones, pero NO usa print() ni input(). Eso lo hace main.py (la Vista).
# Todas las funciones que modifican datos devuelven una tupla (exito, mensaje).

# Importa la clase Cliente (el Modelo) y la tupla con los nombres de sus campos.
from models import Cliente, CAMPOS_CLIENTE



# Importa la clase que lee y guarda la lista de clientes en el archivo JSON.
from shared.json_manager import GestorJSON
# Importa la función que revisa si un texto tiene formato de correo.
from shared.herramientas import es_email_valido


# Crea UN solo gestor para todo el módulo, apuntando al archivo de clientes.
# Al crearse, si la carpeta "data" no existe, GestorJSON la crea.
# Todas las funciones de abajo usan esta misma variable global 'gestor'.
gestor = GestorJSON("data/clientes.json")

# TUPLAS de configuración: fijas, nadie las modifica en tiempo de ejecución
# Campos que el usuario DEBE llenar para poder crear un cliente.
CAMPOS_OBLIGATORIOS = ("nombre", "apellido", "email")
# Campos en los que se busca al usar buscar_clientes() (dirección no se incluye).
CAMPOS_BUSCABLES = ("nombre", "apellido", "email", "telefono", "ciudad")


# ===================== AYUDAS INTERNAS =====================

# Devuelve un CONJUNTO con todos los emails guardados (en minúsculas).
# 'excepto_id' es opcional: sirve para ignorar el email de un cliente concreto
# (se usa al actualizar, para que un cliente no choque con su propio email).
def emails_registrados(excepto_id=None):
    """CONJUNTO con los emails ya usados. Sirve para detectar duplicados al instante."""
    # Esto es una COMPRENSIÓN DE CONJUNTO: { expresión for ... if ... }
    # Se lee así: "para cada registro del archivo, si su id no es excepto_id,
    # agrega su email en minúsculas al conjunto".
    return {
        registro["email"].lower()           # .lower(): "Ana@X.com" y "ana@x.com" cuentan como iguales
        for registro in gestor.leer()       # recorre la lista de diccionarios leída del JSON
        if registro["id"] != excepto_id     # filtro: salta el cliente que se está editando
    }
    # Se usa un conjunto porque buscar con 'in' en un set es casi instantáneo,
    # mientras que en una lista hay que revisar elemento por elemento.


# Calcula el id que le toca al próximo cliente.
def siguiente_id():
    # COMPRENSIÓN DE LISTA: saca solo el "id" de cada registro. Ej: [1, 2, 5]
    ids = [registro["id"] for registro in gestor.leer()]
    # Si hay ids, toma el mayor y le suma 1 (ej: 5 + 1 = 6).
    # Si la lista está vacía (no hay clientes), empieza en 1.
    # (Si se elimina el cliente con el id más alto, ese id se vuelve a usar.)
    return max(ids) + 1 if ids else 1


# ===================== C · CREATE =====================

# Crea un cliente nuevo después de validar sus datos, y lo guarda en el archivo.
def crear_cliente(datos):
    """datos: diccionario con las claves de CAMPOS_CLIENTE. Devuelve (exito, mensaje)."""
    # try/except: si ocurre CUALQUIER error inesperado, el programa no se cae;
    # salta al 'except' del final y devuelve un mensaje de error.
    try:
        # 1) Normalizo: un diccionario con todos los campos, sin espacios sobrantes
        # COMPRENSIÓN DE DICCIONARIO: {clave: valor for ...}
        #   - datos.get(campo, "") -> el valor del campo, o "" si no vino.
        #   - str(...)             -> lo convierte a texto (por si llega un número).
        #   - .strip()             -> quita espacios al inicio y al final.
        # Resultado: SIEMPRE tiene las 6 claves de CAMPOS_CLIENTE y en ese orden.
        valores = {campo: str(datos.get(campo, "")).strip() for campo in CAMPOS_CLIENTE}

        # 2) Reviso obligatorios recorriendo la TUPLA
        # Lista con los campos obligatorios que quedaron vacíos ("" cuenta como False).
        faltantes = [campo for campo in CAMPOS_OBLIGATORIOS if not valores[campo]]
        # Una lista con elementos es True: si falta alguno, se detiene aquí.
        if faltantes:
            # ', '.join(lista) une los elementos con coma. Ej: "nombre, email"
            return False, f"Faltan campos obligatorios: {', '.join(faltantes)}"

        # 3) Formato del email
        # Si es_email_valido devuelve False, 'not' lo vuelve True y se rechaza.
        if not es_email_valido(valores["email"]):
            return False, f"El email '{valores['email']}' no tiene un formato válido"

        # 4) Duplicado: búsqueda instantánea dentro del CONJUNTO
        # Se compara en minúsculas, igual que como se guardan en el conjunto.
        if valores["email"].lower() in emails_registrados():
            return False, "Ese email ya está registrado"

        # 5) Creo el objeto del Modelo. ** convierte el diccionario en argumentos
        # Cliente(6, **{"nombre": "Ana", "apellido": "Pérez", ...}) equivale a
        # Cliente(6, nombre="Ana", apellido="Pérez", ...).
        # Funciona porque las claves de 'valores' se llaman igual que los
        # parámetros de Cliente.__init__.
        cliente = Cliente(siguiente_id(), **valores)

        # 6) Agrego a la LISTA y guardo
        # Lee la lista actual de clientes (lista de diccionarios).
        registros = gestor.leer()
        # Convierte el objeto a diccionario y lo agrega al final de la lista.
        registros.append(cliente.a_diccionario())
        # guardar() devuelve True/False. Si falló, se avisa y no se reporta éxito.
        if not gestor.guardar(registros):
            return False, "No se pudo escribir el archivo"

        # Todo salió bien: devuelve éxito y un mensaje con el nombre y el id asignado.
        return True, f"Cliente {cliente.obtener_nombre_completo()} creado con id {cliente.id}"

    # 'Exception' atrapa cualquier error; 'as error' lo guarda en una variable
    # para poder mostrar su descripción en el mensaje.
    except Exception as error:
        return False, f"Error inesperado: {error}"


# ===================== R · READ =====================

# Devuelve todos los clientes guardados, ya convertidos en objetos Cliente.
def obtener_todos():
    """LISTA de objetos Cliente."""
    # Por cada diccionario del archivo, crea un objeto con Cliente.desde_diccionario.
    # Resultado: [Cliente, Cliente, ...] en el mismo orden del archivo.
    return [Cliente.desde_diccionario(registro) for registro in gestor.leer()]


# Busca un cliente por su id. Devuelve el objeto Cliente o None si no existe.
def obtener_por_id(id_cliente):
    # Recorre uno por uno todos los clientes (búsqueda lineal).
    for cliente in obtener_todos():
        # Compara el id del cliente con el buscado (ambos deben ser int).
        if cliente.id == id_cliente:
            # Lo encontró: 'return' termina la función y el ciclo de inmediato.
            return cliente
    # Si el for terminó sin encontrarlo, devuelve None ("nada").
    return None


# ===================== S · SEARCH =====================

# Busca clientes cuyo nombre, apellido, email, teléfono o ciudad CONTENGA el término.
def buscar_clientes(termino):
    """Búsqueda lineal: revisa registro por registro los campos de CAMPOS_BUSCABLES."""
    # Limpia espacios y pasa a minúsculas para que la búsqueda no distinga
    # mayúsculas: "ANA", "ana" y " Ana " encuentran lo mismo.
    termino = termino.strip().lower()
    # Si el término quedó vacío, no se busca nada: devuelve una lista vacía.
    # (Sin esto, "" estaría "dentro" de cualquier texto y devolvería a todos.)
    if not termino:
        return []

    # Lista donde se irán guardando los clientes que coincidan.
    encontrados = []
    # Ciclo externo: recorre cada cliente (como diccionario) del archivo.
    for registro in gestor.leer():
        # Ciclo interno: revisa cada campo buscable de ESE cliente.
        for campo in CAMPOS_BUSCABLES:                 # recorro la TUPLA de campos
            # registro.get(campo, "") -> valor del campo o "" si no existe.
            # str(...).lower()        -> texto en minúsculas.
            # 'termino in texto'      -> True si el término aparece en cualquier parte.
            if termino in str(registro.get(campo, "")).lower():
                # Coincidió: convierte el diccionario en objeto y lo agrega.
                encontrados.append(Cliente.desde_diccionario(registro))
                break                                   # ya coincidió: paso al siguiente cliente
                # (el break evita agregar al mismo cliente dos veces si
                #  coincide en varios campos, ej. nombre y email)
    # Devuelve la lista de objetos Cliente encontrados (puede estar vacía).
    return encontrados


# ===================== U · UPDATE =====================

# Modifica solo los campos indicados en 'cambios' del cliente con ese id.
# Ej: actualizar_cliente(3, {"ciudad": "Milagro", "telefono": "0991234567"})
def actualizar_cliente(id_cliente, cambios):
    """cambios: diccionario solo con los campos que se quieren modificar."""
    try:
        # DIFERENCIA DE CONJUNTOS: ¿mandaron algún campo que no existe?
        # set(cambios) -> conjunto con las CLAVES del diccionario de cambios.
        # A - B        -> elementos que están en A pero NO en B.
        # Ej: {"ciudad", "edad"} - {"nombre", ..., "ciudad", ...} -> {"edad"}
        # Esto también impide cambiar el "id", porque no está en CAMPOS_CLIENTE.
        desconocidos = set(cambios) - set(CAMPOS_CLIENTE)
        # Si hay campos desconocidos, se rechaza y se listan ordenados.
        if desconocidos:
            return False, f"Campos no válidos: {', '.join(sorted(desconocidos))}"

        # Un diccionario vacío {} es False: si no hay nada que cambiar, se avisa.
        if not cambios:
            return False, "No se indicó ningún cambio"

        # Solo si se quiere cambiar el email, se hacen dos validaciones extra.
        if "email" in cambios:
            # a) Que tenga formato de correo.
            if not es_email_valido(cambios["email"]):
                return False, "El email no tiene un formato válido"
            # b) Que no lo tenga OTRO cliente. Se excluye al propio cliente
            #    (excepto_id) para que pueda volver a guardar su mismo email.
            if cambios["email"].lower() in emails_registrados(excepto_id=id_cliente):
                return False, "Ese email ya lo usa otro cliente"

        # Lee la lista completa de clientes.
        registros = gestor.leer()
        # 'posicion' guardará el índice del cliente en la lista; None = no encontrado.
        posicion = None
        for indice, registro in enumerate(registros):   # enumerate me da índice y valor
            # Ej: enumerate([a, b, c]) produce (0, a), (1, b), (2, c)
            if registro["id"] == id_cliente:
                # Guarda en qué posición está y deja de buscar.
                posicion = indice
                break

        # Se usa 'is None' (y no 'not posicion') porque el índice 0 es válido
        # pero se evalúa como False: 'not 0' daría True por error.
        if posicion is None:
            return False, f"No existe un cliente con id {id_cliente}"

        # dict.update(otro) copia las claves de 'cambios' sobre el diccionario:
        # sobrescribe solo esos campos y deja los demás intactos.
        # Como el diccionario está DENTRO de la lista, la lista queda modificada.
        registros[posicion].update(cambios)             # actualizo el diccionario en su lugar
        # Guarda la lista completa en el archivo.
        # OJO: aquí no se revisa si guardar() devolvió False (a diferencia de crear_cliente).
        gestor.guardar(registros)
        # Mensaje de éxito indicando cuántos campos se cambiaron.
        return True, f"Cliente {id_cliente} actualizado ({len(cambios)} campo/s)"

    # Atrapa cualquier error inesperado (ej: si cambios["email"] no fuera texto).
    except Exception as error:
        return False, f"Error inesperado: {error}"


# ===================== D · DELETE =====================

# Elimina del archivo al cliente con ese id.
def eliminar_cliente(id_cliente):
    # Lee la lista actual de clientes.
    registros = gestor.leer()
    # Construyo una LISTA NUEVA sin ese registro: nunca borro mientras recorro
    # (borrar elementos de una lista mientras se recorre con for hace que
    #  Python se salte elementos). Aquí se copian todos MENOS el del id indicado.
    quedan = [registro for registro in registros if registro["id"] != id_cliente]

    # Si ambas listas tienen el mismo tamaño, no se quitó nada:
    # significa que ese id no existía.
    if len(quedan) == len(registros):
        return False, f"No existe un cliente con id {id_cliente}"

    # Guarda la lista nueva (sin el cliente) reemplazando el archivo.
    # OJO: tampoco se revisa aquí el resultado de guardar().
    gestor.guardar(quedan)
    # Mensaje de éxito.
    return True, f"Cliente {id_cliente} eliminado"


# ===================== EXTRA: estadísticas con conjuntos =====================

# Arma un resumen de los clientes usando conjuntos, listas y un diccionario.
def estadisticas():
    """Devuelve un DICCIONARIO de resumen. Práctica pura de colecciones."""
    # Lee todos los clientes una sola vez y reutiliza la lista.
    registros = gestor.leer()
    # CONJUNTO de ciudades sin repetir.
    #   - if r.get("ciudad") -> ignora clientes sin ciudad ("" o sin la clave).
    #   - .title()           -> "milagro" y "MILAGRO" quedan como "Milagro",
    #                           así el conjunto no las cuenta como distintas.
    ciudades = {r.get("ciudad", "").title() for r in registros if r.get("ciudad")}
    # CONJUNTO de dominios de correo sin repetir.
    #   - "ana@gmail.com".split("@") -> ["ana", "gmail.com"]; [1] toma "gmail.com".
    #   - if "@" in r["email"]       -> evita un IndexError si el email no tiene @.
    dominios = {r["email"].split("@")[1].lower() for r in registros if "@" in r["email"]}
    # LISTA con los nombres de clientes que no tienen teléfono ("" es False).
    # Es lista (no conjunto) porque dos clientes pueden llamarse igual.
    sin_telefono = [r["nombre"] for r in registros if not r.get("telefono")]

    # Devuelve un DICCIONARIO con el resumen.
    return {
        "total": len(registros),          # cantidad total de clientes
        "ciudades": sorted(ciudades),     # sorted(set) -> lista en orden alfabético
        "dominios": sorted(dominios),     # igual: lista ordenada de dominios
        "sin_telefono": sin_telefono,     # nombres de clientes sin teléfono
    }


# ------------------------------------------------------------------
# PRUEBA DE LAS FUNCIONES
# Este bloque SOLO se ejecuta si corres este archivo directamente:
#     python views.py
# Si main.py importa este archivo, este bloque NO se ejecuta.
#
# Cómo leer la prueba: cada función se llama, su resultado se guarda
# en una variable y se imprime. En el texto dice qué deberías ver.
# ------------------------------------------------------------------
if __name__ == "__main__":
    # Funciones de herramientas.py para mostrar el título y los avisos con color.
    from shared.herramientas import imprimir_titulo, imprimir_info, imprimir_exito

    imprimir_titulo("PRUEBA DE views.py")

    # Usamos un archivo de PRUEBA para no dañar los clientes reales.
    gestor = GestorJSON("data/clientes_prueba.json")

    # Guardamos una lista vacía para empezar sin clientes.
    gestor.guardar([])
    imprimir_info("Se usa el archivo data/clientes_prueba.json")

    # ============ 1. crear_cliente ============
    print()
    print("===== 1. crear_cliente =====")

    ana = {
        "nombre": "Ana",
        "apellido": "Pérez",
        "email": "ana@gmail.com",
        "telefono": "0991234567",
        "ciudad": "Milagro",
        "direccion": "Av. Principal",
    }
    resultado = crear_cliente(ana)
    print("Crear a Ana (debe salir True):", resultado)

    luis = {
        "nombre": "Luis",
        "apellido": "Mora",
        "email": "luis@unemi.edu.ec",
        "telefono": "",
        "ciudad": "Guayaquil",
        "direccion": "",
    }
    resultado = crear_cliente(luis)
    print("Crear a Luis (debe salir True):", resultado)

    # ============ 2. obtener_todos ============
    print()
    print("===== 2. obtener_todos =====")

    clientes = obtener_todos()
    print("Cantidad de clientes (debe salir 2):", len(clientes))
    for cliente in clientes:
        print(cliente)

    # ============ 3. obtener_por_id ============
    print()
    print("===== 3. obtener_por_id =====")

    cliente = obtener_por_id(1)
    print("Cliente con id 1 (debe salir Ana):", cliente)

    cliente = obtener_por_id(99)
    print("Cliente con id 99 (debe salir None):", cliente)

    # ============ 4. buscar_clientes ============
    print()
    print("===== 4. buscar_clientes =====")

    encontrados = buscar_clientes("milagro")
    print("Buscar 'milagro' (debe salir 1):", len(encontrados))

    encontrados = buscar_clientes("zzz")
    print("Buscar 'zzz' (debe salir 0):", len(encontrados))

    # ============ 5. actualizar_cliente ============
    print()
    print("===== 5. actualizar_cliente =====")

    cambios = {"ciudad": "Quito"}
    resultado = actualizar_cliente(1, cambios)
    print("Cambiar la ciudad de Ana (debe salir True):", resultado)

    resultado = actualizar_cliente(99, cambios)
    print("Actualizar el id 99 que no existe (debe salir False):", resultado)

    # ============ 6. estadisticas ============
    print()
    print("===== 6. estadisticas =====")

    resumen = estadisticas()
    print("Total de clientes (debe salir 2):", resumen["total"])
    # Aquí se ve que la ciudad de Ana ya cambió a Quito.
    print("Ciudades (debe salir Guayaquil y Quito):", resumen["ciudades"])
    print("Dominios de email:", resumen["dominios"])
    print("Clientes sin teléfono (debe salir Luis):", resumen["sin_telefono"])

    # ============ 7. emails_registrados y siguiente_id ============
    print()
    print("===== 7. emails_registrados y siguiente_id =====")

    emails = emails_registrados()
    print("Emails registrados:", emails)

    nuevo_id = siguiente_id()
    print("Siguiente id (debe salir 3):", nuevo_id)

    # ============ 8. eliminar_cliente ============
    print()
    print("===== 8. eliminar_cliente =====")

    resultado = eliminar_cliente(2)
    print("Eliminar a Luis (debe salir True):", resultado)

    resultado = eliminar_cliente(2)
    print("Eliminar a Luis otra vez (debe salir False):", resultado)

    clientes = obtener_todos()
    print("Clientes que quedan (debe salir 1):", len(clientes))

    # Al terminar, dejamos el archivo de prueba vacío otra vez.
    gestor.guardar([])

    print()
    imprimir_exito("Fin de las pruebas")