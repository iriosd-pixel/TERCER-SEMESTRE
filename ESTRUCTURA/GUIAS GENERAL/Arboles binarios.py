# ================================================================
# ÁRBOLES BINARIOS DE BÚSQUEDA — GUÍA, TALLER Y PROPUESTOS
# ================================================================
# Código de explicación de la guía. Un BST guarda menores a la
# izquierda y mayores a la derecha; no inserta duplicados.

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None


class ArbolBST:
    def __init__(self):
        self.raiz = None

    # ---------- INSERTAR ----------
    def insertar(self, valor):
        self.raiz = self._insertar_rec(self.raiz, valor)

    def _insertar_rec(self, nodo, valor):
        # Caso base: espacio vacío → creamos el nodo
        if nodo is None:
            return NodoArbol(valor)
        # Recursión: bajamos por izquierda o derecha
        if valor < nodo.valor:
            nodo.izq = self._insertar_rec(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self._insertar_rec(nodo.der, valor)
        # Si valor == nodo.valor, no hacemos nada (no duplicados)
        return nodo

    # ---------- BUSCAR ----------
    def buscar(self, valor):
        return self._buscar_rec(self.raiz, valor)

    def _buscar_rec(self, nodo, valor):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        if valor < nodo.valor:
            return self._buscar_rec(nodo.izq, valor)
        return self._buscar_rec(nodo.der, valor)

    # ---------- RECORRIDOS ----------
    def inorden(self):
        """izq → nodo → der  (ordenado)"""
        r = []
        self._inorden_rec(self.raiz, r)
        return r

    def _inorden_rec(self, nodo, r):
        if nodo:
            self._inorden_rec(nodo.izq, r)      # 1. izq
            r.append(nodo.valor)                # 2. nodo
            self._inorden_rec(nodo.der, r)      # 3. der

    def preorden(self):
        """nodo → izq → der  (raíz primero)"""
        r = []
        self._preorden_rec(self.raiz, r)
        return r

    def _preorden_rec(self, nodo, r):
        if nodo:
            r.append(nodo.valor)
            self._preorden_rec(nodo.izq, r)
            self._preorden_rec(nodo.der, r)

    def postorden(self):
        """izq → der → nodo  (raíz al final)"""
        r = []
        self._postorden_rec(self.raiz, r)
        return r

    def _postorden_rec(self, nodo, r):
        if nodo:
            self._postorden_rec(nodo.izq, r)
            self._postorden_rec(nodo.der, r)
            r.append(nodo.valor)

    # ---------- UTILIDADES ----------
    def altura(self):
        return self._altura_rec(self.raiz)

    def _altura_rec(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self._altura_rec(nodo.izq),
                       self._altura_rec(nodo.der))


# --- Uso ---
arbol = ArbolBST()
for v in [50, 30, 70, 20, 40, 60, 80]:
    arbol.insertar(v)

print(arbol.inorden())          # [20, 30, 40, 50, 60, 70, 80] ← ordenado
print(arbol.preorden())         # [50, 30, 20, 40, 70, 60, 80]
print(arbol.postorden())        # [20, 40, 30, 60, 80, 70, 50]
print(arbol.buscar(40))         # True
print(arbol.buscar(35))         # False
print(f"Altura: {arbol.altura()}")   # 3

# ================================================================
# TALLER — Ejercicio 1: BST para gestión de vuelos por ID
# Crear un BST con siete vuelos y buscar un ID.
# ================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: IDs de vuelos
# Proceso: insertar con la regla del BST
# Salida: resultado de búsquedas
# Ejemplo de entrada (guía): vuelos con IDs 50, 30, 70, ...
# Salida esperada (guía): buscar(40): True

#-------- 2. BOSQUEJO A MANO ------------
# Insertar 50 → raíz
# Insertar 30 → 30<50 → izq de 50
# Insertar 70 → 70>50 → der de 50
# Insertar 20 → 20<50 → izq → 20<30 → izq de 30
# Insertar 40 → 40<50 → izq → 40>30 → der de 30
# ...
#
# Buscar 40:
#   50: 40<50 → izq
#   30: 40>30 → der
#   40: ¡encontrado! ✓

#-------- 3. DESCUBRIR EL PATRÓN --------
# Cada comparación descarta una rama. El inorden ordena los IDs.

#-------- 4. ESCRIBIR EL CÓDIGO ---------

class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None


class ArbolBST:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self._insertar_rec(self.raiz, valor)

    def _insertar_rec(self, nodo, valor):
        if nodo is None:
            return NodoArbol(valor)
        if valor < nodo.valor:
            nodo.izq = self._insertar_rec(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self._insertar_rec(nodo.der, valor)
        return nodo

    def buscar(self, valor):
        return self._buscar_rec(self.raiz, valor)

    def _buscar_rec(self, nodo, valor):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        if valor < nodo.valor:
            return self._buscar_rec(nodo.izq, valor)
        return self._buscar_rec(nodo.der, valor)

    def inorden(self):
        r = []
        self._inorden_rec(self.raiz, r)
        return r

    def _inorden_rec(self, nodo, r):
        if nodo:
            self._inorden_rec(nodo.izq, r)
            r.append(nodo.valor)
            self._inorden_rec(nodo.der, r)


# --- Uso ---
vuelos = ArbolBST()
for v in [50, 30, 70, 20, 40, 60, 80]:
    vuelos.insertar(v)

print("Vuelos ordenados:", vuelos.inorden())
# [20, 30, 40, 50, 60, 70, 80]

for buscado in [40, 35, 80]:
    r = vuelos.buscar(buscado)
    print(f"Vuelo {buscado}: {'encontrado ✓' if r else 'no existe'}")

#-------- 5. PRUEBA DE ESCRITORIO -------
# Insertando | Recorrido                    | Ubicación
# 50         | —                            | raíz
# 30         | 50 → izquierda               | izq de 50
# 70         | 50 → derecha                 | der de 50
# 20         | 50 → izquierda → 30 → izq    | izq de 30
# 40         | 50 → izquierda → 30 → der    | der de 30

#CAMBIO
# Añade rango(a, b): retornar los IDs entre a y b aprovechando inorden.
class ArbolBSTConRango(ArbolBST):
    def rango(self, a, b):
        return [id_vuelo for id_vuelo in self.inorden() if a <= id_vuelo <= b]


vuelos_con_rango = ArbolBSTConRango()
for id_vuelo in [50, 30, 70, 20, 40, 60, 80]:
    vuelos_con_rango.insertar(id_vuelo)
print("Vuelos entre 30 y 60:", vuelos_con_rango.rango(30, 60))
# [30, 40, 50, 60]

# ================================================================
# TALLER — Ejercicio 2: Los tres recorridos
# Mostrar inorden, preorden y postorden del árbol del ejemplo.
# ================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: el árbol del ejemplo
# Proceso: recorrer con las tres reglas
# Salida: las tres listas de valores
# Ejemplo de entrada (guía): árbol con raíz=1, izq=2, der=3
# Salida esperada (guía): inorden [2,1,3], preorden [1,2,3], postorden [2,3,1]

#-------- 2. BOSQUEJO A MANO ------------
# Árbol:
#        1
#       / \
#      2   3
#     / \
#    4   5
#
# Inorden  (izq-nodo-der):   4, 2, 5, 1, 3
# Preorden (nodo-izq-der):   1, 2, 4, 5, 3
# Postorden (izq-der-nodo):  4, 5, 2, 3, 1

#-------- 3. DESCUBRIR EL PATRÓN --------
# La recursión es la misma: solo cambia cuándo se añade el nodo.
# Inorden: en medio; preorden: antes; postorden: después.

#-------- 4. ESCRIBIR EL CÓDIGO ---------

class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None


def inorden(nodo, r):
    """izq → NODO → der"""
    if nodo:
        inorden(nodo.izq, r)
        r.append(nodo.valor)
        inorden(nodo.der, r)

def preorden(nodo, r):
    """NODO → izq → der"""
    if nodo:
        r.append(nodo.valor)
        preorden(nodo.izq, r)
        preorden(nodo.der, r)

def postorden(nodo, r):
    """izq → der → NODO"""
    if nodo:
        postorden(nodo.izq, r)
        postorden(nodo.der, r)
        r.append(nodo.valor)


# Construyo el árbol del ejemplo:
#        1
#       / \
#      2   3
#     / \
#    4   5
raiz = NodoArbol(1)
raiz.izq = NodoArbol(2)
raiz.der = NodoArbol(3)
raiz.izq.izq = NodoArbol(4)
raiz.izq.der = NodoArbol(5)

resultado = []
inorden(raiz, resultado)
print("inorden:", resultado)               # [4, 2, 5, 1, 3]

resultado = []
preorden(raiz, resultado)
print("preorden:", resultado)              # [1, 2, 4, 5, 3]

resultado = []
postorden(raiz, resultado)
print("postorden:", resultado)             # [4, 5, 2, 3, 1]

#-------- 5. PRUEBA DE ESCRITORIO -------
# Recorrido | Primer paso             | Resultado
# Inorden   | bajar 1 → 2 → 4        | [4, 2, 5, 1, 3]
# Preorden  | visitar 1 antes de bajar| [1, 2, 4, 5, 3]
# Postorden | visitar 1 al terminar   | [4, 5, 2, 3, 1]

#CAMBIO
# Implementa recorrido por niveles (BFS) con una deque.
from collections import deque

def por_niveles(raiz):
    if raiz is None:
        return []
    cola = deque([raiz])
    resultado = []
    while cola:
        nodo = cola.popleft()
        resultado.append(nodo.valor)
        if nodo.izq is not None:
            cola.append(nodo.izq)
        if nodo.der is not None:
            cola.append(nodo.der)
    return resultado


print("Por niveles:", por_niveles(raiz))  # [1, 2, 3, 4, 5]
print("Árbol vacío:", por_niveles(None))  # []

# ================================================================
# EJERCICIOS PROPUESTOS
# Cada solución está separada y usa el árbol creado en la guía.
# ================================================================
#=======================================================================
# 1) P1 — Contar nodos del árbol
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: un árbol con cero o más nodos.
# Proceso: sumar 1 por cada nodo y contar ambas ramas.
# Salida: número total de nodos.

# Ejemplo de entrada (guía): árbol con 7 nodos
# Salida esperada (guía): 7

#-------- 2. BOSQUEJO A MANO ------------
# Árbol con 50, 30, 70, 20, 40, 60 y 80: 7 nodos.
# Subárbol izquierdo: 3; raíz: 1; subárbol derecho: 3.
# Primero, cada hoja (20, 40, 60 y 80) aporta 1.
# Luego, 30 aporta 1 + 1 + 1 = 3 y 70 también aporta 3.
# Finalmente, 50 aporta 1 + 3 + 3 = 7.

#-------- 3. DESCUBRIR EL PATRÓN --------
# Nodo vacío aporta 0; cualquier otro aporta 1 + izq + der.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
def contar(arbol):
    return _contar_rec(arbol.raiz)


def _contar_rec(nodo):
    if nodo is None:
        return 0
    return 1 + _contar_rec(nodo.izq) + _contar_rec(nodo.der)


arbol_p1 = ArbolBST()
for valor in [50, 30, 70, 20, 40, 60, 80]:
    arbol_p1.insertar(valor)
print("P1 — nodos:", contar(arbol_p1))  # 7

#-------- 5. PRUEBA DE ESCRITORIO -------
# Subárbol       | Nodos
# Izquierdo de 50| 3
# Derecho de 50  | 3
# Total          | 1 + 3 + 3 = 7


#=======================================================================
# 2) P2 — Mínimo y máximo
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: un BST, posiblemente vacío.
# Proceso: seguir la rama izquierda o derecha hasta el extremo.
# Salida: mínimo y máximo, o None si el árbol está vacío.

# Ejemplo de entrada (guía): BST con 50, 30, 70, 20, 40, 60, 80
# Salida esperada (guía): min=20, max=80

#-------- 2. BOSQUEJO A MANO ------------
# Desde 50: 50 → 30 → 20 es el mínimo.
# Desde 50: 50 → 70 → 80 es el máximo.
# En 20 no hay hijo izquierdo; en 80 no hay hijo derecho: allí se detienen
# los dos recorridos. Si la raíz es None, ambos resultados son None.

#-------- 3. DESCUBRIR EL PATRÓN --------
# La regla del BST coloca el menor a la izquierda y el mayor a la derecha.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
def minimo(arbol):
    if not arbol.raiz:
        return None
    nodo = arbol.raiz
    while nodo.izq:
        nodo = nodo.izq
    return nodo.valor


def maximo(arbol):
    if not arbol.raiz:
        return None
    nodo = arbol.raiz
    while nodo.der:
        nodo = nodo.der
    return nodo.valor


arbol_p2 = ArbolBST()
for valor in [50, 30, 70, 20, 40, 60, 80]:
    arbol_p2.insertar(valor)
print("P2 — min/max:", minimo(arbol_p2), maximo(arbol_p2))  # 20 80

#-------- 5. PRUEBA DE ESCRITORIO -------
# Operación | Recorrido      | Resultado
# minimo()  | 50 → 30 → 20 | 20
# maximo()  | 50 → 70 → 80 | 80


#=======================================================================
# 3) P3 — ¿Es un BST válido?
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: un árbol que puede incumplir la regla BST.
# Proceso: obtener inorden y comprobar orden estrictamente creciente.
# Salida: True o False.

# Ejemplo de entrada (guía): árbol correcto
# Salida esperada (guía): True

#-------- 2. BOSQUEJO A MANO ------------
# [20, 30, 40, 50, 60, 70, 80] está ordenado → True.
# Si una rama tiene un valor fuera de lugar, la secuencia no crece → False.
# Comparo 20 < 30, 30 < 40 y así hasta 70 < 80.
# Si el 60 se reemplaza por 40, al comparar 50 < 40 se detecta el error.
# Una secuencia vacía o de un solo valor no tiene pares fuera de orden.

#-------- 3. DESCUBRIR EL PATRÓN --------
# En un BST sin duplicados, inorden produce valores en orden estricto.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
def es_bst_valido(arbol):
    valores = arbol.inorden()
    for i in range(1, len(valores)):
        if valores[i] <= valores[i-1]:
            return False
    return True


arbol_p3 = ArbolBST()
for valor in [50, 30, 70, 20, 40, 60, 80]:
    arbol_p3.insertar(valor)
print("P3 — BST válido:", es_bst_valido(arbol_p3))  # True

#-------- 5. PRUEBA DE ESCRITORIO -------
# Árbol    | Inorden                         | Resultado
# Válido   | [20, 30, 40, 50, 60, 70, 80]    | True
# Alterado | [20, 30, 40, 50, 60, 40, 80]    | False


#=======================================================================
# 4) P4 — Altura del árbol
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: un árbol con uno o más niveles, o vacío.
# Proceso: contar el camino más largo desde la raíz a una hoja.
# Salida: cantidad máxima de niveles.

# Ejemplo de entrada (guía): árbol de la imagen
# Salida esperada (guía): 3

#-------- 2. BOSQUEJO A MANO ------------
# En el ejemplo: nivel 1 = 50; nivel 2 = 30/70;
# nivel 3 = 20/40/60/80. Altura = 3.
# Las hojas tienen altura 1. Los nodos 30 y 70 tienen altura 2.
# La raíz calcula 1 + max(2, 2) = 3. Para un árbol vacío resulta 0.

#-------- 3. DESCUBRIR EL PATRÓN --------
# Un nodo vacío tiene altura 0; otro tiene 1 + máximo de sus hijos.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
def altura_propuesta(arbol):
    return _altura_rec_propuesta(arbol.raiz)


def _altura_rec_propuesta(nodo):
    if nodo is None:
        return 0
    return 1 + max(_altura_rec_propuesta(nodo.izq),
                   _altura_rec_propuesta(nodo.der))


arbol_p4 = ArbolBST()
for valor in [50, 30, 70, 20, 40, 60, 80]:
    arbol_p4.insertar(valor)
print("P4 — altura:", altura_propuesta(arbol_p4))  # 3

#-------- 5. PRUEBA DE ESCRITORIO -------
# Árbol                   | Altura
# Vacío                   | 0
# Solo raíz               | 1
# Siete nodos del ejemplo | 3
