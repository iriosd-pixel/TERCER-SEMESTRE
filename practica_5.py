#================================================
# ------------------------------------------------------TAREA-------------------------------------------
#================================================

#================================================
# 1) Pide una frase al usuario y cuenta cuántas vocales (a, e, i, o, u) tiene. Ignora mayúsculas/minúsculas.
#================================================
#--------ENTENDER EL PROBLEMA--------
#----Entrada: frase ingresada por el usuario
#----Proceso: pasar el texto a minúsculas, recorrer cada letra y contar si pertenece al conjunto de vocales
#----Salida: número total de vocales encontradas

#-------- BOSQUEJO A MANO------------
# frase = "Hola" -> .lower() -> "hola"
# vocales = {'a', 'e', 'i', 'o', 'u'}
# 'h' -> ¿está en vocales? No
# 'o' -> ¿está en vocales? Sí (total = 1)
# 'l' -> ¿está en vocales? No
# 'a' -> ¿está en vocales? Sí (total = 2)

#--------DESCUBRIR EL PATRON-----------
# Convertimos toda la frase a minúsculas con .lower() para evitar diferencias de caja. Iteramos caracter por caracter y usamos la pertenencia rápida a un set con 'in' para sumar al contador.

#--------ESCRIBIR EL CODIGO-----------
frase = input("Frase: ").lower()
vocales = {"a", "e", "i", "o", "u"}
total = 0
for ch in frase:
    if ch in vocales:
        total += 1
print(f"{total} vocales")

#--------PRUEBA DE ESCRITORIO--------
# Línea               | frase   | ch  | ch in vocales | total | Pantalla
# ------------------- | ------- | --- | ------------- | ----: | --------
# `input("Frase: ")`  | "Hola"  | —   | —             |     0 | —
# `for ch in frase`   | "hola"  | 'h' | False         |     0 | —
# `for ch in frase`   | "hola"  | 'o' | True          |     1 | —
# `for ch in frase`   | "hola"  | 'l' | False         |     1 | —
# `for ch in frase`   | "hola"  | 'a' | True          |     2 | —
# `print(...)`        | "hola"  | —   | —             |     2 | 2 vocales


#================================================
# 2) Dada una lista fija de notas [7, 8.5, 6, 9, 10, 5.5], calcula el promedio, la nota máxima y la mínima. Imprime los tres valores con 2 decimales.
#================================================
#--------ENTENDER EL PROBLEMA--------
#----Entrada: lista con notas numéricas [7, 8.5, 6, 9, 10, 5.5]
#----Proceso: calcular promedio dividiendo la suma total entre la cantidad de notas; obtener nota máxima y mínima
#----Salida: promedio, máxima y mínima impresos con formato de 2 decimales

#-------- BOSQUEJO A MANO------------
# notas = [7, 8.5, 6, 9, 10, 5.5]
# suma = 7 + 8.5 + 6 + 9 + 10 + 5.5 = 46.0
# cantidad = 6
# promedio = 46.0 / 6 = 7.6666...
# nota máxima = 10
# nota mínima = 5.5

#--------DESCUBRIR EL PATRON-----------
# Reutilizamos las funciones integradas sum() y len() para obtener el promedio estadístico. Usamos max() y min() para los valores extremos y formateamos el texto usando f-strings con :.2f.

#--------ESCRIBIR EL CODIGO-----------
notas = [7, 8.5, 6, 9, 10, 5.5]
promedio = sum(notas) / len(notas)
print(f"Promedio: {promedio:.2f}")
print(f"Máximo:   {max(notas):.2f}")
print(f"Mínimo:   {min(notas):.2f}")

#--------PRUEBA DE ESCRITORIO--------
# Línea               | sum(notas) | len(notas) | promedio | max(notas) | min(notas) | Pantalla
# ------------------- | ---------: | ---------: | -------: | ---------: | ---------: | ----------------
# `promedio = ...`    |       46.0 |          6 |     7.67 |          — |          — | —
# `print Promedio`    |          — |          — |     7.67 |          — |          — | Promedio: 7.67
# `print Máximo`      |          — |          — |        — |       10.0 |          — | Máximo:   10.00
# `print Mínimo`      |          — |          — |        — |          — |        5.5 | Mínimo:   5.50


#================================================
# 5) Dada la lista ["a", "b", "a", "c", "b", "d"], retorna una nueva lista sin duplicados respetando el orden de la primera aparición. (Con set se pierde el orden — hay que combinar set + list.)
#================================================
#--------ENTENDER EL PROBLEMA--------
#----Entrada: lista de elementos con duplicados ["a", "b", "a", "c", "b", "d"]
#----Proceso: filtrar elementos repetidos preservando la secuencia de aparición original
#----Salida: lista con los elementos únicos en su orden inicial

#-------- BOSQUEJO A MANO------------
# datos: ["a", "b", "a", "c", "b", "d"]
# vistos = set(), resultado = []
# "a" -> no en vistos -> agregar a vistos {"a"} y a resultado ["a"]
# "b" -> no en vistos -> agregar a vistos {"a","b"} y a resultado ["a","b"]
# "a" -> ya está en vistos -> ignorar
# "c" -> no en vistos -> agregar a vistos {"a","b","c"} y a resultado ["a","b","c"]
# "b" -> ya está en vistos -> ignorar
# "d" -> no en vistos -> agregar a vistos {"a","b","c","d"} y a resultado ["a","b","c","d"]

#--------DESCUBRIR EL PATRON-----------
# Los conjuntos (set) ofrecen búsquedas de presencia 'x not in vistos' súper rápidas O(1). La lista auxiliar guarda los elementos en orden estricto de llegada.

#--------ESCRIBIR EL CODIGO-----------
datos = ["a", "b", "a", "c", "b", "d"]
vistos = set()
resultado = []
for x in datos:
    if x not in vistos:
        vistos.add(x)
        resultado.append(x)
print(resultado)

#--------PRUEBA DE ESCRITORIO--------
# Línea               | x   | x not in vistos | vistos             | resultado            | Pantalla
# ------------------- | --- | --------------- | ------------------ | -------------------- | --------------------
# `for x in datos`    | "a" | True            | {"a"}              | ["a"]                | —
# `for x in datos`    | "b" | True            | {"a", "b"}         | ["a", "b"]           | —
# `for x in datos`    | "a" | False           | {"a", "b"}         | ["a", "b"]           | —
# `for x in datos`    | "c" | True            | {"a", "b", "c"}    | ["a", "b", "c"]      | —
# `for x in datos`    | "b" | False           | {"a", "b", "c"}    | ["a", "b", "c"]      | —
# `for x in datos`    | "d" | True            | {"a","b","c","d"}  | ["a","b","c","d"]    | —
# `print(resultado)`  | —   | —               | —                  | —                    | ['a', 'b', 'c', 'd']


#================================================
# 4) Dado un texto, retorna un diccionario con la frecuencia de cada palabra (ignora mayúsculas). Al final, imprime la palabra que más se repite.
#================================================
#--------ENTENDER EL PROBLEMA--------
#----Entrada: cadena de texto
#----Proceso: normalizar a minúsculas, separar por palabras, contar las ocurrencias en un diccionario e identificar la clave con mayor valor
#----Salida: diccionario de frecuencias y la palabra más repetida junto con su cuenta

#-------- BOSQUEJO A MANO------------
# texto = "El perro y el gato y el perro"
# .lower().split() = ["el", "perro", "y", "el", "gato", "y", "el", "perro"]
# conteo = {"el": 3, "perro": 2, "y": 2, "gato": 1}
# max por valor = "el" (3)

#--------DESCUBRIR EL PATRON-----------
# Convertimos el texto completo a minúsculas y lo dividimos por espacios usando .split(). Usamos el método .get(palabra, 0) para inicializar e incrementar contadores sin arrojar KeyError. La función max() con el argumento key=conteo.get extrae la clave con la mayor frecuencia acumulada.

#--------ESCRIBIR EL CODIGO-----------
texto = "El perro y el gato y el perro"
conteo = {}
for palabra in texto.lower().split():
    conteo[palabra] = conteo.get(palabra, 0) + 1

print(conteo)

mas = max(conteo, key=conteo.get)
print(f"Más repetida: '{mas}' ({conteo[mas]} veces)")

#--------PRUEBA DE ESCRITORIO--------
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