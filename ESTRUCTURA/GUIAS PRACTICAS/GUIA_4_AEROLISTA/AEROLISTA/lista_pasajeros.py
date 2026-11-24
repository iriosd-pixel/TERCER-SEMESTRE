# ==============================================================
#  lista_pasajeros.py  ·  Lista enlazada de pasajeros
#  ✍ ESTE ES EL ARCHIVO DONDE TRABAJAS TÚ
# --------------------------------------------------------------
#        head
#         |
#         v
#    +----------+---+    +----------+---+    +----------+---+
#    | #1005    | o-+--->| #1002    | o-+--->| #1009    | o-+---> None
#    | Diana 3C |   |    | Ana 1A   |   |    | Luis 7D  |   |
#    +----------+---+    +----------+---+    +----------+---+
#       data    next        data    next        data    next
#
#  Los pasajeros quedan en ORDEN DE LLEGADA (el orden en que reservaron).
#
#  ✅ Ya funcionan: la clase Nodo, el constructor __init__ y ingresar.
#  ✍ Tú implementas los otros 9 métodos. Reglas:
#     1. Recorre SIEMPRE con el patrón de la Unidad 3:
#            actual = self.head
#            while actual is not None:
#                ...
#                actual = actual.next
#     2. NO conviertas la lista enlazada en una list de Python para
#        buscar, modificar o eliminar (nada de list(), in, index, sort).
#     3. La ÚNICA list de Python permitida es el RESULTADO de listar()
#        y de filtrar_por_clase(): es la "caja" que Flask envía al navegador.
#     4. La clase NUNCA hace print() ni input(): RETORNA valores.
#     5. Para empezar un método, BORRA su línea  raise NotImplementedError(...)
#        y escribe tu código en su lugar.
# ==============================================================

from pasajero import Pasajero


class Nodo:
    """Un vagón del tren: lleva un pasajero (data) y el enganche al siguiente (next)."""

    def __init__(self, data):
        self.data = data          # el Pasajero que viaja en este vagón
        self.next = None          # al nacer no está enganchado a nadie


class ListaPasajeros:
    """Lista enlazada simple con todas las reservas del vuelo."""

    # ----------------------------------------------------------
    # ✅ EJEMPLO RESUELTO 1: el constructor
    # ----------------------------------------------------------
    def __init__(self):
        self.head = None          # la cabeza: el primer nodo (None = avión vacío)
        self.cantidad = 0         # cuántas reservas (nodos) hay

    # ----------------------------------------------------------
    # ✅ EJEMPLO RESUELTO 2: ingresar (= insertar_final de la Unidad 3)
    #    Engancha un pasajero NUEVO al final del tren.
    # ----------------------------------------------------------
    def ingresar(self, pasajero):
        nuevo = Nodo(pasajero)                # 1. creo el vagón con el pasajero

        if self.head is None:                 # 2a. Lista vacía:
            self.head = nuevo                 #     el nuevo es la cabeza
        else:                                 # 2b. Lista con nodos:
            actual = self.head                #     pongo el dedo en la cabeza
            while actual.next is not None:    #     mientras NO sea el último...
                actual = actual.next          #     ...avanzo un vagón
            actual.next = nuevo               #     el último ahora apunta al nuevo

        self.cantidad = self.cantidad + 1     # 3. hay una reserva más
        return True

    # ==========================================================
    # ✍ TAREA · implementa estos métodos (en este orden te será más fácil)
    # ==========================================================

    def esta_vacia(self):
        """Retorna True si no hay ninguna reserva; False si hay al menos una.
        Pista: mira self.head."""
        return self.head is None

    def longitud(self):
        """Retorna cuántas reservas hay.
        Pista: no recorras nada, ya tienes self.cantidad."""
        return self.cantidad

    def listar(self):
        """Retorna una list de Python con TODOS los Pasajero, en orden:
        desde head hasta el último. Si está vacía retorna [].
        ⚠ Guarda el pasajero (actual.data), no el nodo.
        👉 Cuando funcione, ¡el avión se pinta con los asientos ocupados!"""
        resultado=[]
        actual= self.head
        
        while actual is not None:
            resultado.append(actual.data)
            actual=actual.next
        
        return resultado

    def buscar(self, numero):
        """Búsqueda lineal por número de reserva (int).
        Retorna el Pasajero encontrado o None si no existe."""
        actual= self.head
        while actual is not None:
            if actual.data.numero == numero:
                return actual.data
            actual=actual.next
        return None
        
    def buscar_por_asiento(self, asiento):
        """Retorna el Pasajero sentado en ese asiento ("7D") o None si está libre.
        👉 Flask lo usa al hacer clic en un asiento rojo y para no
           vender dos veces el mismo asiento."""
        actual= self.head
        while actual is not None:
            if actual.data.asiento==asiento:
                return actual.data
            actual=actual.next
        return None
        
    def buscar_por_cedula(self, cedula):
        """Retorna el Pasajero con esa cédula (str) o None.
        👉 Flask lo usa para que una persona no reserve dos asientos."""
        actual= self.head
        while actual is not None:
            if actual.data.cedula==cedula:
                return actual.data
            actual=actual.next
        return None
    
    def modificar(self, numero, nuevo_nombre, nueva_edad, nuevo_asiento):
        """Cambia nombre, edad y asiento del pasajero con ese número.
        Usa buscar(). El nodo NO cambia de lugar en la lista: solo cambia su carga.
        Retorna True si lo modificó, False si no existe."""
        pasajero=self.buscar(numero)
        if pasajero is None:
            return False
        else:
            pasajero.nombre= nuevo_nombre
            pasajero.edad= nueva_edad
            pasajero.asiento=nuevo_asiento
            return True
        
    def eliminar(self, numero):
        """Cancela la reserva y retorna el Pasajero eliminado,
        o None si no existía."""

        if self.head is None:
            return None

        actual = self.head

        if actual.data.numero == numero:
            pasajero = actual.data
            self.head = actual.next
            self.cantidad -= 1
            return pasajero

        anterior = actual
        actual = actual.next

        while actual is not None and actual.data.numero != numero:
            anterior = actual
            actual = actual.next

        if actual is None:
            return None

        anterior.next = actual.next
        self.cantidad -= 1
        return actual.data

    def filtrar_por_clase(self, clase):
        """Retorna una list con los pasajeros de esa clase ("Ejecutiva" o
        "Económica"), en el mismo orden de la lista.
        Pista: cada pasajero sabe su clase con  pasajero.clase()"""
        resultado=[]
        actual= self.head
        
        while actual is not None:
            pasajero=actual.data
            if pasajero.clase()== clase:
                resultado.append(pasajero)
            actual=actual.next
        return resultado

    # ==========================================================
    # RETOS OPCIONALES · iremos implementándolos uno por uno
    # ==========================================================


    def contar_menores(self):
        """Cuenta los pasajeros menores de 18 años.
        Pasos:
        1. Crea un contador que empiece en 0.
        2. Coloca actual en self.head para comenzar por el primer nodo.
        3. Mientras actual no sea None, revisa actual.data.edad.
        4. Si la edad es menor que 18, aumenta el contador en 1.
        5. Avanza actual a actual.next en cada vuelta del while.
        6. Al terminar el recorrido, retorna el contador."""
        contador=0
        actual= self.head
        while actual is not None:
            if actual.data.edad<18:
                contador+=1
            actual=actual.next
        return contador

    def pasajeros_de_fila(self, fila):
        """Retorna una lista con los pasajeros de la fila indicada, en orden.
        Pasos:
        1. Crea una lista vacía llamada resultado.
        2. Coloca actual en self.head.
        3. Mientras actual no sea None, guarda el pasajero de actual.data.
        4. Obtén la fila del asiento: el número está antes de la última letra.
           Por ejemplo, en "10B" la fila es 10; conviértela a int.
        5. Si la fila del asiento coincide con el argumento fila,
           agrega el pasajero a resultado.
        6. Avanza actual a actual.next en cada vuelta del while.
        7. Al terminar el recorrido, retorna resultado."""
        resultado=[]
        actual=self.head
        while actual is not None:
            pasajero=actual.data
            fila_asiento=int(pasajero.asiento[:-1])
            if fila_asiento== fila:
                resultado.append(pasajero)
            actual=actual.next
        return resultado

    def mayor(self):
        """Retorna el pasajero de mayor edad, o None si la lista está vacía.
        Pasos:
        1. Si self.head es None, retorna None.
        2. Guarda self.head.data como el mayor provisional.
        3. Coloca actual en el siguiente nodo de la cabeza.
        4. Mientras actual no sea None, compara su edad con la del mayor provisional.
        5. Si actual.data tiene más edad, actualízalo como mayor provisional.
        6. Avanza actual a actual.next en cada vuelta del while.
        7. Al terminar el recorrido, retorna el pasajero mayor provisional."""
        if self.head is None:
            return None

        mayor= self.head.data
        actual=self.head.next
        while actual is not None:
            if actual.data.edad >mayor.edad:
                mayor= actual.data
            actual= actual.next
        return mayor

    def invertir(self):
        """Invierte los enlaces next y actualiza self.head.
        Pasos:
        1. Crea anterior = None y coloca actual en self.head.
        2. Mientras actual no sea None, guarda actual.next en una variable temporal.
        3. Haz que actual.next apunte a anterior.
        4. Avanza anterior a actual y actual al siguiente que guardaste.
        5. Al terminar, asigna anterior a self.head: será la nueva cabeza.
        6. No cambies self.cantidad. Como altera el orden, prueba este método al final.
        7. Si la lista está vacía, el ciclo no se ejecuta y head queda en None."""
        anterior=None
        actual= self.head
        while actual is not None:
            siguiente= actual.next
            actual.next=anterior
            anterior=actual
            actual=siguiente
        self.head=anterior
