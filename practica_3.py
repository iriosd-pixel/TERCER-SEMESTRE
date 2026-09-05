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
#                TAREA
#================================================
#================================================
# 1) Lee un número N y muestra su tabla de multiplicar (del 1 al 12).
#================================================

#--------ENTENDER EL PROBLEMA--------
#----Entrada:
#numero (input)
#----Proceso:
#multiplicar el numero por cada valor del 1 al 12
#----Salida:
#tabla de multiplicar del numero

#-------- BOSQUEJO A MANO------------
#numero: 5
#5 × 1 = 5
#5 × 2 = 10
#5 × 3 = 15
#...
#5 × 12 = 60

#--------DESCUBRIR EL PATRON-----------
#El patrón consiste en repetir la multiplicación del número
#por los valores del 1 al 12.
#Para eso usamos un ciclo for que va aumentando de uno en uno.

#--------ESCRIBIR EL CODIGO-----------
numero= int(input("Ingrese un numero: "))
for i in range(1, 13):
    print(f"{numero} x {i} = {numero*i}")

#--------PRUEBA DE ESCRITORIO---------
# Línea              | numero | i | numero*i | Pantalla
# ------------------ | -----: | -: | -------: | --------
# input              |      5 | — |        — | 5
# for                |      5 | 1 |        5 | —
# print              |      5 | 2 |       10 | 5 x 2 = 10
# print              |      5 | 3 |       15 | 5 x 3 = 15
# ...                |      5 | — |        — | ...
# print              |      5 |12 |       60 | 5 x 12 = 60

#================================================
# 2) Lee un número y cuenta cuántos dígitos tiene (sin convertir a string).
#================================================

#--------ENTENDER EL PROBLEMA--------
#----Entrada:
#numero (input)
#----Proceso:
#dividir el numero entre 10 hasta que llegue a 0
#contar cada división realizada
#----Salida:
#cantidad de dígitos del numero

#-------- BOSQUEJO A MANO------------
#numero: 4356
#
#4356 // 10 = 435
#435 // 10 = 43
#43 // 10 = 4
#4 // 10 = 0
#
#contador = 4

#--------DESCUBRIR EL PATRON-----------
#El patrón consiste en dividir el número entre 10 usando //.
#Cada división elimina un dígito del número.
#Por cada división aumentamos el contador en 1.
#Cuando el número llega a 0, ya contamos todos sus dígitos.

#--------ESCRIBIR EL CODIGO-----------
valores= abs(int(input("Ingrese una cifra numérica: ")))
contador=0
if valores==0:
    contador= 1
else:
    while valores>0:
        contador=contador+1
        valores=valores//10
print(f"En la cifra hay {contador} numeros")

#--------PRUEBA DE ESCRITORIO---------
# Línea                    | valores | contador | Pantalla
# ------------------------ | -------: | --------: | --------
# input                    |     4356 |        0 | 4356
# contador=contador+1      |      435 |        1 | —
# valores=valores//10      |      435 |        1 | —
# contador=contador+1      |       43 |        2 | —
# valores=valores//10      |       43 |        2 | —
# contador=contador+1      |        4 |        3 | —
# valores=valores//10      |        4 |        3 | —
# contador=contador+1      |        0 |        4 | —
# print                    |        0 |        4 | En la cifra hay 4 numeros

#================================================
# 3) Lee N números y muestra la suma de los pares y la suma de los impares por separado.
#================================================

#--------ENTENDER EL PROBLEMA--------
#----Entrada:
#cantidad de numeros
#los numeros que vamos a ingresar
#----Proceso:
#comprobar si cada numero es par o impar
#sumar los pares en una variable y los impares en otra
#----Salida:
#suma de los pares y suma de los impares

#-------- BOSQUEJO A MANO------------
#cantidad: 5
#numeros: 2, 5, 4, 7, 6
#
#pares: 2 + 4 + 6 = 12
#impares: 5 + 7 = 12

#--------DESCUBRIR EL PATRON-----------
#El patrón consiste en revisar cada número usando % 2.
#Si el resto es 0, el número es par.
#Si el resto es diferente de 0, es impar.
#Después sumamos cada número en su respectiva variable.

#--------ESCRIBIR EL CODIGO-----------
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

#--------PRUEBA DE ESCRITORIO---------
# Línea              | valor | suma_par | suma_impar | Pantalla
# ------------------ | ----: | --------: | ----------: | --------
# input cantidad     |     — |         0 |          0 | 5
# input valor        |     2 |         0 |          0 | 2
# suma_par           |     2 |         2 |          0 | —
# input valor        |     5 |         2 |          0 | 5
# suma_impar         |     5 |         2 |          5 | —
# input valor        |     4 |         2 |          5 | 4
# suma_par           |     4 |         6 |          5 | —
# input valor        |     7 |         6 |          5 | 7
# suma_impar         |     7 |         6 |         12 | —
# input valor        |     6 |         6 |         12 | 6
# suma_par           |     6 |        12 |         12 | —
# print              |     — |        12 |         12 | Suma par: 12, suma impar: 12

#================================================
# 4) Pide una edad y valida que esté entre 0 y 120. Si el usuario ingresa algo inválido, vuelve a pedirla.
#================================================

#--------ENTENDER EL PROBLEMA--------
#----Entrada:
#edad (input)
#----Proceso:
#comprobar que la edad esté entre 0 y 120
#si no está dentro del rango, volver a pedirla
#----Salida:
#edad válida

#-------- BOSQUEJO A MANO------------
#edad: 150
#150 está entre 0 y 120? NO
#volver a pedir
#
#edad: 25
#25 está entre 0 y 120? SI
#resultado: edad válida = 25

#--------DESCUBRIR EL PATRON-----------
#El patrón consiste en repetir la pregunta mientras
#la edad sea inválida.
#Usamos while True para repetir y break para salir
#cuando encontramos una edad válida.

#--------ESCRIBIR EL CODIGO-----------
while True:
    edad = int(input("Ingrese una edad"))
    if edad >= 0 and edad <= 120:
        break
    print ("Inválida, intenta de nuevo")
print(f"Edad válida: {edad}")

#--------PRUEBA DE ESCRITORIO---------
# Línea              | edad | Pantalla
# ------------------ | ---: | --------
# input              | 150  | 150
# if                 | 150  | —
# print inválida     | 150  | Inválida, intenta de nuevo
# input              | 25   | 25
# if                 | 25   | —
# break              | 25   | —
# print              | 25   | Edad válida: 25

#================================================
# 5) Genera un número secreto entre 1 y 100. El usuario intenta adivinar.
#================================================

#--------ENTENDER EL PROBLEMA--------
#----Entrada:
#numero que intenta adivinar el usuario
#----Proceso:
#comparar el intento con el numero secreto
#decir si debe ingresar un numero mayor o menor
#contar los intentos realizados
#----Salida:
#cantidad de intentos cuando adivine

#-------- BOSQUEJO A MANO------------
#numero secreto: 50
#
#intento: 30
#30 es menor que 50 → pedir un numero mayor
#
#intento: 70
#70 es mayor que 50 → pedir un numero menor
#
#intento: 50
#50 es igual a 50 → correcto
#
#intentos: 3

#--------DESCUBRIR EL PATRON-----------
#El patrón consiste en repetir los intentos hasta encontrar
#el número secreto.
#Cada vez que el usuario intenta, aumentamos el contador.
#Si el intento es mayor o menor, damos una pista.
#Cuando es igual al secreto, usamos break para terminar.

#--------ESCRIBIR EL CODIGO-----------
import random
secreto= random.randint(1, 100)
intentos=0

while True:
    intento= int(input("Ingrese un numero para adivinar (1 al 100)"))
    intentos+=1
    if intento==secreto:
        print(f"¡Correcto en {intentos} intentos!")
        break
    elif intento>secreto:
        print("EL numero es mayor que el secreto")
    else:
        print("El numero es menor que el secreto")

#--------PRUEBA DE ESCRITORIO---------
# Para la prueba suponemos que el numero secreto es 50.
#
# Línea              | secreto | intento | intentos | Pantalla
# ------------------ | -------: | ------: | --------: | --------
# random             |       50 |       — |         0 | —
# input              |       50 |      30 |         1 | 30
# elif               |       50 |      30 |         1 | El numero es menor
# input              |       50 |      70 |         2 | 70
# if/elif            |       50 |      70 |         2 | El numero es mayor
# input              |       50 |      50 |         3 | 50
# if                 |       50 |      50 |         3 | Correcto en 3 intentos
# break              |       50 |      50 |         3 | —

#================================================
# 6) Muestra los primeros N números de Fibonacci.
#================================================

#--------ENTENDER EL PROBLEMA--------
#----Entrada:
#cantidad de numeros que queremos mostrar
#----Proceso:
#mostrar el numero actual y sumar los dos numeros anteriores
#----Salida:
#los primeros N numeros de Fibonacci

#-------- BOSQUEJO A MANO------------
#cantidad: 6
#
#a=0
#b=1
#
#muestro 0
#siguiente=0+1=1
#
#muestro 1
#siguiente=1+1=2
#
#muestro 1
#siguiente=1+2=3
#
#resultado:
#0 1 1 2 3 5

#--------DESCUBRIR EL PATRON-----------
#El patrón consiste en sumar los dos números anteriores
#para obtener el siguiente.
#Después de mostrar un número, cambiamos los valores de a y b
#para continuar con la serie.

#--------ESCRIBIR EL CODIGO-----------
can_numeros= int(input("Ingrese la cantidad de numero que desea saber de la serie de figonashi: "))
a=0
b=1
for i in range(can_numeros):
    print(a, end=" ")
    siguiente= a+b
    a=b
    b=siguiente

#--------PRUEBA DE ESCRITORIO---------
# Línea                  | a | b | siguiente | Pantalla
# ---------------------- | -: | -: | --------: | --------
# inicio                 | 0 | 1 |         — | —
# print                  | 0 | 1 |         — | 0
# siguiente=a+b         | 0 | 1 |         1 | —
# a=b                    | 1 | 1 |         1 | —
# b=siguiente            | 1 | 1 |         1 | —
# print                  | 1 | 1 |         1 | 0 1
# siguiente=a+b         | 1 | 1 |         2 | —
# a=b                    | 1 | 1 |         2 | —
# b=siguiente            | 1 | 2 |         2 | —
# print                  | 1 | 2 |         2 | 0 1 1
# siguiente=a+b         | 1 | 2 |         3 | —
# a=b                    | 2 | 2 |         3 | —
# b=siguiente            | 2 | 3 |         3 | —
# ...
# resultado              | — | — |         — | 0 1 1 2 3 5