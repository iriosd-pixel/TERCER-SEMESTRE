#================================================
# EJEMPLOS PUESTOS POR LA IA MAS CAMBIOS
#================================================

#================================================
# 1) Leer el nombre del usuario y saludarlo por su nombre.
#================================================
nombre = input("¿Cómo te llamas? ")
print(f"Hola, {nombre}. Bienvenida al curso.")
#CAMBIO
#Amplíalo para que además pida la edad y muestre «tienes X años».
nombre = input("¿Cómo te llamas? ")
edad= int(input("Ingrese su edad: "))
print(f"Hola, {nombre}. Bienvenida al curso. Tienes {edad} anos")

#================================================
# 2) Leer tres notas de un estudiante y mostrar su promedio.
#================================================
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

promedio = (n1 + n2 + n3) / 3      # PROCESO en una línea

print(f"Promedio: {promedio:.1f}")  # :.1f muestra un decimal
#CAMBIO
#Modifícalo para que muestre «Aprueba» si el promedio es ≥ 7 y «Reprueba» si no. (Necesitas el if del módulo 3).
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

promedio = (n1 + n2 + n3) / 3
print(f"Promedio: {promedio:.1f}")
if promedio >= 7:
    print("Aprovado")
else:
    print("Reprovado")

#================================================
# 3) Leer la base y la altura de un rectángulo y mostrar su área y su perímetro.
# Recuerda: área = base × altura, perímetro = 2 × (base + altura).
#================================================
base = float(input("Base: "))
altura = float(input("Altura: "))

area = base * altura                # PROCESO 1
perimetro = 2 * (base + altura)     # PROCESO 2

print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")
#CAMBIO
#Ampliar para leer el radio de un círculo y mostrar área (π·r²) y perímetro (2·π·r).
# Usa import math y math.pi.
radio = float(input("Ingrese radio: "))
P=3.1416
area =  PI*(radio**2)
perimetro = 2 * PI*radio
print(f"El area del circulo: {area:.2f}")
print(f"El perimetro del circulo: {perimetro:.2f}")

#================================================
#                 TAREA
#================================================

#================================================
# 1) Función area_rectangulo(base, altura) que retorne el área.
#================================================
#--------ENTENDER EL PROBLEMA--------
#----Entrada: base, altura (parámetros)
#----Proceso: area = base * altura
#----Salida: área calculada del rectángulo

#-------- BOSQUEJO A MANO------------
# base: 5
# altura: 3
# area = 5 * 3 = 15

#--------DESCUBRIR EL PATRON-----------
# Para calcular el área de cualquier rectángulo multiplicamos la base por la altura.

#--------ESCRIBIR EL CODIGO-----------
def area_rectangulo(base, altura):
    return base * altura

# Uso
print(area_rectangulo(5, 3))    # 15
print(area_rectangulo(4.5, 2))  # 9.0

#--------PRUEBA DE ESCRITORIO--------
# Línea                   | base | altura | Pantalla
# ----------------------- | ---: | -----: | --------
# `area_rectangulo(5, 3)` |    5 |      3 | 15
# `area_rectangulo(4.5,2)`|  4.5 |      2 | 9.0


#================================================
# 2) Función maximo(a, b, c) que retorne el mayor de tres números.
#================================================
#--------ENTENDER EL PROBLEMA--------
#----Entrada: tres números a, b, c (parámetros)
#----Proceso: comparar los valores para encontrar el número mayor
#----Salida: el número de mayor valor

#-------- BOSQUEJO A MANO------------
# a: 5, b: 9, c: 3
# mayor = 5
# ¿9 > 5? Sí -> mayor = 9
# ¿3 > 9? No -> mayor = 9

#--------DESCUBRIR EL PATRON-----------
# Asumimos que el primer número es el mayor y luego lo comparamos con los demás; si encontramos uno más grande, actualizamos la variable mayor.

#--------ESCRIBIR EL CODIGO-----------
def maximo(a, b, c):
    return max(a, b, c)
print(maximo(5, 7, 44))

#mximo
def maximo_manual(a, b, c):
    mayor = a
    if b > mayor: mayor = b
    if c > mayor: mayor = c
    return mayor

print(maximo(5, 9, 3))          # 9
print(maximo_manual(5, 9, 3))   # 9

#--------PRUEBA DE ESCRITORIO--------
# Línea                     |  a |  b |  c | mayor | Pantalla
# ------------------------- | -: | -: | -: | ----: | --------
# `maximo(5, 7, 44)`        |  5 |  7 | 44 |     — | 44
# `maximo_manual(5, 9, 3)`  |  5 |  9 |  3 |     9 | 9


#================================================
# 3) Un año es bisiesto si es divisible entre 4 y no entre 100, O si es divisible entre 400.
#================================================
#--------ENTENDER EL PROBLEMA--------
#----Entrada: año (input)
#----Proceso: verificar si el año es divisible por 400 O (divisible por 4 Y NO por 100)
#----Salida: "El año es bisiesto" o "El año no es bisiesto"

#-------- BOSQUEJO A MANO------------
# año: 2024
# ¿2024 % 400 == 0? No
# ¿2024 % 4 == 0 y 2024 % 100 != 0? Sí -> Es bisiesto

#--------DESCUBRIR EL PATRON-----------
# Si el año se divide exactamente para 400 es bisiesto. Si no, debe ser divisible para 4 pero no para 100.

#--------ESCRIBIR EL CODIGO-----------
def año_bisiesto(año):
    bisiesto = False
    if año % 400 == 0:
        return True
    if año % 4 == 0 and año % 100 != 0:
        return True
    else:
        return False

año = int(input("Ingrese un año"))

if año_bisiesto(año):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")

# Pruebas
for y in [2024, 2023, 2000, 1900]:
    print(f"{y}: {año_bisiesto(y)}")

#--------PRUEBA DE ESCRITORIO--------
# Línea                |  año | año % 400 == 0 | año % 4 == 0 and año % 100 != 0 | Pantalla
# -------------------- | ---: | ------------: | ------------------------------: | ---------------------
# `input`              | 2024 |          —    |                            —    | 2024
# `año_bisiesto(2024)` | 2024 |        False  |                         True    | El año es bisiesto


#================================================
# 4) Función factorial(n) y luego combinatoria(n, k) = n! / (k! · (n-k)!).
#================================================
#--------ENTENDER EL PROBLEMA--------
#----Entrada: n (para factorial), n y k (para combinatoria)
#----Proceso:
# 1) factorial(n) = 1 * 2 * ... * n
# 2) combinatoria(n, k) = factorial(n) // (factorial(k) * factorial(n - k))
#----Salida: resultado del factorial y número total de combinaciones

#-------- BOSQUEJO A MANO------------
# n = 5, k = 2
# factorial(5) = 1 * 2 * 3 * 4 * 5 = 120
# arriba = 120
# abajo = factorial(2) * factorial(3) = 2 * 6 = 12
# resultado = 120 // 12 = 10

#--------DESCUBRIR EL PATRON-----------
# Para el factorial acumulamos multiplicaciones desde 1 hasta n. Para la combinatoria reutilizamos la función factorial para resolver la fórmula dividiendo arriba entre abajo.

#--------ESCRIBIR EL CODIGO-----------
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

def combinatoria(n, k):
    arriba = factorial(n)
    abajo = factorial(k) * factorial(n - k)
    return arriba // abajo

# Uso
print(factorial(5))
print(combinatoria(5, 2))

#--------PRUEBA DE ESCRITORIO--------
# Línea                 |  n |  k | arriba | abajo | Pantalla
# --------------------- | -: | -: | -----: | ----: | --------
# `factorial(5)`        |  5 |  — |      — |     — | 120
# `combinatoria(5, 2)`  |  5 |  2 |    120 |    12 | 10


#================================================
# 5) Programa que use funciones separadas para cada operación
# (sumar, restar, multiplicar, dividir) y un menú que llame a la correcta.
#================================================
#--------ENTENDER EL PROBLEMA--------
#----Entrada: opción elegida (1-5), números a y b
#----Proceso: según la opción, llamar a la función correspondiente y calcular el resultado
#----Salida: resultado de la operación elegida

#-------- BOSQUEJO A MANO------------
# opción: 1 (sumar)
# a = 5, b = 3
# r = sumar(5, 3) = 8

#--------DESCUBRIR EL PATRON-----------
# Usamos un bucle while para mantener el menú activo. Validamos que la opción esté entre 1 y 4 antes de pedir los números e invocamos la función requerida.

#--------ESCRIBIR EL CODIGO-----------
def sumar(a, b): return a + b
def restar(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b):
    if b == 0:
        return None
    return a / b

while True:
    print("\n--Mostrar menu--")
    print("1: Sumar")
    print("2: Restar")
    print("3: Multiplicar")
    print("4: Dividir")
    print("5: Salir")

    opcion = int(input("Elija una opcion: "))

    if opcion == 5:
        print("Saliendo del programa...")
        break

    if opcion < 1 or opcion > 5:
        print("Opción inválida")
        continue

    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))

    if opcion == 1:
        r = sumar(a, b)
    elif opcion == 2:
        r = restar(a, b)
    elif opcion == 3:
        r = multiplicar(a, b)
    elif opcion == 4:
        r = dividir(a, b)
        if r is None:
            print("No se puede dividir entre 0")
            continue

    print(f"La respuesta es: {r}")

#--------PRUEBA DE ESCRITORIO--------
# Línea           | opción |  a |  b |    r | Pantalla
# --------------- | -----: | -: | -: | ---: | ---------------------
# `input` opción  |      1 |  — |  — |    — | 1
# `input` a y b   |      1 |  5 |  3 |    — | a: 5, b: 3
# `sumar(5, 3)`   |      1 |  5 |  3 |    8 | La respuesta es: 8