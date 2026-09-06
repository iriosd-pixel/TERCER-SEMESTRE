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
def contar_primos(n):
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


#CAMBIO
#Escribe es_narcisista(n): retorna True si el número es igual a la suma de sus
# dígitos elevados al número de dígitos. Ej.: 153 = 1³+5³+3³.
def es_narcisita(n):
    numero=abs(n)
    exponente= len(str(numero))
    suma_numeros=0
    temp= numero
    while temp > 0:
        digito=temp%10          # último dígito
        suma_numeros += digito ** exponente
        temp = temp // 10                # quita el último dígito
    if numero == 0:
        return True
    return suma_numeros==numero

num = int(input("Ingrese una cifra numérica: "))
if es_narcisita(num):
    print(f"El numero {num} es narcicista")
else:
    print(f"El numero {num} no es narcicista")
n=int(input("Ingrese una cifra numerica"))
