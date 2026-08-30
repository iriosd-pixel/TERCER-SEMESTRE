#________1) Pide una temperatura en grados Celsius y muéstrala en Fahrenheit. Fórmula: F = C × 9/5 + 32.

#--------ENTENDER EL PROBLEMA--------
#----Entrada:
#temperatura (input)
#----Proceso:
#grados_fahrenheit= (temperatura*9/5)+32
#----Salida:
#temperatura en grados fahrenheit

#-------- BOSQUEJO A MANO------------
#temperatura: 30
#grados farenheit= (30*9/5)+32

#--------DESCUBRIR EL PATRON-----------
#En este caso no hay patron asi que, solo toca pedir la temperatura y esos datos se reemplazan en la formula

#--------ESCRIBIR EL CODIGO-----------
temperatura= float(input("Ingrese la temperatura:"))
grados_fahrenheit= (temperatura*9/5)+32
print(f"La temperatura en grados fahrenheit es: {grados_fahrenheit}")

#--------PRUBA DE ESCRITORIO---------
#linea         temperatura              pantalla
#input:          30
#print           30                         86.0


#_________2) Pide un total de segundos y muéstralos como hh:mm:ss. Ej.: 3725 segundos → 1:02:05.
#--------ENTENDER EL PROBLEMA--------
#----Entrada:
#segundos (input)
#----Proceso:
#horas= segundos//3600
#resto= segundos%3600
#minutos= resto//60
#segundos=resto%60
#----Salida:
#3725 segundos → 1:02:05

#-------- BOSQUEJO A MANO------------
#segundo: 6000
#horas= 6000//3600
#resto= 6000%3600
#minutos= resto//60
#segundos=resto%60

#--------DESCUBRIR EL PATRON-----------
#el patron en este caso es que los segundos deben de dividirse para 3600, que es el total de segundos de una hora, de eso debe de sacarse el resto, osea los segundos que sobren y ese resto debe de dividirse para 60 para sacar los minutosy y luego sacar el mod de 60 para calcular el total de segundos

#--------ESCRIBIR EL CODIGO-----------
segundos= int(input("Ingrese la segundos:"))
horas= segundos//3600
resto= segundos%3600
minutos= resto//60
segundos=resto%60
print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")

#--------PRUEBA DE ESCRITORIO--------
# Línea                    | segundos | horas | resto | minutos | Pantalla
# ------------------------ | -------: | ----: | ----: | ------: | --------
# `input`                  |     6000 |     — |     — |       — | 6000
# `resto = segundos%3600`  |     6000 |     1 |  2400 |       — | —
# `minutos = resto//60`    |     6000 |     1 |  2400 |      40 | —
# `segundos = resto%60`    |        0 |     1 |  2400 |      40 | —
# `print`                  |        0 |     1 |  2400 |      40 | 01:40:00

#________3) Lee dos números y muéstralos intercambiados. Python permite hacerlo en una sola línea, muy diferente a JS
#--------ENTENDER EL PROBLEMA--------
#----Entrada:
#dos numeross (input)
#----Proceso:
#a, b = b, a
#----Salida:
#a = {a}, b = {b}

#-------- BOSQUEJO A MANO------------
#a:5
#b:8
#5,8=8,5
#a=8: b=5

#--------DESCUBRIR EL PATRON-----------
#En este caso usamos el intercambio pythonico que consiste que python intercambia las variables en una sola linea de manera automatica

#--------ESCRIBIR EL CODIGO-----------
a= int(input("a: "))
b= int(input("b: "))
a,b= b,a
print(f"a:{a}, b:{b}")

#----PRUEBA DE ESCRITORIO--------
# Línea        |  a |  b | Pantalla |
# ------------ | -: | -: | -------- |
# `input` de a |  5 |  — | 5        |
# `input` de b |  5 |  8 | 8        |
# `a,b = b,a`  |  8 |  5 | —        |
# `print`      |  8 |  5 | a:8, b:5 |


#_______4) Lee el precio de un producto sin IVA y muestra el IVA (15%) y el total.
#--------ENTENDER EL PROBLEMA--------
#----Entrada:
#subtotal a pagar(input)
#----Proceso:
#iva=subtotal*0.15
#total=subtotal+iva
#----Salida:
#total a pagar

#-------- BOSQUEJO A MANO------------
#precio = 80
#iva = 80 × 0.15 = 12
#total = 80 + 12 = 92l

#--------DESCUBRIR EL PATRON-----------
#aqui lo que debemos de hacer es multiplicar el valor del producto por 0.15 que es el IVA en Ecuador y eso lo presentamos, luego debemos de sumar ese iva mas el subtotal de la compra

#--------ESCRIBIR EL CODIGO-----------
precio=float(input("Ingrese el precio:"))
IVA=0.15
subtotal=precio*IVA
total=precio+subtotal
print(f"el IVA de la compra es: {subtotal}")
print(f"el total de la compra es: {total:.2f}")
#-------PRUEBA DE ESCRITORIO---------
# Línea                   | precio |  IVA | subtotal | total | Pantalla     |
# ----------------------- | -----: | ---: | -------: | ----: | ------------ |
# `input`                 |     80 | 0.15 |        — |     — | 80           |
# `subtotal=precio*IVA`   |     80 | 0.15 |     12.0 |     — | —            |
# `total=precio+subtotal` |     80 | 0.15 |     12.0 |  92.0 | —            |
# `print`                 |     80 | 0.15 |     12.0 |  92.0 | IVA: 12.0    |
# `print`                 |     80 | 0.15 |     12.0 |  92.0 | Total: 92.00 |
