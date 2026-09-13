'''
------------------------------------------------TAREA---------------------------------------------
======================================
1) Validador de notas con promedio
======================================
'''
class Calificador():
    def __init__(self):
        self.notas=[]
    def validar_nota(self, nota):
        if nota>=0 and nota<=100:
            return True
        else:
            return False
    
    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return  self.notas
    
    def promedio(self):
        return sum(self.notas)/len(self.notas)
    
calificador_notas= Calificador()
print(calificador_notas.cargar_notas(85, 92, 110, 78, -5, 88))
print(calificador_notas.promedio())


'''
======================================
2) Contador de palabras únicas
======================================

'''
class Analizador_Texto():
    def __init__(self):
        self.lista_palabras=[]
        self.conjunto=set()
    
    def agregar_palabra(self, palabra):
        if not palabra in self.conjunto:
            self.lista_palabras.append(palabra)
            self.conjunto.add(palabra)
        
    def contar_palabras(self):
        return len(self.conjunto)
    
    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)
            
analizar=Analizador_Texto()

analizar.agregar_palabra("python")
analizar.agregar_palabra("Hola")
analizar.agregar_palabra("Hola")

analizar.agregar_multiples("hola", "mundo", "python", "codigo")

print("La lsita de palabras es: ", analizar.lista_palabras)
print( "EL conjutno  palabras es: ", analizar.conjunto)
print("Las palbras total son: ", analizar.contar_palabras())

'''
======================================
3) Gestor de compras con totales
======================================
Clase CarroCompras que: 
(1) tenga método agregar_articulo(nombre, precio) que guarde en un diccionario {nombre: precio}; 
(2) tenga método total_carrito() que retorne la suma de todos los_artlista_articulos; 
(3) tenga método articulos_por_rango(precio_min, precio_max) que retorne una lista con artículos dentro del rango.

'''
class Carro_Compras:
    def __init__(self):
        self.lista_productos={}
    
    def agregar_articulo(self, nombre, precio):
        self.lista_productos[nombre]=precio
        
    def total_carrito(self):
        return sum(self.lista_productos.values())
    
    def articulos_por_rango(self, precio_min, precio_max):
        lista_articulos=[]
        for nombre, precio in self.lista_productos.items():
            if precio_min <= precio <= precio_max:
                lista_articulos.append(nombre)
                
        return lista_articulos
    
carro=Carro_Compras()

carro.agregar_articulo("pan", 1.25)
carro.agregar_articulo("aceite", 1.00)
carro.agregar_articulo("leche", 1.25)
carro.agregar_articulo("azucar", 1.25)

print("EL total del carrito es: ", carro.total_carrito())
print(carro.articulos_por_rango(1, 1.50))

'''
======================================
4) Inversor de secuencias
======================================
Clase InversorSecuencia que: 
(1) tenga método invertir_lista(lista) que retorne la lista invertida sin usar reversed() (usa manual con bucles); 
(2) tenga método invertir_multiples(*listas) que reutilice el anterior para invertir varias listas 
y retorne un diccionario {lista_original: lista_invertida}.

'''
class InversorSecuencia:
    def invertir_lista(self, lista):
        lista_invertida = []

        for indice in range(len(lista) - 1, -1, -1):
            lista_invertida.append(lista[indice])

        return lista_invertida

    def invertir_multiples(self, *listas):
        resultados = {}

        for lista in listas:
            resultados[tuple(lista)] = self.invertir_lista(lista)

        return resultados


inversor = InversorSecuencia()

print(inversor.invertir_lista([1, 2, 3, 4]))
print(inversor.invertir_multiples([1, 2, 3], ["a", "b", "c"]))


