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
PI=3.1416
area =  PI*(radio**2)
perimetro = 2 * PI*radio
print(f"El area del circulo: {area:.2f}")
print(f"El perimetro del circulo: {perimetro:.2f}")



#================================================
#--------------------------------TAREA-----------------------
#================================================

#================================================
# 1) Leer el nombre del usuario y saludarlo por su nombre.
#================================================
#--------ENTENDER EL PROBLEMA--------
#----Entrada: nombre del usuario
#----Proceso: solicitar el nombre por consola y generar un saludo personalizado
#----Salida: mensaje de bienvenida con el nombre

#-------- BOSQUEJO A MANO------------
# nombre = "Ana"
# mensaje = "Hola, Ana. Bienvenida al curso."

#--------DESCUBRIR EL PATRON-----------
# Leemos texto desde teclado mediante input() e incrustamos el valor en una cadena de formato f-string.

#--------ESCRIBIR EL CODIGO-----------
nombre = input("¿Cómo te llamas? ")
print(f"Hola, {nombre}. Bienvenida al curso.")

#--------PRUEBA DE ESCRITORIO--------
# Línea                 | nombre | Pantalla
# --------------------- | ------ | -----------------------------------
# `input(...)`          | "Ana"  | ¿Cómo te llamas?
# `print(...)`          | "Ana"  | Hola, Ana. Bienvenida al curso.

#CAMBIO
#Amplíalo para que además pida la edad y muestre «tienes X años».
#--------ENTENDER EL PROBLEMA--------
#----Entrada: nombre y edad
#----Proceso: leer ambos datos, convertir edad a entero y mostrar el saludo completo
#----Salida: mensaje con nombre y edad incluidos

#-------- BOSQUEJO A MANO------------
# nombre = "Ana", edad = 20
# mensaje = "Hola, Ana. Bienvenida al curso. Tienes 20 anos"

#--------DESCUBRIR EL PATRON-----------
# Convertimos el segundo input a int y concatenamos ambas variables dentro del f-string.

#--------ESCRIBIR EL CODIGO-----------
nombre = input("¿Cómo te llamas? ")
edad= int(input("Ingrese su edad: "))
print(f"Hola, {nombre}. Bienvenida al curso. Tienes {edad} anos")

#--------PRUEBA DE ESCRITORIO--------
# Línea                 | nombre | edad | Pantalla
# --------------------- | ------ | ---: | ------------------------------------------------
# `input(...)` nombre   | "Ana"  |    — | ¿Cómo te llamas?
# `input(...)` edad     | "Ana"  |   20 | Ingrese su edad:
# `print(...)`          | "Ana"  |   20 | Hola, Ana. Bienvenida al curso. Tienes 20 anos


#================================================
# 2) Leer tres notas de un estudiante y mostrar su promedio.
#================================================
#--------ENTENDER EL PROBLEMA--------
#----Entrada: tres notas decimales
#----Proceso: sumar las tres notas y dividirlas entre 3
#----Salida: promedio impreso con 1 decimal

#-------- BOSQUEJO A MANO------------
# n1 = 8.0, n2 = 7.0, n3 = 9.0
# promedio = (8.0 + 7.0 + 9.0) / 3 = 8.0

#--------DESCUBRIR EL PATRON-----------
# Encapsulamos la suma entre paréntesis para asegurar la prioridad de operaciones antes de dividir.

#--------ESCRIBIR EL CODIGO-----------
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

promedio = (n1 + n2 + n3) / 3      # PROCESO en una línea

print(f"Promedio: {promedio:.1f}")  # :.1f muestra un decimal

#--------PRUEBA DE ESCRITORIO--------
# Línea                 |  n1 |  n2 |  n3 | promedio | Pantalla
# --------------------- | --: | --: | --: | -------: | ----------------
# `inputs`              | 8.0 | 7.0 | 9.0 |        — | Nota 1: ...
# `promedio = ...`      | 8.0 | 7.0 | 9.0 |      8.0 | —
# `print(...)`          | 8.0 | 7.0 | 9.0 |      8.0 | Promedio: 8.0

#CAMBIO
#Modifícalo para que muestre «Aprueba» si el promedio es ≥ 7 y «Reprueba» si no. (Necesitas el if del módulo 3).
#--------ENTENDER EL PROBLEMA--------
#----Entrada: tres notas decimales
#----Proceso: calcular promedio y evaluar si es mayor o igual a 7 para determinar estado
#----Salida: promedio impreso y estado ("Aprovado" o "Reprovado")

#-------- BOSQUEJO A MANO------------
# n1 = 6.0, n2 = 7.0, n3 = 8.0 -> promedio = 7.0
# ¿7.0 >= 7? Sí -> imprime "Aprovado"

#--------DESCUBRIR EL PATRON-----------
# Evaluamos el promedio calculado mediante una estructura condicional if/else simple.

#--------ESCRIBIR EL CODIGO-----------
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

promedio = (n1 + n2 + n3) / 3
print(f"Promedio: {promedio:.1f}")
if promedio >= 7:
    print("Aprovado")
else:
    print("Reprovado")

#--------PRUEBA DE ESCRITORIO--------
# Línea                 |  n1 |  n2 |  n3 | promedio | promedio >= 7 | Pantalla
# --------------------- | --: | --: | --: | -------: | ------------- | ----------------
# `inputs`              | 8.0 | 7.0 | 9.0 |        — | —             | Nota 1: ...
# `promedio = ...`      | 8.0 | 7.0 | 9.0 |      8.0 | —             | Promedio: 8.0
# `if/else`             | 8.0 | 7.0 | 9.0 |      8.0 | True          | Aprovado


#================================================
# 3) Leer la base y la altura de un rectángulo y mostrar su área y su perímetro.
# Recuerda: área = base × altura, perímetro = 2 × (base + altura).
#================================================
#--------ENTENDER EL PROBLEMA--------
#----Entrada: base y altura de un rectángulo
#----Proceso: area = base * altura; perimetro = 2 * (base + altura)
#----Salida: área y perímetro con 2 decimales

#-------- BOSQUEJO A MANO------------
# base = 4.0, altura = 2.0
# area = 4.0 * 2.0 = 8.00
# perimetro = 2 * (4.0 + 2.0) = 12.00

#--------DESCUBRIR EL PATRON-----------
# Aplicamos las fórmulas geométricas directas operando con valores flotantes.

#--------ESCRIBIR EL CODIGO-----------
base = float(input("Base: "))
altura = float(input("Altura: "))

area = base * altura                # PROCESO 1
perimetro = 2 * (base + altura)     # PROCESO 2

print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")

#--------PRUEBA DE ESCRITORIO--------
# Línea                 | base | altura |  area | perimetro | Pantalla
# --------------------- | ---: | -----: | ----: | --------: | ----------------
# `inputs`              |  4.0 |    2.0 |     — |         — | Base: ...
# `area = ...`          |  4.0 |    2.0 |  8.00 |         — | —
# `perimetro = ...`     |  4.0 |    2.0 |  8.00 |     12.00 | —
# `prints`              |  4.0 |    2.0 |  8.00 |     12.00 | Área: 8.00 \n Perímetro: 12.00

#CAMBIO
#Ampliar para leer el radio de un círculo y mostrar área (π·r²) y perímetro (2·π·r).
#--------ENTENDER EL PROBLEMA--------
#----Entrada: radio de un círculo
#----Proceso: calcular área = PI * r² y perímetro = 2 * PI * r
#----Salida: área y perímetro del círculo formateados a 2 decimales

#-------- BOSQUEJO A MANO------------
# radio = 5.0, PI = 3.1416
# area = 3.1416 * (5.0^2) = 78.54
# perimetro = 2 * 3.1416 * 5.0 = 31.42

#--------DESCUBRIR EL PATRON-----------
# Definimos la constante PI y usamos el operador exponente `**` para calcular la potencia del radio.

#--------ESCRIBIR EL CODIGO-----------
radio = float(input("Ingrese radio: "))
PI=3.1416
area =  PI*(radio**2)
perimetro = 2 * PI*radio
print(f"El area del circulo: {area:.2f}")
print(f"El perimetro del circulo: {perimetro:.2f}")

#--------PRUEBA DE ESCRITORIO--------
# Línea                 | radio |     PI |  area | perimetro | Pantalla
# --------------------- | ----: | -----: | ----: | --------: | ------------------------------
# `input`               |   5.0 |      — |     — |         — | Ingrese radio:
# `area = ...`          |   5.0 | 3.1416 | 78.54 |         — | —
# `perimetro = ...`     |   5.0 | 3.1416 | 78.54 |     31.42 | —
# `prints`              |   5.0 | 3.1416 | 78.54 |     31.42 | El area del circulo: 78.54 ...


#================================================
#                TAREA
#================================================

#================================================
# 1) Pide una temperatura en grados Celsius y muéstrala en Fahrenheit. Fórmula: F = C × 9/5 + 32.
#================================================
#--------ENTENDER EL PROBLEMA--------
#----Entrada: temperatura en grados Celsius (flotante)
#----Proceso: aplicar la fórmula de conversión F = C * 9 / 5 + 32
#----Salida: temperatura equivalente en Fahrenheit con 1 decimal

#-------- BOSQUEJO A MANO------------
# celsius = 100.0
# fahrenheit = 100.0 * 9 / 5 + 32 = 180.0 + 32 = 212.0 °F

#--------DESCUBRIR EL PATRON-----------
# Multiplicamos los grados Celsius por el factor 9/5 y le sumamos 32 respetando la jerarquía aritmética de izquierda a derecha.

#--------ESCRIBIR EL CODIGO-----------
celsius = float(input("Temperatura en °C: "))
fahrenheit = celsius * 9/5 + 32
print(f"{fahrenheit:.1f} °F")

#--------PRUEBA DE ESCRITORIO--------
# Línea                 | celsius | fahrenheit | Pantalla
# --------------------- | ------: | ---------: | ------------
# `input`               |   100.0 |          — | Temperatura en °C:
# `fahrenheit = ...`    |   100.0 |      212.0 | —
# `print(...)`          |   100.0 |      212.0 | 212.0 °F


#================================================
# 2) Pide un total de segundos y muéstralos como hh:mm:ss. Ej.: 3725 segundos → 1:02:05.
#================================================
#--------ENTENDER EL PROBLEMA--------
#----Entrada: cantidad total de segundos (entero)
#----Proceso: descomponer el total en horas (// 3600), minutos (// 60 del resto) y segundos (% 60 del resto)
#----Salida: tiempo formateado en hh:mm:ss con ceros a la izquierda

#-------- BOSQUEJO A MANO------------
# total = 3725
# horas = 3725 // 3600 = 1
# resto = 3725 % 3600 = 125
# minutos = 125 // 60 = 2
# segundos = 125 % 60 = 5 -> "1:02:05"

#--------DESCUBRIR EL PATRON-----------
# Usamos división entera `//` para extraer unidades completas y módulo `%` para obtener el residuo sobrante. Aplicamos el especificador `:02d` para rellenar con un cero inicial si la cifra es menor a 10.

#--------ESCRIBIR EL CODIGO-----------
total = int(input("Segundos totales: "))
horas = total // 3600
resto = total % 3600
minutos = resto // 60
segundos = resto % 60
print(f"{horas}:{minutos:02d}:{segundos:02d}")

#--------PRUEBA DE ESCRITORIO--------
# Línea                 | total | horas | resto | minutos | segundos | Pantalla
# --------------------- | ----: | ----: | ----: | ------: | -------: | --------
# `input`               |  3725 |     — |     — |       — |        — | Segundos totales:
# `horas = ...`         |  3725 |     1 |     — |       — |        — | —
# `resto = ...`         |  3725 |     1 |   125 |       — |        — | —
# `minutos = ...`       |  3725 |     1 |   125 |       2 |        — | —
# `segundos = ...`      |  3725 |     1 |   125 |       2 |        5 | —
# `print(...)`          |  3725 |     1 |   125 |       2 |        5 | 1:02:05


#================================================
# 3) Lee dos números y muéstralos intercambiados. Python permite hacerlo en una sola línea, muy diferente a JS.
#================================================
#--------ENTENDER EL PROBLEMA--------
#----Entrada: dos variables numéricas a y b
#----Proceso: intercambiar sus valores almacenados
#----Salida: mostrar los valores de a y b actualizados

#-------- BOSQUEJO A MANO------------
# a = 5, b = 10
# a, b = b, a
# a -> 10, b -> 5

#--------DESCUBRIR EL PATRON-----------
# Aprovechamos el empaquetado y desempaquetado de tuplas de Python (`a, b = b, a`) para realizar la asignación paralela simultánea sin requerir una variable auxiliar temporal.

#--------ESCRIBIR EL CODIGO-----------
a = int(input("a: "))
b = int(input("b: "))

# Intercambio pythónico (una sola línea)
a, b = b, a

print(f"a = {a}, b = {b}")

#--------PRUEBA DE ESCRITORIO--------
# Línea                 |  a |  b | Pantalla
# --------------------- | -: | -: | ---------------
# `inputs`              |  5 | 10 | a: ... b: ...
# `a, b = b, a`         | 10 |  5 | —
# `print(...)`          | 10 |  5 | a = 10, b = 5


#================================================
# 4) Lee el precio de un producto sin IVA y muestra el IVA (15%) y el total.
#================================================
#--------ENTENDER EL PROBLEMA--------
#----Entrada: precio base del producto (flotante)
#----Proceso: calcular iva = precio * 0.15 y total = precio + iva
#----Salida: desglose del IVA y total a pagar formateados como moneda ($) a 2 decimales

#-------- BOSQUEJO A MANO------------
# precio = 100.00
# iva = 100.00 * 0.15 = 15.00
# total = 100.00 + 15.00 = 115.00

#--------DESCUBRIR EL PATRON-----------
# Calculamos el impuesto porcentual mediante multiplicación por tasa fija (0.15) y lo sumamos directamente al monto original.

#--------ESCRIBIR EL CODIGO-----------
precio = float(input("Precio sin IVA: $"))
iva = precio * 0.15
total = precio + iva

print(f"IVA:   ${iva:.2f}")
print(f"Total: ${total:.2f}")

#--------PRUEBA DE ESCRITORIO--------
# Línea                 | precio |   iva |  total | Pantalla
# --------------------- | -----: | ----: | -----: | --------------------------
# `input`               | 100.00 |     — |      — | Precio sin IVA: $
# `iva = ...`           | 100.00 | 15.00 |      — | —
# `total = ...`         | 100.00 | 15.00 | 115.00 | —
# `prints`              | 100.00 | 15.00 | 115.00 | IVA:   $15.00 \n Total: $115.00