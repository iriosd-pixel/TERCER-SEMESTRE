'''
------------------------------------------------TAREA---------------------------------------------
======================================
1) Validador de notas con promedio
======================================
'''
#-------- ENTENDER EL PROBLEMA --------
#----Entrada: una o varias notas numericas.
#----Proceso: validar que cada nota este entre 0 y 100, guardar las validas y calcular su promedio.
#----Salida: lista de notas validas y promedio.

#-------- BOSQUEJO A MANO --------
# notas: 85, 92, 110, 78, -5, 88
# 85 y 92 son validas; 110 y -5 no se guardan.
# notas finales: [85, 92, 78, 88]
# promedio: 343 / 4 = 85.75

#-------- DESCUBRIR EL PATRON --------
# validar_nota revisa cada valor antes de que cargar_notas lo agregue a la lista.

#-------- ESCRIBIR EL CODIGO --------
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
    

#-------- PRUEBA DE ESCRITORIO --------
# Linea                         | Resultado
# ----------------------------- | ----------------------
# cargar_notas(85, 92, 110...)  | [85, 92, 78, 88]
# promedio()                    | 85.75
calificador_notas= Calificador()
print(calificador_notas.cargar_notas(85, 92, 110, 78, -5, 88))
print(calificador_notas.promedio())

'''
======================================
2) Contador de palabras únicas
======================================

'''
#-------- ENTENDER EL PROBLEMA --------
#----Entrada: una o varias palabras.
#----Proceso: guardar una palabra solo si no se repite.
#----Salida: lista y cantidad de palabras unicas.

#-------- BOSQUEJO A MANO --------
# "hola" -> se guarda.
# "hola" -> ya existe, no se guarda otra vez.
# "mundo" -> se guarda.

#-------- DESCUBRIR EL PATRON --------
# El conjunto revisa si la palabra existe y la lista conserva el orden.

#-------- ESCRIBIR EL CODIGO --------
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
            

#-------- PRUEBA DE ESCRITORIO --------
# Linea                         | Resultado
# ----------------------------- | ----------------------
# agregar_palabra("Hola")       | se agrega a la lista
# agregar_palabra("Hola")       | no se repite
# contar_palabras()              | cantidad de palabras unicas
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
#-------- ENTENDER EL PROBLEMA --------
#----Entrada: nombre y precio de productos.
#----Proceso: guardar productos, sumar precios y filtrar por rango.
#----Salida: total del carrito y lista de productos.

#-------- BOSQUEJO A MANO --------
# pan = 1.25 -> se guarda.
# aceite = 1.00 -> se guarda.
# total: 1.25 + 1.00 = 2.25.

#-------- DESCUBRIR EL PATRON --------
# El diccionario guarda el nombre del producto junto con su precio.

#-------- ESCRIBIR EL CODIGO --------
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
    

#-------- PRUEBA DE ESCRITORIO --------
# Linea                         | Resultado
# ----------------------------- | ----------------------
# agregar_articulo("pan", 1.25) | pan queda guardado
# total_carrito()                | suma los precios
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
#-------- ENTENDER EL PROBLEMA --------
#----Entrada: una o varias listas.
#----Proceso: recorrer cada lista y colocar sus elementos al reves.
#----Salida: lista invertida o diccionario de listas invertidas.

#-------- BOSQUEJO A MANO --------
# lista: [1, 2, 3]
# 1 -> [1]
# 2 -> [2, 1]
# 3 -> [3, 2, 1]

#-------- DESCUBRIR EL PATRON --------
# Cada elemento se coloca al inicio de una nueva lista.

#-------- ESCRIBIR EL CODIGO --------
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

#-------- PRUEBA DE ESCRITORIO --------
# Linea                         | Resultado
# ----------------------------- | ----------------------
# invertir_lista([1, 2, 3])     | [3, 2, 1]
# invertir_multiples(...)        | invierte cada lista
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
#-------- ENTENDER EL PROBLEMA --------
#----Entrada: varios numeros.
#----Proceso: revisar si cada numero es par o impar.
#----Salida: diccionario y cantidades de pares e impares.

#-------- BOSQUEJO A MANO --------
# 4 % 2 = 0 -> es par.
# 5 % 2 = 1 -> es impar.

#-------- DESCUBRIR EL PATRON --------
# El residuo de dividir entre 2 permite saber si un numero es par.

#-------- ESCRIBIR EL CODIGO --------
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
    

#-------- PRUEBA DE ESCRITORIO --------
# Linea                         | Resultado
# ----------------------------- | ----------------------
# separar(4, 5, 6)              | pares [4, 6], impares [5]
# cantidad_pares_impares()      | (2, 1)
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
#-------- ENTENDER EL PROBLEMA --------
#----Entrada: una o varias temperaturas.
#----Proceso: guardar temperaturas y calcular minima, maxima y promedio.
#----Salida: las tres estadisticas.

#-------- BOSQUEJO A MANO --------
# temperaturas: [25, 15, 30]
# minima: 15; maxima: 30; promedio: 70 / 3.

#-------- DESCUBRIR EL PATRON --------
# Una lista permite usar min(), max(), sum() y len().

#-------- ESCRIBIR EL CODIGO --------
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
            

#-------- PRUEBA DE ESCRITORIO --------
# Linea                         | Resultado
# ----------------------------- | ----------------------
# registrar_multiples(25,15,30) | guarda tres temperaturas
# promedio()                    | 23.33
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
#-------- ENTENDER EL PROBLEMA --------
#----Entrada: nombre y edad de personas.
#----Proceso: guardar datos, buscar mayores y calcular promedio.
#----Salida: nombres de mayores y promedio de edades.

#-------- BOSQUEJO A MANO --------
# Ana = 25 -> cumple edad minima de 18.
# Carlos = 15 -> no cumple edad minima de 18.

#-------- DESCUBRIR EL PATRON --------
# El diccionario relaciona cada nombre con su edad.

#-------- ESCRIBIR EL CODIGO --------
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
    

#-------- PRUEBA DE ESCRITORIO --------
# Linea                         | Resultado
# ----------------------------- | ----------------------
# personas_mayores(18)          | lista de nombres mayores
# edad_promedio()               | promedio de todas las edades
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
#-------- ENTENDER EL PROBLEMA --------
#----Entrada: equipos y nombres de jugadores.
#----Proceso: crear equipos, agregar jugadores y comparar cantidades.
#----Salida: nombre del equipo con mas integrantes.

#-------- BOSQUEJO A MANO --------
# Emelec: [Ana, Luis, Sol]
# Barcelona: [Carlos, Rosa]
# Emelec tiene mas jugadores.

#-------- DESCUBRIR EL PATRON --------
# El diccionario guarda cada equipo con una lista de jugadores.

#-------- ESCRIBIR EL CODIGO --------
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


#-------- PRUEBA DE ESCRITORIO --------
# Linea                         | Resultado
# ----------------------------- | ----------------------
# crear_equipo("Emelec")        | crea una lista vacia
# equipo_mayor_integrantes()    | equipo con mas jugadores
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
#-------- ENTENDER EL PROBLEMA --------
#----Entrada: un texto.
#----Proceso: contar vocales, consonantes y digitos.
#----Salida: diccionario de cantidades y texto mas largo.

#-------- BOSQUEJO A MANO --------
# "hola 1"
# vocales: o, a -> 2
# consonantes: h, l -> 2
# digitos: 1 -> 1

#-------- DESCUBRIR EL PATRON --------
# Se revisa cada caracter y se usa solo_vocales para las vocales.

#-------- ESCRIBIR EL CODIGO --------
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


#-------- PRUEBA DE ESCRITORIO --------
# Linea                         | Resultado
# ----------------------------- | ----------------------
# contar_por_tipo("hola 1")     | vocales 2, consonantes 2, digitos 1
# texto_mas_largo               | guarda el texto mas extenso
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
#-------- ENTENDER EL PROBLEMA --------
#----Entrada: descripcion y prioridad de tareas.
#----Proceso: guardar tareas, buscar las altas y eliminar una.
#----Salida: lista de tareas prioritarias o actualizada.

#-------- BOSQUEJO A MANO --------
# ("estudiar", "alta") -> se guarda.
# La prioridad "alta" aparece en tareas_prioritarias().

#-------- DESCUBRIR EL PATRON --------
# Cada tarea se guarda como una tupla dentro de una lista.

#-------- ESCRIBIR EL CODIGO --------
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


#-------- PRUEBA DE ESCRITORIO --------
# Linea                         | Resultado
# ----------------------------- | ----------------------
# agregar_tarea("estudiar","alta") | se guarda la tarea
# tareas_prioritarias()         | muestra las tareas altas
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
#-------- ENTENDER EL PROBLEMA --------
#----Entrada: elementos que pueden repetirse.
#----Proceso: contar cada elemento dentro de un diccionario.
#----Salida: elemento mas frecuente y su cantidad.

#-------- BOSQUEJO A MANO --------
# "sol" -> contador 1.
# "luna" -> contador 1.
# "sol" -> contador 2.

#-------- DESCUBRIR EL PATRON --------
# El diccionario guarda cada elemento como clave y su cantidad como valor.

#-------- ESCRIBIR EL CODIGO --------
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


#-------- PRUEBA DE ESCRITORIO --------
# Linea                         | Resultado
# ----------------------------- | ----------------------
# agregar_elemento("sol")       | sol: 1
# frecuencia_elemento("sol")    | devuelve su cantidad
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
#-------- ENTENDER EL PROBLEMA --------
#----Entrada: inicio y fin de uno o varios rangos.
#----Proceso: crear numeros de los rangos y quitar repetidos.
#----Salida: tupla o lista de numeros.

#-------- BOSQUEJO A MANO --------
# inicio = 1, fin = 3.
# resultado: (1, 2, 3).

#-------- DESCUBRIR EL PATRON --------
# range() genera los numeros y un conjunto elimina los repetidos.

#-------- ESCRIBIR EL CODIGO --------
class SelectorRango():
    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin+1))
    
    def elementos_en_multiples_rangos(self, *rangos):
        conjunto=set()
        for inicio, fin in rangos:
            for num in range(inicio, fin+1):
                conjunto.add(num)
        return list(conjunto)
    


#-------- PRUEBA DE ESCRITORIO --------
# Linea                         | Resultado
# ----------------------------- | ----------------------
# crear_rango(1, 3)             | (1, 2, 3)
# rangos (1,3) y (2,4)          | [1, 2, 3, 4]
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
#-------- ENTENDER EL PROBLEMA --------
#----Entrada: dos o mas listas.
#----Proceso: alternar los elementos de cada lista.
#----Salida: una lista combinada.

#-------- BOSQUEJO A MANO --------
# lista1: [1, 3]
# lista2: [2, 4]
# resultado: [1, 2, 3, 4].

#-------- DESCUBRIR EL PATRON --------
# Se usa el mismo indice para tomar un elemento de cada lista.

#-------- ESCRIBIR EL CODIGO --------
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
    

#-------- PRUEBA DE ESCRITORIO --------
# Linea                         | Resultado
# ----------------------------- | ----------------------
# intercalar([1,3], [2,4])      | [1, 2, 3, 4]
# intercalar_multiples(...)     | combina todas las listas
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
#-------- ENTENDER EL PROBLEMA --------
#----Entrada: estudiante y nota.
#----Proceso: guardar notas, buscar aprobados y la nota mayor.
#----Salida: lista de aprobados y mejor estudiante.

#-------- BOSQUEJO A MANO --------
# Ana = 8 -> aprueba con minimo 7.
# Luis = 5 -> no aprueba con minimo 7.

#-------- DESCUBRIR EL PATRON --------
# Un diccionario relaciona el estudiante con su nota.

#-------- ESCRIBIR EL CODIGO --------
class RegistroNotas():
    def __init__(self):
        self.dic_notas={}
    
    def registrar(self, estudiante, nota):
        self.dic_notas[estudiante]=nota
    
    def estudiantes_aprobados(self, nota_minima):
        estudiantes_pasados=[]
        for estudiante, nota in self.dic_notas.items():
            if nota >= nota_minima:
                estudiantes_pasados.append(estudiante)
        return estudiantes_pasados
    
    def mejor_estudiante(self):
        if not self.dic_notas:
            return None
        
        mejor_estudiante=-1
        nombre_estudiante=""
        for estudiante, nota in self.dic_notas.items():
            if nota > mejor_estudiante:
                mejor_estudiante=nota
                nombre_estudiante=estudiante
        return nombre_estudiante
    

#-------- PRUEBA DE ESCRITORIO --------
# Linea                         | Resultado
# ----------------------------- | ----------------------
# registrar("Ana", 8)          | guarda la nota de Ana
# estudiantes_aprobados(7)      | lista de aprobados
rn= RegistroNotas()

rn.registrar("soria", 6)
rn.registrar("axel", 5)
rn.registrar("carlos", 2)
rn.registrar("Ismael", 10)

print(rn.estudiantes_aprobados(5))
print(rn.mejor_estudiante())

''''
======================================
15: DIVISORES DE UN NÚMERO
======================================
Clase DivisorFinder que: 
(1) tenga método encontrar_divisores(numero) que retorne una tupla con todos los divisores; 
(2) tenga método es_perfecto(numero) que retorne True si la suma de sus divisores (excepto él mismo) es igual a él; 
(3) tenga método encontrar_multiples_divisores(*numeros) que retorne un diccionario {número: tupla_divisores}.
'''
#-------- ENTENDER EL PROBLEMA --------
#----Entrada: uno o varios numeros.
#----Proceso: encontrar divisores y verificar si un numero es perfecto.
#----Salida: tuplas o diccionario de divisores.

#-------- BOSQUEJO A MANO --------
# numero: 6
# divisores: 1, 2, 3, 6.
# 1 + 2 + 3 = 6, por eso es perfecto.

#-------- DESCUBRIR EL PATRON --------
# Un numero es divisor cuando el residuo de la division es cero.

#-------- ESCRIBIR EL CODIGO --------
class DivisorFinder():
    def encontrar_divisores(self, numero):
        divisores=[]
        for i in range(1, numero+1):
            if numero %i==0:
                divisores.append(i)
        return tuple(divisores)
    
    def es_perfecto(self, numero):
        divisores= self.encontrar_divisores(numero)
        divisores_propio= divisores[:-1]
        return sum(divisores_propio)==numero
    
    def encontrar_multiples_divisores(self, *numeros):
        resultados={}
        for num in numeros:
            resultados[num]=self.encontrar_divisores(num)
        return resultados
    

#-------- PRUEBA DE ESCRITORIO --------
# Linea                         | Resultado
# ----------------------------- | ----------------------
# encontrar_divisores(6)        | (1, 2, 3, 6)
# es_perfecto(6)                | True
df=DivisorFinder()
print(df.encontrar_divisores(10))
print(df.es_perfecto(6))
print(df.encontrar_multiples_divisores(8,9,10,20))

''''
======================================
16: Codificador/Decodificador
======================================

Clase CodificadorCesar que: 
(1) tenga método codificar_letra(letra, desplazamiento) que retorne la letra desplazada en el alfabeto (usar operador %); 
(2) tenga método codificar_palabra(palabra, desplazamiento) que reutilice para toda la palabra; 
(3) tenga un diccionario como atributo para historial de codificaciones.
'''
#-------- ENTENDER EL PROBLEMA --------
#----Entrada: letra o palabra y desplazamiento.
#----Proceso: mover cada letra dentro del alfabeto.
#----Salida: texto codificado e historial.

#-------- BOSQUEJO A MANO --------
# letra: "a", desplazamiento: 3.
# nueva letra: "d".

#-------- DESCUBRIR EL PATRON --------
# El operador % permite volver al inicio despues de la letra z.

#-------- ESCRIBIR EL CODIGO --------
class CodificadorCesar:

    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        if "a" <= letra <= "z":
            posicion_original = ord(letra) - ord("a")
            nueva_posicion = (posicion_original + desplazamiento) % 26
            return chr(nueva_posicion + ord("a"))
        elif "A" <= letra <= "Z":
            posicion_original = ord(letra) - ord("A")
            nueva_posicion = (posicion_original + desplazamiento) % 26
            return chr(nueva_posicion + ord("A"))
        else:
            return letra

    def codificar_palabra(self, palabra, desplazamiento):
        palabra_codificada = ""

        for caracter in palabra:
            palabra_codificada += self.codificar_letra(caracter, desplazamiento)
        self.historial[palabra] = palabra_codificada

        return palabra_codificada


#-------- PRUEBA DE ESCRITORIO --------
# Linea                         | Resultado
# ----------------------------- | ----------------------
# codificar_letra("a", 3)      | "d"
# codificar_letra("z", 1)      | "a"
codificador = CodificadorCesar()

print("--- PRUEBA 1: Letras individuales ---")
print("Letra 'a' con desplazamiento 3  ->", codificador.codificar_letra("a", 3))  
print("Letra 'z' con desplazamiento 1  ->", codificador.codificar_letra("z", 1)) 
print("Letra 'Z' con desplazamiento 3  ->", codificador.codificar_letra("Z", 3))

print("\n--- PRUEBA 2: Palabras completas ---")
resultado1 = codificador.codificar_palabra("python", 3)
print("Palabra 'python' (k=3) ->", resultado1)

resultado2 = codificador.codificar_palabra("Hola Mundo", 5)
print("Palabra 'Hola Mundo' (k=5) ->", resultado2)

print("\n--- PRUEBA 3: Historial de codificaciones ---")
print("Historial registrado:", codificador.historial)

''''
======================================
17: Grupo de edades
======================================
Clase AgrupadorEdades que: 
(1) tenga método clasificar_edad(edad) que retorne la categoría ("niño", "adolescente", "adulto", "mayor"); 
(2) tenga método agrupar_por_categoria(*edades) que retorne un diccionario con {categoría: [edades]}; 
(3) tenga método edad_promedio_categoria(categoria).
'''
#-------- ENTENDER EL PROBLEMA --------
#----Entrada: varias edades.
#----Proceso: clasificar cada edad y agruparla por categoria.
#----Salida: diccionario de categorias y promedios.

#-------- BOSQUEJO A MANO --------
# 5 -> nino.
# 14 -> adolescente.
# 20 -> adulto.

#-------- DESCUBRIR EL PATRON --------
# Las condiciones if determinan la categoria de cada edad.

#-------- ESCRIBIR EL CODIGO --------
class AgrupadorEdades():
    def __init__(self):
        self.categoria={}
         
    def clasificar_edad(self, edad):
        if edad>=65:
            return "mayor"
        elif edad <65 and edad>=18:
            return "bebe"
        elif edad<18 and edad >=12:
            return "adolescente"
        elif edad <12 and edad>=0:
            return "niño"
        else:
            return "la edad ingresada no es valida"
    
    def agrupar_por_categoria(self, *edades):
        self.categoria={}
        for edad in edades:
            categoria_edad= self.clasificar_edad(edad)
            if categoria_edad not in self.categoria:
                self.categoria[categoria_edad]=[]
            self.categoria[categoria_edad].append(edad)
        return self.categoria
    
    def edad_promedio_categoria(self, categoria):
        if categoria in self.categoria:
            lista_edades= self.categoria[categoria]
            return sum(lista_edades)/len(lista_edades)
        return f"No hay datos registrados para la categoría '{categoria}'"


#-------- PRUEBA DE ESCRITORIO --------
# Linea                         | Resultado
# ----------------------------- | ----------------------
# clasificar_edad(5)            | "nino"
# agrupar_por_categoria(5,14,20)| diccionario de categorias
ae=AgrupadorEdades()

print( ae.agrupar_por_categoria(19))
print(ae.agrupar_por_categoria(5,10,18,50,14))
print(ae.edad_promedio_categoria("adolescente"))

''''
======================================
18: Matriz de distancias
======================================
Clase CalculadorDistancia que: 
(1) tenga método distancia_euclidiana(p1, p2) que reciba dos tuplas (x,y) y calcule la distancia; 
(2) tenga método punto_mas_cercano(referencia, *puntos) que retorne el punto más cercano a referencia; 
(3) tenga un atributo lista para guardar todas las distancias calculadas.
'''
#-------- ENTENDER EL PROBLEMA --------
#----Entrada: dos puntos o varios puntos.
#----Proceso: calcular distancias y comparar cual es menor.
#----Salida: distancia y punto mas cercano.

#-------- BOSQUEJO A MANO --------
# p1 = (0, 0), p2 = (3, 4).
# distancia: raiz de 9 + 16 = 5.

#-------- DESCUBRIR EL PATRON --------
# Se aplica la formula de distancia euclidiana.

#-------- ESCRIBIR EL CODIGO --------
class CalculadorDistancia:
    def __init__(self):
        self.lista_distancias = []

    def distancia_euclidiana(self, p1, p2):
        x1 = p1[0]
        y1 = p1[1]

        x2 = p2[0]
        y2 = p2[1]
        
        diferencia_x = (x2 - x1) ** 2
        diferencia_y = (y2 - y1) ** 2
        distancia = (diferencia_x + diferencia_y) ** 0.5
        self.lista_distancias.append(distancia)
        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        punto_cercano = None
        distancia_minima = 999999.0

        for punto in puntos:
            dist = self.distancia_euclidiana(referencia, punto)

            if dist < distancia_minima:
                distancia_minima = dist
                punto_cercano = punto

        return punto_cercano



#-------- PRUEBA DE ESCRITORIO --------
# Linea                         | Resultado
# ----------------------------- | ----------------------
# distancia_euclidiana((0,0),(3,4)) | 5
# punto_mas_cercano((0,0),...)  | punto con menor distancia
cd = CalculadorDistancia()

print(
    "Ej 18 - Distancia entre (0,0) y (3,4):",
    cd.distancia_euclidiana((0, 0), (3, 4)),
)
print(
    "Ej 18 - Punto más cercano a (0,0):",
    cd.punto_mas_cercano((0, 0), (5, 5), (1, 2), (8, 8)),
)
print("Ej 18 - Lista de distancias calculadas:", cd.lista_distancias)

''''
======================================
19: Inventario de productos
======================================
Clase Inventario que: 
(1) tenga método agregar_stock(producto, cantidad) que guarde en un diccionario; 
(2) tenga método restar_stock(producto, cantidad) que disminuya y retorne True si hay suficiente; 
(3) tenga método productos_bajo_stock(minimo) que retorne una lista de productos con cantidad < minimo.
'''
#-------- ENTENDER EL PROBLEMA --------
#----Entrada: producto, cantidad y minimo.
#----Proceso: aumentar o restar stock y revisar existencias bajas.
#----Salida: confirmacion y lista de productos bajos.

#-------- BOSQUEJO A MANO --------
# pan = 10.
# restar 3 -> pan queda con 7.

#-------- DESCUBRIR EL PATRON --------
# Un diccionario guarda el producto junto a su cantidad.

#-------- ESCRIBIR EL CODIGO --------
class Inventario():
    def __init__(self):
        self.dic_productos={}
    
    def agregar_stock(self, producto, cantidad):
        if producto  in self.dic_productos:
            self.dic_productos[producto]= self.dic_productos[producto]+cantidad
        else:
            self.dic_productos[producto]=cantidad
    
    def restar_stock(self, producto, cantidad):
        if producto in self.dic_productos:
            cantidad_actual= self.dic_productos[producto]
            if cantidad_actual>= cantidad:
                self.dic_productos[producto]-=cantidad
                return True
            else:
                return False
        else:
            return False
    
    def productos_bajo_stock(self, minimo):
        lista_bajos=[]
        for producto, cantidad in self.dic_productos.items():
            if cantidad < minimo:
                lista_bajos.append(producto)
        return lista_bajos
    

#-------- PRUEBA DE ESCRITORIO --------
# Linea                         | Resultado
# ----------------------------- | ----------------------
# agregar_stock("pan", 10)     | pan: 10
# restar_stock("pan", 3)       | True y pan queda en 7
inv= Inventario()

inv.agregar_stock("aceite", 10)
inv.agregar_stock("pan", 50)
print(inv.restar_stock("pan", 20))
print(inv.productos_bajo_stock(11))

''''
======================================
20: Analizador de patrones en textos
======================================
Clase AnalizadorPatrones que: 
(1) tenga método encontrar_palabras(texto, patron) que busque palabras que inicien con el patrón y retorne una lista; 
(2) tenga método agrupar_por_longitud(texto) que retorne un diccionario {longitud: [palabras]}; 
(3) tenga método palabras_unicas() usando un conjunto.
'''
#-------- ENTENDER EL PROBLEMA --------
#----Entrada: un texto y, cuando sea necesario, un patron.
#----Proceso: buscar palabras, agruparlas por longitud y quitar repetidas.
#----Salida: listas, diccionario o conjunto de palabras.

#-------- BOSQUEJO A MANO --------
# texto: "casa carro sol".
# patron: "ca".
# palabras encontradas: ["casa", "carro"].

#-------- DESCUBRIR EL PATRON --------
# Se separa el texto en palabras y un conjunto permite obtener las unicas.

#-------- ESCRIBIR EL CODIGO --------
class AnalizadorPatrones:
    def encontrar_palabras(self, texto, patron):
        palabras=texto.split()
        lista_palabras=[]
        for palabra in palabras:
            if palabra.startswith(patron):
                lista_palabras.append(palabra)
        return lista_palabras

    def agrupar_por_longitud(self, texto):
        lista_palabras = texto.split()
        dic_longitudes = {}

        for palabra in lista_palabras:
            largo = len(palabra)
            if largo in dic_longitudes:
                dic_longitudes[largo].append(palabra)
            else:
                dic_longitudes[largo] = [palabra]
        return dic_longitudes
    
    def palabras_unicas(self, texto):
        lista_palabras = texto.split()
        conjunto_unicos = set()
        for palabra in lista_palabras:
            conjunto_unicos.add(palabra)
        return conjunto_unicos
    

#-------- PRUEBA DE ESCRITORIO --------
# Linea                         | Resultado
# ----------------------------- | ----------------------
# encontrar_palabras(texto,"ca")| ["casa", "carro"]
# palabras_unicas(texto)        | conjunto sin repetidas
analizador = AnalizadorPatrones()
texto_ejemplo = "el perro de pedro juega con otro perro en el parque"

print("--- PRUEBA 1: Encontrar palabras que inician con 'pe' ---")
print(analizador.encontrar_palabras(texto_ejemplo, "pe"))
print("\n--- PRUEBA 2: Agrupar palabras por longitud ---")
print(analizador.agrupar_por_longitud("hola sol luna"))
print("\n--- PRUEBA 3: Palabras únicas ---")
print(analizador.palabras_unicas(texto_ejemplo))
