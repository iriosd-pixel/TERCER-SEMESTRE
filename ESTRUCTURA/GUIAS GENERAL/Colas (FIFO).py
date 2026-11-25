class MiCola:
    def __init__(self):
        self._datos = []

    def encolar(self, valor):
        """Añade al final"""
        self._datos.append(valor)

    def desencolar(self):
        """Saca del frente y lo retorna"""
        if self.esta_vacia():
            raise IndexError("Cola vacía")
        return self._datos.pop(0)          # OJO: pop(0) mueve todos → O(n)

    def frente(self):
        """Mira el del frente sin sacarlo"""
        if self.esta_vacia():
            raise IndexError("Cola vacía")
        return self._datos[0]

    def esta_vacia(self):
        return len(self._datos) == 0

    def tamano(self):
        return len(self._datos)

    def __str__(self):
        return "cola: [" + " ← ".join(str(x) for x in self._datos) + "]"


# --- Uso ---
cola = MiCola()
cola.encolar("Ana")
cola.encolar("Carlos")
cola.encolar("Diana")
print(cola)                                # cola: [Ana ← Carlos ← Diana]
print(cola.frente())                       # Ana (no la saca)
print(cola.desencolar())                   # Ana (la saca)
print(cola)      
# cola: [Carlos ← Diana]



#cola optimizada
from collections import deque

# Cola de atención al cliente
cola = deque()

# Encolar
cola.append("Ana")        # entra al final
cola.append("Carlos")
cola.append("Diana")

# Desencolar
primero = cola.popleft()  # sale del frente → "Ana"
frente = cola[0]          # peek → "Carlos"

print(cola)               # deque(['Carlos', 'Diana'])
print(len(cola))          # 2

# Deque también permite añadir al frente (útil en algoritmos)
cola.appendleft("VIP")    # entra al frente
print(cola)               # deque(['VIP', 'Carlos', 'Diana'])

#---------------------------------------------------------------------------------AQUI EMPIEZA------------------------------------------------------

#=======================================================================
# TALLER — 3 ejercicios paso a paso
#1 ) Simular una fila de banco: los clientes llegan (encolar) y el cajero los atiende en orden (desencolar).
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: opción del menú y datos
# Proceso: menú con encolar/desencolar/frente
# Salida: estado de la fila y siguiente en atención
# Ejemplo de entrada (guía): llegan 3, atender 1
# Salida esperada (guía): atendido: Ana. Quedan: Beto, Carlos

#-------- 2. BOSQUEJO A MANO ------------
# cola = []
#
# Ana llega  → encolar("Ana")  → [Ana]
# Beto llega → encolar("Beto") → [Ana, Beto]
# Carlos llega → encolar("Carlos") → [Ana, Beto, Carlos]
#
# atender → desencolar() → "Ana"  → [Beto, Carlos]
# frente → "Beto"

#-------- 3. DESCUBRIR EL PATRÓN --------
# Una cola trabaja con FIFO: primero en entrar, primero en salir.
# Los clientes normales se agregan al final con append().

#-------- 4. ESCRIBIR EL CÓDIGO ---------
from collections import deque

cola = deque()

while True:
    print("\n1.Llega cliente 2.Atender 3.Ver frente 4.Ver toda la cola 5.Salir")
    op = input("Opción: ")

    if op == "1":
        nom = input("Nombre: ")
        cola.append(nom)
        print(f"{nom} entró a la fila. {len(cola)} clientes en espera.")

    elif op == "2":
        if not cola:
            print("No hay clientes")
        else:
            atendido = cola.popleft()
            print(f"Atendiendo a: {atendido}. Quedan {len(cola)}.")

    elif op == "3":
        if not cola:
            print("Fila vacía")
        else:
            print(f"Siguiente: {cola[0]}")

    elif op == "4":
        if not cola:
            print("(vacía)")
        else:
            for i, c in enumerate(cola):
                marca = " ← siguiente" if i == 0 else ""
                print(f"  {i+1}. {c}{marca}")

    elif op == "5":
        break

#-------- 5. PRUEBA DE ESCRITORIO -------
# Acción              | Fila             | Resultado
# ------------------- | ---------------- | ------------------
# Llega Ana           | [Ana]            | 1 cliente en espera
# Llega Carlos        | [Ana, Carlos]    | 2 clientes en espera
# Atender             | [Carlos]         | Se atiende a Ana
# Ver frente          | [Carlos]         | Siguiente: Carlos

#CAMBIO
#Añade prioridad: los clientes VIP entran al frente con cola.appendleft(nom).
# Esta versión agrega una opción para clientes VIP.
cola = deque()
while True:
    print("\n1.Llega cliente 2.Llega VIP 3.Atender 4.Ver frente 5.Ver cola 6.Salir")
    op = input("Opción: ")

    if op == "1":
        nom = input("Nombre: ")
        cola.append(nom)
        print(f"{nom} entró al final de la fila.")

    elif op == "2":
        nom = input("Nombre VIP: ")
        cola.appendleft(nom)
        print(f"{nom} entró al frente de la fila.")

    elif op == "3":
        if not cola:
            print("No hay clientes")
        else:
            print(f"Atendiendo a: {cola.popleft()}")

    elif op == "4":
        if not cola:
            print("Fila vacía")
        else:
            print(f"Siguiente: {cola[0]}")

    elif op == "5":
        print(list(cola) if cola else "(vacía)")

    elif op == "6":
        break

    
#=======================================================================
# 2) Un sistema recibe documentos para imprimir. Los procesa en orden de llegada. Cada documento tarda su número de páginas × 2 segundos.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: trabajos con nombre y páginas
# Proceso: cola de trabajos, procesar en orden
# Salida: estado y tiempos
# Ejemplo de entrada (guía): 3 docs: A(5p), B(2p), C(10p)
# Salida esperada (guía): Total: 34 segundos

#-------- 2. BOSQUEJO A MANO ------------
# cola = [(A, 5), (B, 2), (C, 10)]
#
# procesa A → 10s   cola: [(B, 2), (C, 10)], transcurrido=10
# procesa B →  4s   cola: [(C, 10)],        transcurrido=14
# procesa C → 20s   cola: [],               transcurrido=34
#
# total: 34 segundos

#-------- 3. DESCUBRIR EL PATRÓN --------
# La cola conserva el orden en que llegaron los documentos.
# En cada vuelta sacamos el primero, calculamos su tiempo y lo sumamos.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
from collections import deque

def procesar_impresora(trabajos):
    cola = deque(trabajos)
    tiempo_total = 0

    while cola:
        nombre, paginas = cola.popleft()      # FIFO: el primero en llegar
        tiempo = paginas * 2
        tiempo_total += tiempo
        print(f"Imprimiendo {nombre}: {paginas} páginas → {tiempo}s "
              f"(acumulado {tiempo_total}s)")

    return tiempo_total


# --- Uso ---
trabajos = [
    ("Contrato.pdf", 5),
    ("Recibo.pdf", 2),
    ("Manual.pdf", 10),
]

total = procesar_impresora(trabajos)
print(f"\nTiempo total: {total}s")

#-------- 5. PRUEBA DE ESCRITORIO -------
# Documento    | Páginas | Tiempo | Tiempo acumulado
# ------------ | ------- | ------ | ----------------
# Contrato.pdf | 5       | 10 s   | 10 s
# Recibo.pdf   | 2       | 4 s    | 14 s
# Manual.pdf   | 10      | 20 s   | 34 s

#CAMBIO
#Añade opción «cancelar trabajo por nombre» — busca en la deque y usa cola.remove((nombre, ...)).
def cancelar_trabajo(cola, nombre):
    for trabajo in cola:
        if trabajo[0] == nombre:
            cola.remove(trabajo)
            print(f"Trabajo cancelado: {nombre}")
            return True

    print(f"No se encontró el trabajo: {nombre}")
    return False

# --- Prueba del cambio ---
cola_cancelar = deque(trabajos)
cancelar_trabajo(cola_cancelar, "Recibo.pdf")
print(list(cola_cancelar))
# [('Contrato.pdf', 5), ('Manual.pdf', 10)]


#=======================================================================
# 3) Extender la cola para que acepte una prioridad. Los de mayor prioridad se atienden primero, y entre iguales, por orden de llegada.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: elementos con nombre y prioridad
# Proceso: usar múltiples deques (una por nivel de prioridad)
# Salida: el orden correcto de atención
# Ejemplo de entrada (guía): Ana(1), Luis(3), Diana(1)
# Salida esperada (guía): Orden: Luis (3), Ana (1), Diana (1)

#-------- 2. BOSQUEJO A MANO ------------
# prioridades:
#    3 (alta)  → deque([Luis])
#    2         → deque([])
#    1 (baja)  → deque([Ana, Diana])
#
# atender:
#    busca en prioridad 3 → Luis
#    busca en prioridad 3 → vacía
#    busca en prioridad 2 → vacía
#    busca en prioridad 1 → Ana
#    busca en prioridad 1 → Diana
#
# resultado: Luis, Ana, Diana ✓

#-------- 3. DESCUBRIR EL PATRÓN --------
# Usamos una cola separada para cada nivel de prioridad.
# Revisamos desde el nivel más alto; cada cola mantiene el orden de llegada.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
from collections import deque

class ColaPrioridad:
    def __init__(self, niveles=3):
        # Un deque por cada nivel (índice = prioridad, más alto = más urgente)
        self.niveles = niveles
        self.colas = [deque() for _ in range(niveles + 1)]

    def encolar(self, valor, prioridad):
        if not 0 < prioridad <= self.niveles:
            raise ValueError(f"Prioridad entre 1 y {self.niveles}")
        self.colas[prioridad].append(valor)

    def desencolar(self):
        """Saca el de mayor prioridad; entre iguales, el más antiguo."""
        # Recorremos de la prioridad más alta a la más baja
        for i in range(self.niveles, 0, -1):
            if self.colas[i]:
                return self.colas[i].popleft()
        raise IndexError("Cola vacía")

    def __str__(self):
        s = []
        for i in range(self.niveles, 0, -1):
            if self.colas[i]:
                s.append(f"  P{i}: {list(self.colas[i])}")
        return "\n".join(s) if s else "(vacía)"


# --- Uso ---
cp = ColaPrioridad(3)
cp.encolar("Ana", 1)
cp.encolar("Luis", 3)
cp.encolar("Diana", 1)
cp.encolar("Beto", 2)

print(cp)
# P3: ['Luis']
# P2: ['Beto']
# P1: ['Ana', 'Diana']

# Atender en orden
while True:
    try:
        print("Atendiendo:", cp.desencolar())
    except IndexError:
        break
# Luis / Beto / Ana / Diana

#-------- 5. PRUEBA DE ESCRITORIO -------
# Elemento | Prioridad | Orden de atención
# -------- | --------- | -----------------
# Luis     | 3         | 1
# Beto     | 2         | 2
# Ana      | 1         | 3
# Diana    | 1         | 4

#CAMBIO
#Añade una opción para cambiar la prioridad de un elemento ya encolado (buscarlo, moverlo).
def cambiar_prioridad(cola, valor, prioridad_nueva):
    if not 0 < prioridad_nueva <= cola.niveles:
        raise ValueError(f"Prioridad entre 1 y {cola.niveles}")

    for prioridad_actual in range(1, cola.niveles + 1):
        if valor in cola.colas[prioridad_actual]:
            cola.colas[prioridad_actual].remove(valor)
            cola.encolar(valor, prioridad_nueva)
            return True

    return False

# --- Prueba del cambio ---
cp_cambio = ColaPrioridad(3)
cp_cambio.encolar("Ana", 1)
cp_cambio.encolar("Luis", 3)
cp_cambio.encolar("Beto", 2)

if cambiar_prioridad(cp_cambio, "Ana", 3):
    print("Prioridad de Ana actualizada")
print(cp_cambio)
# Ana pasa al nivel 3, después de Luis porque llegó más tarde a ese nivel.

#=======================================================================
# EJERCICIOS PROPUESTOS
#=======================================================================
#=======================================================================
# 1) P1 — Fila con tickets numerados: Simulador con tickets automáticos: al llegar un cliente se le asigna un número (1, 2, 3...). Al atender, se llama el siguiente.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: tres clientes que llegan y dos turnos de atención.
# Proceso: asignar tickets consecutivos; atender en orden FIFO.
# Salida: los números atendidos y los que siguen esperando.
# Ejemplo de entrada (guía): 3 llegadas, 2 atenciones
# Salida esperada (guía): atendidos 1 y 2; quedan: [ticket 3]

#-------- 2. BOSQUEJO A MANO ------------
# Llega Ana: ticket 1, cola [1], próximo = 2.
# Llega Beto: ticket 2, cola [1, 2], próximo = 3.
# Llega Carlos: ticket 3, cola [1, 2, 3], próximo = 4.
# Atender dos veces: salen 1 y 2; queda [3].

#-------- 3. DESCUBRIR EL PATRÓN --------
# El contador aumenta solo al asignar un ticket.
# La deque conserva el orden de llegada al sacar con popleft().

#-------- 4. ESCRIBIR EL CÓDIGO ---------
from collections import deque

cola = deque()
proximo = 1

while True:
    print("\n1.Llega 2.Atender 3.Ver cola 4.Salir")
    op = input("Opción: ")

    if op == "1":
        cola.append(proximo)
        print(f"Ticket {proximo} asignado. {len(cola)} en espera.")
        proximo += 1
    elif op == "2":
        if not cola:
            print("Sin clientes")
        else:
            print(f"Turno {cola.popleft()}")
    elif op == "3":
        print(list(cola))
    elif op == "4":
        break

#-------- 5. PRUEBA DE ESCRITORIO -------
# Acción | Cola | Próximo ticket | Resultado
# Llega Ana | [1] | 2 | asignado 1
# Llega Beto | [1, 2] | 3 | asignado 2
# Llega Carlos | [1, 2, 3] | 4 | asignado 3
# Atender 2 veces | [3] | 4 | turnos 1 y 2

#=======================================================================
# 2) P2 — Round-robin (turno rotativo): Se rotan turnos entre jugadores. Al «terminar el turno», el jugador vuelve al final de la cola. Muestra 10 turnos consecutivos.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: jugadores Ana, Beto y Carlos; diez turnos.
# Proceso: sacar al primero y devolverlo al final después de jugar.
# Salida: el orden de los diez turnos.
# Ejemplo de entrada (guía): jugadores = [A, B, C]
# Salida esperada (guía): A, B, C, A, B, C, A, B, C, A

#-------- 2. BOSQUEJO A MANO ------------
# Cola inicial [Ana, Beto, Carlos].
# Turno 1: sale Ana; cola [Beto, Carlos, Ana].
# Turno 2: sale Beto; cola [Carlos, Ana, Beto].
# Turno 3: sale Carlos; vuelve a quedar [Ana, Beto, Carlos].
# El ciclo se repite; el turno 10 corresponde a Ana.

#-------- 3. DESCUBRIR EL PATRÓN --------
# Cada turno rota exactamente una posición.
# Después de tres turnos, los tres jugadores han participado una vez.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
from collections import deque

jugadores = deque(["Ana", "Beto", "Carlos"])

for turno in range(10):
    actual = jugadores.popleft()      # sale del frente
    print(f"Turno {turno+1}: {actual}")
    jugadores.append(actual)          # vuelve al final

#-------- 5. PRUEBA DE ESCRITORIO -------
# Turno | Sale | Cola después de reencolar
# 1 | Ana | [Beto, Carlos, Ana]
# 2 | Beto | [Carlos, Ana, Beto]
# 3 | Carlos | [Ana, Beto, Carlos]
# 10 | Ana | [Beto, Carlos, Ana]

#=======================================================================
# 3) P3 — Cola con máximo (histórico): Cola normal, pero con un método adicional maximo_visto() que retorna el máximo valor que HA PASADO por la cola (aunque ya haya salido).
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: valores 5, 3, 8 y 2.
# Proceso: mantener una cola FIFO y guardar el máximo histórico al encolar.
# Salida: 8, incluso después de vaciar la cola.
# Ejemplo de entrada (guía): encola 5, 3, 8, 2 y desencola todo
# Salida esperada (guía): Máximo visto: 8

#-------- 2. BOSQUEJO A MANO ------------
# Máximo inicial = -infinito.
# Encolar 5: máximo = 5; encolar 3: sigue 5.
# Encolar 8: máximo = 8; encolar 2: sigue 8.
# Desencolar 5, 3, 8 y 2: máximo histórico sigue siendo 8.

#-------- 3. DESCUBRIR EL PATRÓN --------
# El máximo se actualiza al entrar un valor mayor.
# Desencolar cambia la cola actual, no el máximo que alguna vez pasó por ella.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
from collections import deque

class ColaConMax:
    def __init__(self):
        self._datos = deque()
        self._max_visto = float("-inf")

    def encolar(self, v):
        self._datos.append(v)
        if v > self._max_visto:
            self._max_visto = v

    def desencolar(self):
        if not self._datos:
            raise IndexError("vacía")
        return self._datos.popleft()

    def maximo_visto(self):
        return self._max_visto


c = ColaConMax()
for x in [5, 3, 8, 2]:
    c.encolar(x)
while c._datos:
    print(c.desencolar())
print("Máximo visto:", c.maximo_visto())

#-------- 5. PRUEBA DE ESCRITORIO -------
# Acción | Cola | Máximo visto
# Encolar 5 | [5] | 5
# Encolar 3 | [5, 3] | 5
# Encolar 8 | [5, 3, 8] | 8
# Desencolar todo | [] | 8

#=======================================================================
# 4) P4 — Simulador de café: dos cajas: Los clientes llegan a UNA cola. Hay 2 cajas; cada una toma al primero de la cola cuando queda libre. Cada cliente tarda entre 30 y 90 segundos. Simula 10 clientes.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: diez clientes, una cola y dos cajas.
# Proceso: dar a cada caja libre el siguiente cliente y reducir su tiempo restante.
# Salida: orden de atención y tiempo total de la simulación.
# Ejemplo de entrada (guía): 10 clientes
# Salida esperada (guía): Tiempo total: ~350s

#-------- 2. BOSQUEJO A MANO ------------
# Segundo 0: caja 1 toma Cliente-1 y caja 2 toma Cliente-2.
# Ambas descuentan un segundo en cada vuelta.
# Cuando una caja termina, en la siguiente vuelta toma el primer cliente pendiente.
# La simulación termina cuando no quedan clientes ni cajas ocupadas.

#-------- 3. DESCUBRIR EL PATRÓN --------
# La cola es única: nunca se adelanta un cliente.
# Cada caja guarda su cliente y su tiempo restante; None significa libre.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
import random
from collections import deque

random.seed(42)                     # para reproducibilidad
cola = deque([f"Cliente-{i+1}" for i in range(10)])

# Dos cajas: cada una guarda (cliente, tiempo_restante) o None si libre
cajas = [None, None]

segundo = 0

while cola or any(cajas):
    # Cada caja libre agarra al primero
    for i in range(2):
        if cajas[i] is None and cola:
            cliente = cola.popleft()
            tiempo = random.randint(30, 90)
            cajas[i] = [cliente, tiempo]
            print(f"[{segundo}s] Caja {i+1}: atendiendo a {cliente} ({tiempo}s)")

    # Cada caja ocupada trabaja 1 segundo
    for i in range(2):
        if cajas[i]:
            cajas[i][1] -= 1
            if cajas[i][1] == 0:
                print(f"[{segundo+1}s] Caja {i+1}: terminó con {cajas[i][0]}")
                cajas[i] = None

    segundo += 1

print(f"\nTiempo total: {segundo}s")

#-------- 5. PRUEBA DE ESCRITORIO -------
# Momento | Cola | Caja 1 | Caja 2
# Inicio | 10 clientes | libre | libre
# Segundo 0 | 8 clientes | Cliente-1 | Cliente-2
# Al liberar una caja | 7 clientes | siguiente cliente | otra caja continúa
# Final | [] | libre | libre
