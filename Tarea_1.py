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
'''
class InversorSecuencia:
    def invertir_lista(self, lista):
        lista_invertida = []

        for indice in lista:
            lista_invertida= [indice]+lista_invertida

        return lista_invertida

    def invertir_multiples(self, *listas):
        resultados = {}

        for lista in listas:
            llave=tuple(lista)
            valor=self.invertir_lista(lista)
            resultados[llave]=valor

        return resultados
inversor = InversorSecuencia()

print(inversor.invertir_lista([1, 2, 3, 4]))
print(inversor.invertir_multiples([1, 2, 3], ["a", "b", "c"]))

'''
======================================
5) Detector de números pares e impares
======================================
Clase AnalizadorNumeros que: (1) tenga método es_par(numero) que retorne True/False; 
(2) tenga método separar(*numeros) que retorne un diccionario {'pares': [...], 'impares': [...]} reutilizando es_par; 
(3) tenga método cantidad_pares_impares() que retorne una tupla (cant_pares, cant_impares).
'''
class AnalizadorNumeros():
    def es_par(self, numero):
        if numero%2==0:
            return True
        else:
            return False
    
    def separar(self, *numeros):
        numeros_pares_impares={'Pares':[], 'Impares':[]}
        for numero in numeros:
            if self.es_par(numero):
                numeros_pares_impares['Pares'].append(numero)
            else:
                numeros_pares_impares['Impares'].append(numero)
        return numeros_pares_impares
    
todos= AnalizadorNumeros()

todos.separar(4,5,6,7,8,9,10,11,12)

'''
======================================
6) Estadísticas de temperatura
======================================
Clase GestorTemperatura que: (1) tenga método registrar_temperatura(temp) que guarde en una lista; 
(2) tenga método minima()`, `maxima()`, `promedio() que calculen estadísticas; 
(3) tenga método registrar_multiples(*temps) que reutilice el registro para varias temperaturas.
'''
class GestorTemperatura():
    def __init__(self):
        self.lista_temperaturas=[]
    
    def registrar_temperatura(self, temp):
        self.lista_temperaturas.append(temp)
        
    def  minima(self):
        return min(self.lista_temperaturas)
    
    def maxima(self):
        return max(self.lista_temperaturas)
    
    def promedio(self):
        return sum(self.lista_temperaturas)/len(self.lista_temperaturas)
    
    def registrar_multiples(self, *temps):
        for temp in temps:
            self.registrar_temperatura(temp)
            
gt=GestorTemperatura()

gt.registrar_temperatura(25)
gt.registrar_multiples(15,16,15,14,30)
print("La temperatura maxima es: ", gt.minima())
print("La temperatura minima es: ", gt.maxima())
print("El promedio es: ", gt.promedio())


'''
======================================
7) Mapeador de edades
======================================
Clase GestorPersonas que: (1) tenga método agregar_persona(nombre, edad) que guarde en un diccionario; 
(2) tenga método personas_mayores(edad_minima) que retorne una lista de nombres cuya edad sea ≥; 
(3) tenga método edad_promedio() que retorne el promedio de edades.

'''
class GestorPersonas():
    def __init__(self):
        self.persona={}
    
    def agregar_persona(self, nombre, edad):
        self.persona[nombre]=edad
    
    def personas_mayores(self, edad_minima):
        self.lista_nombres=[]
        for nombre, edad in self.persona.items():
            if edad>=edad_minima:
                self.lista_nombres.append(nombre)
        return self.lista_nombres
    
    def edad_promedio(self):
        total_edades=sum(self.persona.values())
        cantidad_personas=len(self.persona)
        return total_edades/cantidad_personas
    
Gp= GestorPersonas()

Gp.agregar_persona("Ismael", 19)
Gp.agregar_persona("Ana", 25)
Gp.agregar_persona("Carlos", 15)
Gp.agregar_persona("Rosa", 75)

print("La edad minima es 18: ", Gp.personas_mayores(18))
print("El promedio de edades es: ", Gp.edad_promedio())








'''
======================================
9) Validador de caracteres
======================================
Clase AnalizadorString que: (1) tenga método solo_vocales(letra) que retorne True si es vocal; 
(2) tenga método contar_por_tipo(texto) que retorne un diccionario {'vocales': cant, 'consonantes': cant, 'digitos': cant} reutilizando métodos; 
(3) tenga atributo que guarde el texto más largo analizado.
'''

class AnalizadorString():
    def __init__(self):
        self.texto_mas_largo=""
    
    def solo_vocales(self, letras):
            if letras.lower() in "aeiou":
                return True
            else:
                return False
    
    def contar_por_tipo(self, texto):
        contadores={'vocales': 0, 'consonantes':0, 'digitos':0}
        for letra in texto:
            letra_minuscula= letra.lower()
            if self.solo_vocales(letra):
                contadores['vocales']+=1
            elif (letra_minuscula >="a" and letra_minuscula <="z") or letra_minuscula=="ñ":
                contadores['consonantes']+=1
            elif letra>= '0' and letra<= '9':
                contadores['digitos']+=1
        if len(texto)>len(self.texto_mas_largo):
            self.texto_mas_largo=texto
        return contadores

As=AnalizadorString()

print("Analisis 1",As.contar_por_tipo("hola como estas Ismael? tienes 19 años me gusta el numero 11"))
print("Analisis 2",As.contar_por_tipo("hola mundo, 123"))

print("EL texto mas largo es: ", As.texto_mas_largo)