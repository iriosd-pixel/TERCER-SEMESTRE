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
    def __init__(self):
        self.numeros_pares_impares={'Pares':[], 'Impares':[]}

    def es_par(self, numero):
        if numero%2==0:
            return True
        else:
            return False
    
    def separar(self, *numeros):
        self.numeros_pares_impares={'Pares':[], 'Impares':[]}
        for numero in numeros:
            if self.es_par(numero):
                self.numeros_pares_impares['Pares'].append(numero)
            else:
                self.numeros_pares_impares['Impares'].append(numero)
        return self.numeros_pares_impares

    def cantidad_pares_impares(self):
        cantidad_pares=len(self.numeros_pares_impares['Pares'])
        cantidad_impares=len(self.numeros_pares_impares['Impares'])
        return cantidad_pares, cantidad_impares
    
todos= AnalizadorNumeros()

print(todos.separar(4,5,6,7,8,9,10,11,12))
print(todos.cantidad_pares_impares())

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
print("La temperatura minima es: ", gt.minima())
print("La temperatura maxima es: ", gt.maxima())
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
8) Asignador de equipos
======================================
Clase Equipos que: 
(1) tenga método crear_equipo(nombre_equipo) que inicie un equipo como una lista vacía en un diccionario; 
(2) tenga método agregar_jugador(equipo, jugador) que añada el jugador al equipo; 
(3) tenga método equipo_mayor_integrantes() que retorne el nombre del equipo con más jugadores.
'''
class Equipos():
    def __init__(self):
        self.dic_equipos={}
        
    def crear_equipo(self, nombre_equipo):
        self.dic_equipos[nombre_equipo]=[]
        return self.dic_equipos
    
    def agregar_jugador(self, equipo, jugador):
        if equipo in self.dic_equipos:
            self.dic_equipos[equipo].append(jugador)
            
    
    def equipo_mayor_integrantes(self):
        max_juagores=-1
        equipo_lider=" "
        for equipo, jugadores in self.dic_equipos.items():
            if len(jugadores)> max_juagores:
                max_juagores=len(jugadores)
                equipo_lider=equipo
        return equipo_lider

eq=Equipos()

eq.crear_equipo("Emelec")
eq.crear_equipo("Barcelona")


eq.agregar_jugador("Emelec", "Axel")
eq.agregar_jugador("Emelec", "Linda")
eq.agregar_jugador("Emelec", "Carlos")
eq.agregar_jugador("Emelec", "Ismael")
eq.agregar_jugador("Barcelona", "Carlos")
eq.agregar_jugador("Barcelona", "Luis")

print(eq.dic_equipos)
print(eq.equipo_mayor_integrantes())


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

'''
======================================
10) Gestor de tareas con prioridad
======================================
 Clase Tareas
1. Tenga un método `agregar_tarea(descripcion, prioridad)` que guarde las tareas en una lista de tuplas `(descripción, prioridad)`.
2. Tenga un método `tareas_prioritarias()` que retorne únicamente las tareas cuya prioridad sea **alta**.
3. Tenga un método `eliminar_completada(descripcion)` que elimine de la lista una tarea según su descripción.
'''
class tareas():
    def __init__(self):
        self.lista_tareas=[]

    def agregar_tarea(self, descripcion, prioridad):
        lista_tuplas= (descripcion, prioridad)
        self.lista_tareas.append(lista_tuplas)

    def tareas_prioritarias(self):
        lista_prioritaria=[]
        for descripcion, prioridad in self.lista_tareas:
            if prioridad.lower() =="alta":
                lista_prioritaria.append(descripcion)
        return lista_prioritaria

    def eliminar_completada(self, descripcion):
        for tarea in self.lista_tareas:
            desc=tarea[0]
            if desc == descripcion:
                self.lista_tareas.remove(tarea)
                break
        return self.lista_tareas

ta= tareas()

ta.agregar_tarea("pasar materia de proramacion", "alta")
ta.agregar_tarea("termianr ecuaciones", "media")
ta.agregar_tarea("estudiar ecuacones", "alta")

print(ta.tareas_prioritarias())
print(ta.eliminar_completada("termianr ecuaciones"))

''''
======================================
11) Gestor de tareas con prioridad
======================================
Crear una clase `ContadorFrecuencia` que:
1. Tenga un método `agregar_elemento(elemento)` que guarde elementos en un diccionario contando cuántas veces se repiten.
2. Tenga un método `elemento_mas_frecuente()` que retorne el elemento que tenga la mayor frecuencia.
3. Tenga un método `frecuencia_elemento(elemento)` que retorne cuántas veces aparece un elemento.
'''
class ContadorFrecuencia():
    def __init__(self):
        self.lista_elementos={}

    def agregar_elemento(self, elemento):
        if elemento in self.lista_elementos:
            self.lista_elementos[elemento]+=1
        else:
            self.lista_elementos[elemento]=1

    def elemento_mas_frecuente(self):
        ele_mayor=None
        mayor=0
        for elemento, cantidad in self.lista_elementos.items():
            if cantidad> mayor:
                mayor=cantidad
                ele_mayor=elemento
        return ele_mayor

    def frecuencia_elemento(self, elemento):
        for ele, cantidad in self.lista_elementos.items():
            if ele== elemento:
                return cantidad
        return 0

cf=ContadorFrecuencia()

cf.agregar_elemento("mercurio")
cf.agregar_elemento("uranio")
cf.agregar_elemento("pluton")
cf.agregar_elemento("mercurio")
cf.agregar_elemento("potasio")
cf.agregar_elemento("mercurio")

print("el elemnto mas frecuente es: ", cf.elemento_mas_frecuente())
print("Se reite:", cf.frecuencia_elemento("mercurio"), " veces")

''''
======================================
12) SELECTOR DE RANGO CON TUPLAS
======================================
Clase SelectorRango que: 
(1) tenga método crear_rango(inicio, fin) que retorne una tupla con números en ese rango; 
(2) tenga método elementos_en_multiples_rangos(*rangos) que reciba múltiples tuplas (inicio,fin) y retorne una lista combinada 
sin duplicados usando un conjunto.
'''
class SelectorRango():
    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin+1))
    
    def elementos_en_multiples_rangos(self, *rangos):
        conjunto=set()
        for inicio, fin in rangos:
            for num in range(inicio, fin+1):
                conjunto.add(num)
        return list(conjunto)
    

sr=SelectorRango()

print(sr.crear_rango(1, 10))
print(sr.elementos_en_multiples_rangos((1, 5), (4, 8),(3, 20)))

''''
======================================
13) Combinador de listas
======================================
Clase CombinadorListas que: 
(1) tenga método intercalar(lista1, lista2) que retorne una lista alternando elementos de ambas; 
(2) tenga método intercalar_multiples(*listas) que reutilice para varias listas.
'''
class CombinadorListas():
    def intercalar(self, lista1, lista2):
        resultado=[]
        largo1=len(lista1)
        largo2=len(lista2)
        lar_maximo=largo1
        
        if largo2>lar_maximo:
            lar_maximo=largo2
        
        for i in range(lar_maximo):
            if i<len(lista1):
                resultado.append(lista1[i])
            if i <len(lista2):
                resultado.append(lista2[i])
        return resultado
    
    def intercalar_multiples(self, *listas):
        lar_maximo=0
        resultados=[]
        
        for lista in listas:
            if len(lista)>lar_maximo:
                lar_maximo=len(lista)

        for i in range(lar_maximo):
            for lista in listas:
                if i < len(lista):
                    resultados.append(lista[i])
        return resultados
    
cl=CombinadorListas()

print(cl.intercalar([1,3,5,7,9], [2,4,6,8,10]))
print(cl.intercalar_multiples([1,3,5,7,9], [2,4,6,8,10], [11,13,15,17,19], [12,14,16,18,20]))

''''
======================================
14) Mapeo de estudiantes a notas
======================================
Clase RegistroNotas que: 
(1) tenga método registrar(estudiante, nota) que guarde en un diccionario; 
(2) tenga método estudiantes_aprobados(nota_minima) que retorne lista de estudiantes; 
(3) tenga método mejor_estudiante() que retorne nombre y nota del que tiene mayor calificación.
'''
class RegistroNotas():
    def registrar(estudiante, nota):
        pass
    
    def estudiantes_aprobados(nota_minima):
        pass
    
    def mejor_estudiante():
        pass