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

    def __str__(self):
        return str(self._datos)

    def __repr__(self):
        return str(self._datos)

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

print(pila1.peek())                             # C  (no lo saca)
print(pila1.pop())                              # C  (lo saca)
print(pila1.pop())                              # B
print(pila1)   

print(pila3.peek())                             # C  (no lo saca)
print(pila3.pop())                              # C  (lo saca)
print(pila3.pop())                              # B
try:
    print(pila3.pop())
except("e"):
    print("e")
print(pila3)                                    # tope [A]

#tarea hacer el mismp procedimiento que ellos pero no usar appen, len ni anda eso, hacerlo invertido, trabajarlo como pila y como cola, los mismo metodos y poner los ejrcicios de ambas que estan en la guia, menu uno cola, menu dos pila y menu 3 lsos ejrcicios.