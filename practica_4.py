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