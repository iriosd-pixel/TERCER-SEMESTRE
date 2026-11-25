# ================================================================
# GRAFOS — GUÍA, TALLER Y PROPUESTOS
# ================================================================
# Código de explicación: lista de adyacencia y clase Grafo.

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Grafo del ejemplo
rutas = {
    "GYE": ["UIO", "CUE", "MTA"],
    "UIO": ["GYE", "MEC", "MTA"],
    "CUE": ["GYE"],
    "MTA": ["GYE", "UIO"],
    "MEC": ["UIO"],
}

# Vecinos de Guayaquil
print(rutas["GYE"])              # ['UIO', 'CUE', 'MTA']

# ¿Hay vuelo directo GYE → MEC?
print("MEC" in rutas["GYE"])     # False

# Todas las ciudades
print(list(rutas.keys()))        # ['GYE', 'UIO', 'CUE', 'MTA', 'MEC']

from collections import deque

class Grafo:
    def __init__(self, dirigido=False):
        self.adyacencia = {}
        self.dirigido = dirigido

    def agregar_nodo(self, nodo):
        if nodo not in self.adyacencia:
            self.adyacencia[nodo] = []

    def agregar_arista(self, origen, destino):
        self.agregar_nodo(origen)
        self.agregar_nodo(destino)
        self.adyacencia[origen].append(destino)
        if not self.dirigido:
            self.adyacencia[destino].append(origen)   # bidireccional

    def vecinos(self, nodo):
        return self.adyacencia.get(nodo, [])

    def bfs(self, inicio):
        """Recorrido por amplitud — nivel por nivel."""
        visitados = set([inicio])
        cola = deque([inicio])
        resultado = []
        while cola:
            nodo = cola.popleft()
            resultado.append(nodo)
            for vecino in self.adyacencia.get(nodo, []):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        return resultado

    def dfs(self, inicio):
        """Recorrido en profundidad — hasta el fondo, luego retrocede."""
        visitados = set()
        resultado = []
        self._dfs_rec(inicio, visitados, resultado)
        return resultado

    def _dfs_rec(self, nodo, visitados, resultado):
        if nodo in visitados:
            return
        visitados.add(nodo)
        resultado.append(nodo)
        for vecino in self.adyacencia.get(nodo, []):
            self._dfs_rec(vecino, visitados, resultado)

    def camino_mas_corto(self, inicio, fin):
        """BFS con reconstrucción del camino."""
        if inicio == fin:
            return [inicio]
        visitados = {inicio: None}     # nodo → nodo anterior en el camino
        cola = deque([inicio])
        while cola:
            nodo = cola.popleft()
            for vecino in self.adyacencia.get(nodo, []):
                if vecino not in visitados:
                    visitados[vecino] = nodo
                    if vecino == fin:
                        # Reconstruir el camino
                        camino = [fin]
                        while visitados[camino[-1]] is not None:
                            camino.append(visitados[camino[-1]])
                        return list(reversed(camino))
                    cola.append(vecino)
        return None                    # no hay camino


# --- Uso ---
g = Grafo()
g.agregar_arista("GYE", "UIO")
g.agregar_arista("GYE", "CUE")
g.agregar_arista("GYE", "MTA")
g.agregar_arista("UIO", "MTA")
g.agregar_arista("UIO", "MEC")

print("Vecinos GYE:", g.vecinos("GYE"))         # ['UIO', 'CUE', 'MTA']
print("BFS desde GYE:", g.bfs("GYE"))           # ['GYE', 'UIO', 'CUE', 'MTA', 'MEC']
print("DFS desde GYE:", g.dfs("GYE"))           # ['GYE', 'UIO', 'MTA', 'MEC', 'CUE']
print("Camino CUE → MEC:", g.camino_mas_corto("CUE", "MEC"))
# ['CUE', 'GYE', 'UIO', 'MEC']

# Guardamos la clase de explicación antes de la clase del taller.
GrafoBase = Grafo

# ================================================================
# TALLER — Ejercicio 1: Red de vuelos, ¿hay conexión?
# ================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: grafo y dos ciudades
# Proceso: BFS o DFS desde la ciudad origen
# Salida: True/False si hay ruta
# Ejemplo de entrada (guía): GYE → MEC
# Salida esperada (guía): True (vía UIO)

#-------- 2. BOSQUEJO A MANO ------------
# grafo:
#  GYE — UIO — MEC
#   |     |
#  CUE   MTA
#
# ¿GYE → MEC?
#  BFS desde GYE:
#    visitados = {GYE}
#    cola = [GYE]
#
#    pop GYE. Vecinos: UIO, CUE, MTA (no visitados)
#    → visitados={GYE, UIO, CUE, MTA}, cola=[UIO, CUE, MTA]
#
#    pop UIO. Vecinos: MEC (no visitado, GYE ya).
#    → MEC == fin → True ✓

#-------- 3. DESCUBRIR EL PATRÓN --------
# Visitar todos los alcanzables responde si existe una ruta.
# Un set evita visitar dos veces el mismo nodo en un grafo con ciclos.

#-------- 4. ESCRIBIR EL CÓDIGO ---------

from collections import deque

class Grafo:
    def __init__(self):
        self.adyacencia = {}

    def agregar_arista(self, a, b):
        self.adyacencia.setdefault(a, []).append(b)
        self.adyacencia.setdefault(b, []).append(a)

    def hay_ruta(self, inicio, fin):
        """BFS: retorna True si desde inicio se llega a fin."""
        if inicio not in self.adyacencia or fin not in self.adyacencia:
            return False

        visitados = set([inicio])
        cola = deque([inicio])

        while cola:
            nodo = cola.popleft()
            if nodo == fin:
                return True
            for vecino in self.adyacencia[nodo]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        return False


# --- Uso ---
g = Grafo()
g.agregar_arista("GYE", "UIO")
g.agregar_arista("GYE", "CUE")
g.agregar_arista("GYE", "MTA")
g.agregar_arista("UIO", "MTA")
g.agregar_arista("UIO", "MEC")
# Ciudad aislada
g.agregar_arista("GPS", "GPS")     # solo se conecta consigo misma

print(g.hay_ruta("GYE", "MEC"))    # True (vía UIO)
print(g.hay_ruta("CUE", "MEC"))    # True (vía GYE → UIO)
print(g.hay_ruta("GPS", "UIO"))    # False (aislada)

#-------- 5. PRUEBA DE ESCRITORIO -------
# Paso      | Cola              | Visitados                | Resultado
# Inicial   | [GYE]             | {GYE}                    | —
# pop GYE   | [UIO, CUE, MTA]   | + UIO, CUE, MTA          | —
# pop UIO   | [CUE, MTA, MEC]   | + MEC                    | —
# pop MEC   | resto de cola     | MEC ya visitado         | True

#CAMBIO
# Retorna el mínimo número de escalas: 0 en vuelo directo,
# 1 si hay una ciudad intermedia y None si no hay ruta.
class GrafoConEscalas(Grafo):
    def escalas_minimas(self, inicio, fin):
        if inicio not in self.adyacencia or fin not in self.adyacencia:
            return None
        cola = deque([(inicio, 0)])  # ciudad, número de vuelos
        visitados = {inicio}
        while cola:
            ciudad, vuelos = cola.popleft()
            if ciudad == fin:
                return max(0, vuelos - 1)
            for vecino in self.adyacencia[ciudad]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append((vecino, vuelos + 1))
        return None


vuelos_escalas = GrafoConEscalas()
for origen, destino in [("GYE", "UIO"), ("GYE", "CUE"),
                        ("GYE", "MTA"), ("UIO", "MTA"),
                        ("UIO", "MEC")]:
    vuelos_escalas.agregar_arista(origen, destino)
vuelos_escalas.agregar_arista("GPS", "GPS")
print("Escalas GYE → UIO:", vuelos_escalas.escalas_minimas("GYE", "UIO"))  # 0
print("Escalas GYE → MEC:", vuelos_escalas.escalas_minimas("GYE", "MEC"))  # 1
print("Escalas GPS → MEC:", vuelos_escalas.escalas_minimas("GPS", "MEC"))  # None

# ================================================================
# TALLER — Ejercicio 2: Grafo de una red social
# ================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: grafo de amistades
# Proceso: vecinos directos y vecinos de vecinos
# Salida: listas de amistades
# Ejemplo de entrada (guía): Ana-Beto, Ana-Carlos, Beto-Diana
# Salida esperada (guía): amigos_de_amigos(Ana) = {Diana}

#-------- 2. BOSQUEJO A MANO ------------
# Ana ─ Beto ─ Diana
#   \
#    Carlos ─ Elena
#
# son_amigos(Ana, Beto) → True (arista directa)
# son_amigos(Ana, Diana) → False
#
# amigos_de_amigos(Ana):
#   amigos de Ana: {Beto, Carlos}
#   amigos de Beto: {Ana, Diana}
#   amigos de Carlos: {Ana, Elena}
#
#   candidatos: {Diana, Elena}
#   quito los que ya son amigos directos de Ana: {Diana, Elena}
#   quito la propia Ana: {Diana, Elena}
#
#   → {Diana, Elena}

#-------- 3. DESCUBRIR EL PATRÓN --------
# La amistad se representa con aristas no dirigidas.
# Unir los amigos de cada amigo; quitar directos y a la propia persona.

#-------- 4. ESCRIBIR EL CÓDIGO ---------

class RedSocial:
    def __init__(self):
        self.amigos = {}      # nombre → set de amigos

    def agregar_persona(self, p):
        if p not in self.amigos:
            self.amigos[p] = set()

    def hacer_amigos(self, a, b):
        self.agregar_persona(a)
        self.agregar_persona(b)
        self.amigos[a].add(b)
        self.amigos[b].add(a)

    def son_amigos(self, a, b):
        return b in self.amigos.get(a, set())

    def amigos_de_amigos(self, persona):
        """Personas a distancia 2 (amigos de mis amigos)."""
        if persona not in self.amigos:
            return set()

        directos = self.amigos[persona]
        candidatos = set()
        for amigo in directos:
            candidatos |= self.amigos[amigo]     # unión

        # Quitar los directos y a la propia persona
        return candidatos - directos - {persona}


# --- Uso ---
red = RedSocial()
red.hacer_amigos("Ana", "Beto")
red.hacer_amigos("Ana", "Carlos")
red.hacer_amigos("Beto", "Diana")
red.hacer_amigos("Carlos", "Elena")

print(red.son_amigos("Ana", "Beto"))            # True
print(red.son_amigos("Ana", "Diana"))           # False
print(red.amigos_de_amigos("Ana"))              # {'Diana', 'Elena'}
print(red.amigos_de_amigos("Beto"))             # {'Carlos'}

#-------- 5. PRUEBA DE ESCRITORIO -------
# Persona | Amigos directos | Amigos de amigos | Resultado
# Ana     | Beto, Carlos    | Diana, Elena     | {Diana, Elena}
# Beto    | Ana, Diana      | Carlos           | {Carlos}

#CAMBIO
# Sugerir personas a distancia 2, ordenadas por la cantidad de
# amigos en común. Devuelve (persona, cantidad) en cada sugerencia.
class RedSocialConSugerencias(RedSocial):
    def sugerencias(self, persona):
        if persona not in self.amigos:
            return []
        directos = self.amigos[persona]
        candidatos = self.amigos_de_amigos(persona)
        conteos = [
            (candidato, len(directos & self.amigos[candidato]))
            for candidato in candidatos
        ]
        return sorted(conteos, key=lambda par: (-par[1], par[0]))


red_sugerencias = RedSocialConSugerencias()
for a, b in [("Ana", "Beto"), ("Ana", "Carlos"),
             ("Beto", "Diana"), ("Carlos", "Diana"),
             ("Carlos", "Elena")]:
    red_sugerencias.hacer_amigos(a, b)
print("Sugerencias para Ana:", red_sugerencias.sugerencias("Ana"))
# [('Diana', 2), ('Elena', 1)]

# ================================================================
# EJERCICIOS PROPUESTOS
# Cada solución funciona por separado con un grafo de ejemplo.
# ================================================================

#=======================================================================
# 1) P1 — Contar nodos y aristas
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: grafo y su lista de adyacencia.
# Proceso: contar claves y sumar longitudes de sus listas.
# Salida: tupla (nodos, aristas).

# Ejemplo de entrada (guía): grafo de 5 nodos, 6 aristas
# Salida esperada (guía): (5, 6)

#-------- 2. BOSQUEJO A MANO ------------
# Cinco nodos y seis conexiones bidireccionales:
# la suma de vecinos es 12, así que aristas = 12 // 2 = 6.
# Por ejemplo, los grados 4, 3, 1, 2 y 2 suman 12.
# Cada conexión se ve desde sus dos extremos; por eso se divide entre 2.
# Si el grafo fuera dirigido, cada arco aparece una vez y no se divide.

#-------- 3. DESCUBRIR EL PATRÓN --------
# Cada arista aparece dos veces si el grafo no es dirigido.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
def estadisticas(grafo):
    nodos = len(grafo.adyacencia)
    # cada arista se cuenta dos veces (en cada extremo) si no es dirigido
    aristas = sum(len(v) for v in grafo.adyacencia.values())
    if not grafo.dirigido:
        aristas //= 2
    return nodos, aristas


grafo_p1 = GrafoBase()
for origen, destino in [("GYE", "UIO"), ("GYE", "CUE"),
                        ("GYE", "MTA"), ("UIO", "MTA"),
                        ("UIO", "MEC"), ("GYE", "MEC")]:
    grafo_p1.agregar_arista(origen, destino)
print("P1 — nodos y aristas:", estadisticas(grafo_p1))  # (5, 6)

#-------- 5. PRUEBA DE ESCRITORIO -------
# Nodos | Suma de grados | ¿Dirigido? | Aristas
# 5     | 12             | No         | 6


#=======================================================================
# 2) P2 — Grado de un nodo
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: nombre del nodo.
# Proceso: contar los vecinos de ese nodo.
# Salida: cantidad de conexiones.

# Ejemplo de entrada (guía): grado(GYE) en el ejemplo
# Salida esperada (guía): 3

#-------- 2. BOSQUEJO A MANO ------------
# GYE conecta UIO, CUE y MTA: su grado es 3.
# Tomo la lista de GYE: [UIO, CUE, MTA] y cuento sus 3 elementos.
# Para un nodo aislado la lista queda vacía y el grado es 0.

#-------- 3. DESCUBRIR EL PATRÓN --------
# El grado coincide con la longitud de la lista de vecinos.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
def grado(grafo, nodo):
    return len(grafo.adyacencia.get(nodo, []))


grafo_p2 = GrafoBase()
for origen, destino in [("GYE", "UIO"), ("GYE", "CUE"),
                        ("GYE", "MTA"), ("UIO", "MTA"),
                        ("UIO", "MEC")]:
    grafo_p2.agregar_arista(origen, destino)
print("P2 — grado GYE:", grado(grafo_p2, "GYE"))  # 3

#-------- 5. PRUEBA DE ESCRITORIO -------
# Nodo | Vecinos       | Grado
# GYE  | UIO, CUE, MTA | 3
# MEC  | UIO           | 1


#=======================================================================
# 3) P3 — Componentes conexos
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: grafo con uno o más grupos aislados entre sí.
# Proceso: iniciar BFS desde cada nodo aún no visitado.
# Salida: número de componentes conexos.

# Ejemplo de entrada (guía): 6 nodos en 2 grupos
# Salida esperada (guía): 2 componentes

#-------- 2. BOSQUEJO A MANO ------------
# Grupo 1: GYE, UIO, CUE, MTA, MEC. Grupo 2: GPS.
# Dos recorridos BFS necesarios → dos componentes.
# Inicio en GYE y marco los cinco nodos alcanzables; el contador pasa a 1.
# Los cuatro siguientes ya están visitados, por lo que no abren otro BFS.
# GPS sigue sin visitar: lo marco y el contador pasa a 2.

#-------- 3. DESCUBRIR EL PATRÓN --------
# Cada nuevo BFS descubre exactamente un grupo.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
def componentes_conexos(grafo):
    """Cuenta cuántos «trozos» aislados hay en el grafo."""
    visitados = set()
    componentes = 0

    for nodo in grafo.adyacencia:
        if nodo not in visitados:
            # nuevo componente; hago BFS/DFS desde aquí
            componentes += 1
            _bfs_marcar(grafo, nodo, visitados)
    return componentes


def _bfs_marcar(grafo, inicio, visitados):
    cola = deque([inicio])
    visitados.add(inicio)
    while cola:
        nodo = cola.popleft()
        for v in grafo.adyacencia[nodo]:
            if v not in visitados:
                visitados.add(v)
                cola.append(v)


grafo_p3 = GrafoBase()
for origen, destino in [("GYE", "UIO"), ("GYE", "CUE"),
                        ("GYE", "MTA"), ("UIO", "MTA"),
                        ("UIO", "MEC")]:
    grafo_p3.agregar_arista(origen, destino)
grafo_p3.agregar_nodo("GPS")
print("P3 — componentes:", componentes_conexos(grafo_p3))  # 2

#-------- 5. PRUEBA DE ESCRITORIO -------
# Inicio | Nodos marcados            | Componentes
# GYE    | GYE, UIO, CUE, MTA, MEC  | 1
# GPS    | GPS                       | 2


#=======================================================================
# 4) P4 — Todos los caminos entre A y B
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: origen y destino de un grafo.
# Proceso: buscar en profundidad sin repetir nodos en un camino.
# Salida: lista de todos los caminos simples posibles.

# Ejemplo de entrada (guía): GYE → MEC
# Salida esperada (guía): [GYE, UIO, MEC], [GYE, MTA, UIO, MEC]

#-------- 2. BOSQUEJO A MANO ------------
# De GYE a MEC: GYE → UIO → MEC y GYE → MTA → UIO → MEC.
# Al llegar a MEC guardo una copia del camino recorrido.
# Regreso a UIO, quito el último nodo y pruebo otra rama.
# Si una rama vuelve a un nodo ya presente (por ejemplo, GYE), la descarto
# para evitar ciclos y sigo hasta agotar las rutas posibles.

#-------- 3. DESCUBRIR EL PATRÓN --------
# Al llegar al destino, copiar el camino actual.
# Al retroceder, quitar el último nodo para probar otra rama.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
def todos_caminos(grafo, origen, destino):
    """Retorna lista de todos los caminos simples de origen a destino."""
    resultado = []
    _buscar_caminos(grafo, origen, destino, [origen], resultado)
    return resultado


def _buscar_caminos(grafo, actual, destino, camino_hasta_ahora, resultado):
    if actual == destino:
        resultado.append(list(camino_hasta_ahora))   # copia
        return
    for vecino in grafo.adyacencia.get(actual, []):
        if vecino not in camino_hasta_ahora:         # evitar ciclos
            camino_hasta_ahora.append(vecino)
            _buscar_caminos(grafo, vecino, destino, camino_hasta_ahora, resultado)
            camino_hasta_ahora.pop()                 # backtracking


grafo_p4 = GrafoBase()
for origen, destino in [("GYE", "UIO"), ("GYE", "CUE"),
                        ("GYE", "MTA"), ("UIO", "MTA"),
                        ("UIO", "MEC")]:
    grafo_p4.agregar_arista(origen, destino)
print("P4 — caminos GYE → MEC:", todos_caminos(grafo_p4, "GYE", "MEC"))
# [['GYE', 'UIO', 'MEC'], ['GYE', 'MTA', 'UIO', 'MEC']]

#-------- 5. PRUEBA DE ESCRITORIO -------
# Ruta explorada               | ¿Llega a MEC?
# GYE → UIO → MEC             | Sí, guardar
# GYE → MTA → UIO → MEC       | Sí, guardar
# GYE → CUE → GYE             | No, evitar ciclo
