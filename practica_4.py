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