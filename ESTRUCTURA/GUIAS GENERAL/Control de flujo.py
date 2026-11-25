#=======================================================================
# EJEMPLOS DE EXPLICACIÓN DE LA GUÍA
# Cada ejemplo se puede ejecutar llamando a su función.
#=======================================================================
# Ejemplo de explicación 1
def ejemplo_explicacion_1():
    nota = int(input("Nota (0-100): "))

    if nota >= 90:
        print("Sobresaliente")     # se ejecuta si nota >= 90
    elif nota >= 70:
        print("Aprobado")           # se ejecuta si nota está entre 70 y 89
    elif nota >= 60:
        print("Recuperación")       # se ejecuta si nota está entre 60 y 69
    else:
        print("Reprobado")          # todos los demás casos

    # La indentación (4 espacios) es OBLIGATORIA
    # Python usa la sangría para saber qué está DENTRO del if
    print("Fin del programa")       # esto se ejecuta SIEMPRE (fuera del if)

# Ejemplo de explicación 2
def ejemplo_explicacion_2():
    edad = 20
    tiene_licencia = True

    # AND: las DOS deben ser verdaderas
    if edad >= 18 and tiene_licencia:
        print("Puede manejar")

    # OR: al menos UNA debe ser verdadera
    if edad < 12 or edad > 65:
        print("Descuento aplicable")

    # NOT: invierte el valor
    if not tiene_licencia:
        print("Debe sacar licencia primero")

    # Rango cómodo (Python permite comparar en cadena)
    if 18 <= edad <= 65:
        print("Edad laboral")

# Ejemplo de explicación 3
def ejemplo_explicacion_3():
    # Contar del 1 al 5
    for i in range(1, 6):
        print(i)

    # Recorrer los elementos de una lista
    notas = [8, 6, 10, 7, 9]
    for nota in notas:
        print(nota)

    # Con índice también
    for i, nota in enumerate(notas):
        print(f"[{i}] {nota}")

    # Recorrer un texto
    for letra in "Python":
        print(letra)

# Ejemplo de explicación 4
def ejemplo_explicacion_4():
    opcion = 0
    while opcion != 3:                        # sigue mientras opcion NO sea 3
        print("1. Saludar")
        print("2. Despedir")
        print("3. Salir")
        opcion = int(input("Opción: "))

        if opcion == 1:
            print("¡Hola!")
        elif opcion == 2:
            print("¡Adiós!")
        elif opcion == 3:
            print("Cerrando programa...")
        else:
            print("Opción inválida")

# Ejemplo de explicación 5
def ejemplo_explicacion_5():
    # BREAK: salir del bucle inmediatamente
    for i in range(100):
        if i == 5:
            break              # el bucle termina aquí
        print(i)               # solo imprime 0, 1, 2, 3, 4

    # CONTINUE: saltar a la siguiente vuelta
    for i in range(10):
        if i % 2 == 0:
            continue           # los pares se saltan
        print(i)               # imprime solo 1, 3, 5, 7, 9

    # Patrón while True + break: repetir hasta que pase algo
    while True:
        nombre = input("Nombre (o 'fin' para terminar): ")
        if nombre == "fin":
            break
        print(f"Hola, {nombre}")

#=======================================================================
#EJEMPLOS PUESTOS POR LA IA MAS CAMBIOS
#=======================================================================
#=======================================================================
# TALLER — 6 ejercicios paso a paso
# 1) Leer un número N y mostrar los números del 1 al N.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: n (entero)
# Proceso: recorrer desde 1 hasta N con un for
# Salida: los N números uno por línea
# Ejemplo de entrada (guía): n = 5
# Salida esperada (guía): 1 2 3 4 5

#-------- 2. BOSQUEJO A MANO ------------
# n = 5
#
# for i in range(1, 6):   # 1, 2, 3, 4, 5
#     print(i)

#-------- 3. DESCUBRIR EL PATRÓN --------
# Tabla de decisión del range: Si quiero contar del 1 al N, uso range(1, N+1). El segundo número es exclusivo: range(1, 6) da 1, 2, 3, 4, 5, no llega a 6. El error clásico es escribir range(1, N): te falta el último número.

#-------- 4. ESCRIBIR EL CÓDIGO ---------

n = int(input("N: "))

for i in range(1, n + 1):      # ¡ojo con el n+1!
    print(i)
#-------- 5. PRUEBA DE ESCRITORIO -------
# i | Pantalla
# 1 | 1
# 2 | 1 2
# 3 | 1 2 3
# 4 | 1 2 3 4
# 5 | 1 2 3 4 5 ✓


#CAMBIO
#Cámbialo para que muestre del N al 1 (hacia atrás). Pista: range(n, 0, -1).
n = int(input("N: "))

for i in range(n, 0, -1):
    print(i)

#=======================================================================
# 2) Leer N y calcular la suma de 1 + 2 + 3 + ... + N.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: n (entero)
# Proceso: acumular en una variable con un bucle
# Salida: la suma total
# Ejemplo de entrada (guía): n = 5
# Salida esperada (guía): Suma: 15 (1+2+3+4+5)

#-------- 2. BOSQUEJO A MANO ------------
# n = 5, suma = 0 (INICIALIZACIÓN)
#
# i=1:  suma = 0 + 1 = 1
# i=2:  suma = 1 + 2 = 3
# i=3:  suma = 3 + 3 = 6
# i=4:  suma = 6 + 4 = 10
# i=5:  suma = 10 + 5 = 15   ← resultado

#-------- 3. DESCUBRIR EL PATRÓN --------
# Aquí aparece el patrón acumulador: una variable (suma) que se va aumentando dentro del bucle. La regla de oro del acumulador: inicializarlo en 0 si vas a sumar, en 1 si vas a multiplicar. Y siempre fuera del bucle, porque si lo pones dentro, en cada vuelta lo reseteas. Curiosidad: Python tiene sum(range(1, n+1)) que hace lo mismo en una línea. Pero como estamos aprendiendo, usamos el bucle explícito.

#-------- 4. ESCRIBIR EL CÓDIGO ---------

n = int(input("N: "))
suma = 0                    # INICIALIZACIÓN del acumulador

for i in range(1, n + 1):
    suma = suma + i         # equivale a: suma += i

print(f"Suma: {suma}")
#-------- 5. PRUEBA DE ESCRITORIO -------
# i | suma antes | suma después
# 1 | 0 | 1
# 2 | 1 | 3
# 3 | 3 | 6
# 4 | 6 | 10
# 5 | 10 | 15 ✓


#CAMBIO
#Adaptarlo para calcular la suma de los pares del 2 al 100. Pista: range(2, 101, 2).
suma = 0                    # INICIALIZACIÓN del acumulador

for i in range(2, 101, 2):
    suma = suma + i         # equivale a: suma += i

print(f"Suma: {suma}")

#=======================================================================
# 3) Leer N y calcular el factorial (N! = 1 × 2 × 3 × ... × N). Ejemplo: 5! = 120.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: n (entero)
# Proceso: acumulador multiplicativo
# Salida: el factorial
# Ejemplo de entrada (guía): n = 5
# Salida esperada (guía): 5! = 120

#-------- 2. BOSQUEJO A MANO ------------
# n = 5, fact = 1 (INICIALIZACIÓN)
#
# i=1:  fact = 1 * 1 = 1
# i=2:  fact = 1 * 2 = 2
# i=3:  fact = 2 * 3 = 6
# i=4:  fact = 6 * 4 = 24
# i=5:  fact = 24 * 5 = 120   ← resultado

#-------- 3. DESCUBRIR EL PATRÓN --------
# Mismo patrón que el ejercicio anterior, pero multiplicativo. Lo que cambia es la inicialización: si empiezas en 0, todo el resultado será 0 (porque cualquier cosa × 0 = 0). Empezar en 1 es la clave. Regla: elemento neutro — 0 para la suma (n + 0 = n), 1 para la multiplicación (n × 1 = n).

#-------- 4. ESCRIBIR EL CÓDIGO ---------

n = int(input("N: "))
fact = 1                    # INICIALIZACIÓN: 1 porque vamos a multiplicar

for i in range(1, n + 1):
    fact = fact * i         # o: fact *= i

print(f"{n}! = {fact}")
#-------- 5. PRUEBA DE ESCRITORIO -------
# i | fact
# antes | 1
# 1 | 1
# 2 | 2
# 3 | 6
# 4 | 24
# 5 | 120 ✓


#CAMBIO
# Probar también 100! sin pedir otra entrada.
fact_100 = 1
for i in range(1, 101):
    fact_100 *= i
print(f"100! = {fact_100}")

#=======================================================================
# 4) Leer las notas de N estudiantes (una por una) y contar cuántos aprobaron (nota ≥ 7 sobre 10).
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: n (cantidad) y n notas
# Proceso: recorrer con for y contar con un contador
# Salida: cuántos tienen nota ≥ 7 (escala de 0 a 10)
# Ejemplo de entrada (guía): n = 4, notas = 8, 5, 9, 6
# Salida esperada (guía): Aprobados: 2 de 4

#-------- 2. BOSQUEJO A MANO ------------
# n = 4, aprobados = 0 (INICIALIZACIÓN)
#
# nota=8 → 8 >= 7 → aprobados = 1
# nota=5 → 5 >= 7 → NO cambia
# nota=9 → 9 >= 7 → aprobados = 2
# nota=6 → 6 >= 7 → NO cambia
#
# resultado: 2 aprobados

#-------- 3. DESCUBRIR EL PATRÓN --------
# Aquí aparece el patrón contador: como el acumulador, pero solo suma 1 cuando pasa algo. Se combina con un if dentro del bucle. Fíjate que hay dos bucles imaginarios juntos: (1) uno que lee las N notas, (2) dentro del cuerpo, un if que decide si aumentar el contador.

#-------- 4. ESCRIBIR EL CÓDIGO ---------

n = int(input("¿Cuántos estudiantes? "))
aprobados = 0                       # contador arranca en 0

for i in range(n):
    nota = float(input(f"Nota {i+1}: "))
    if nota >= 7:                   # el 7 es el umbral (o 70 si es sobre 100)
        aprobados += 1              # aumenta solo si aprobó

print(f"Aprobados: {aprobados} de {n}")
#-------- 5. PRUEBA DE ESCRITORIO -------
# i | nota | aprobados
# antes | — | 0
# 0 | 8 | 1
# 1 | 5 | 1
# 2 | 9 | 2
# 3 | 6 | 2 ✓


#CAMBIO
#Añade un contador para reprobados y muestra el porcentaje de aprobación.
n = int(input("¿Cuántos estudiantes? "))
aprobados = 0                       # contador arranca en 0
reprobados = 0
for i in range(n):
    nota = float(input(f"Nota {i+1}: "))
    if nota >= 7:                   # el 7 es el umbral (o 70 si es sobre 100)
        aprobados += 1             # aumenta solo si aprobó
    else:
        reprobados += 1
print(f"Aprobados: {aprobados} de {n}")
print(f"Reprobados: {reprobados} de {n}")
porcentaje_aprobacion = aprobados / n * 100 if n else 0
print(f"Porcentaje de aprobación: {porcentaje_aprobacion:.1f}%")

#=======================================================================
# 5) Leer las notas de N estudiantes y mostrar la nota más alta.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: n y las n notas
# Proceso: guardar la nota más alta encontrada hasta ahora, actualizarla si aparece una mayor
# Salida: la nota más alta
# Ejemplo de entrada (guía): n = 5, notas = 6, 9, 4, 8, 10
# Salida esperada (guía): Máxima: 10

#-------- 2. BOSQUEJO A MANO ------------
# nota máxima = -infinito (o = primera nota)
#
# leo 6  → 6 > -inf → máx = 6
# leo 9  → 9 > 6   → máx = 9
# leo 4  → 4 > 9   → NO cambia
# leo 8  → 8 > 9   → NO cambia
# leo 10 → 10 > 9  → máx = 10
#
# resultado: 10

#-------- 3. DESCUBRIR EL PATRÓN --------
# Patrón campeón (o mayor). Guardas la mejor nota vista hasta ese momento y la actualizas cuando aparece una mayor. El problema es cómo inicializar. Dos opciones: • Con la primera nota leída (mejor): el bucle empieza en el segundo dato.• Con un valor imposible (float negativo infinito): el bucle empieza en el primero. Aquí usamos la segunda porque queda más limpia con range(n).

#-------- 4. ESCRIBIR EL CÓDIGO ---------

n = int(input("¿Cuántas notas? "))
maxima = float("-inf")              # valor imposible: nada será menor

for i in range(n):
    nota = float(input(f"Nota {i+1}: "))
    if nota > maxima:               # ¿es mayor que el récord?
        maxima = nota               # sí → actualizamos

print(f"Máxima: {maxima}")
#-------- 5. PRUEBA DE ESCRITORIO -------
# i | nota | máxima antes | máxima después
# 0 | 6 | -inf | 6
# 1 | 9 | 6 | 9
# 2 | 4 | 9 | 9
# 3 | 8 | 9 | 9
# 4 | 10 | 9 | 10 ✓


#CAMBIO
#Adaptarlo para encontrar la menor nota. Cambio: float("inf") y if nota < minima:.
n = int(input("¿Cuántas notas? "))
minima = float("inf")              # valor imposible: nada será menor

for i in range(n):
    nota = float(input(f"Nota {i+1}: "))
    if nota < minima:               # ¿es menor que el récord?
        minima = nota               # sí → actualizamos

print(f"Mínima: {minima}")


#=======================================================================
# 6) Leer un número y determinar si es primo (solo divisible entre 1 y él mismo).
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: n (entero)
# Proceso: probar divisores de 2 hasta √n usando bandera
# Salida: "n es primo" o "n no es primo"
# Ejemplo de entrada (guía): n = 17
# Salida esperada (guía): 17 es primo

#-------- 2. BOSQUEJO A MANO ------------
# n = 17, es_primo = True (bandera)
#
# Pruebo divisores del 2 al √17 ≈ 4:
#   17 % 2 = 1 (no divide)
#   17 % 3 = 2 (no divide)
#   17 % 4 = 1 (no divide)
#
# Ninguno dividió → 17 es primo ✓

#-------- 3. DESCUBRIR EL PATRÓN --------
# Aquí usamos el patrón bandera: una variable booleana que empieza en True y cambia a False apenas se descarta. Optimización clave: solo hace falta probar hasta √n, no hasta n. Si n tiene un divisor mayor que √n, forzosamente tiene otro menor que ya habríamos encontrado. Un caso especial: 0 y 1 no son primos. Se descarta al inicio.

#-------- 4. ESCRIBIR EL CÓDIGO ---------

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
#-------- 5. PRUEBA DE ESCRITORIO -------
# n | i probado | n % i | es_primo
# 17 | 2 | 1 | True
# 17 | 3 | 2 | True
# 17 | 4 | 1 | True
# 17 | fin bucle | — | True → primo ✓


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





#=======================================================================
# EJERCICIOS PROPUESTOS
#=======================================================================
#=======================================================================
# 1) Lee un número N y muestra su tabla de multiplicar (del 1 al 12).
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
#----Entrada:
#numero (input)
#----Proceso:
#multiplicar el numero por cada valor del 1 al 12
#----Salida:
#tabla de multiplicar del numero

# Ejemplo de entrada (guía): n = 7
# Salida esperada (guía): 7 × 1 = 7 7 × 2 = 14 ... 7 × 12 = 84

#-------- 2. BOSQUEJO A MANO ------------
#numero: 5
#5 × 1 = 5
#5 × 2 = 10
#5 × 3 = 15
#...
#5 × 12 = 60

#-------- 3. DESCUBRIR EL PATRÓN --------
#El patrón consiste en repetir la multiplicación del número
#por los valores del 1 al 12.
#Para eso usamos un ciclo for que va aumentando de uno en uno.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
numero= int(input("Ingrese un numero: "))
for i in range(1, 13):
    print(f"{numero} x {i} = {numero*i}")

#-------- 5. PRUEBA DE ESCRITORIO -------
# Línea              | numero | i | numero*i | Pantalla
# ------------------ | -----: | -: | -------: | --------
# input              |      5 | — |        — | 5
# for                |      5 | 1 |        5 | —
# print              |      5 | 2 |       10 | 5 x 2 = 10
# print              |      5 | 3 |       15 | 5 x 3 = 15
# ...                |      5 | — |        — | ...
# print              |      5 |12 |       60 | 5 x 12 = 60

#=======================================================================
# 2) Lee un número y cuenta cuántos dígitos tiene (sin convertir a string).
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
#----Entrada:
#numero (input)
#----Proceso:
#dividir el numero entre 10 hasta que llegue a 0
#contar cada división realizada
#----Salida:
#cantidad de dígitos del numero

# Ejemplo de entrada (guía): num = 12345
# Salida esperada (guía): 5 dígitos

#-------- 2. BOSQUEJO A MANO ------------
#numero: 4356
#
#4356 // 10 = 435
#435 // 10 = 43
#43 // 10 = 4
#4 // 10 = 0
#
#contador = 4

#-------- 3. DESCUBRIR EL PATRÓN --------
#El patrón consiste en dividir el número entre 10 usando //.
#Cada división elimina un dígito del número.
#Por cada división aumentamos el contador en 1.
#Cuando el número llega a 0, ya contamos todos sus dígitos.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
valores= abs(int(input("Ingrese una cifra numérica: ")))
contador=0
if valores==0:
    contador= 1
else:
    while valores>0:
        contador=contador+1
        valores=valores//10
print(f"En la cifra hay {contador} numeros")

#-------- 5. PRUEBA DE ESCRITORIO -------
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

#=======================================================================
# 3) Lee N números y muestra la suma de los pares y la suma de los impares por separado.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
#----Entrada:
#cantidad de numeros
#los numeros que vamos a ingresar
#----Proceso:
#comprobar si cada numero es par o impar
#sumar los pares en una variable y los impares en otra
#----Salida:
#suma de los pares y suma de los impares

# Ejemplo de entrada (guía): n = 5, nums = 4 7 2 9 6
# Salida esperada (guía): Suma pares: 12 Suma impares: 16

#-------- 2. BOSQUEJO A MANO ------------
#cantidad: 5
#numeros: 2, 5, 4, 7, 6
#
#pares: 2 + 4 + 6 = 12
#impares: 5 + 7 = 12

#-------- 3. DESCUBRIR EL PATRÓN --------
#El patrón consiste en revisar cada número usando % 2.
#Si el resto es 0, el número es par.
#Si el resto es diferente de 0, es impar.
#Después sumamos cada número en su respectiva variable.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
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

#-------- 5. PRUEBA DE ESCRITORIO -------
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

#=======================================================================
# 4) Pide una edad y valida que esté entre 0 y 120. Si el usuario ingresa algo inválido, vuelve a pedirla.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
#----Entrada:
#edad (input)
#----Proceso:
#comprobar que la edad esté entre 0 y 120
#si no está dentro del rango, volver a pedirla
#----Salida:
#edad válida

# Ejemplo de entrada (guía): edad = -5 → repite edad = 150 → repite edad = 25 → OK
# Salida esperada (guía): Edad válida: 25

#-------- 2. BOSQUEJO A MANO ------------
#edad: 150
#150 está entre 0 y 120? NO
#volver a pedir
#
#edad: 25
#25 está entre 0 y 120? SI
#resultado: edad válida = 25

#-------- 3. DESCUBRIR EL PATRÓN --------
#El patrón consiste en repetir la pregunta mientras
#la edad sea inválida.
#Usamos while True para repetir y break para salir
#cuando encontramos una edad válida.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
while True:
    edad = int(input("Ingrese una edad"))
    if edad >= 0 and edad <= 120:
        break
    print ("Inválida, intenta de nuevo")
print(f"Edad válida: {edad}")

#-------- 5. PRUEBA DE ESCRITORIO -------
# Línea              | edad | Pantalla
# ------------------ | ---: | --------
# input              | 150  | 150
# if                 | 150  | —
# print inválida     | 150  | Inválida, intenta de nuevo
# input              | 25   | 25
# if                 | 25   | —
# break              | 25   | —
# print              | 25   | Edad válida: 25

#=======================================================================
# 5) Genera un número secreto entre 1 y 100. El usuario intenta adivinar.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
#----Entrada:
#numero que intenta adivinar el usuario
#----Proceso:
#comparar el intento con el numero secreto
#decir si debe ingresar un numero mayor o menor
#contar los intentos realizados
#----Salida:
#cantidad de intentos cuando adivine

# Ejemplo de entrada (guía): secreto=42, usuario adivina en 6 intentos
# Salida esperada (guía): ¡Correcto en 6 intentos!

#-------- 2. BOSQUEJO A MANO ------------
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

#-------- 3. DESCUBRIR EL PATRÓN --------
#El patrón consiste en repetir los intentos hasta encontrar
#el número secreto.
#Cada vez que el usuario intenta, aumentamos el contador.
#Si el intento es mayor o menor, damos una pista.
#Cuando es igual al secreto, usamos break para terminar.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
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
        print("Prueba con un número menor")
    else:
        print("Prueba con un número mayor")

#-------- 5. PRUEBA DE ESCRITORIO -------
# Para la prueba suponemos que el numero secreto es 50.
#
# Línea              | secreto | intento | intentos | Pantalla
# ------------------ | -------: | ------: | --------: | --------
# random             |       50 |       — |         0 | —
# input              |       50 |      30 |         1 | 30
# else               |       50 |      30 |         1 | Prueba con un número mayor
# input              |       50 |      70 |         2 | 70
# elif               |       50 |      70 |         2 | Prueba con un número menor
# input              |       50 |      50 |         3 | 50
# if                 |       50 |      50 |         3 | Correcto en 3 intentos
# break              |       50 |      50 |         3 | —

#=======================================================================
# 6) Muestra los primeros N números de Fibonacci.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
#----Entrada:
#cantidad de numeros que queremos mostrar
#----Proceso:
#mostrar el numero actual y sumar los dos numeros anteriores
#----Salida:
#los primeros N numeros de Fibonacci

# Ejemplo de entrada (guía): n = 8
# Salida esperada (guía): 0 1 1 2 3 5 8 13

#-------- 2. BOSQUEJO A MANO ------------
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

#-------- 3. DESCUBRIR EL PATRÓN --------
#El patrón consiste en sumar los dos números anteriores
#para obtener el siguiente.
#Después de mostrar un número, cambiamos los valores de a y b
#para continuar con la serie.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
can_numeros= int(input("Ingrese la cantidad de numero que desea saber de la serie de figonashi: "))
a=0
b=1
for i in range(can_numeros):
    print(a, end=" ")
    siguiente= a+b
    a=b
    b=siguiente

#-------- 5. PRUEBA DE ESCRITORIO -------
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
