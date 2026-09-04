#================================================
#EJEMPLOS PUESTOS POR LA IA MAS CAMBIOS
#================================================

#================================================
# 1) Leer un número N y mostrar los números del 1 al N.
#================================================
n = int(input("N: "))

for i in range(1, n + 1):      # ¡ojo con el n+1!
    print(i)
#CAMBIO
#Cámbialo para que muestre del N al 1 (hacia atrás). Pista: range(n, 0, -1).
n = int(input("N: "))

for i in range(n, 0, -1):
    print(i)

#================================================
# 2) Leer N y calcular la suma de 1 + 2 + 3 + ... + N.
#================================================
n = int(input("N: "))
suma = 0                    # INICIALIZACIÓN del acumulador

for i in range(1, n + 1):
    suma = suma + i         # equivale a: suma += i

print(f"Suma: {suma}")
#CAMBIO
#Adaptarlo para calcular la suma de los pares del 2 al 100. Pista: range(2, 101, 2).
n = int(input("N: "))
suma = 0                    # INICIALIZACIÓN del acumulador

for i in range(2, 101, 2):
    suma = suma + i         # equivale a: suma += i

print(f"Suma: {suma}")

#================================================
# 3) Leer N y calcular el factorial (N! = 1 × 2 × 3 × ... × N). Ejemplo: 5! = 120.
#================================================
n = int(input("N: "))
fact = 1                    # INICIALIZACIÓN: 1 porque vamos a multiplicar

for i in range(1, n + 1):
    fact = fact * i         # o: fact *= i

print(f"{n}! = {fact}")
#PROBAR
#¿Qué pasa con N muy grande (100!)? Python maneja enteros infinitos,
# pruébalo. En JS con enteros normales explotaría.

#================================================
# 4) Leer las notas de N estudiantes (una por una) y contar cuántos aprobaron (nota ≥ 70).
#================================================
n = int(input("¿Cuántos estudiantes? "))
aprobados = 0                       # contador arranca en 0

for i in range(n):
    nota = float(input(f"Nota {i+1}: "))
    if nota >= 7:                   # el 7 es el umbral (o 70 si es sobre 100)
        aprobados += 1              # aumenta solo si aprobó

print(f"Aprobados: {aprobados} de {n}")
#CAMBIO
#Añade un contador para reprobados y muestra el porcentaje de aprobación.
n = int(input("¿Cuántos estudiantes? "))
aprobados = 0                       # contador arranca en 0
reprobados= 0
for i in range(n):
    nota = float(input(f"Nota {i+1}: "))
    if nota >= 7:                   # el 7 es el umbral (o 70 si es sobre 100)
        aprobados += 1             # aumenta solo si aprobó
    else:
        reprobados += 1
print(f"Aprobados: {aprobados} de {n}")
print(f"Aprobados: {reprobados} de {n}")

#================================================
# 6) Leer las notas de N estudiantes y mostrar la nota más alta.
#================================================
n = int(input("¿Cuántas notas? "))
maxima = float("-inf")              # valor imposible: nada será menor

for i in range(n):
    nota = float(input(f"Nota {i+1}: "))
    if nota > maxima:               # ¿es mayor que el récord?
        maxima = nota               # sí → actualizamos

print(f"Máxima: {maxima}")
#CAMBIO
#Adaptarlo para encontrar la menor nota. Cambio: float("inf") y if nota < minima:.
n = int(input("¿Cuántas notas? "))
minima = float("inf")              # valor imposible: nada será menor

for i in range(n):
    nota = float(input(f"Nota {i+1}: "))
    if nota < minima:               # ¿es mayor que el récord?
        minima = nota               # sí → actualizamos

print(f"Máxima: {minima}")


#================================================
# 7) Leer un número y determinar si es primo (solo divisible entre 1 y él mismo).
#================================================
n = int(input("Número: "))
es_primo = True                     # BANDERA: asumimos que sí

if n < 2:
    es_primo = False                # 0 y 1 no son primos
else:
    # Probar divisores del 2 hasta √n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:              # si i divide exacto a n...
            es_primo = False        # ...no es primo
            break                   # optimización: no seguir probando

if es_primo:
    print(f"{n} es primo")
else:
    print(f"{n} NO es primo")
#CAMBIO
#Genera una lista de todos los primos entre 2 y 100.
primos = []  # Lista vacía para guardar los números primos

for n in range(2, 101):  # Evaluamos automáticamente del 2 al 100
    es_primo = True

    for i in range(2, int(n**0.5) + 1):  # Probamos divisores
        if n % i == 0:
            es_primo = False
            break  # Ya no es primo, salimos del ciclo interno

    if es_primo:
        primos.append(n)  # Guardamos el número en la lista

print("Números primos entre 2 y 100:")
print(primos)















#================================================
#
#================================================









#================================================
# 1) Lee un número N y muestra su tabla de multiplicar (del 1 al 12).
#================================================
numero= int(input("Ingrese un numero: "))
for i in range(1, 22):
    print(f"{numero} x {i} = {numero*i}")

#================================================
# 2) Lee un número y cuenta cuántos dígitos tiene (sin convertir a string).
#================================================
valores= abs(int(input("Ingrese una cifra numérica: ")))
contador=0
if valores==0:
    contador= 1
else:
    while valores>0:
        contador=contador+1
        valores=valores//10
print(f"En la cifra hay {contador} numeros")

#================================================
# 3) Lee N números y muestra la suma de los pares y la suma de los impares por separado.
#================================================
cantidad=int(input("Ingrese la cantidad de numeros: "))
suma_par=0
suma_impar=0
for i in range(cantidad):
    valor=int(input("Ingrese un numero: "))
    if valor%2==0:
        suma_par=suma_par+valor
    else:
        suma_impar=suma_impar+valor
print(f"La suma par es: {suma_par} y la suma impar es: {suma_impar}")

#================================================
# 4) Pide una edad y valida que esté entre 0 y 120. Si el usuario ingresa algo inválido, vuelve a pedirla.
#================================================
while True:
    edad = int(input("Ingrese una edad"))
    if edad >= 0 and edad <= 120:
        break
    print ("Inválida, intenta de nuevo")
print(f"Edad válida: {edad}")

#================================================
# 5) Genera un número secreto entre 1 y 100. El usuario intenta adivinar. En cada intento le dices si es «mayor» o «menor». Cuenta cuántos intentos usó.
#================================================
