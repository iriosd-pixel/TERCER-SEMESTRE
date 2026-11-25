#=======================================================================
# EJEMPLOS DE EXPLICACIÓN DE LA GUÍA
# Cada ejemplo se puede ejecutar llamando a su función.
#=======================================================================
# Ejemplo de explicación 1
def ejemplo_explicacion_1():
    # Creación
    saludo = "Hola mundo"
    mensaje = 'con comillas simples también'
    multi = """tres comillas
    para varias líneas"""

    # Acceso e índice negativo
    print(saludo[0])   # 'H'
    print(saludo[-1])  # 'o' (último)

    # Slicing (rebanadas)
    print(saludo[0:4])  # 'Hola'
    print(saludo[5:])   # 'mundo'

    # Longitud y recorrido
    print(len(saludo))  # 10
    for ch in saludo:
        print(ch)

    # Inmutabilidad
    # saludo[0] = "h"  ← ERROR: TypeError
    saludo = "h" + saludo[1:]  # ← se crea una NUEVA cadena

# Ejemplo de explicación 2
def ejemplo_explicacion_2():
    # Creación
    vacia = []
    notas = [7, 8.5, 9, 6.5]
    mezcla = [1, "dos", True, [3, 4]]  # admite cualquier tipo

    # Acceso, longitud, verificación
    print(notas[0])       # 7
    print(notas[-1])      # 6.5 (último)
    print(len(notas))     # 4
    print(9 in notas)     # True

    # Modificación
    notas[0] = 10          # cambiar por índice
    notas.append(8)         # añadir al final → O(1)
    notas.insert(0, 5)      # insertar al inicio → O(n)
    notas.remove(6.5)        # quita la primera ocurrencia de 6.5
    ultima = notas.pop()      # saca y retorna el último

    # Recorrido
    for n in notas:
        print(n)

    for i, n in enumerate(notas):
        print(f"posición {i} → {n}")

    # Ordenamiento
    notas.sort()              # in-place, ascendente
    notas.sort(reverse=True)  # in-place, descendente
    nueva = sorted(notas)   # retorna copia ordenada

    # Slicing y copia
    primeras = notas[:2]     # primeros 2
    copia = notas[:]          # copia completa (no alias)

    # Comprensión de listas
    cuadrados = [n*n for n in range(6)]  # [0,1,4,9,16,25]
    pares = [n for n in notas if n % 2 == 0]

# Ejemplo de explicación 3
def ejemplo_explicacion_3():
    # Creación (los paréntesis son opcionales)
    punto = (3, 4)
    color = 255, 128, 0       # también es tupla
    uno = (5,)                # cuidado: (5) es int, (5,) es tupla

    # Acceso — igual que list
    print(punto[0], punto[1])   # 3 4

    # Inmutabilidad
    # punto[0] = 10  ← ERROR: TypeError

    # Desempaquetado — súper pythónico
    x, y = punto
    r, g, b = color

    # Retornar varios valores es una tupla implícita
    def min_max(lst):
        return min(lst), max(lst)

    lo, hi = min_max([3, 1, 4, 1, 5])

    # Métodos limitados: count() e index()
    c = (1, 2, 3, 2, 1)
    print(c.count(2))       # 2
    print(c.index(3))       # 2

# Ejemplo de explicación 4
def ejemplo_explicacion_4():
    # Creación
    vacio = set()          # ← {} es dict, no set!
    letras = {"a", "b", "c"}
    unicos = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3}

    # Operaciones básicas
    letras.add("d")         # añade uno
    letras.discard("z")     # quita si existe (no falla si no)
    letras.remove("a")      # quita, KeyError si no existe
    print("b" in letras)  # True — búsqueda O(1)
    print(len(letras))     # cuántos elementos

    # Recorrido (sin orden garantizado)
    for x in letras:
        print(x)

    # Operaciones de conjunto (como en matemáticas)
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    print(a | b)  # unión         → {1,2,3,4,5,6}
    print(a & b)  # intersección  → {3,4}
    print(a - b)  # diferencia    → {1,2}
    print(a ^ b)  # diferencia sim → {1,2,5,6}

    # Caso típico: eliminar duplicados de una lista
    palabras = ["sí", "no", "sí", "tal vez", "no"]
    sin_repetir = list(set(palabras))  # orden no garantizado

# Ejemplo de explicación 5
def ejemplo_explicacion_5():
    # Creación
    vacio = {}
    persona = {"nombre": "Ana", "edad": 30, "ciudad": "Guayaquil"}
    alt = dict(nombre="Ana", edad=30)   # forma alterna

    # Lectura
    print(persona["nombre"])     # "Ana" — KeyError si no existe
    print(persona.get("tel"))    # None — nunca falla
    print(persona.get("tel", "—"))  # "—" — valor por defecto

    # Modificación
    persona["edad"] = 31           # cambia el valor
    persona["email"] = "a@x.com"    # añade nueva clave
    del persona["ciudad"]         # elimina
    persona.pop("edad", None)      # elimina si existe, retorna valor

    # Verificación de clave
    if "nombre" in persona:
        print("tiene nombre")

    # Recorrido
    for clave in persona:                # solo claves
        print(clave, persona[clave])
    for clave, valor in persona.items():  # claves y valores juntos
        print(f"{clave} = {valor}")
    for valor in persona.values():         # solo valores
        print(valor)

    # Caso típico: contar frecuencias
    texto = "la casa de la abuela"
    conteo = {}
    for palabra in texto.split():
        conteo[palabra] = conteo.get(palabra, 0) + 1
    print(conteo)  # {'la': 2, 'casa': 1, 'de': 1, 'abuela': 1}

#=======================================================================
# EJERCICIOS PROPUESTOS
#=======================================================================
#=======================================================================
# 1) Pide una frase al usuario y cuenta cuántas vocales (a, e, i, o, u) tiene. Ignora mayúsculas/minúsculas.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
#----Entrada: frase ingresada por el usuario
#----Proceso: pasar el texto a minúsculas, recorrer cada letra y contar si pertenece al conjunto de vocales
#----Salida: número total de vocales encontradas

# Ejemplo de entrada (guía): frase = "Hola Mundo"
# Salida esperada (guía): 4 vocales

#-------- 2. BOSQUEJO A MANO ------------
# frase = "Hola" -> .lower() -> "hola"
# vocales = {'a', 'e', 'i', 'o', 'u'}
# 'h' -> ¿está en vocales? No
# 'o' -> ¿está en vocales? Sí (total = 1)
# 'l' -> ¿está en vocales? No
# 'a' -> ¿está en vocales? Sí (total = 2)

#-------- 3. DESCUBRIR EL PATRÓN --------
# Convertimos toda la frase a minúsculas con .lower() para evitar diferencias de caja. Iteramos caracter por caracter y usamos la pertenencia rápida a un set con 'in' para sumar al contador.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
frase = input("Frase: ").lower()
vocales = {"a", "e", "i", "o", "u"}
total = 0
for ch in frase:
    if ch in vocales:
        total += 1
print(f"{total} vocales")

#-------- 5. PRUEBA DE ESCRITORIO -------
# Línea               | frase   | ch  | ch in vocales | total | Pantalla
# ------------------- | ------- | --- | ------------- | ----: | --------
# `input("Frase: ")`  | "Hola"  | —   | —             |     0 | —
# `for ch in frase`   | "hola"  | 'h' | False         |     0 | —
# `for ch in frase`   | "hola"  | 'o' | True          |     1 | —
# `for ch in frase`   | "hola"  | 'l' | False         |     1 | —
# `for ch in frase`   | "hola"  | 'a' | True          |     2 | —
# `print(...)`        | "hola"  | —   | —             |     2 | 2 vocales


#=======================================================================
# 2) Dada una lista fija de notas [7, 8.5, 6, 9, 10, 5.5], calcula el promedio, la nota máxima y la mínima. Imprime los tres valores con 2 decimales.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
#----Entrada: lista con notas numéricas [7, 8.5, 6, 9, 10, 5.5]
#----Proceso: calcular promedio dividiendo la suma total entre la cantidad de notas; obtener nota máxima y mínima
#----Salida: promedio, máxima y mínima impresos con formato de 2 decimales

# Ejemplo de entrada (guía): [7, 8.5, 6, 9, 10, 5.5]
# Salida esperada (guía): Promedio: 7.67 Máximo: 10.00 Mínimo: 5.50

#-------- 2. BOSQUEJO A MANO ------------
# notas = [7, 8.5, 6, 9, 10, 5.5]
# suma = 7 + 8.5 + 6 + 9 + 10 + 5.5 = 46.0
# cantidad = 6
# promedio = 46.0 / 6 = 7.6666...
# nota máxima = 10
# nota mínima = 5.5

#-------- 3. DESCUBRIR EL PATRÓN --------
# Reutilizamos las funciones integradas sum() y len() para obtener el promedio estadístico. Usamos max() y min() para los valores extremos y formateamos el texto usando f-strings con :.2f.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
notas = [7, 8.5, 6, 9, 10, 5.5]
promedio = sum(notas) / len(notas)
print(f"Promedio: {promedio:.2f}")
print(f"Máximo:   {max(notas):.2f}")
print(f"Mínimo:   {min(notas):.2f}")

#-------- 5. PRUEBA DE ESCRITORIO -------
# Línea               | sum(notas) | len(notas) | promedio | max(notas) | min(notas) | Pantalla
# ------------------- | ---------: | ---------: | -------: | ---------: | ---------: | ----------------
# `promedio = ...`    |       46.0 |          6 |     7.67 |          — |          — | —
# `print Promedio`    |          — |          — |     7.67 |          — |          — | Promedio: 7.67
# `print Máximo`      |          — |          — |        — |       10.0 |          — | Máximo:   10.00
# `print Mínimo`      |          — |          — |        — |          — |        5.5 | Mínimo:   5.50


#=======================================================================
# 3) Dada la lista ["a", "b", "a", "c", "b", "d"], retorna una nueva lista sin duplicados respetando el orden de la primera aparición. (Con set se pierde el orden — hay que combinar set + list.)
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
#----Entrada: lista de elementos con duplicados ["a", "b", "a", "c", "b", "d"]
#----Proceso: filtrar elementos repetidos preservando la secuencia de aparición original
#----Salida: lista con los elementos únicos en su orden inicial

# Ejemplo de entrada (guía): ["a","b","a","c","b","d"]
# Salida esperada (guía): ["a","b","c","d"]

#-------- 2. BOSQUEJO A MANO ------------
# datos: ["a", "b", "a", "c", "b", "d"]
# vistos = set(), resultado = []
# "a" -> no en vistos -> agregar a vistos {"a"} y a resultado ["a"]
# "b" -> no en vistos -> agregar a vistos {"a","b"} y a resultado ["a","b"]
# "a" -> ya está en vistos -> ignorar
# "c" -> no en vistos -> agregar a vistos {"a","b","c"} y a resultado ["a","b","c"]
# "b" -> ya está en vistos -> ignorar
# "d" -> no en vistos -> agregar a vistos {"a","b","c","d"} y a resultado ["a","b","c","d"]

#-------- 3. DESCUBRIR EL PATRÓN --------
# Los conjuntos (set) ofrecen búsquedas de presencia 'x not in vistos' súper rápidas O(1). La lista auxiliar guarda los elementos en orden estricto de llegada.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
datos = ["a", "b", "a", "c", "b", "d"]
vistos = set()
resultado = []
for x in datos:
    if x not in vistos:
        vistos.add(x)
        resultado.append(x)
print(resultado)

#-------- 5. PRUEBA DE ESCRITORIO -------
# Línea               | x   | x not in vistos | vistos             | resultado            | Pantalla
# ------------------- | --- | --------------- | ------------------ | -------------------- | --------------------
# `for x in datos`    | "a" | True            | {"a"}              | ["a"]                | —
# `for x in datos`    | "b" | True            | {"a", "b"}         | ["a", "b"]           | —
# `for x in datos`    | "a" | False           | {"a", "b"}         | ["a", "b"]           | —
# `for x in datos`    | "c" | True            | {"a", "b", "c"}    | ["a", "b", "c"]      | —
# `for x in datos`    | "b" | False           | {"a", "b", "c"}    | ["a", "b", "c"]      | —
# `for x in datos`    | "d" | True            | {"a","b","c","d"}  | ["a","b","c","d"]    | —
# `print(resultado)`  | —   | —               | —                  | —                    | ['a', 'b', 'c', 'd']


#=======================================================================
# 4) Dado un texto, retorna un diccionario con la frecuencia de cada palabra (ignora mayúsculas). Al final, imprime la palabra que más se repite.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
#----Entrada: cadena de texto
#----Proceso: normalizar a minúsculas, separar por palabras, contar las ocurrencias en un diccionario e identificar la clave con mayor valor
#----Salida: diccionario de frecuencias y la palabra más repetida junto con su cuenta

# Ejemplo de entrada (guía): "El perro y el gato y el perro"
# Salida esperada (guía): {'el': 3, 'perro': 2, 'y': 2, 'gato': 1} Más repetida: 'el' (3 veces)

#-------- 2. BOSQUEJO A MANO ------------
# texto = "El perro y el gato y el perro"
# .lower().split() = ["el", "perro", "y", "el", "gato", "y", "el", "perro"]
# conteo = {"el": 3, "perro": 2, "y": 2, "gato": 1}
# max por valor = "el" (3)

#-------- 3. DESCUBRIR EL PATRÓN --------
# Convertimos el texto completo a minúsculas y lo dividimos por espacios usando .split(). Usamos el método .get(palabra, 0) para inicializar e incrementar contadores sin arrojar KeyError. La función max() con el argumento key=conteo.get extrae la clave con la mayor frecuencia acumulada.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
texto = "El perro y el gato y el perro"
conteo = {}
for palabra in texto.lower().split():
    conteo[palabra] = conteo.get(palabra, 0) + 1

print(conteo)

mas = max(conteo, key=conteo.get)
print(f"Más repetida: '{mas}' ({conteo[mas]} veces)")

#-------- 5. PRUEBA DE ESCRITORIO -------
# Línea               | palabra | conteo                                       | mas   | Pantalla
# ------------------- | ------- | -------------------------------------------- | ----- | --------------------------------------------------
# `split()`           | —       | {}                                           | —     | —
# `for palabra...`    | "el"    | {"el": 1}                                    | —     | —
# `for palabra...`    | "perro" | {"el": 1, "perro": 1}                        | —     | —
# `for palabra...`    | "y"     | {"el": 1, "perro": 1, "y": 1}                | —     | —
# `for palabra...`    | "el"    | {"el": 2, "perro": 1, "y": 1}                | —     | —
# ... fin del bucle   | —       | {"el": 3, "perro": 2, "y": 2, "gato": 1}      | —     | —
# `print(conteo)`     | —       | —                                            | —     | {'el': 3, 'perro': 2, 'y': 2, 'gato': 1}
# `mas = max(...)`    | —       | —                                            | "el"  | —
# `print(...)`        | —       | —                                            | "el"  | Más repetida: 'el' (3 veces)
