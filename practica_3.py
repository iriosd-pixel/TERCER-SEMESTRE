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

