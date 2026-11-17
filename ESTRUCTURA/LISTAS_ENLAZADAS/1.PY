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