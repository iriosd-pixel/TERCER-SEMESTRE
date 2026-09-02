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