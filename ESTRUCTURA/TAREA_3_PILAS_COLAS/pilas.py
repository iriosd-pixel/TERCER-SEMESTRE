from personas import Pasajero

class MiPila:
    def __init__(self):
        self._datos = []                       # arreglo interno

    def push(self, valor):
        """Añade al tope"""
        self._datos.append(valor)

    def pop(self):
        """Saca y retorna el del tope"""
        if self.esta_vacia():
            raise IndexError("Pila vacía")
        return self._datos.pop()

    def peek(self):
        """Mira el del tope sin sacarlo"""
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
    
    
from personas import Pasajero


class Colass:
    """Lista construida a mano sobre un arreglo de tamaño fijo.
    datos     -> [p1, p2, p3, None, None, ...]
    capacidad -> total de cajones     cantidad -> cajones ocupados
    zSin append, insert, pop, remove, sort, reverse, copy, len, in, slicing.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def añadir(self, pasajero):                      # ✅ resuelto
        if self.cantidad == self.capacidad:
            print("  ⚠ La lista está llena")
            return False
        self.datos[self.cantidad] = pasajero          # primer cajón libre
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):                                 # ✅ resuelto
        if self.cantidad == 0:
            print("  (lista vacía)")
            return
        for i in range(self.cantidad):
            print(f"  [{i}] {self.datos[i]}")



