# =====================================================================
#  ejercicios.py  —  OPCIÓN 3 DEL MENÚ: "Listar ejercicios"
# ---------------------------------------------------------------------
#  Aquí van TODOS los ejercicios del módulo 📋 Listas de la guía:
#     • 3 ejercicios DESARROLLADOS (taller paso a paso)  -> T1, T2, T3
#     • 5 ejercicios PROPUESTOS (solución oculta)         -> P1 ... P5
#
#  Cada ejercicio es UNA función sin parámetros que:
#     1) imprime su enunciado corto,
#     2) usa datos fijos de prueba (los indicados en cada función),
#     3) muestra el resultado.
#
#  REGLA: en cada ejercicio resuelve con DOS versiones cuando se indique:
#     ✋ MANUAL (bucles, patrones del módulo 0)  y  🐍 PYTHON (built-ins
#     y comprensiones). Imprime ambas para comparar.
#  Cuando termines una función, BORRA la línea "pass".
# =====================================================================

from lista_python import ListaPasajerosPython
from pasajero import Pasajero


# ============================ DESARROLLADOS ==========================

def ejercicio_t1():
    """
    T1 — CRUD de pasajeros con clase Pasajero + list   (Taller, Medio)
    -----------------------------------------------------------------
    Demuestra (sin menú, con llamadas directas) el CRUD completo usando
    tu clase ListaPasajerosPython:
        añadir 3 pasajeros -> listar -> buscar por cédula -> modificar
        -> eliminar -> listar otra vez -> ordenar por NOMBRE con
        sort(key=lambda p: p.nombre)  (es el reto del taller).
    Importa así:  from lista_python import ListaPasajerosPython from pasajero import Pasajero
    """
    lista = ListaPasajerosPython()
    pasajeros = [
        Pasajero(1, "Carlos", "111", 20, "2026-11-01", "Quito", "1A"),
        Pasajero(2, "Ana", "222", 25, "2026-11-02", "Lima", "2B"),
        Pasajero(3, "Beatriz", "333", 30, "2026-11-03", "Bogotá", "3C"),
    ]

    print("Añadir 3 pasajeros:")
    for pasajero in pasajeros:
        lista.añadir(pasajero)
    lista.listar()

    print("\nBuscar cédula 222:")
    posicion = lista.buscar("222")
    print(lista.pasajeros[posicion] if posicion != -1 else "No encontrado")

    print("\nModificar Ana:")
    lista.modificar("222", "Ana María", 26)
    lista.listar()

    print("\nEliminar cédula 333:")
    lista.eliminar_por_valor("333")
    lista.listar()

    print("\nOrdenar por nombre:")
    lista.pasajeros.sort(key=lambda pasajero: pasajero.nombre)
    lista.listar()


def ejercicio_t2():
    """
    T2 — Estadísticas de una lista de notas   (Taller, Medio)
    -----------------------------------------------------------------
    Datos:  nombres = ["Ana", "Luis", "Diana", "Beto", "Elena"]
            notas   = [ 8,     6,      10,      7,      5  ]
    Muestra: promedio, máxima, mínima, cantidad de aprobados (>= 7)
            y el nombre del mejor estudiante.
    ✋ MANUAL : un solo for con acumulador, campeón y contador.
    🐍 PYTHON : sum, max, min, len, notas.index(max(notas)) y
            aprobados con COMPRENSIÓN: [n for n in notas if n >= 7]
    Salida esperada: Promedio 7.20 · Máx 10 (Diana) · Mín 5 · Aprobados 3 de 5
    """
    nombres = ["Ana", "Luis", "Diana", "Beto", "Elena"]
    notas = [8, 6, 10, 7, 5]

    suma = 0
    aprobados = 0
    campeon = notas[0]
    posicion_campeon = 0
    for i in range(len(notas)):
        suma += notas[i]
        if notas[i] >= 7:
            aprobados += 1
        if notas[i] > campeon:
            campeon = notas[i]
            posicion_campeon = i

    nota_maxima = max(notas)
    aprobados_python = [nota for nota in notas if nota >= 7]

    print("MANUAL")
    print(f"Promedio {suma / len(notas):.2f} · Máx {campeon} ({nombres[posicion_campeon]}) "
          f"· Mín {min(notas)} · Aprobados {aprobados} de {len(notas)}")
    print("PYTHON")
    posicion_maxima = notas.index(nota_maxima)
    print(f"Promedio {sum(notas) / len(notas):.2f} · Máx {nota_maxima} ({nombres[posicion_maxima]}) "
          f"· Mín {min(notas)} · Aprobados {len(aprobados_python)} de {len(notas)}")


def ejercicio_t3():
    """
    T3 — Ordenar una lista (bubble sort)   (Taller, Avanzado)
    -----------------------------------------------------------------
    Datos: [5, 2, 8, 1, 9, 3, 7]
    ✋ MANUAL : burbuja con bandera hubo_swap (sobre una COPIA lista[:]).
    🐍 PYTHON : sorted(lista) y lista.sort(reverse=True).
    Extra    : palabras = ["python", "a", "código", "el"] ordenadas con key=len
    Salida esperada: [1, 2, 3, 5, 7, 8, 9]
    """
    lista = [5, 2, 8, 1, 9, 3, 7]
    ascendente = lista[:]

    for final in range(len(ascendente) - 1, 0, -1):
        hubo_swap = False
        for i in range(final):
            if ascendente[i] > ascendente[i + 1]:
                ascendente[i], ascendente[i + 1] = ascendente[i + 1], ascendente[i]
                hubo_swap = True
        if not hubo_swap:
            break

    descendente = lista[:]
    descendente.sort(reverse=True)
    palabras = ["python", "a", "código", "el"]

    print("MANUAL: Burbuja:", ascendente)
    print("PYTHON: sorted:", sorted(lista))
    print("PYTHON: sort descendente:", descendente)
    print("Extra: palabras por longitud:", sorted(palabras, key=len))


# ============================= PROPUESTOS ============================

def ejercicio_p1():
    """
    P1 — Contar apariciones de un valor
    Datos: lista = [1, 3, 2, 3, 4, 3, 5],  v = 3
    ✋ MANUAL : patrón contador.   🐍 PYTHON : lista.count(v)
    🧩 COMPRENSIÓN: len([x for x in lista if x == v])
    Salida esperada: 3 aparece 3 veces
    """
    lista = [1, 3, 2, 3, 4, 3, 5]
    valor = 3

    contador = 0
    for elemento in lista:
        if elemento == valor:
            contador += 1

    print(f"MANUAL: {valor} aparece {contador} veces")
    print(f"PYTHON: {valor} aparece {lista.count(valor)} veces")
    print(f"COMPRENSIÓN: {valor} aparece "
          f"{len([elemento for elemento in lista if elemento == valor])} veces")


def ejercicio_p2():
    """
    P2 — Invertir una lista SIN lista.reverse()
    Datos: [1, 2, 3, 4, 5]
    ✋ MANUAL : for con range(len(lista)-1, -1, -1) y append.
    🐍 PYTHON : lista[::-1]  y  list(reversed(lista))
    🧩 COMPRENSIÓN: [lista[i] for i in range(len(lista)-1, -1, -1)]
    Salida esperada: [5, 4, 3, 2, 1]
    """
    lista = [1, 2, 3, 4, 5]
    invertida = []

    for i in range(len(lista) - 1, -1, -1):
        invertida.append(lista[i])

    print("MANUAL:", invertida)
    print("PYTHON slicing:", lista[::-1])
    print("PYTHON reversed:", list(reversed(lista)))
    print("COMPRENSIÓN:",
          [lista[i] for i in range(len(lista) - 1, -1, -1)])


def ejercicio_p3():
    """
    P3 — Números únicos manteniendo el orden
    Datos: [1, 3, 2, 3, 4, 1, 5, 2]
    ✋ MANUAL : recorrer y añadir si "not in unicos".
    🐍 PYTHON : list(dict.fromkeys(nums))   (y explica por qué list(set(nums))
            NO garantiza el orden)
    Salida esperada: [1, 3, 2, 4, 5]
    """
    numeros = [1, 3, 2, 3, 4, 1, 5, 2]
    unicos = []

    for numero in numeros:
        if numero not in unicos:
            unicos.append(numero)

    print("MANUAL:", unicos)
    print("PYTHON dict.fromkeys:", list(dict.fromkeys(numeros)))
    print("Nota: list(set(numeros)) no garantiza el orden.")


def ejercicio_p4():
    """
    P4 — Segundo mayor (sin ordenar toda la lista)
    Datos: [5, 2, 9, 7, 9, 3, 8]
    ✋ MANUAL : dos campeones (mayor y segundo) en un solo recorrido.
    🐍 PYTHON (para comprobar): sorted(set(nums))[-2]
    Salida esperada: Mayor 9 · Segundo 8
    """
    numeros = [5, 2, 9, 7, 9, 3, 8]
    mayor = None
    segundo = None

    for numero in numeros:
        if mayor is None or numero > mayor:
            segundo = mayor
            mayor = numero
        elif numero != mayor and (segundo is None or numero > segundo):
            segundo = numero

    print(f"Mayor {mayor} · Segundo {segundo}")
    print(f"Comprobación: sorted(set(numeros))[-2] = {sorted(set(numeros))[-2]}")


def ejercicio_p5():
    """
    P5 — Fusionar dos listas ordenadas (sin sort)
    Datos: a = [1, 3, 5, 7],  b = [2, 4, 6, 8, 10]
    ✋ MANUAL : dos índices i, j comparando cabezas (base del merge sort)
            y al final extend con lo que sobre.
    🐍 PYTHON (para comprobar): sorted(a + b)
    Salida esperada: [1, 2, 3, 4, 5, 6, 7, 8, 10]
    """
    a = [1, 3, 5, 7]
    b = [2, 4, 6, 8, 10]
    fusionada = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            fusionada.append(a[i])
            i += 1
        else:
            fusionada.append(b[j])
            j += 1

    fusionada.extend(a[i:])
    fusionada.extend(b[j:])

    print("MANUAL:", fusionada)
    print("PYTHON:", sorted(a + b))


# ============================== CATÁLOGO =============================
#  (código, título, tipo, función)   ->  tipo: "taller" o "propuesto"
#  ✅ Ya está armado: NO lo cambies, úsalo en menu_ejercicios().
EJERCICIOS = [
    ("T1", "CRUD de pasajeros con clase Pasajero + list", "taller", ejercicio_t1),
    ("T2", "Estadísticas de una lista de notas",          "taller", ejercicio_t2),
    ("T3", "Ordenar una lista (bubble sort)",             "taller", ejercicio_t3),
    ("P1", "Contar apariciones de un valor",              "propuesto", ejercicio_p1),
    ("P2", "Invertir una lista",                          "propuesto", ejercicio_p2),
    ("P3", "Números únicos",                              "propuesto", ejercicio_p3),
    ("P4", "Segundo mayor",                               "propuesto", ejercicio_p4),
    ("P5", "Fusionar dos listas ordenadas",               "propuesto", ejercicio_p5),
]


def menu_ejercicios():
    """
    QUÉ HACE : muestra los ejercicios agrupados y ejecuta el que elija
            el usuario, hasta que escriba 0.
    PASOS    :
    1. Con COMPRENSIONES separa el catálogo:
            taller     = [e for e in EJERCICIOS if e[2] == "taller"]
            propuestos = [e for e in EJERCICIOS if e[2] == "propuesto"]
    2. Muestra:
            --- DESARROLLADOS (taller) ---
            T1. CRUD de pasajeros ...
            --- PROPUESTOS ---
            P1. Contar apariciones ...
            0.  Volver
    3. Lee el código (ej. "t2") y pásalo a mayúsculas con .upper().
    4. Busca la tupla con ese código (otra comprensión o next(...)):
            encontrados = [e for e in EJERCICIOS if e[0] == codigo]
    5. Si existe -> llama a su función:  encontrados[0][3]()
        Si no     -> "Código no válido".
    6. Repite hasta que el usuario escriba "0".
    """
    while True:
        taller = [ejercicio for ejercicio in EJERCICIOS if ejercicio[2] == "taller"]
        propuestos = [ejercicio for ejercicio in EJERCICIOS if ejercicio[2] == "propuesto"]

        print("\n--- DESARROLLADOS (taller) ---")
        for codigo, titulo, _, _ in taller:
            print(f"{codigo}. {titulo}")

        print("--- PROPUESTOS ---")
        for codigo, titulo, _, _ in propuestos:
            print(f"{codigo}. {titulo}")
        print("0. Volver")

        codigo = input("Ejercicio: ").strip().upper()
        if codigo == "0":
            break

        encontrados = [ejercicio for ejercicio in EJERCICIOS if ejercicio[0] == codigo]
        if encontrados:
            print()
            encontrados[0][3]()
        else:
            print("Código no válido")