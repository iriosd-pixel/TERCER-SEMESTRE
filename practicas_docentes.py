
# ==========================================
# 31/08/2026
# 1. Búcles simples y búsqueda con break
# ==========================================

# Contar del 0 al 4
for i in range(5):  # Genera (0, 1, 2, 3, 4)
    print(i)

enc = "n"
for i in range(2, 8):
    if i == 4:
        enc = "s"
        break
    print(i)

if enc == "s":
    print("Se encontró el valor buscado")
else:
    print("No se encontró el valor buscado")


# ==========================================
# 2. Recorrer listas (Buscar Mayor y Menor)
# ==========================================

notas = [8, 6, 10, 7, 9]
may = notas[0]
men = notas[0]

for nota in notas:
    if nota > may:
        may = nota
    if nota < men:
        men = nota

print(f"mayor: {may}, menor: {men}")


# ==========================================
# 3. Recorrer con índice (enumerate)
# ==========================================

acu = 0
cont = 0

for i, nota in enumerate(notas):
    if i % 2 == 0:  # Evalúa índices pares (0, 2, 4...)
        acu = acu + nota
        cont = cont + 1
        print(f"[{i}] {nota}")

# Promedio/Suma evadiendo división por cero si cont fuera 0
promedio = acu / cont if cont > 0 else 0
print(f"Suma de notas en índices pares: {promedio}")


# ==========================================
# 4. Recorrer cadenas de texto
# ==========================================

#           012345 (posiciones)
cv = 0  # Contador de vocales
ca = 0  # Contador de letras del alfabeto
vocales = "aeiouAEIOU"

for letra in "DAniel":
    # Opción A: Verificación rápida usando 'in'
    if letra in vocales:
        cv += 1
        print(f"Vocal encontrada: {letra}")

    # Verificación de rango de caracteres alfabéticos
    if ("A" <= letra <= "Z") or ("a" <= letra <= "z"):
        ca += 1

    # Opción B: Comparación tradicional usando operadores 'or'
    if (
        letra == "A"
        or letra == "a"
        or letra == "E"
        or letra == "e"
        or letra == "I"
        or letra == "i"
        or letra == "O"
        or letra == "o"
        or letra == "U"
        or letra == "u"
    ):
        cv = cv + 1