#================================================
#EJEMPLOS PUESTOS POR LA IA MAS CAMBIOS
#================================================

#================================================
# 1)Escribir una función calcular_iva(precio) que
# reciba un precio y retorne el IVA (15%). Usarla desde el programa principal.
#================================================
def calcular_iva(precio):
    return precio * 0.15

# --- Programa principal ---
precio = float(input("Precio: $"))
iva = calcular_iva(precio)
print(f"IVA de ${precio}: ${iva:.2f}")
#CAMBIO
#Amplíala: define calcular_total(precio) que retorne precio + IVA usando la función anterior.
def calcular_total(precio):
    return precio + calcular_iva(precio)

#================================================
# 2) Escribir una función que reciba un número y retorne True si es primo, False si no.
#================================================
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# --- Uso 1: verificar uno ---
num = int(input("Número: "))
if es_primo(num):
    print(f"{num} es primo")
else:
    print(f"{num} NO es primo")

# --- Uso 2: listar primos entre 2 y 30 ---
print("Primos entre 2 y 30:")
for k in range(2, 31):
    if es_primo(k):
        print(k, end=" ")

#CAMBIO
#Escribe una función contar_primos(a, b) que cuente cuántos primos hay entre a y b.
def contar_primos(a,b):
    contador = 0
    for i in range(a, b+1):
        if es_primo(i):
            contador+=1
    return contador
#----------Programa principal--------------
a=int(input("Ingrese desde donde empieza"))
b=int(input("Ingrese hasta donde termina"))

cantidad=contar_primos(a,b)
print(f"Hay {cantidad} números primos entre {a} y {b}.")

#================================================
# 3) Escribir una función suma_digitos(n) que retorne la suma de los dígitos de un número.
#================================================
def suma_digitos(n):
    n = abs(n)                     # por si es negativo
    suma = 0
    while n > 0:
        suma += n % 10             # último dígito
        n = n // 10                # quita el último dígito
    return suma

# Uso
num = int(input("Número: "))
print(f"Suma: {suma_digitos(num)}")

# También sirve para varios
for x in [123, 4783, 999]:
    print(f"{x} → {suma_digitos(x)}")
#CAMBIO
#Escribe es_narcisista(n): retorna True si el número es igual a la suma de sus
# dígitos elevados al número de dígitos. Ej.: 153 = 1³+5³+3³.

def es_narcisista(n):
    numero = abs(n)
    exponente = len(str(numero))
    suma_numeros = 0
    temp = numero

    while temp > 0:
        digito = temp % 10
        suma_numeros += digito ** exponente
        temp = temp // 10

    return suma_numeros == numero

# ---------- Programa principal --------------
num = int(input("Ingrese una cifra numérica: "))

if es_narcisista(num):
    print(f"El número {num} es narcisista.")
else:
    print(f"El número {num} NO es narcisista.")

#================================================
# 4) Rediseñar el menú de saludar/despedir del módulo 3, pero esta vez con cada opción como función separada.
#================================================
def saludar():
    nombre = input("Nombre: ")
    print(f"¡Hola, {nombre}!")

def despedir():
    nombre = input("Nombre: ")
    print(f"¡Adiós, {nombre}!")

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Saludar")
    print("2. Despedir")
    print("3. Salir")

# Programa principal
while True:
    mostrar_menu()
    opcion = input("Opción: ")
    if opcion == "1":
        saludar()
    elif opcion == "2":
        despedir()
    elif opcion == "3":
        print("Adiós")
        break
    else:
        print("Opción inválida")
#CAMBIO
#Añade una función calcular() que pida dos números y muestre suma, resta, multiplicación y división.
# Nueva opción del menú.
def saludar():
    nombre = input("Nombre: ")
    print(f"¡Hola, {nombre}!")

def despedir():
    nombre = input("Nombre: ")
    print(f"¡Adiós, {nombre}!")

def calcular():
    a= int(input("Ingrese el primer numero: "))
    b= int(input("Ingrese el segundo numero: "))

    suma=a+b
    print(f"Suma: {suma}")
    resta=a-b
    print(f"Resta: {resta}")
    multiplicacion=a*b
    print(f"Multiplicacion: {multiplicacion}")
    division=a/b
    print(f"Division: {division}")
    print("---CALCULO TERMINADO---")

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Saludar")
    print("2. Despedir")
    print("3. Calcular")
    print("4. Salir")

# Programa principal
while True:
    mostrar_menu()
    opcion = input("Opción: ")
    if opcion == "1":
        saludar()
    elif opcion == "2":
        despedir()
    elif opcion == "3":
        calcular()
    elif opcion == "4":
        print("Adiós")
        break
    else:
        print("Opción inválida")

#================================================
#                 TAREA COMPLETA
#================================================

#================================================
# 1) Función area_rectangulo(base, altura)
#================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: base, altura (parámetros)
# Proceso: area = base * altura
# Salida:  área calculada del rectángulo

#-------- 2. BOSQUEJO A MANO ------------
# base: 5, altura: 3
# area = 5 * 3 = 15

#-------- 3. DESCUBRIR EL PATRON --------
# Para calcular el área de cualquier rectángulo multiplicamos la base por la altura.

#-------- 4. ESCRIBIR EL CODIGO ---------
def area_rectangulo(base, altura):
    return base * altura

# Uso
print(area_rectangulo(5, 3))    # 15
print(area_rectangulo(4.5, 2))  # 9.0

#-------- 5. PRUEBA DE ESCRITORIO -------
# Línea                   | base | altura | Pantalla
# ----------------------- | ---: | -----: | --------
# area_rectangulo(5, 3)   |    5 |      3 | 15
# area_rectangulo(4.5, 2) |  4.5 |      2 | 9.0


#================================================
# 2) Función maximo(a, b, c)
#================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: tres números a, b, c (parámetros)
# Proceso: comparar los valores para encontrar el número mayor
# Salida:  el número de mayor valor

#-------- 2. BOSQUEJO A MANO ------------
# a: 5, b: 9, c: 3
# mayor = 5
# ¿9 > 5? Sí -> mayor = 9
# ¿3 > 9? No -> mayor = 9

#-------- 3. DESCUBRIR EL PATRON --------
# Asumimos que el primer número es el mayor y luego lo comparamos con los demás;
# si encontramos uno más grande, actualizamos la variable mayor.

#-------- 4. ESCRIBIR EL CODIGO ---------
def maximo(a, b, c):
    return max(a, b, c)

def maximo_manual(a, b, c):
    mayor = a
    if b > mayor: mayor = b
    if c > mayor: mayor = c
    return mayor

# Uso
print(maximo(5, 9, 3))          # 9
print(maximo_manual(5, 9, 3))   # 9

#-------- 5. PRUEBA DE ESCRITORIO -------
# Línea                     |  a |  b |  c | mayor | Pantalla
# ------------------------- | -: | -: | -: | ----: | --------
# maximo_manual(5, 9, 3)    |  5 |  9 |  3 |     9 | 9


#================================================
# 3) Año bisiesto
#================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: año (input)
# Proceso: verificar si el año es divisible por 400 O (divisible por 4 Y NO por 100)
# Salida:  "El año es bisiesto" o "El año no es bisiesto"

#-------- 2. BOSQUEJO A MANO ------------
# año: 2024
# ¿2024 % 400 == 0? No
# ¿2024 % 4 == 0 y 2024 % 100 != 0? Sí -> Es bisiesto

#-------- 3. DESCUBRIR EL PATRON --------
# Si el año se divide exactamente para 400 es bisiesto.
# Si no, debe ser divisible para 4 pero no para 100.

#-------- 4. ESCRIBIR EL CODIGO ---------
def año_bisiesto(año):
    if año % 400 == 0:
        return True
    if año % 4 == 0 and año % 100 != 0:
        return True
    else:
        return False

# Uso (Comentado el input para que no detenga la ejecución si lo pruebas directo)
# año_input = int(input("Ingrese un año: "))
# if año_bisiesto(año_input):
#     print("El año es bisiesto")
# else:
#     print("El año no es bisiesto")

# Pruebas automáticas
for y in [2024, 2023, 2000, 1900]:
    print(f"{y}: {año_bisiesto(y)}")

#-------- 5. PRUEBA DE ESCRITORIO -------
# Línea              |  año | % 400 == 0 | % 4 == 0 y % 100 != 0 | Pantalla
# ------------------ | ---: | ---------: | --------------------: | ------------------
# año_bisiesto(2024) | 2024 |      False |                  True | True (bisiesto)
# año_bisiesto(1900) | 1900 |      False |                 False | False (no bisiesto)


#================================================
# 4) Factorial y Combinatoria
#================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: n (para factorial), n y k (para combinatoria)
# Proceso:
#   1) factorial(n) = 1 * 2 * ... * n
#   2) combinatoria(n, k) = factorial(n) // (factorial(k) * factorial(n - k))
# Salida:  resultado del factorial y número total de combinaciones

#-------- 2. BOSQUEJO A MANO ------------
# n = 5, k = 2
# factorial(5) = 1 * 2 * 3 * 4 * 5 = 120
# abajo = factorial(2) * factorial(3) = 2 * 6 = 12
# resultado = 120 // 12 = 10

#-------- 3. DESCUBRIR EL PATRON --------
# Para el factorial acumulamos multiplicaciones desde 1 hasta n.
# Para la combinatoria reutilizamos la función factorial para la fórmula matemática.

#-------- 4. ESCRIBIR EL CODIGO ---------
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
print(factorial(5))        # 120
print(combinatoria(5, 2))  # 10

#-------- 5. PRUEBA DE ESCRITORIO -------
# Línea                 |  n |  k | arriba | abajo | Pantalla
# --------------------- | -: | -: | -----: | ----: | --------
# factorial(5)          |  5 |  — |      — |     — | 120
# combinatoria(5, 2)    |  5 |  2 |    120 |    12 | 10


#================================================
# 5) Calculadora con Menú
#================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: opción elegida (1-5), números a y b
# Proceso: según la opción, llamar a la función correspondiente y calcular el resultado
# Salida:  resultado de la operación elegida

#-------- 2. BOSQUEJO A MANO ------------
# opción: 1 (sumar)
# a = 5, b = 3
# r = sumar(5, 3) = 8

#-------- 3. DESCUBRIR EL PATRON --------
# Usamos un bucle `while` para mantener el menú activo. Validamos la opción.
# Pedimos los números, invocamos la función requerida e imprimimos el resultado.

#-------- 4. ESCRIBIR EL CODIGO ---------
def sumar(a, b): return a + b
def restar(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b):
    if b == 0:
        return None
    return a / b

# Comentado para que no se quede esperando datos si corres todo el script junto

while True:
    print("\n--Mostrar menu--")
    print("1: Sumar | 2: Restar | 3: Multiplicar | 4: Dividir | 5: Salir")

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


#-------- 5. PRUEBA DE ESCRITORIO -------
# Aquí simulamos qué pasaría si un usuario ingresa ciertos valores:
#
# Acción               | opcion |  a |  b |    r | Pantalla / Consola
# -------------------- | -----: | -: | -: | ---: | --------------------------------
# input opcion         |      1 |  - |  - |    - | Elija una opcion: 1
# input a y b          |      1 | 10 |  5 |    - | Ingrese el primer numero: 10 ...
# evaluar sumar(10, 5) |      1 | 10 |  5 |   15 | La respuesta es: 15
# input opcion         |      4 |  - |  - |    - | Elija una opcion: 4
# input a y b          |      4 |  8 |  0 |    - | Ingrese el primer numero: 8 ...
# evaluar dividir(8,0) |      4 |  8 |  0 | None | No se puede dividir entre 0
# input opcion         |      5 |  - |  - |    - | Elija una opcion: 5
# evaluar break        |      5 |  - |  - |    - | Saliendo del programa...