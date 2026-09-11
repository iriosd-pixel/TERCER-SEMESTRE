#================================================
#EJEMPLOS PUESTOS POR LA IA MAS CAMBIOS
#================================================
from enum import nonmember


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
            return False           # sale inmediatamente
    return True                    # llegó al final sin encontrar divisor

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
#                TAREA
#================================================
#================================================
# 1) Función area_rectangulo(base, altura) que retorne el área.
#================================================
def area_rectangulo(base, altura):
    return base * altura

# Uso
print(area_rectangulo(5, 3))    # 15
print(area_rectangulo(4.5, 2))  # 9.0

#================================================
# 2) Función maximo(a, b, c) que retorne el mayor de tres números.
#================================================
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

#================================================
# 3) Un año es bisiesto si es divisible entre 4 y no entre 100, O si es divisible entre 400.
#================================================
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

#================================================
# 4) Función factorial(n) y luego combinatoria(n, k) = n! / (k! · (n-k)!).
#================================================
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

#================================================
# 5) Programa que use funciones separadas para cada operación
# (sumar, restar, multiplicar, dividir) y un menú que llame a la correcta.
#================================================
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
        print("Saliendo del programa")
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