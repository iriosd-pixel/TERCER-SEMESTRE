from pasajero import Pasajero


class MiCola:
    """Cola (FIFO) hecha a mano sobre un arreglo de tamaño fijo.
    datos  -> [FRENTE, ..., FINAL, None, None]
    FRENTE -> datos[0]             (el primero que llegó: el único que sale)
    FINAL  -> datos[cantidad - 1]  (los nuevos se ponen detrás de él)
    ⛔ Mismas prohibiciones que MiLista: sin append, pop, insert, remove, index,
    sort, reverse, copy, len(), in, slicing ni comprensiones.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def encolar(self, pasajero):                     # ✅ resuelto (= añadir de MiLista)
        if self.buscar(pasajero.numero)!=-1:
            print("Ya existe un pasajero con ese numero")
            return False
        
        if self.buscar_cedula(pasajero.cedula)!= -1:
            print("Ya existe un pasajero con esa cedula")
            return False
        
        if self.cantidad == self.capacidad:
            print("  ⚠ La cola está llena")
            return False
        
        self.datos[self.cantidad] = pasajero          # se pone a la fila por detrás
        self.cantidad += 1
        return True

    def listar(self):                                 # ✅ EJEMPLO: del FRENTE al FINAL
        if self.esta_vacia():
            print("  (Cola vacia)")
            return
        
        for i in range(self.cantidad):                # 0, 1, ..., cantidad-1  (hacia adelante)
            if i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FRENTE")
            elif i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← FINAL")
            else:
                print(f"  [{i}] {self.datos[i]}")

    # ------- ✍ IMPLEMENTA (tabla 3) · recorre SIEMPRE del frente al final -------
    def desencolar(self):
        if self.esta_vacia():
            print("La cola esta vacia")
            return None
        
        pasajero=self.datos[0]
        for i in range(self.cantidad-1):
            self.datos[i]=self.datos[i+1]
        
        self.datos[self.cantidad-1]=None
        self.cantidad-=1
        return pasajero

    def ver_frente(self):
        if self.esta_vacia():
            return None
        
        return self.datos[0]

    def buscar(self, numero):
        for i in range(self.cantidad):
            if self.datos[i].numero==numero:
                return i
        return -1
    
    def buscar_cedula(self, cedula):
        for i in range(self.cantidad):
            if self.datos[i].cedula== cedula:
                return i
        return -1
    
    def ordenar_asc(self):
        copia=self.copiar()
        posiciones= [None]*self.cantidad
        
        for i in range(self.cantidad):
            posiciones[i]=i
        
        for vuelta in range(self.cantidad-1):
            for i in range(self.cantidad-1):
                if copia.datos[i].numero> copia.datos[i+1].numero:
                    aux= copia.datos[i]
                    copia.datos[i]=copia.datos[i+1]
                    copia.datos[i+1]=aux
                    
                    aux_posicion=posiciones[i]
                    posiciones[i]=posiciones[i+1]
                    posiciones[i+1]=aux_posicion
        return copia, posiciones
    
    def busqueda_binaria(self, numero):
        copia, posiciones= self.ordenar_asc()
        
        izquierda=0
        derecha= copia.cantidad-1
        
        while izquierda <= derecha:
            medio=(izquierda+derecha)//2
            numero_medio= copia.datos[medio].numero
            
            if numero_medio == numero:
                return posiciones[medio]
            elif numero_medio<numero:
                izquierda=medio+1
            else:
                derecha=medio-1
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        posicion= self.buscar(numero)
        
        if posicion==-1:
            print(f"NO exitse un pasajero con el numero { numero}")
            return False
        self.datos[posicion].destino=nuevo_destino
        self.datos[posicion].asiento=nuevo_asiento
        return True

    def eliminar_por_numero(self, numero):
        if self.esta_vacia():
            print("la cola esta vacia")
            return False
        
        if self.buscar(numero)==-1:
            print(f"NO existe el pasajero con el numero {numero}")
            return False
        
        cantidad_inicial= self.cantidad
        
        for i in range(cantidad_inicial):
            pasajero=self.desencolar()
            
            if pasajero.numero != numero:
                self.encolar(pasajero)
                
        return True
    
    def copiar(self):
        nueva= MiCola(self.capacidad)
        
        for i in range(self.cantidad):
            nueva.encolar(self.datos[i])
        
        return nueva

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad==0
    
    def filtrar_mayores_de_edad(self):
        resultado=MiCola(self.capacidad)
        
        for i in range(self.cantidad):
            pasajero= self.datos[i]
            
            if pasajero.es_mayor_de_edad():
                resultado.encolar(pasajero)
        return resultado
    
    def nombres_en_mayusculas(self):
        nombres= [None]*self.cantidad
        
        for i in range(self.cantidad):
            nombres[i]= self.datos[i].nombre.upper()
        
        return nombres