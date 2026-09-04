#================================================
#EJEMPLOS PUESTOS POR LA IA MAS CAMBIOS
#================================================

#================================================
# 1) Leer el precio de un producto sin IVA y mostrar el IVA y el precio final.
# El IVA en Ecuador es 15%.
#================================================
IVA = 0.15                              # constante en MAYÚSCULA

precio = float(input("Precio sin IVA: $"))
iva = precio * IVA
total = precio + iva

print(f"IVA:   ${iva:.2f}")
print(f"Total: ${total:.2f}")
#CAMBIO
#Añadir un descuento del 10% que se aplique antes del IVA.
# Muestra los tres valores: descuento, IVA, total.
IVA = 0.15                              # constante en MAYÚSCULA
DESCUENTO= 0.10
precio = float(input("Precio sin IVA: $"))

precio_des = precio * DESCUENTO
precio = precio - precio_des

iva = precio * IVA
total = precio + iva

print(f"Descuento: ${precio_des:.2f}")
print(f"IVA:       ${iva:.2f}")
print(f"Total:     ${total:.2f}")

#================================================
# 2) Leer un número entero y determinar si es par o impar.
#================================================
num = int(input("Ingresa un número: "))

# Ternario: expresión que devuelve un valor u otro según la condición
resultado = "par" if num % 2 == 0 else "impar"

print(f"{num} es {resultado}")
#CAMBIO
#Modifícalo para que además diga si es múltiplo de 3, de 5, o de ambos.
num = int(input("Ingresa un número: "))

# Ternario: expresión que devuelve un valor u otro según la condición
resultado = "par" if num % 2 == 0 else "impar"

if num % 3 == 0 and num % 5 == 0:
    print(f"{num} es multiplo de ambos")
elif num % 3 == 0:
    print(f"{num} es multiplo de 3")
elif num % 5 == 0:
    print(f"{num} es multiplo de 5")
else:
    print(f"{num} no es multiplo de 3 ni de 5")

print(f"{num} es {resultado}")

#================================================
# 3) Leer una cantidad total de segundos y mostrarla como hh:mm:ss.
# Ejemplo: 3725 segundos → 01:02:05.
#================================================
total = int(input("Segundos totales: "))

horas = total // 3600
resto = total % 3600
minutos = resto // 60
segundos = resto % 60

print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")
# CAMBIO
#Al revés: leer hh:mm:ss y convertir a segundos totales. Tendrás que usar split(":").
# 1. Leemos el tiempo como texto
tiempo = input("Ingresa el tiempo (hh:mm:ss): ")

# 2. Cortamos el texto usando ":" y lo guardamos en tres variables
h, m, s = tiempo.split(":")

# 3. Convertimos esos textos a números enteros (int) para poder calcular
horas = int(h)
minutos = int(m)
segundos = int(s)

# 4. Calculamos el total de segundos
# - Cada hora tiene 3600 segundos (60 * 60)
# - Cada minuto tiene 60 segundos
total_segundos = (horas * 3600) + (minutos * 60) + segundos

# 5. Mostramos el resultado
print(f"El total es: {total_segundos} segundos")

#================================================
# 4) Un cajero solo tiene billetes de $20, $10, $5 y $1. Dado un monto,
# mostrar cuántos billetes de cada uno se necesitan (usando la mínima cantidad).
#================================================
monto = int(input("Monto: $"))
resto = monto

b20 = resto // 20; resto = resto % 20
b10 = resto // 10; resto = resto % 10
b5  = resto // 5;  resto = resto % 5
b1  = resto // 1;  resto = resto % 1

print(f"$20 × {b20}")
print(f"$10 × {b10}")
print(f"$5  × {b5}")
print(f"$1  × {b1}")
#CAMBIO
#Añadir billete de $50 al inicio. Después probar con monedas de
# $0.25, $0.10, $0.05 y $0.01 (necesitas trabajar con centavos).
# 1. Ahora leemos el monto como un número con decimales (float)
monto = float(input("Monto: $"))

# 2. Convertimos a centavos
# Usamos round() para asegurar que no haya problemas de redondeo
resto = int(round(monto * 100))

# 3. Billetes (convertidos a centavos, ej: $50 = 5000 centavos)
b50 = resto // 5000; resto = resto % 5000
b20 = resto // 2000; resto = resto % 2000
b10 = resto // 1000; resto = resto % 1000
b5  = resto // 500;  resto = resto % 500
b1  = resto // 100;  resto = resto % 100

# 4. Monedas (ya son centavos)
m25 = resto // 25; resto = resto % 25
m10 = resto // 10; resto = resto % 10
m5  = resto // 5;  resto = resto % 5
m1  = resto // 1;  resto = resto % 1

# 5. Imprimimos los resultados
print("--- Billetes ---")
print(f"$50   × {b50}")
print(f"$20   × {b20}")
print(f"$10   × {b10}")
print(f"$5    × {b5}")
print(f"$1    × {b1}")

print("--- Monedas ---")
print(f"$0.25 × {m25}")
print(f"$0.10 × {m10}")
print(f"$0.05 × {m5}")
print(f"$0.01 × {m1}")












#================================================
#
#================================================




















#================================================
#
#================================================











#_______1) Lee un número de 3 cifras y muestra la suma de sus dígitos. Ejemplo: 435 → 4+3+5 = 12.
#--------ENTENDER EL PROBLEMA--------
#----Entrada:
#numero (input)
#----Proceso:
#centenas = numero // 100
#resto = numero % 100
#decenas = resto // 10
#unidades = resto % 10
#suma = centenas + decenas + unidades
#----Salida:
#la suma de los tres dígitos del número
#----Ejemplo de entrada:
#numero = 435
#----Salida esperada:
#4 + 3 + 5 = 12

#--------BOSQUEJO A MANO------------
#numero = 435
#centenas = 435 // 100 = 4
#resto = 435 % 100 = 35
#decenas = 35 // 10 = 3
#unidades = 35 % 10 = 5
#suma = 4 + 3 + 5 = 12

#--------DESCUBRIR EL PATRÓN-----------
#El patrón consiste en separar el número en centenas, decenas y unidades usando división entera y módulo, para después sumar los tres dígitos.

#--------ESCRIBIR EL CÓDIGO-----------
numero=int(input("ingrese numero:"))
centenas=numero//100
resto=numero%100
decenas=resto//10
unidades=resto%10
suma=centenas+decenas+unidades
print(suma)

#--------PRUEBA DE ESCRITORIO---------

#Usando numero = 435

# Línea                            | numero | centenas | resto | decenas | unidades | suma | Pantalla |
# -------------------------------- | ------ | -------- | ----- | ------- | -------- | ---- | -------- |
# input                            | 435    | —        | —     | —       | —        | —    | 435      |
# centenas = numero//100           | 435    | 4        | —     | —       | —        | —    | —        |
#resto = numero%100               | 435    | 4        | 35    | —       | —        | —    | —        |
#decenas = resto//10              | 435    | 4        | 35    | 3       | —        | —    | —        |
#unidades = resto%10              | 435    | 4        | 35    | 3       | 5        | —    | —        |
#suma = centenas+decenas+unidades | 435    | 4        | 35    | 3       | 5        | 12   | —        |
#print(suma)                      | 435    | 4        | 35    | 3       | 5        | 12   | 12       |

#_______2) Lee una cantidad de minutos y muéstrala como «X horas Y minutos». Ejemplo: 135 → «2 horas 15 minutos».

#--------ENTENDER EL PROBLEMA--------
#----Entrada:
#valores (input)
#----Proceso:
#horas = valores // 60
#minutos = valores % 60
#----Salida:
#la cantidad de horas y minutos
#----Ejemplo de entrada:
#valores = 135
#----Salida esperada:
#2 horas 15 minutos

#--------BOSQUEJO A MANO------------
#valores = 135
#horas = 135 // 60 = 2
#minutos = 135 % 60 = 15

#--------DESCUBRIR EL PATRÓN-----------
#El patrón consiste en dividir los minutos para 60 para obtener las horas y usar el módulo de 60 para obtener los minutos restantes.

#--------ESCRIBIR EL CÓDIGO-----------
valores= int(input("ingrese el valor:"))
horas=valores//60
minutos=valores%60
print(f"{horas} horas e {minutos} minutos")

#--------PRUEBA DE ESCRITORIO---------
#Usando valores = 135
# Línea                | valores | horas | minutos | Pantalla             |
# -------------------- | ------- | ----- | ------- | -------------------- |
# input                | 135     | —     | —       | 135                  |
# horas = valores//60  | 135     | 2     | —       | —                    |
# minutos = valores%60 | 135     | 2     | 15      | —                    |
# print                | 135     | 2     | 15      | 2 horas e 15 minutos |


#_______3) Lee peso (kg) y estatura (m) y calcula el IMC. Fórmula: IMC = peso / estatura². Muestra el IMC con 2 decimales.

#--------ENTENDER EL PROBLEMA--------
#----Entrada:
#peso (input)
#estatura (input)
#----Proceso:
#Imc = peso / estatura**2
#----Salida:
#el IMC con 2 decimales
#----Ejemplo de entrada:
#peso = 70
#estatura = 1.75
#----Salida esperada:
#IMC = 22.86

#--------BOSQUEJO A MANO------------
#peso = 70
#estatura = 1.75
#Imc = 70 / 1.75²
#Imc = 70 / 3.0625
#Imc = 22.86

#--------DESCUBRIR EL PATRÓN-----------
#El patrón consiste en dividir el peso para la estatura elevada al cuadrado y mostrar el resultado con dos decimales.

#--------ESCRIBIR EL CÓDIGO-----------
peso=float(input("ingrese el peso:"))
estatura=float(input("ingrese el estatura:"))
Imc=peso/estatura**2
print(f"El IMC es {Imc:.2f}")

#--------PRUEBA DE ESCRITORIO---------
#Usando peso = 70 y estatura = 1.75
# Línea                  | peso | estatura | Imc   | Pantalla        |
# ---------------------- | ---- | -------- | ----- | --------------- |
# input peso             | 70   | —        | —     | 70              |
# input estatura         | 70   | 1.75     | —     | 1.75            |
# Imc = peso/estatura**2 | 70   | 1.75     | 22.86 | —               |
# print                  | 70   | 1.75     | 22.86 | El IMC es 22.86 |


#_______4) Lee un número decimal y una cantidad de decimales, y muéstralo redondeado. Ejemplo: 3.14159 con 2 decimales → 3.14.

#--------ENTENDER EL PROBLEMA--------
#----Entrada:
#numero_decimal (input)
#cantidad_decimales (input)
#----Proceso:
#resultado = round(numero_decimal, cantidad_decimales)
#----Salida:
#el número redondeado con la cantidad de decimales indicada
#----Ejemplo de entrada:
#numero_decimal = 3.14159
#cantidad_decimales = 2
#----Salida esperada:
#3.14

#--------BOSQUEJO A MANO------------
#numero_decimal = 3.14159
#cantidad_decimales = 2
#resultado = round(3.14159, 2)
#resultado = 3.14

#--------DESCUBRIR EL PATRÓN-----------
#El patrón consiste en utilizar la función round() para redondear el número según la cantidad de decimales indicada.

#--------ESCRIBIR EL CÓDIGO-----------
numero_decimal=float(input("ingrese el numero decimal:"))
cantidad_decimales=int(input("Ingrese la cantidad de decimales:"))
resultado=round(numero_decimal, cantidad_decimales)
print(resultado)

#--------PRUEBA DE ESCRITORIO---------
#Usando numero_decimal = 3.14159 y cantidad_decimales = 2
# Línea                                                 | numero_decimal | cantidad_decimales | resultado | Pantalla |
# ----------------------------------------------------- | -------------- | ------------------ | --------- | -------- |
# input                                                 | 3.14159        | —                  | —         | 3.14159  |
# input                                                 | 3.14159        | 2                  | —         | 2        |
# resultado = round(numero_decimal, cantidad_decimales) | 3.14159        | 2                  | 3.14      | —        |
# print                                                 | 3.14159        | 2                  | 3.14      | 3.14     |


#_______5) Un producto vale $12. Si compras 10 o más te dan 15% de descuento, si compras entre 5 y 9 te dan 5%. Calcula el total.

#--------ENTENDER EL PROBLEMA--------
#----Entrada:
#cantidad (input)
#----Proceso:
#Si cantidad >= 10, el descuento es 15%.
#Si cantidad está entre 5 y 9, el descuento es 5%.
#Si cantidad es menor que 5, no hay descuento.
#subtotal_pagar = cantidad × 12
#total_pagar = subtotal_pagar - (subtotal_pagar × descuento)
#----Salida:
#el descuento y el total a pagar
#----Ejemplo de entrada:
#cantidad = 10
#----Salida esperada:
#Descuento: 15%
#Total: $102.00

#--------BOSQUEJO A MANO------------
#cantidad = 10
#PRECIO = 12
#descuento = 15% = 0.15
#subtotal_pagar = 10 × 12 = 120
#total_pagar = 120 - (120 × 0.15)
#total_pagar = 102

#--------DESCUBRIR EL PATRÓN-----------
#El patrón consiste en determinar el descuento según la cantidad de productos, calcular el subtotal y restar el descuento para obtener el total.

#--------ESCRIBIR EL CÓDIGO-----------PRECIO=12
cantidad=int(input("Ingrese la cantidad de productos"))
PRECIO=12
if cantidad>=10:
    descuento=0.15
elif cantidad>=5 and cantidad<=9:
    descuento=0.05
else:
    descuento=0
subtotal_pagar= cantidad*PRECIO
total_pagar=subtotal_pagar-(subtotal_pagar*descuento)
print(f"El descuento es: {descuento}")
print(f"El total es: {total_pagar:.2f}")

#--------PRUEBA DE ESCRITORIO---------
#Usando cantidad = 10
# Línea                                                     | PRECIO | cantidad | descuento | subtotal_pagar | total_pagar | Pantalla              |
# --------------------------------------------------------- | ------ | -------- | --------- | -------------- | ----------- | --------------------- |
# `PRECIO = 12`                                             | 12     | —        | —         | —              | —           | —                     |
# `input`                                                   | 12     | 10       | —         | —              | —           | 10                    |
# `if cantidad >= 10`                                       | 12     | 10       | 0.15      | —              | —           | —                     |
# `subtotal_pagar = cantidad*PRECIO`                        | 12     | 10       | 0.15      | 120            | —           | —                     |
# `total_pagar = subtotal_pagar-(subtotal_pagar*descuento)` | 12     | 10       | 0.15      | 120            | 102         | —                     |
# `print`                                                   | 12     | 10       | 0.15      | 120            | 102         | El descuento es: 0.15 |
# `print`                                                   | 12     | 10       | 0.15      | 120            | 102         | El total es: 102.00   |
