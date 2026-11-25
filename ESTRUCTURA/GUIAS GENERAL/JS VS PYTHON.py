#=======================================================================
# EJEMPLOS DE EXPLICACIÓN DE LA GUÍA
# Cada ejemplo se puede ejecutar llamando a su función.
#=======================================================================
# Ejemplo de explicación 1
# Comparación en JavaScript (referencia, no se ejecuta en Python):
# let nombre = "Ana";
# console.log(`Hola ${nombre}`);

# Ejemplo de explicación 2
def ejemplo_explicacion_2():
    nombre = "Ana"
    print(f"Hola {nombre}")

# Ejemplo de explicación 3
def ejemplo_explicacion_3():
    nombre = input("¿Cómo te llamas? ")        # siempre retorna str
    edad = int(input("Tu edad: "))              # convertir a entero
    precio = float(input("Precio del boleto: "))  # convertir a decimal

    # f-string: mete variables directamente en el texto
    print(f"{nombre} tiene {edad} años y pagó ${precio:.2f}")

#=======================================================================
# EJEMPLOS PUESTOS POR LA IA MAS CAMBIOS
#=======================================================================
#=======================================================================
# 1) Leer el nombre del usuario y saludarlo por su nombre.
#=======================================================================
nombre = input("¿Cómo te llamas? ")
print(f"Hola, {nombre}. Bienvenida al curso.")
#CAMBIO
#Amplíalo para que además pida la edad y muestre «tienes X años».
nombre = input("¿Cómo te llamas? ")
edad= int(input("Ingrese su edad: "))
print(f"Hola, {nombre}. Bienvenida al curso. Tienes {edad} años")

#=======================================================================
# 2) Leer tres notas de un estudiante y mostrar su promedio.
#=======================================================================
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
    print("Aprueba")
else:
    print("Reprueba")

#=======================================================================
# 3) Leer la base y la altura de un rectángulo y mostrar su área y su perímetro.
# Recuerda: área = base × altura, perímetro = 2 × (base + altura).
#=======================================================================
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
import math
area = math.pi * radio**2
perimetro = 2 * math.pi * radio
print(f"El area del circulo: {area:.2f}")
print(f"El perimetro del circulo: {perimetro:.2f}")



#=======================================================================
# TALLER — 3 ejercicios paso a paso
#=======================================================================
#=======================================================================
# 1) Leer el nombre del usuario y saludarlo por su nombre.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: nombre (input)
# Proceso: concatenar «Hola,» con el nombre
# Salida: el saludo completo
# Ejemplo de entrada (guía): nombre = Ana
# Salida esperada (guía): Hola, Ana. Bienvenida al curso.

#-------- 2. BOSQUEJO A MANO ------------
# nombre = "Ana"
#
# Salida:  Hola, Ana. Bienvenida al curso.

#-------- 3. DESCUBRIR EL PATRÓN --------
# Leemos texto desde teclado mediante input() e incrustamos el valor en una cadena de formato f-string.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
nombre = input("¿Cómo te llamas? ")
print(f"Hola, {nombre}. Bienvenida al curso.")

#-------- 5. PRUEBA DE ESCRITORIO -------
# Línea                 | nombre | Pantalla
# --------------------- | ------ | -----------------------------------
# `input(...)`          | "Ana"  | ¿Cómo te llamas?
# `print(...)`          | "Ana"  | Hola, Ana. Bienvenida al curso.

#CAMBIO
#Amplíalo para que además pida la edad y muestre «tienes X años».
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: n1, n2, n3 (input)
# Proceso: sumar las tres y dividir para 3
# Salida: el promedio
# Ejemplo de entrada (guía): n1 = 8, n2 = 6, n3 = 10
# Salida esperada (guía): Promedio: 8.0

#-------- 2. BOSQUEJO A MANO ------------
# n1 = 8, n2 = 6, n3 = 10
#
# paso 1: sumo    8 + 6 + 10 = 24
# paso 2: divido  24 / 3     = 8.0
# paso 3: muestro "Promedio: 8.0"

#-------- 3. DESCUBRIR EL PATRÓN --------
# Convertimos el segundo input a int y concatenamos ambas variables dentro del f-string.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
nombre = input("¿Cómo te llamas? ")
edad= int(input("Ingrese su edad: "))
print(f"Hola, {nombre}. Bienvenida al curso. Tienes {edad} años")

#-------- 5. PRUEBA DE ESCRITORIO -------
# Línea                 | nombre | edad | Pantalla
# --------------------- | ------ | ---: | ------------------------------------------------
# `input(...)` nombre   | "Ana"  |    — | ¿Cómo te llamas?
# `input(...)` edad     | "Ana"  |   20 | Ingrese su edad:
# `print(...)`          | "Ana"  |   20 | Hola, Ana. Bienvenida al curso. Tienes 20 años


#=======================================================================
# 2) Leer tres notas de un estudiante y mostrar su promedio.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: base, altura (input)
# Proceso: aplicar las dos fórmulas
# Salida: el área y el perímetro
# Ejemplo de entrada (guía): base = 5, altura = 3
# Salida esperada (guía): Área: 15.00 Perímetro: 16.00

#-------- 2. BOSQUEJO A MANO ------------
# base = 5, altura = 3
#
# área      = 5 × 3 = 15
# perímetro = 2 × (5 + 3) = 16

#-------- 3. DESCUBRIR EL PATRÓN --------
# Encapsulamos la suma entre paréntesis para asegurar la prioridad de operaciones antes de dividir.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

promedio = (n1 + n2 + n3) / 3      # PROCESO en una línea

print(f"Promedio: {promedio:.1f}")  # :.1f muestra un decimal

#-------- 5. PRUEBA DE ESCRITORIO -------
# Línea                 |  n1 |  n2 |  n3 | promedio | Pantalla
# --------------------- | --: | --: | --: | -------: | ----------------
# `inputs`              | 8.0 | 7.0 | 9.0 |        — | Nota 1: ...
# `promedio = ...`      | 8.0 | 7.0 | 9.0 |      8.0 | —
# `print(...)`          | 8.0 | 7.0 | 9.0 |      8.0 | Promedio: 8.0

#CAMBIO
#Modifícalo para que muestre «Aprueba» si el promedio es ≥ 7 y «Reprueba» si no. (Necesitas el if del módulo 3).
#-------- 1. ENTENDER EL PROBLEMA --------
#----Entrada: tres notas decimales
#----Proceso: calcular promedio y evaluar si es mayor o igual a 7 para determinar estado
#----Salida: promedio impreso y estado ("Aprueba" o "Reprueba")

#-------- 2. BOSQUEJO A MANO ------------
# n1 = 6.0, n2 = 7.0, n3 = 8.0 -> promedio = 7.0
# ¿7.0 >= 7? Sí -> imprime "Aprueba"

#-------- 3. DESCUBRIR EL PATRÓN --------
# Evaluamos el promedio calculado mediante una estructura condicional if/else simple.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

promedio = (n1 + n2 + n3) / 3
print(f"Promedio: {promedio:.1f}")
if promedio >= 7:
    print("Aprueba")
else:
    print("Reprueba")

#-------- 5. PRUEBA DE ESCRITORIO -------
# Línea                 |  n1 |  n2 |  n3 | promedio | promedio >= 7 | Pantalla
# --------------------- | --: | --: | --: | -------: | ------------- | ----------------
# `inputs`              | 8.0 | 7.0 | 9.0 |        — | —             | Nota 1: ...
# `promedio = ...`      | 8.0 | 7.0 | 9.0 |      8.0 | —             | Promedio: 8.0
# `if/else`             | 8.0 | 7.0 | 9.0 |      8.0 | True          | Aprueba


#=======================================================================
# 3) Leer la base y la altura de un rectángulo y mostrar su área y su perímetro.
# Recuerda: área = base × altura, perímetro = 2 × (base + altura).
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
#----Entrada: base y altura de un rectángulo
#----Proceso: area = base * altura; perimetro = 2 * (base + altura)
#----Salida: área y perímetro con 2 decimales

#-------- 2. BOSQUEJO A MANO ------------
# base = 4.0, altura = 2.0
# area = 4.0 * 2.0 = 8.00
# perimetro = 2 * (4.0 + 2.0) = 12.00

#-------- 3. DESCUBRIR EL PATRÓN --------
# Aplicamos las fórmulas geométricas directas operando con valores flotantes.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
base = float(input("Base: "))
altura = float(input("Altura: "))

area = base * altura                # PROCESO 1
perimetro = 2 * (base + altura)     # PROCESO 2

print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")

#-------- 5. PRUEBA DE ESCRITORIO -------
# Línea                 | base | altura |  area | perimetro | Pantalla
# --------------------- | ---: | -----: | ----: | --------: | ----------------
# `inputs`              |  4.0 |    2.0 |     — |         — | Base: ...
# `area = ...`          |  4.0 |    2.0 |  8.00 |         — | —
# `perimetro = ...`     |  4.0 |    2.0 |  8.00 |     12.00 | —
# `prints`              |  4.0 |    2.0 |  8.00 |     12.00 | Área: 8.00 \n Perímetro: 12.00

#CAMBIO
#Ampliar para leer el radio de un círculo y mostrar área (π·r²) y perímetro (2·π·r).
#-------- 1. ENTENDER EL PROBLEMA --------
#----Entrada: radio de un círculo
#----Proceso: calcular área = math.pi * r² y perímetro = 2 * math.pi * r
#----Salida: área y perímetro del círculo formateados a 2 decimales

#-------- 2. BOSQUEJO A MANO ------------
# radio = 5.0, math.pi ≈ 3.14159265
# area = math.pi * (5.0**2) ≈ 78.54
# perimetro = 2 * math.pi * 5.0 ≈ 31.42

#-------- 3. DESCUBRIR EL PATRÓN --------
# Usamos math.pi y el operador exponente `**` para calcular la potencia del radio.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
radio = float(input("Ingrese radio: "))
import math
area = math.pi * radio**2
perimetro = 2 * math.pi * radio
print(f"El area del circulo: {area:.2f}")
print(f"El perimetro del circulo: {perimetro:.2f}")

#-------- 5. PRUEBA DE ESCRITORIO -------
# Línea                 | radio | math.pi |  area | perimetro | Pantalla
# --------------------- | ----: | -----: | ----: | --------: | ------------------------------
# `input`               |   5.0 |      — |     — |         — | Ingrese radio:
# `area = ...`          |   5.0 | 3.14159 | 78.54 |         — | —
# `perimetro = ...`     |   5.0 | 3.14159 | 78.54 |     31.42 | —
# `prints`              |   5.0 | 3.14159 | 78.54 |     31.42 | El area del circulo: 78.54 ...


#=======================================================================
# EJERCICIOS PROPUESTOS
#=======================================================================
#=======================================================================
# 1) Pide una temperatura en grados Celsius y muéstrala en Fahrenheit. Fórmula: F = C × 9/5 + 32.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
#----Entrada: temperatura en grados Celsius (flotante)
#----Proceso: aplicar la fórmula de conversión F = C * 9 / 5 + 32
#----Salida: temperatura equivalente en Fahrenheit con 1 decimal

# Ejemplo de entrada (guía): celsius = 25
# Salida esperada (guía): 77.0 °F

#-------- 2. BOSQUEJO A MANO ------------
# celsius = 100.0
# fahrenheit = 100.0 * 9 / 5 + 32 = 180.0 + 32 = 212.0 °F

#-------- 3. DESCUBRIR EL PATRÓN --------
# Multiplicamos los grados Celsius por el factor 9/5 y le sumamos 32 respetando la jerarquía aritmética de izquierda a derecha.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
celsius = float(input("Temperatura en °C: "))
fahrenheit = celsius * 9/5 + 32
print(f"{fahrenheit:.1f} °F")

#-------- 5. PRUEBA DE ESCRITORIO -------
# Línea                 | celsius | fahrenheit | Pantalla
# --------------------- | ------: | ---------: | ------------
# `input`               |   100.0 |          — | Temperatura en °C:
# `fahrenheit = ...`    |   100.0 |      212.0 | —
# `print(...)`          |   100.0 |      212.0 | 212.0 °F


#=======================================================================
# 2) Pide un total de segundos y muéstralos como hh:mm:ss. Ej.: 3725 segundos → 1:02:05.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
#----Entrada: cantidad total de segundos (entero)
#----Proceso: descomponer el total en horas (// 3600), minutos (// 60 del resto) y segundos (% 60 del resto)
#----Salida: tiempo formateado en hh:mm:ss con ceros a la izquierda

# Ejemplo de entrada (guía): total = 3725
# Salida esperada (guía): 1:02:05

#-------- 2. BOSQUEJO A MANO ------------
# total = 3725
# horas = 3725 // 3600 = 1
# resto = 3725 % 3600 = 125
# minutos = 125 // 60 = 2
# segundos = 125 % 60 = 5 -> "1:02:05"

#-------- 3. DESCUBRIR EL PATRÓN --------
# Usamos división entera `//` para extraer unidades completas y módulo `%` para obtener el residuo sobrante. Aplicamos el especificador `:02d` para rellenar con un cero inicial si la cifra es menor a 10.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
total = int(input("Segundos totales: "))
horas = total // 3600
resto = total % 3600
minutos = resto // 60
segundos = resto % 60
print(f"{horas}:{minutos:02d}:{segundos:02d}")

#-------- 5. PRUEBA DE ESCRITORIO -------
# Línea                 | total | horas | resto | minutos | segundos | Pantalla
# --------------------- | ----: | ----: | ----: | ------: | -------: | --------
# `input`               |  3725 |     — |     — |       — |        — | Segundos totales:
# `horas = ...`         |  3725 |     1 |     — |       — |        — | —
# `resto = ...`         |  3725 |     1 |   125 |       — |        — | —
# `minutos = ...`       |  3725 |     1 |   125 |       2 |        — | —
# `segundos = ...`      |  3725 |     1 |   125 |       2 |        5 | —
# `print(...)`          |  3725 |     1 |   125 |       2 |        5 | 1:02:05


#=======================================================================
# 3) Lee dos números y muéstralos intercambiados. Python permite hacerlo en una sola línea, muy diferente a JS.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
#----Entrada: dos variables numéricas a y b
#----Proceso: intercambiar sus valores almacenados
#----Salida: mostrar los valores de a y b actualizados

# Ejemplo de entrada (guía): a = 5, b = 8
# Salida esperada (guía): a = 8, b = 5

#-------- 2. BOSQUEJO A MANO ------------
# a = 5, b = 10
# a, b = b, a
# a -> 10, b -> 5

#-------- 3. DESCUBRIR EL PATRÓN --------
# Aprovechamos el empaquetado y desempaquetado de tuplas de Python (`a, b = b, a`) para realizar la asignación paralela simultánea sin requerir una variable auxiliar temporal.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
a = int(input("a: "))
b = int(input("b: "))

# Intercambio pythónico (una sola línea)
a, b = b, a

print(f"a = {a}, b = {b}")

#-------- 5. PRUEBA DE ESCRITORIO -------
# Línea                 |  a |  b | Pantalla
# --------------------- | -: | -: | ---------------
# `inputs`              |  5 | 10 | a: ... b: ...
# `a, b = b, a`         | 10 |  5 | —
# `print(...)`          | 10 |  5 | a = 10, b = 5


#=======================================================================
# 4) Lee el precio de un producto sin IVA y muestra el IVA (15%) y el total.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
#----Entrada: precio base del producto (flotante)
#----Proceso: calcular iva = precio * 0.15 y total = precio + iva
#----Salida: desglose del IVA y total a pagar formateados como moneda ($) a 2 decimales

# Ejemplo de entrada (guía): precio = 100
# Salida esperada (guía): IVA: $15.00 Total: $115.00

#-------- 2. BOSQUEJO A MANO ------------
# precio = 100.00
# iva = 100.00 * 0.15 = 15.00
# total = 100.00 + 15.00 = 115.00

#-------- 3. DESCUBRIR EL PATRÓN --------
# Calculamos el impuesto porcentual mediante multiplicación por tasa fija (0.15) y lo sumamos directamente al monto original.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
precio = float(input("Precio sin IVA: $"))
iva = precio * 0.15
total = precio + iva

print(f"IVA:   ${iva:.2f}")
print(f"Total: ${total:.2f}")

#-------- 5. PRUEBA DE ESCRITORIO -------
# Línea                 | precio |   iva |  total | Pantalla
# --------------------- | -----: | ----: | -----: | --------------------------
# `input`               | 100.00 |     — |      — | Precio sin IVA: $
# `iva = ...`           | 100.00 | 15.00 |      — | —
# `total = ...`         | 100.00 | 15.00 | 115.00 | —
# `prints`              | 100.00 | 15.00 | 115.00 | IVA:   $15.00 \n Total: $115.00
