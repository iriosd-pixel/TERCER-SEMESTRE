#codigo hecho por la ia
class MiLista:
    def __init__(self, capacidad=10):
        # Arreglo interno con espacios reservados (rellenamos con None)
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0             # cuántos elementos hay realmente

    def ingresar(self, valor):
        """Añade al final. Si no hay espacio, avisa."""
        if self.cantidad >= self.capacidad:
            print("Lista llena")
            return
        self.datos[self.cantidad] = valor
        self.cantidad += 1

    def listar(self):
        """Muestra todos los elementos activos."""
        if self.cantidad == 0:
            print("Lista vacía")
            return
        for i in range(self.cantidad):
            print(f"[{i}] {self.datos[i]}")

    def buscar(self, valor):
        """Búsqueda lineal → posición o -1"""
        for i in range(self.cantidad):
            if self.datos[i] == valor:
                return i
        return -1

    def modificar(self, viejo, nuevo):
        """Buscar + reemplazar"""
        pos = self.buscar(viejo)
        if pos == -1:
            print(f"'{viejo}' no encontrado")
            return
        self.datos[pos] = nuevo
        print(f"[{pos}] '{viejo}' → '{nuevo}'")

    def eliminar(self, valor):
        """Buscar + mover todo lo de la derecha una posición a la izquierda"""
        pos = self.buscar(valor)
        if pos == -1:
            print(f"'{valor}' no encontrado")
            return
        for i in range(pos, self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]
        self.datos[self.cantidad - 1] = None
        self.cantidad -= 1
        print(f"'{valor}' eliminado")

    def __len__(self):
        return self.cantidad

    def __str__(self):
        activos = [str(self.datos[i]) for i in range(self.cantidad)]
        return "[" + ", ".join(activos) + "]"


# --- Uso ---
mi = MiLista(capacidad=5)
mi.ingresar("Ana")
mi.ingresar("Beto")
mi.ingresar("Carlos")
mi.listar()                                # [0] Ana / [1] Beto / [2] Carlos
print(mi.buscar("Beto"))                   # 1
mi.modificar("Beto", "Roberto")
mi.eliminar("Ana")
print(mi)                                  # [Roberto, Carlos]
print(f"Total: {len(mi)}")

# Crear
pasajeros = []

# AGREGAR
pasajeros.append("Ana")
pasajeros.append("Carlos")
pasajeros.insert(1, "Beto")     # inserta en posición 1
# → ["Ana", "Beto", "Carlos"]

# LISTAR con índice
for i, p in enumerate(pasajeros):
    print(f"[{i}] {p}")

# BUSCAR
if "Ana" in pasajeros:
    print(f"Ana está en posición {pasajeros.index('Ana')}")

# MODIFICAR
pos = pasajeros.index("Beto")
pasajeros[pos] = "Roberto"

# ELIMINAR
pasajeros.remove("Carlos")       # por valor
pasajeros.pop(0)                 # por posición (retorna el eliminado)

# ORDENAR
pasajeros.sort()                 # alfabético
pasajeros.sort(reverse=True)     # descendente

# TAMAÑO
print(f"Total: {len(pasajeros)}")

# Comprensiones de listas: código de explicación de la guía.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Transformar: elevar al cuadrado
cuadrados = [n**2 for n in numeros]
# → [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Filtrar: solo los pares
pares = [n for n in numeros if n % 2 == 0]
# → [2, 4, 6, 8, 10]

# Combinar: cuadrados de los pares
cuadrados_pares = [n**2 for n in numeros if n % 2 == 0]
# → [4, 16, 36, 64, 100]

# Sobre strings
nombres = ["Ana", "beto", "CARLOS"]
mayus = [n.upper() for n in nombres]
# → ["ANA", "BETO", "CARLOS"]

# Comparación con for tradicional
# ANTES (5 líneas)
pares_v2 = []
for n in numeros:
    if n % 2 == 0:
        pares_v2.append(n)

# AHORA (1 línea)
pares_v3 = [n for n in numeros if n % 2 == 0]



#====================================================AQUI EMPIEZA============================================
#=======================================================================
#=======================================================================
# TALLER — 3 ejercicios paso a paso
# 1) Sistema completo: agregar, listar, buscar por cédula, modificar y eliminar pasajeros. Usa clase Pasajero y una list como contenedor.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: opción del menú y datos
# Proceso: operaciones sobre la lista con validaciones
# Salida: resultado de cada acción
# Ejemplo de entrada (guía): 1) Agregar Ana / 3) Buscar por cédula
# Salida esperada (guía): Agregado ✓ / Ana (0912...)

#-------- 2. BOSQUEJO A MANO ------------
# class Pasajero(nombre, cedula)
#
# lista = []
# menú:
#   1. Agregar    → lista.append(Pasajero(...))
#   2. Listar     → for p in lista: print(p)
#   3. Buscar     → next((p for p in lista if p.cedula==ced), None)
#   4. Modificar  → buscar + p.nombre = nuevo
#   5. Eliminar   → lista[:] = [p for p in lista if p.cedula != ced]
#   6. Salir      → break

#-------- 3. DESCUBRIR EL PATRÓN --------
# La lista guarda objetos Pasajero.
# Para encontrar uno, recorremos la lista y comparamos su cédula.
# Para ordenar por nombre, usamos sort() y tomamos el nombre de cada pasajero.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
class Pasajero:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def __str__(self):
        return f"{self.nombre} ({self.cedula})"


def buscar_por_cedula(lista, ced):
    """Retorna el objeto o None."""
    return next((p for p in lista if p.cedula == ced), None)


# --- Programa principal ---
lista = []

while True:
    print("\n--- MENÚ ---")
    print("1.Agregar 2.Listar 3.Buscar 4.Modificar 5.Eliminar 6.Salir")
    op = input("Opción: ")

    if op == "1":
        nom = input("Nombre: ")
        ced = input("Cédula: ")
        if buscar_por_cedula(lista, ced):
            print("Ya existe un pasajero con esa cédula")
        else:
            lista.append(Pasajero(nom, ced))
            print("Agregado ✓")

    elif op == "2":
        if not lista:
            print("No hay pasajeros")
        for i, p in enumerate(lista):
            print(f"[{i}] {p}")

    elif op == "3":
        ced = input("Cédula: ")
        p = buscar_por_cedula(lista, ced)
        print(p if p else "No existe")

    elif op == "4":
        ced = input("Cédula: ")
        p = buscar_por_cedula(lista, ced)
        if p:
            p.nombre = input("Nuevo nombre: ")
            print("Modificado ✓")
        else:
            print("No existe")

    elif op == "5":
        ced = input("Cédula: ")
        p = buscar_por_cedula(lista, ced)
        if p:
            lista.remove(p)
            print("Eliminado ✓")
        else:
            print("No existe")

    elif op == "6":
        break

#-------- 5. PRUEBA DE ESCRITORIO -------
# Acción | lista
# append Ana | [Ana(1)]
# append Luis | [Ana(1), Luis(2)]
# buscar cédula 2 | encontrado: Luis
# modificar 2 → Roberto | [Ana(1), Roberto(2)]
# remove cédula 1 | [Roberto(2)]

#CAMBIO
# Añade una opción «Ordenar por nombre» que use lista.sort(key=lambda p: p.nombre).
# En el menú, la opción 6 ordena y la opción 7 sale.
# --- Programa principal ---
lista = []

while True:
    print("\n--- MENÚ ---")
    print("1.Agregar 2.Listar 3.Buscar 4.Modificar 5.Eliminar 6.Ordenar 7.Salir")
    op = input("Opción: ")

    if op == "1":
        nom = input("Nombre: ")
        ced = input("Cédula: ")
        if buscar_por_cedula(lista, ced):
            print("Ya existe un pasajero con esa cédula")
        else:
            lista.append(Pasajero(nom, ced))
            print("Agregado ✓")

    elif op == "2":
        if not lista:
            print("No hay pasajeros")
        for i, p in enumerate(lista):
            print(f"[{i}] {p}")

    elif op == "3":
        ced = input("Cédula: ")
        p = buscar_por_cedula(lista, ced)
        print(p if p else "No existe")

    elif op == "4":
        ced = input("Cédula: ")
        p = buscar_por_cedula(lista, ced)
        if p:
            p.nombre = input("Nuevo nombre: ")
            print("Modificado ✓")
        else:
            print("No existe")

    elif op == "5":
        ced = input("Cédula: ")
        p = buscar_por_cedula(lista, ced)
        if p:
            lista.remove(p)
            print("Eliminado ✓")
        else:
            print("No existe")

    elif op == "6":
        lista.sort(key=lambda p: p.nombre)
        print("Lista ordenada por nombre")

    elif op == "7":
        break

# Prueba del cambio — ordenar por nombre
# Acción              | Lista antes       | Resultado
# ------------------- | ----------------- | -----------------------
# Agregar Ana         | []                | [Ana]
# Agregar Beto        | [Ana]             | [Ana, Beto]
# Ordenar por nombre  | [Beto, Ana]       | [Ana, Beto]
# Salir               | cualquiera        | termina el menú

#=======================================================================
# Dada una lista de N notas, calcular: promedio, máxima, mínima, cantidad de aprobados y el nombre del mejor estudiante (paralelo con nombres).
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: N, lista de nombres y lista de notas
# Proceso: recorridos en paralelo para calcular estadísticas
# Salida: todas las métricas
# Ejemplo de entrada (guía): 3 estudiantes: Ana=8, Luis=6, Diana=10
# Salida esperada (guía): Prom: 8.0, Máx: 10 (Diana), Mín: 6, Aprob: 2/3

#-------- 2. BOSQUEJO A MANO ------------
# nombres = ["Ana", "Luis", "Diana"]
# notas   = [ 8,     6,      10 ]
#
# promedio = (8+6+10) / 3 = 8.0
# máxima   = 10 (índice 2 → Diana)
# aprobados = 2 (8>=7, 10>=7)

#-------- 3. DESCUBRIR EL PATRÓN --------
# Los nombres y las notas tienen el mismo orden y se relacionan por índice.
# La desviación estándar mide cuánto se alejan las notas del promedio.
# Primero calculamos el promedio y luego aplicamos la fórmula indicada.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
import math

nombres = ["Ana", "Luis", "Diana", "Beto", "Elena"]
notas   = [ 8,     6,      10,      7,      5]

# Python trae todo esto:
print(f"Promedio: {sum(notas) / len(notas):.2f}")
print(f"Máxima: {max(notas)}")
print(f"Mínima: {min(notas)}")

# Aprobados: filtro + len
aprobados = [n for n in notas if n >= 7]
print(f"Aprobados: {len(aprobados)} de {len(notas)}")

# Mejor estudiante: índice del máximo
idx_max = notas.index(max(notas))
print(f"Mejor: {nombres[idx_max]} con {notas[idx_max]}")

# --- Versión manual (para entender qué hace por dentro) ---
suma = 0
maxima = notas[0]
minima = notas[0]
idx_max_manual = 0
aprob_manual = 0

for i in range(len(notas)):
    suma += notas[i]
    if notas[i] > maxima:
        maxima = notas[i]
        idx_max_manual = i
    if notas[i] < minima:
        minima = notas[i]
    if notas[i] >= 7:
        aprob_manual += 1

print(f"\nManual → prom: {suma/len(notas):.2f}, máx: {maxima}, aprob: {aprob_manual}")

#-------- 5. PRUEBA DE ESCRITORIO -------
# i | notas[i] | suma | máxima | aprobados
# 0 | 8 | 8 | 8 | 1
# 1 | 6 | 14 | 8 | 1
# 2 | 10 | 24 | 10 | 2
# 3 | 7 | 31 | 10 | 3
# 4 | 5 | 36 | 10 | 3

#CAMBIO
# Desviación estándar: raíz cuadrada del promedio de las diferencias al cuadrado.
promedio = sum(notas) / len(notas)
desviacion = math.sqrt(sum((n - promedio) ** 2 for n in notas) / len(notas))

# Python trae todo esto:
print(f"Promedio: {promedio:.2f}")
print(f"Máxima: {max(notas)}")
print(f"Mínima: {min(notas)}")
print(f"Desviación estándar: {desviacion:.2f}")

# Aprobados: filtro + len
aprobados = [n for n in notas if n >= 7]
print(f"Aprobados: {len(aprobados)} de {len(notas)}")

# Mejor estudiante: índice del máximo
idx_max = notas.index(max(notas))
print(f"Mejor: {nombres[idx_max]} con {notas[idx_max]}")

# --- Versión manual (para entender qué hace por dentro) ---
suma = 0
maxima = notas[0]
minima = notas[0]
idx_max_manual = 0
aprob_manual = 0

for i in range(len(notas)):
    suma += notas[i]
    if notas[i] > maxima:
        maxima = notas[i]
        idx_max_manual = i
    if notas[i] < minima:
        minima = notas[i]
    if notas[i] >= 7:
        aprob_manual += 1

print(f"\nManual → prom: {suma/len(notas):.2f}, máx: {maxima}, aprob: {aprob_manual}")

# Prueba del cambio — desviación estándar
# Resultado             | Valor
# --------------------- | -----
# Promedio              | 7.20
# Máxima                | 10
# Mínima                | 5
# Cantidad de aprobados | 3 de 5
# Mejor estudiante     | Diana con 10
# Desviación estándar  | 1.72

#=======================================================================
#Implementar el algoritmo de ordenamiento burbuja sobre una lista. Luego comparar con list.sort().
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: una lista de números desordenada
# Proceso: recorrer varias veces intercambiando pares consecutivos
# Salida: la lista ordenada
# Ejemplo de entrada (guía): [5, 2, 8, 1, 9]
# Salida esperada (guía): [1, 2, 5, 8, 9]

#-------- 2. BOSQUEJO A MANO ------------
# [5, 2, 8, 1, 9]
#
# Vuelta 1:
#   5>2 → swap → [2, 5, 8, 1, 9]
#   5<8 → nada
#   8>1 → swap → [2, 5, 1, 8, 9]
#   8<9 → nada
# Vuelta 2:
#   2<5 → nada
#   5>1 → swap → [2, 1, 5, 8, 9]
#   5<8, 8<9 → nada
# Vuelta 3:
#   2>1 → swap → [1, 2, 5, 8, 9]
#
# Estable ✓

#-------- 3. DESCUBRIR EL PATRÓN --------
# Burbuja compara dos números vecinos.
# Si están en el orden incorrecto, los intercambia.
# Repite las vueltas hasta que la lista quede ordenada.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
def bubble_sort(lista):
    n = len(lista)
    # Copia para no modificar el original
    arr = lista[:]
    for vuelta in range(n - 1):
        # Bandera para optimizar: si en una vuelta no hubo swaps, ya está ordenado
        hubo_swap = False
        for i in range(n - 1 - vuelta):
            if arr[i] > arr[i + 1]:
                # Intercambio en una línea
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                hubo_swap = True
        if not hubo_swap:
            break
    return arr


# --- Uso ---
notas = [5, 2, 8, 1, 9, 3, 7]

# Nuestra versión
ordenada = bubble_sort(notas)
print(ordenada)                            # [1, 2, 3, 5, 7, 8, 9]

# La versión de Python (usa Timsort, mucho más rápido)
copia = notas[:]                           # copia para no romper el original
copia.sort()
print(copia)                               # [1, 2, 3, 5, 7, 8, 9]

# Descendente
copia.sort(reverse=True)
print(copia)                               # [9, 8, 7, 5, 3, 2, 1]

# Ordenar por criterio (ej. por longitud del string)
palabras = ["python", "a", "código", "el"]
palabras.sort(key=len)
print(palabras)                            # ['a', 'el', 'python', 'código']

#-------- 5. PRUEBA DE ESCRITORIO -------
# Vuelta | Estado después de intercambiar vecinos
# Inicial | [5, 2, 8, 1, 9]
# 1      | [2, 5, 1, 8, 9]
# 2      | [2, 1, 5, 8, 9]
# 3      | [1, 2, 5, 8, 9] ✓

#CAMBIO

#Implementa selection sort: en cada vuelta busca el mínimo del resto y lo coloca al inicio.
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: una lista de números desordenados.
# Proceso: buscar el número menor de la parte que aún no está ordenada
#          y colocarlo al inicio de esa parte.
# Salida: devolver una nueva lista ordenada de menor a mayor.

#-------- 2. BOSQUEJO A MANO ------------
# Lista: [5, 2, 4, 1]
# El menor es 1, se coloca al inicio: [1, 2, 4, 5].

#-------- 3. DESCUBRIR EL PATRÓN --------
# En cada vuelta guardamos la posición del menor.
# Al terminar la búsqueda, intercambiamos ese número con el primero pendiente.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
def selection_sort(lista):
    # Hacemos una copia para conservar la lista original.
    arr = lista[:]

    for inicio in range(len(arr) - 1):
        posicion_menor = inicio

        for i in range(inicio + 1, len(arr)):
            if arr[i] < arr[posicion_menor]:
                posicion_menor = i

        arr[inicio], arr[posicion_menor] = arr[posicion_menor], arr[inicio]

    return arr

# --- Uso ---
numeros = [5, 2, 4, 1]
ordenados = selection_sort(numeros)
print(ordenados)                            # [1, 2, 4, 5]
print(numeros)                              # [5, 2, 4, 1], la original no cambia

# Prueba del cambio — selection sort
# Vuelta | Menor encontrado | Lista después de colocar el menor
# ------ | ---------------- | ----------------------------------
# 1      | 1                | [1, 2, 4, 5]
# 2      | 2                | [1, 2, 4, 5]
# 3      | 4                | [1, 2, 4, 5]


#=======================================================================
# EJERCICIOS PROPUESTOS
#=======================================================================
#=======================================================================
# 1) Dada una lista de números y un valor, contar cuántas veces aparece.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: una lista de números y el valor que queremos contar.
# Proceso: revisar cada número y aumentar el contador cuando coincida.
# Salida: mostrar cuántas veces aparece el valor.

# Ejemplo de entrada (guía): lista=[1,3,2,3,4,3], v=3
# Salida esperada (guía): 3 aparece 3 veces

#-------- 2. BOSQUEJO A MANO ------------
# Lista: [1, 3, 2, 3, 4, 3, 5]. Valor: 3.
# Coincidencias: 3, 3, 3. Total: 3 veces.

#-------- 3. DESCUBRIR EL PATRÓN --------
# Empezamos el contador en cero.
# Cada coincidencia suma uno al contador.
# También podemos usar count() para obtener el mismo resultado.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
lista = [1, 3, 2, 3, 4, 3, 5]
v = 3

# Manual
count = 0
for x in lista:
    if x == v:
        count += 1
print(f"{v} aparece {count} veces")

# Pythonic
print(f"{v} aparece {lista.count(v)} veces")

#-------- 5. PRUEBA DE ESCRITORIO -------
# Número revisado | ¿Es igual a 3? | Contador
# --------------- | -------------- | --------
# 1               | No             | 0
# 3               | Sí             | 1
# 2               | No             | 1
# 3               | Sí             | 2
# 4               | No             | 2
# 3               | Sí             | 3
# 5               | No             | 3

#=======================================================================
# 2) Invertir el orden de una lista sin usar lista.reverse().
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: una lista de elementos.
# Proceso: recorrerla desde el último elemento hasta el primero.
# Salida: mostrar una nueva lista en orden inverso.

# Ejemplo de entrada (guía): [1, 2, 3, 4, 5]
# Salida esperada (guía): [5, 4, 3, 2, 1]

#-------- 2. BOSQUEJO A MANO ------------
# Lista original: [1, 2, 3, 4, 5]
# Lista invertida: [5, 4, 3, 2, 1]

#-------- 3. DESCUBRIR EL PATRÓN --------
# Empezamos por el último índice y retrocedemos hasta el índice cero.
# También se puede invertir con slicing o con reversed().

#-------- 4. ESCRIBIR EL CÓDIGO ---------
lista = [1, 2, 3, 4, 5]

# Con bucle
invertida = []
for i in range(len(lista) - 1, -1, -1):
    invertida.append(lista[i])
print(invertida)

# Con slicing (pythonic)
print(lista[::-1])

# Con reversed
print(list(reversed(lista)))

#-------- 5. PRUEBA DE ESCRITORIO -------
# Índice recorrido | Elemento añadido | Lista invertida
# --------------- | ----------------- | -----------------
# 4               | 5                 | [5]
# 3               | 4                 | [5, 4]
# 2               | 3                 | [5, 4, 3]
# 1               | 2                 | [5, 4, 3, 2]
# 0               | 1                 | [5, 4, 3, 2, 1]

#=======================================================================
# 3) Dada una lista con posibles duplicados, retornar una lista sin duplicados manteniendo el orden.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: una lista que puede tener números repetidos.
# Proceso: agregar a una nueva lista solo los números que aún no aparecen.
# Salida: mostrar los valores únicos conservando el orden original.

# Ejemplo de entrada (guía): [1, 3, 2, 3, 4, 1]
# Salida esperada (guía): [1, 3, 2, 4]

#-------- 2. BOSQUEJO A MANO ------------
# Original: [1, 3, 2, 3, 4, 1, 5, 2]
# Sin repetidos y en el mismo orden: [1, 3, 2, 4, 5]

#-------- 3. DESCUBRIR EL PATRÓN --------
# Recorremos la lista original de izquierda a derecha.
# Si el número no está en la lista nueva, lo agregamos.
# set() también quita duplicados, pero no es la opción para conservar el orden.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
nums = [1, 3, 2, 3, 4, 1, 5, 2]

# Manual (mantiene orden)
unicos = []
for x in nums:
    if x not in unicos:
        unicos.append(x)
print(unicos)                       # [1, 3, 2, 4, 5]

# Rápido (NO mantiene orden)
print(list(set(nums)))

# Rápido MANTENIENDO orden (Python 3.7+)
print(list(dict.fromkeys(nums)))    # [1, 3, 2, 4, 5]

#-------- 5. PRUEBA DE ESCRITORIO -------
# Número revisado | ¿Ya está en unicos? | unicos
# --------------- | ------------------- | ----------------
# 1               | No                  | [1]
# 3               | No                  | [1, 3]
# 2               | No                  | [1, 3, 2]
# 3               | Sí                  | [1, 3, 2]
# 4               | No                  | [1, 3, 2, 4]
# 1               | Sí                  | [1, 3, 2, 4]
# 5               | No                  | [1, 3, 2, 4, 5]
# 2               | Sí                  | [1, 3, 2, 4, 5]

#=======================================================================
# 4) Encontrar el segundo número más grande de una lista (sin ordenar toda la lista).
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: una lista de números.
# Proceso: encontrar el mayor y el segundo mayor distinto sin ordenar la lista.
# Salida: mostrar ambos números.

# Ejemplo de entrada (guía): [5, 2, 9, 7, 9, 3]
# Salida esperada (guía): Segundo mayor: 7

#-------- 2. BOSQUEJO A MANO ------------
# Lista: [5, 2, 9, 7, 9, 3, 8]
# Mayor: 9. Segundo mayor distinto: 8.

#-------- 3. DESCUBRIR EL PATRÓN --------
# Guardamos dos valores: el mayor y el segundo mayor.
# Si aparece un nuevo mayor, el mayor anterior pasa a ser el segundo.
# Los números iguales al mayor no cuentan como segundo mayor.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
nums = [5, 2, 9, 7, 9, 3, 8]

# Dos campeones: mayor y segundo
mayor = float("-inf")
segundo = float("-inf")

for n in nums:
    if n > mayor:
        segundo = mayor         # el que era mayor pasa a segundo
        mayor = n
    elif n > segundo and n < mayor:
        segundo = n

print(f"Mayor: {mayor}")
print(f"Segundo: {segundo}")

#-------- 5. PRUEBA DE ESCRITORIO -------
# Número revisado | Mayor | Segundo
# --------------- | ----- | -------
# 5               | 5     | -inf
# 2               | 5     | 2
# 9               | 9     | 5
# 7               | 9     | 7
# 9               | 9     | 7
# 8               | 9     | 8

#=======================================================================
# 5) Dadas dos listas ordenadas, fusionarlas en una tercera también ordenada, sin usar sort().
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: dos listas que ya están ordenadas.
# Proceso: comparar sus elementos y agregar primero el menor.
# Salida: una tercera lista ordenada, sin usar sort().

# Ejemplo de entrada (guía): a=[1,3,5], b=[2,4,6,8]
# Salida esperada (guía): [1, 2, 3, 4, 5, 6, 8]

#-------- 2. BOSQUEJO A MANO ------------
# Lista A: [1, 3, 5]. Lista B: [2, 4, 6].
# Comparando sus elementos, el resultado es [1, 2, 3, 4, 5, 6].

#-------- 3. DESCUBRIR EL PATRÓN --------
# Usamos un índice para cada lista.
# Cada comparación agrega el menor y avanza el índice correspondiente.
# Al final agregamos los elementos que hayan quedado.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
a = [1, 3, 5, 7]
b = [2, 4, 6, 8, 10]

resultado = []
i = j = 0

# Recorremos las dos listas a la par
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        resultado.append(a[i])
        i += 1
    else:
        resultado.append(b[j])
        j += 1

# Añadimos lo que quede de la más larga
resultado.extend(a[i:])
resultado.extend(b[j:])

print(resultado)                    # [1, 2, 3, 4, 5, 6, 7, 8, 10]

#-------- 5. PRUEBA DE ESCRITORIO -------
# Comparación | Elemento agregado | Resultado parcial
# ----------- | ----------------- | -------------------------
# 1 y 2       | 1                 | [1]
# 3 y 2       | 2                 | [1, 2]
# 3 y 4       | 3                 | [1, 2, 3]
# 5 y 4       | 4                 | [1, 2, 3, 4]
# Al terminar | se agrega lo que queda | [1, 2, 3, 4, 5, 6, 7, 8, 10]
