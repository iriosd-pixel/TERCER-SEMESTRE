class Estudiante:
    def __init__(self, nombre, cedula, carrera):
        self.nombre= nombre
        self.cedula=cedula
        self.carrera=carrera
        
    def __str__(self):
        return f"nombre:{self.nombre} carrera:{self.carrera}"
    
    def  __repr__(self):
        return f"nombre:{self.nombre} carrera:{self.carrera}"
    
class MiPila:
    def __init__(self):
        self._datos = []                       # arreglo interno

    def push(self, valor):
        """Añade al tope- como añadir"""
        self._datos.append(valor)

    def __repr__(self):
        return self.__str__()

    def pop(self):
        """Saca y retorna el ultimo elemnto como eliminar"""
        if self.esta_vacia():
            raise IndexError("Pila vacía")
        return self._datos.pop()

    def peek(self):
        """Muestra el ultimo elemnto pero sin sacarlo, con codigo manual"""
        if self.esta_vacia():
            raise IndexError("Pila vacía")
        return self._datos[-1]                 # el último es el tope

    def esta_vacia(self):
        return len(self._datos) == 0

    def tamano(self):
        return len(self._datos)

    def __str__(self):
        # Mostramos de arriba a abajo (tope primero)
        elementos = " → ".join(str(x) for x in reversed(self._datos))
        return f"tope [{elementos}]"




# --- Uso ---
pila1 = MiPila()
pila1.push("30")
pila1.push("10")
pila1.push("15")

print(pila1)

pila2= MiPila()
pila2.push("Ana")
pila2.push("Dan")
pila2.push("Isma")

print(pila2)

pila3 = MiPila()

estu = Estudiante("Ana", "0942343435", "software")
pila3.push(estu)

pila3.push(Estudiante("Dan", "0952456435", "software"))

print(pila3)

print(pila1.peek())                             # 15 (no lo saca)
print(pila1.pop())                              # 15 (lo saca)
print(pila1.pop())                              # 10
print(pila1)   

print(pila3.peek())                             # Dan (no lo saca)
print(pila3.pop())                              # Dan (lo saca)
print(pila3.pop())                              # Ana
try:
    print(pila3.pop())
except IndexError:
    print("e")
print(pila3)                                    # tope []


# Opción 1: list como pila
pila = []
pila.append("acción 1")               # push
pila.append("acción 2")
ultimo = pila.pop()                   # pop → "acción 2"
tope = pila[-1] if pila else None     # peek

# Opción 2: deque (más eficiente para pilas grandes)
from collections import deque
pila = deque()
pila.append("a")                      # push
pila.append("b")
pila.pop()                            # pop → "b"



#===================================================0AQUI EMPIEZA=====================================

#=======================================================================
# TALLER — 3 ejercicios paso a paso
# 1) Usar una pila para invertir una cadena de texto.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: una cadena
# Proceso: empujar cada letra a la pila, luego desapilar hasta vaciarla
# Salida: la cadena al revés
# Ejemplo de entrada (guía): s = "Python"
# Salida esperada (guía): nohtyP

#-------- 2. BOSQUEJO A MANO ------------
# s = "Python"
#
# Push cada letra:
#   push('P') → [P]
#   push('y') → [P, y]
#   ...
#   push('n') → [P, y, t, h, o, n]  (tope=n)
#
# Pop y concatenar:
#   pop() = n → "n"
#   pop() = o → "no"
#   ...
#   resultado: "nohtyP" ✓

#-------- 3. DESCUBRIR EL PATRÓN --------
# Una pila permite invertir el orden porque el último elemento agregado
# es el primero que sale.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
from collections import deque

def invertir_con_pila(s):
    pila = deque()
    # Fase 1: apilar todas las letras
    for letra in s:
        pila.append(letra)
    # Fase 2: desapilar formando la salida
    resultado = ""
    while pila:
        resultado += pila.pop()
    return resultado


print(invertir_con_pila("Python"))    # nohtyP
print(invertir_con_pila("Hola"))      # aloH

# Comparación con la versión pythonic
print("Python"[::-1])                 # nohtyP (una línea)

#-------- 5. PRUEBA DE ESCRITORIO -------
# Acción             | Elementos en la pila | Resultado
# ------------------ | -------------------- | ---------
# Invertir "Sol"     | S, o, l              | loS
# Invertir "Python"  | P, y, t, h, o, n     | nohtyP

#CAMBIO
# Adaptarlo para invertir solo palabras (no caracteres): "Hola Mundo" → "Mundo Hola".
# Separamos las palabras con split(" "), las apilamos y luego las sacamos.
def invertir_palabras_taller(s):
    pila = deque()
    for palabra in s.split(" "):
        pila.append(palabra)

    palabras_invertidas = []
    while pila:
        palabras_invertidas.append(pila.pop())
    return " ".join(palabras_invertidas)

print(invertir_palabras_taller("Hola Mundo"))  # Mundo Hola

#=======================================================================
# 2) Dada una expresión con paréntesis, corchetes y llaves, verificar que estén correctamente balanceados y anidados.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: una cadena con símbolos
# Proceso: usar una pila: apilar aperturas, al cerrar comprobar match
# Salida: True si está balanceado, False si no
# Ejemplo de entrada (guía): s = "({[]})"
# Salida esperada (guía): True

#-------- 2. BOSQUEJO A MANO ------------
# "({[]})"
#
# ( → push  → pila: [(]
# { → push  → pila: [(, {]
# [ → push  → pila: [(, {, []
# ] → pop [ → match ✓ → pila: [(, {]
# } → pop { → match ✓ → pila: [(]
# ) → pop ( → match ✓ → pila: []
#
# Pila vacía al final → balanceado ✓
#
# Ejemplo malo: "({[)]}"
# [ → push, ) → pop [ → NO match → False

#-------- 3. DESCUBRIR EL PATRÓN --------
# Guardamos cada símbolo de apertura en la pila.
# Cuando encontramos un cierre, comprobamos que coincida con el tope.
# Al final, la pila debe quedar vacía.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
from collections import deque

def paren_balanceado(s):
    pila = deque()
    parejas = {")": "(", "]": "[", "}": "{"}   # cierre → apertura

    for ch in s:
        if ch in "([{":
            pila.append(ch)
        elif ch in ")]}":
            if not pila or pila.pop() != parejas[ch]:
                return False
    return len(pila) == 0


# Pruebas
tests = ["()", "({[]})", "()[]{}", "(]", "({[)]}", "((("]
for t in tests:
    print(f"{t!r:15} → {paren_balanceado(t)}")

#-------- 5. PRUEBA DE ESCRITORIO -------
# Expresión | Revisión                     | Resultado
# --------- | ---------------------------- | ---------
# "()"      | apertura y cierre coinciden | True
# "(]"      | los símbolos no coinciden   | False
# "((("     | quedan aperturas abiertas   | False

#CAMBIO
# Amplíalo para reportar la posición del error cuando no está balanceado.
# Esta versión se deja aparte para que se note el cambio.
def paren_balanceado_con_error(s):
    pila = deque()
    parejas = {")": "(", "]": "[", "}": "{"}

    for posicion, ch in enumerate(s, start=1):
        if ch in "([{":
            pila.append((ch, posicion))
        elif ch in ")]}":
            if not pila:
                return False, posicion
            apertura, _ = pila.pop()
            if apertura != parejas[ch]:
                return False, posicion

    if pila:
        return False, pila[-1][1]
    return True, None

for t in ["()", "(]", "((("]:
    balanceado, posicion_error = paren_balanceado_con_error(t)
    if balanceado:
        print(f"{t!r:5} → Balanceada")
    else:
        print(f"{t!r:5} → Error en posición {posicion_error}")


#=======================================================================
# 3) Convertir un número decimal a binario usando el algoritmo de divisiones sucesivas por 2. Los residuos se apilan y al final se leen al revés (desapilando).
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: un entero positivo
# Proceso: dividir sucesivamente entre 2, apilar residuos, luego desapilar
# Salida: el número en binario
# Ejemplo de entrada (guía): n = 13
# Salida esperada (guía): 1101

#-------- 2. BOSQUEJO A MANO ------------
# 13 / 2 = 6, sobra 1 → push 1  pila: [1]
#  6 / 2 = 3, sobra 0 → push 0  pila: [1, 0]
#  3 / 2 = 1, sobra 1 → push 1  pila: [1, 0, 1]
#  1 / 2 = 0, sobra 1 → push 1  pila: [1, 0, 1, 1]
#
# Ahora desapilo: 1, 1, 0, 1 → "1101" ✓

#-------- 3. DESCUBRIR EL PATRÓN --------
# Al convertir a binario, los residuos salen en orden inverso,
# por eso usamos una pila.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
from collections import deque

def decimal_a_binario(n):
    if n == 0:
        return "0"

    pila = deque()
    while n > 0:
        residuo = n % 2
        pila.append(residuo)
        n = n // 2

    # Desapilar y armar el resultado
    binario = ""
    while pila:
        binario += str(pila.pop())
    return binario


# Pruebas
for n in [0, 1, 5, 13, 100, 255]:
    print(f"{n:4d} → {decimal_a_binario(n)}")

# Verificar con la nativa
print(bin(13))          # 0b1101

#-------- 5. PRUEBA DE ESCRITORIO -------
# Operación                 | Entrada | Resultado
# ------------------------- | ------- | ---------
# Decimal a binario         | 13      | 1101

#CAMBIO
# Al revés: convertir una cadena binaria a decimal.
def binario_a_decimal(s):
    decimal = 0
    for digito in s:
        if digito not in "01":
            raise ValueError("El número debe contener solo 0 y 1")
        decimal = decimal * 2 + int(digito)
    return decimal

print(binario_a_decimal("1101"))  # 13

# Prueba del cambio:
# "1101" = (1 × 8) + (1 × 4) + (0 × 2) + (1 × 1) = 13
# Binario a decimal         | "1101"  | 13

#=======================================================================
# EJERCICIOS PROPUESTOS
#=======================================================================
#=======================================================================
# 1) Programa que use una pila para historial: opciones «Hacer acción», «Deshacer», «Ver historial».
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: una opción del menú y la descripción de una acción.
# Proceso: guardar cada acción, quitar la última al deshacer
#          y mostrar las acciones que aún quedan.
# Salida: mostrar qué se hizo, deshizo o qué hay en el historial.

# Ejemplo de entrada (guía): hacer A, hacer B, deshacer
# Salida esperada (guía): Historial: [A]

#-------- 2. BOSQUEJO A MANO ------------
# Hacer "Escribir": historial [Escribir].
# Hacer "Guardar": historial [Escribir, Guardar].
# Deshacer: se quita Guardar y queda [Escribir].

#-------- 3. DESCUBRIR EL PATRÓN --------
# Las acciones se guardan en una pila.
# La última acción agregada es la primera que se deshace.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
from collections import deque

historial = deque()

while True:
    print("\n1.Hacer 2.Deshacer 3.Ver historial 4.Salir")
    op = input("Opción: ")

    if op == "1":
        accion = input("Descripción: ")
        historial.append(accion)
        print(f"Hecho: {accion}")

    elif op == "2":
        if not historial:
            print("Nada que deshacer")
        else:
            deshecha = historial.pop()
            print(f"Deshecho: {deshecha}")

    elif op == "3":
        if not historial:
            print("(vacío)")
        else:
            for i, a in enumerate(historial):
                print(f"  {i+1}. {a}")

    elif op == "4":
        break

#-------- 5. PRUEBA DE ESCRITORIO -------
# Opción      | Acción            | Historial
# ----------- | ----------------- | -----------------------
# Hacer       | Escribir          | [Escribir]
# Hacer       | Guardar            | [Escribir, Guardar]
# Deshacer    | quita Guardar      | [Escribir]
# Ver historial| muestra acciones | [Escribir]

#=======================================================================
# 2) Usar una pila para invertir el ORDEN de las palabras (no las letras).
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: una frase con varias palabras.
# Proceso: apilar cada palabra y sacarlas en orden inverso.
# Salida: mostrar las mismas palabras, pero de atrás hacia adelante.

# Ejemplo de entrada (guía): s = "Hola Mundo desde Python"
# Salida esperada (guía): Python desde Mundo Hola

#-------- 2. BOSQUEJO A MANO ------------
# Frase: "Hola Mundo desde Python"
# Al desapilar las palabras: Python, desde, Mundo, Hola.
# Resultado: "Python desde Mundo Hola".

#-------- 3. DESCUBRIR EL PATRÓN --------
# Separamos la frase en palabras, no en letras.
# La pila cambia el orden porque el último elemento sale primero.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
from collections import deque

def invertir_palabras(frase):
    pila = deque()
    for palabra in frase.split():
        pila.append(palabra)

    resultado = []
    while pila:
        resultado.append(pila.pop())
    return " ".join(resultado)


print(invertir_palabras("Hola Mundo desde Python"))
# Python desde Mundo Hola

#-------- 5. PRUEBA DE ESCRITORIO -------
# Acción          | Palabra agregada/sacada | Resultado parcial
# --------------- | ----------------------- | ---------------------------
# Apilar          | Hola                    | pila: [Hola]
# Apilar          | Mundo                   | pila: [Hola, Mundo]
# Desapilar       | Mundo                   | Mundo
# Desapilar       | Hola                    | Mundo Hola

#=======================================================================
# 3) Verificar si una palabra es palíndromo (se lee igual al derecho y al revés): «reconocer», «ana».
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: una palabra o frase.
# Proceso: comparar sus letras de izquierda a derecha y de derecha a izquierda.
# Salida: indicar si se lee igual en ambos sentidos.

# Ejemplo de entrada (guía): s = "reconocer"
# Salida esperada (guía): Sí, es palíndromo

#-------- 2. BOSQUEJO A MANO ------------
# "ana": al derecho ana, al revés ana -> sí es palíndromo.
# "python": al derecho python, al revés nohtyp -> no es palíndromo.

#-------- 3. DESCUBRIR EL PATRÓN --------
# Quitamos espacios y convertimos el texto a minúsculas.
# Apilamos la mitad izquierda y la comparamos con la mitad derecha.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
from collections import deque

def es_palindromo(s):
    s = s.lower().replace(" ", "")     # normaliza
    pila = deque()

    # Apila la mitad izquierda
    mitad = len(s) // 2
    for i in range(mitad):
        pila.append(s[i])

    # Compara con la mitad derecha (saltando el central si len es impar)
    inicio_der = mitad + (1 if len(s) % 2 == 1 else 0)
    for i in range(inicio_der, len(s)):
        if pila.pop() != s[i]:
            return False
    return True


for p in ["ana", "reconocer", "python", "anita lava la tina"]:
    print(f"{p!r}: {es_palindromo(p)}")

#-------- 5. PRUEBA DE ESCRITORIO -------
# Texto                  | Texto normalizado | Resultado
# ---------------------- | ----------------- | ----------------
# "ana"                  | ana               | Sí es palíndromo
# "reconocer"            | reconocer         | Sí es palíndromo
# "python"               | python            | No es palíndromo
# "anita lava la tina"   | anitalavalatina   | Sí es palíndromo

#=======================================================================
# 4) En notación postfija («polaca inversa»), los operadores van después: 3 4 + = 7. Evalúa una expresión como 3 4 + 5 * = 35.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: una expresión con números y operadores en notación postfija.
# Proceso: apilar los números; cuando aparece un operador,
#          sacar los dos últimos y hacer la operación.
# Salida: mostrar el resultado de la expresión.

# Ejemplo de entrada (guía): "3 4 + 5 *"
# Salida esperada (guía): 35

#-------- 2. BOSQUEJO A MANO ------------
# Expresión: 3 4 + 5 *
# Primero: 3 + 4 = 7.
# Después: 7 × 5 = 35.

#-------- 3. DESCUBRIR EL PATRÓN --------
# Cuando aparece un operador, el primer número que sacamos es b.
# El siguiente que sacamos es a.
# El orden importa en la resta y en la división.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
from collections import deque

def evaluar_postfija(expr):
    pila = deque()
    for token in expr.split():
        if token in "+-*/":
            b = pila.pop()      # OJO al orden: b sale primero
            a = pila.pop()
            if token == "+": pila.append(a + b)
            elif token == "-": pila.append(a - b)
            elif token == "*": pila.append(a * b)
            elif token == "/": pila.append(a / b)
        else:
            pila.append(int(token))
    return pila.pop()


print(evaluar_postfija("3 4 +"))         # 7
print(evaluar_postfija("3 4 + 5 *"))     # 35
print(evaluar_postfija("5 1 2 + 4 * + 3 -"))  # 14

#-------- 5. PRUEBA DE ESCRITORIO -------
# Token | Operación          | Pila
# ----- | ------------------ | --------
# 3     | apilar 3           | [3]
# 4     | apilar 4           | [3, 4]
# +     | 3 + 4 = 7           | [7]
# 5     | apilar 5           | [7, 5]
# *     | 7 × 5 = 35          | [35]
