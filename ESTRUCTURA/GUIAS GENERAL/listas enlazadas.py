class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{str(self.data)} -> {str(self.next)}"

    def __repr__(self):
        return f"Nodo({repr(self.data)}, {repr(self.next)})"
    
# 1. Creo tres vagones sueltos (cada uno con next = None)
a = Nodo("Ana")
b = Nodo("Beto")
c = Nodo("Carlos")

# 2. Los engancho: cada uno apunta al siguiente
a.next = b
b.next = c

# 3. Desde a puedo llegar a todos siguiendo las flechas
print(a.data)                 # Ana
print(a.next.data)            # Beto
print(a.next.next.data)       # Carlos
print(a.next.next.next)       # None

actual=a
while actual is not None:
    print(actual.data)
    actual=actual.next
#para eliminar a beto hago a.next.bext ahi el engncge de b ya no etsa xq hace un salto directamnet e a c
def __str__(self):
        return " → ".join(str(data) for data in self.a_lista()) + " → None"

def __repr__(self):
    return f"ListaEnlazada({repr(self.a_lista())})"

class Nodo:
    """Un vagón: dato + referencia al siguiente."""
    def __init__(self, data):
        self.data = data
        self.next = None


class ListaEnlazada:
    def __init__(self):
        self.head = None                       # el primer nodo (o None)
        self.tamano = 0

    # ---------- INSERTAR ----------
    def insertar_inicio(self, data):
        """O(1) — el nuevo se convierte en head."""
        nuevo = Nodo(data)
        nuevo.next = self.head
        self.head = nuevo
        self.tamano += 1

    def insertar_final(self, data):
        """O(n) — hay que recorrer hasta el último."""
        nuevo = Nodo(data)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:                 # avanza hasta el último
                actual = actual.next
            actual.next = nuevo
        self.tamano += 1

    # ---------- BUSCAR ----------
    def buscar(self, data):
        """Retorna True si existe."""
        actual = self.head
        while actual:
            if actual.data == data:
                return True
            actual = actual.next
        return False

    # ---------- ELIMINAR ----------
    def eliminar(self, data):
        """Elimina el primer nodo con ese dato."""
        if not self.head:
            return False

        # Caso especial: es el primero
        if self.head.data == data:
            self.head = self.head.next
            self.tamano -= 1
            return True

        # Buscamos el nodo ANTERIOR al que hay que borrar
        actual = self.head
        while actual.next and actual.next.data != data:
            actual = actual.next

        if not actual.next:
            return False                       # no encontrado

        # Saltamos el nodo: actual.next.next lo desconecta
        actual.next = actual.next.next
        self.tamano -= 1
        return True

    # ---------- RECORRIDO ----------
    def listar(self):
        actual = self.head
        while actual:
            print(actual.data, end=" → ")
            actual = actual.next
        print("None")

    def a_lista(self):
        """Convierte a list de Python (útil para debug)."""
        resultado = []
        actual = self.head
        while actual:
            resultado.append(actual.data)
            actual = actual.next
        return resultado

    def __len__(self):
        return self.tamano

    def __str__(self):
        return " → ".join(str(x) for x in self.a_lista()) + " → None"


# --- Uso ---
lista = ListaEnlazada()
lista.insertar_final("Ana")
lista.insertar_final("Carlos")
lista.insertar_final("Diana")
lista.insertar_inicio("VIP-Beto")
print(lista)                                   # VIP-Beto → Ana → Carlos → Diana → None
print(f"Tamaño: {len(lista)}")                 # 4
print(f"Existe Ana? {lista.buscar('Ana')}")    # True
lista.eliminar("Carlos")
print(lista)                                   # VIP-Beto → Ana → Diana → None


#--------------------------------------------AQUI EMPIEZA--------------------------------------------
#=======================================================================
# TALLER — 2 ejercicios paso a paso
#Añadir método insertar_en(pos, data) a ListaEnlazada. Insertar el nuevo nodo en la posición dada (0=inicio, len=final).
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: posición y dato
# Proceso: recorrer hasta la posición anterior, hacer el enlace
# Salida: la lista con el nuevo nodo
# Ejemplo de entrada (guía): insertar 'X' en pos=2 en [A,B,C,D]
# Salida esperada (guía): [A, B, X, C, D]

#-------- 2. BOSQUEJO A MANO ------------
# insertar_en(2, "X") sobre [A → B → C → D]
#
# pos=0 → sería inicio (usar insertar_inicio)
#
# Recorro hasta el nodo de la posición pos-1 (aquí, B):
#    actual = head          (A)
#    1 salto: actual = B    ← me detengo aquí
#
# Nuevo nodo:
#    nuevo.next = actual.next    (nuevo → C)
#    actual.next = nuevo         (B → nuevo)
#
# Resultado: A → B → X → C → D

#-------- 3. DESCUBRIR EL PATRÓN --------
# La posición 0 es el inicio y la posición tamano es el final.
# Para otra posición, llegamos al nodo anterior y cambiamos los enlaces.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListaEnlazada:
    def __init__(self):
        self.head = None
        self.tamano = 0

    def insertar_inicio(self, data):
        nuevo = Nodo(data)
        nuevo.next = self.head
        self.head = nuevo
        self.tamano += 1

    def insertar_final(self, data):
        nuevo = Nodo(data)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo
        self.tamano += 1

    def insertar_en(self, pos, data):
        """Inserta en la posición dada."""
        if pos < 0 or pos > self.tamano:
            raise IndexError(f"Posición {pos} fuera de rango")

        if pos == 0:
            self.insertar_inicio(data)
            return
        if pos == self.tamano:
            self.insertar_final(data)
            return

        # Avanzar hasta el nodo pos-1
        actual = self.head
        for _ in range(pos - 1):
            actual = actual.next

        # Enlazar: primero el nuevo apunta al siguiente, luego actual apunta al nuevo
        nuevo = Nodo(data)
        nuevo.next = actual.next
        actual.next = nuevo
        self.tamano += 1

    def a_lista(self):
        r = []
        actual = self.head
        while actual:
            r.append(actual.data)
            actual = actual.next
        return r


# --- Uso ---
l = ListaEnlazada()
for x in "ABCD":
    l.insertar_final(x)
print(l.a_lista())                              # ['A', 'B', 'C', 'D']

l.insertar_en(2, "X")
print(l.a_lista())                              # ['A', 'B', 'X', 'C', 'D']

l.insertar_en(0, "@")
print(l.a_lista())                              # ['@', 'A', 'B', 'X', 'C', 'D']

l.insertar_en(6, "$")                           # al final
print(l.a_lista())                              # ['@', 'A', 'B', 'X', 'C', 'D', '$']

#-------- 5. PRUEBA DE ESCRITORIO -------
# Acción          | Posición | Resultado
# --------------- | -------- | -------------------------
# Insertar X      | 2        | ['A', 'B', 'X', 'C', 'D']
# Insertar @      | 0        | ['@', 'A', 'B', 'X', 'C', 'D']
# Insertar $      | 6        | ['@', 'A', 'B', 'X', 'C', 'D', '$']

#CAMBIO
#Añade el método eliminar_en(pos) con la misma lógica: recorrer hasta pos-1 y saltar el siguiente.
class ListaEnlazadaConEliminacion(ListaEnlazada):
    def eliminar_en(self, pos):
        if pos < 0 or pos >= self.tamano:
            raise IndexError(f"Posición {pos} fuera de rango")

        if pos == 0:
            self.head = self.head.next
        else:
            actual = self.head
            for _ in range(pos - 1):
                actual = actual.next
            actual.next = actual.next.next

        self.tamano -= 1

# --- Prueba del cambio ---
l_eliminar = ListaEnlazadaConEliminacion()
for x in ["A", "B", "C", "D"]:
    l_eliminar.insertar_final(x)
l_eliminar.eliminar_en(2)
print(l_eliminar.a_lista())                    # ['A', 'B', 'D']


#=======================================================================
# Invertir el orden de los nodos de una lista enlazada, modificando los punteros. NO crear una nueva lista.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: una lista enlazada
# Proceso: recorrer una vez cambiando los punteros
# Salida: la misma lista con los nodos invertidos
# Ejemplo de entrada (guía): A → B → C → D
# Salida esperada (guía): D → C → B → A

#-------- 2. BOSQUEJO A MANO ------------
# A → B → C → D → None
#
# Necesito 3 variables: anterior, actual, siguiente
#
# anterior=None, actual=A
#   1) siguiente = actual.next    (B)
#   2) actual.next = anterior     (A → None)
#   3) anterior = actual          (anterior = A)
#   4) actual = siguiente         (actual = B)
#
# Repito para B → apunta a A
# Repito para C → apunta a B
# Repito para D → apunta a C
#
# Al final: head = anterior = D

#-------- 3. DESCUBRIR EL PATRÓN --------
# Usamos anterior, actual y siguiente para no perder el resto de la lista.
# Guardamos el siguiente nodo, giramos el enlace y avanzamos.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListaEnlazada:
    def __init__(self):
        self.head = None

    def insertar_final(self, data):
        nuevo = Nodo(data)
        if not self.head:
            self.head = nuevo
        else:
            a = self.head
            while a.next:
                a = a.next
            a.next = nuevo

    def invertir(self):
        """Invierte la lista in-place — O(n) tiempo, O(1) espacio."""
        anterior = None
        actual = self.head

        while actual:
            siguiente = actual.next   # 1. guardo lo que viene
            actual.next = anterior    # 2. giro el puntero hacia atrás
            anterior = actual         # 3. avanzo anterior
            actual = siguiente        # 4. avanzo actual

        self.head = anterior          # el último visto es la nueva head

    def listar(self):
        a = self.head
        while a:
            print(a.data, end=" → ")
            a = a.next
        print("None")


# --- Uso ---
l = ListaEnlazada()
for x in ["A", "B", "C", "D"]:
    l.insertar_final(x)
l.listar()                                      # A → B → C → D → None
l.invertir()
l.listar()                                      # D → C → B → A → None
#-------- 5. PRUEBA DE ESCRITORIO -------
# Paso             | anterior | actual | Resultado de los enlaces
# ---------------- | -------- | ------ | ------------------------
# Inicio           | None     | A      | A -> B -> C -> D
# Después de A     | A        | B      | A -> None
# Después de B     | B        | C      | B -> A -> None
# Final            | D        | None   | D -> C -> B -> A -> None

#CAMBIO
#Amplíalo: recursivo. Función _invertir_rec(nodo) que retorna la nueva head.
def _invertir_rec(nodo):
    if nodo is None or nodo.next is None:
        return nodo

    nueva_head = _invertir_rec(nodo.next)
    nodo.next.next = nodo
    nodo.next = None
    return nueva_head

# --- Prueba del cambio ---
l_recursiva = ListaEnlazada()
for x in ["A", "B", "C", "D"]:
    l_recursiva.insertar_final(x)
l_recursiva.head = _invertir_rec(l_recursiva.head)
l_recursiva.listar()                           # D → C → B → A → None


#=======================================================================
# EJERCICIOS PROPUESTOS
#=======================================================================
#=======================================================================
# 1) Método contar() que retorne cuántos nodos hay, recorriéndolos uno a uno (sin usar self.tamano).
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: una lista enlazada.
# Proceso: recorrer nodo por nodo y contar cuántos hay.
# Salida: devolver la cantidad de nodos.

# Ejemplo de entrada (guía): A → B → C → D
# Salida esperada (guía): 4

#-------- 2. BOSQUEJO A MANO ------------
# Lista: A -> B -> C
# Contar A: 1, contar B: 2, contar C: 3.
# Resultado: 3 nodos.

#-------- 3. DESCUBRIR EL PATRÓN --------
# Empezamos en head y avanzamos usando next.
# Cada vez que visitamos un nodo, aumentamos el contador en uno.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
def contar(lista):
    cantidad = 0
    actual = lista.head
    while actual:
        cantidad += 1
        actual = actual.next
    return cantidad


lista_p1 = ListaEnlazada()
for dato in ["A", "B", "C", "D"]:
    lista_p1.insertar_final(dato)
print("P1 — nodos:", contar(lista_p1))  # 4

#-------- 5. PRUEBA DE ESCRITORIO -------
# Nodo recorrido | Contador
# -------------- | --------
# A              | 1
# B              | 2
# C              | 3

#=======================================================================
# 2) Modifica buscar para que retorne la posición (0..n-1) o -1 si no está.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: el dato que queremos encontrar.
# Proceso: recorrer la lista y llevar la posición actual.
# Salida: devolver la posición o -1 si no se encuentra.

# Ejemplo de entrada (guía): buscar 'C' en A→B→C
# Salida esperada (guía): 2

#-------- 2. BOSQUEJO A MANO ------------
# Lista: A -> B -> C. Buscar C devuelve 2.
# Buscar X devuelve -1 porque no está en la lista.

#-------- 3. DESCUBRIR EL PATRÓN --------
# La primera posición es 0. Aumentamos la posición al avanzar.
# Si llegamos al final sin encontrar el dato, devolvemos -1.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
def buscar_pos(lista, data):
    posicion = 0
    actual = lista.head
    while actual:
        if actual.data == data:
            return posicion
        actual = actual.next
        posicion += 1
    return -1


lista_p2 = ListaEnlazada()
for dato in ["A", "B", "C"]:
    lista_p2.insertar_final(dato)
print("P2 — posición de C:", buscar_pos(lista_p2, "C"))  # 2
print("P2 — posición de X:", buscar_pos(lista_p2, "X"))  # -1

#-------- 5. PRUEBA DE ESCRITORIO -------
# Dato buscado | Resultado
# ------------ | ---------
# C            | 2
# X            | -1

#=======================================================================
# 3) Método desde_final(k): k=1 es el último nodo.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: una posición k contada desde el final.
# Proceso: usar dos referencias separadas por k nodos.
# Salida: devolver el dato del nodo pedido o None si k no sirve.

# Ejemplo de entrada (guía): A→B→C→D→E, k=2
# Salida esperada (guía): D

#-------- 2. BOSQUEJO A MANO ------------
# Lista: A -> B -> C -> D.
# k=1 devuelve D; k=2 devuelve C.

#-------- 3. DESCUBRIR EL PATRÓN --------
# Avanzamos primero una referencia k pasos.
# Luego movemos ambas referencias juntas hasta llegar al final.
# La segunda referencia queda en el nodo solicitado.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
def desde_final(lista, k):
    if k <= 0:
        return None

    adelantado = lista.head
    for _ in range(k):
        if adelantado is None:
            return None
        adelantado = adelantado.next

    detras = lista.head
    while adelantado:
        adelantado = adelantado.next
        detras = detras.next
    return detras.data


lista_p3 = ListaEnlazada()
for dato in ["A", "B", "C", "D", "E"]:
    lista_p3.insertar_final(dato)
print("P3 — segundo desde el final:", desde_final(lista_p3, 2))  # D

#-------- 5. PRUEBA DE ESCRITORIO -------
# k | Resultado
# - | ---------
# 1 | D
# 2 | C

#=======================================================================
# 4) Método tiene_ciclo() con el algoritmo de Floyd (liebre y tortuga).
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: una lista enlazada que puede tener un enlace circular.
# Proceso: comparar una referencia lenta con otra que avanza más rápido.
# Salida: True si se encuentran; False si se llega al final.

# Ejemplo de entrada (guía): lista sin ciclo
# Salida esperada (guía): False

#-------- 2. BOSQUEJO A MANO ------------
# Sin ciclo: A -> B -> C -> None, la liebre llega al final.
# Con ciclo: D apunta a B, las dos referencias se encuentran.

#-------- 3. DESCUBRIR EL PATRÓN --------
# La tortuga avanza un nodo y la liebre avanza dos.
# Si hay ciclo, la liebre alcanza a la tortuga.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
def tiene_ciclo(lista):
    tortuga = lista.head
    liebre = lista.head
    while liebre and liebre.next:
        tortuga = tortuga.next
        liebre = liebre.next.next
        if tortuga is liebre:
            return True
    return False


lista_p4 = ListaEnlazada()
for dato in ["A", "B", "C", "D"]:
    lista_p4.insertar_final(dato)
print("P4 — sin ciclo:", tiene_ciclo(lista_p4))  # False
lista_p4.head.next.next.next.next = lista_p4.head.next
print("P4 — con ciclo:", tiene_ciclo(lista_p4))  # True

#-------- 5. PRUEBA DE ESCRITORIO -------
# Lista                    | Resultado
# ------------------------ | ---------
# A -> B -> C -> None       | False
# D apunta a B (ciclo)      | True

