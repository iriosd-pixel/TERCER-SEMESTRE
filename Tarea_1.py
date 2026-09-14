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




'''''
#======================================
# Ej. 10: Gestor de tareas con prioridad
# Clase Tareas que: 
# (1) tenga método agregar_tarea(descripcion, prioridad) que guarde en una lista de tuplas (descripción, prioridad); 
# (2) tenga método tareas_prioritarias() que retorne solo las de prioridad alta; 
# (3) tenga método eliminar_completada(descripcion) que borre la tarea de la lista.
#======================================
class Tareas():
    def __init__(self):
        self.lista_tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        tupla_tarea = (descripcion, prioridad)
        self.lista_tareas.append(tupla_tarea)

    def tareas_prioritarias(self):
        lista_prioritarias = []
        for tarea in self.lista_tareas:
            prioridad = tarea[1]
            if prioridad == "alta":
                lista_prioritarias.append(tarea)
        return lista_prioritarias

    def eliminar_completada(self, descripcion):
        for tarea in self.lista_tareas:
            desc = tarea[0]
            if desc == descripcion:
                self.lista_tareas.remove(tarea)
                break


# Pruebas Ejercicio 10
t = Tareas()
t.agregar_tarea("Estudiar", "alta")
t.agregar_tarea("Leer", "baja")
print("Ej 10 - Tareas prioritarias:", t.tareas_prioritarias())
t.eliminar_completada("Leer")
print("Ej 10 - Lista tras eliminar 'Leer':", t.lista_tareas)


#======================================
# Ej. 11: Contador de frecuencia
# Clase ContadorFrecuencia que: 
# (1) tenga método agregar_elemento(elemento) que guarde en un diccionario contando repeticiones; 
# (2) tenga método elemento_mas_frecuente() que retorne el elemento con mayor frecuencia; 
# (3) tenga método frecuencia_elemento(elemento) que retorne cuántas veces aparece.
#======================================
class ContadorFrecuencia():
    def __init__(self):
        self.dic_frecuencias = {}

    def agregar_elemento(self, elemento):
        if elemento in self.dic_frecuencias:
            self.dic_frecuencias[elemento] = self.dic_frecuencias[elemento] + 1
        else:
            self.dic_frecuencias[elemento] = 1

    def elemento_mas_frecuente(self):
        elemento_mayor = None
        max_conteo = -1
        for elemento, conteo in self.dic_frecuencias.items():
            if conteo > max_conteo:
                max_conteo = conteo
                elemento_mayor = elemento
        return elemento_mayor

    def frecuencia_elemento(self, elemento):
        if elemento in self.dic_frecuencias:
            return self.dic_frecuencias[elemento]
        else:
            return 0


# Pruebas Ejercicio 11
cf = ContadorFrecuencia()
cf.agregar_elemento("a")
cf.agregar_elemento("b")
cf.agregar_elemento("a")
print("Ej 11 - Elemento más frecuente:", cf.elemento_mas_frecuente())
print("Ej 11 - Frecuencia de 'a':", cf.frecuencia_elemento("a"))


#======================================
# Ej. 12: Selector de rango con tuplas
# Clase SelectorRango que: 
# (1) tenga método crear_rango(inicio, fin) que retorne una tupla con números en ese rango; 
# (2) tenga método elementos_en_multiples_rangos(*rangos) que reciba múltiples tuplas (inicio,fin) y retorne una lista combinada sin duplicados usando un conjunto.
#======================================
class SelectorRango():
    def crear_rango(self, inicio, fin):
        lista_numeros = []
        for num in range(inicio, fin + 1):
            lista_numeros.append(num)
        return tuple(lista_numeros)

    def elementos_en_multiples_rangos(self, *rangos):
        conjunto_unicos = set()
        for rango in rangos:
            inicio = rango[0]
            fin = rango[1]
            for num in range(inicio, fin + 1):
                conjunto_unicos.add(num)
        
        lista_resultado = []
        for elemento in conjunto_unicos:
            lista_resultado.append(elemento)
        
        lista_resultado.sort()
        return lista_resultado


# Pruebas Ejercicio 12
sr = SelectorRango()
print("Ej 12 - Rango creado:", sr.crear_rango(1, 3))
print("Ej 12 - Múltiples rangos combinados:", sr.elementos_en_multiples_rangos((1, 3), (2, 4)))


#======================================
# Ej. 13: Combinador de listas
# Clase CombinadorListas que: 
# (1) tenga método intercalar(lista1, lista2) que retorne una lista alternando elementos de ambas; 
# (2) tenga método intercalar_multiples(*listas) que reutilice para varias listas.
#======================================
class CombinadorListas():
    def intercalar(self, lista1, lista2):
        resultado = []
        largo1 = len(lista1)
        largo2 = len(lista2)
        
        largo_maximo = largo1
        if largo2 > largo_maximo:
            largo_maximo = largo2
        
        for i in range(largo_maximo):
            if i < largo1:
                resultado.append(lista1[i])
            if i < largo2:
                resultado.append(lista2[i])
        return resultado

    def intercalar_multiples(self, *listas):
        resultado = []
        largo_maximo = 0
        for lista in listas:
            if len(lista) > largo_maximo:
                largo_maximo = len(lista)
        
        for i in range(largo_maximo):
            for lista in listas:
                if i < len(lista):
                    resultado.append(lista[i])
        return resultado


# Pruebas Ejercicio 13
cl = CombinadorListas()
print("Ej 13 - Intercalar 2 listas:", cl.intercalar([1, 2], [3, 4]))
print("Ej 13 - Intercalar múltiples listas:", cl.intercalar_multiples([1, 2], [3, 4], [5, 6]))


#======================================
# Ej. 14: Mapeo de estudiantes a notas
# Clase RegistroNotas que: 
# (1) tenga método registrar(estudiante, nota) que guarde en un diccionario; 
# (2) tenga método estudiantes_aprobados(nota_minima) que retorne lista de estudiantes; 
# (3) tenga método mejor_estudiante() que retorne nombre y nota del que tiene mayor calificación.
#======================================
class RegistroNotas():
    def __init__(self):
        self.dic_notas = {}

    def registrar(self, estudiante, nota):
        self.dic_notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        aprobados = []
        for estudiante, nota in self.dic_notas.items():
            if nota >= nota_minima:
                aprobados.append(estudiante)
        return aprobados

    def mejor_estudiante(self):
        nombre_mejor = ""
        nota_mayor = -1
        for estudiante, nota in self.dic_notas.items():
            if nota > nota_mayor:
                nota_mayor = nota
                nombre_mejor = estudiante
        return (nombre_mejor, nota_mayor)


# Pruebas Ejercicio 14
rn = RegistroNotas()
rn.registrar("Ana", 95)
rn.registrar("Bob", 70)
print("Ej 14 - Estudiantes aprobados (>= 80):", rn.estudiantes_aprobados(80))
print("Ej 14 - Mejor estudiante:", rn.mejor_estudiante())


#======================================
# Ej. 15: Divisores de un número
# Clase DivisorFinder que: 
# (1) tenga método encontrar_divisores(numero) que retorne una tupla con todos los divisores; 
# (2) tenga método es_perfecto(numero) que retorne True si la suma de sus divisores (excepto él mismo) es igual a él; 
# (3) tenga método encontrar_multiples_divisores(*numeros) que retorne un diccionario {número: tupla_divisores}.
#======================================
class DivisorFinder():
    def encontrar_divisores(self, numero):
        lista_divisores = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                lista_divisores.append(i)
        return tuple(lista_divisores)

    def es_perfecto(self, numero):
        tupla_divisores = self.encontrar_divisores(numero)
        suma = 0
        for divisor in tupla_divisores:
            if divisor != numero:
                suma = suma + divisor
        if suma == numero:
            return True
        else:
            return False

    def encontrar_multiples_divisores(self, *numeros):
        dic_resultado = {}
        for num in numeros:
            dic_resultado[num] = self.encontrar_divisores(num)
        return dic_resultado


# Pruebas Ejercicio 15
df = DivisorFinder()
print("Ej 15 - Divisores de 12:", df.encontrar_divisores(12))
print("Ej 15 - ¿El 6 es perfecto?:", df.es_perfecto(6))
print("Ej 15 - Múltiples divisores:", df.encontrar_multiples_divisores(6, 12))


#======================================
# Ej. 16: Codificador/Decodificador
# Clase CodificadorCesar que: 
# (1) tenga método codificar_letra(letra, desplazamiento) que retorne la letra desplazada en el alfabeto (usar operador %); 
# (2) tenga método codificar_palabra(palabra, desplazamiento) que reutilice para toda la palabra; 
# (3) tenga un diccionario como atributo para historial de codificaciones.
#======================================
class CodificadorCesar():
    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        codigo_ascii = ord(letra)
        if codigo_ascii >= 97 and codigo_ascii <= 122:
            nueva_posicion = ((codigo_ascii - 97) + desplazamiento) % 26
            letra_codificada = chr(97 + nueva_posicion)
            return letra_codificada
        elif codigo_ascii >= 65 and codigo_ascii <= 90:
            nueva_posicion = ((codigo_ascii - 65) + desplazamiento) % 26
            letra_codificada = chr(65 + nueva_posicion)
            return letra_codificada
        else:
            return letra

    def codificar_palabra(self, palabra, desplazamiento):
        palabra_codificada = ""
        for letra in palabra:
            letra_nueva = self.codificar_letra(letra, desplazamiento)
            palabra_codificada = palabra_codificada + letra_nueva
        
        self.historial[palabra] = palabra_codificada
        return palabra_codificada


# Pruebas Ejercicio 16
cc = CodificadorCesar()
print("Ej 16 - Codificar 'hola' (+3):", cc.codificar_palabra("hola", 3))
print("Ej 16 - Historial registrado:", cc.historial)


#======================================
# Ej. 17: Grupo de edades
# Clase AgrupadorEdades que: 
# (1) tenga método clasificar_edad(edad) que retorne la categoría ("niño", "adolescente", "adulto", "mayor"); 
# (2) tenga método agrupar_por_categoria(*edades) que retorne un diccionario con {categoría: [edades]}; 
# (3) tenga método edad_promedio_categoria(categoria).
#======================================
class AgrupadorEdades():
    def __init__(self):
        self.dic_agrupado = {}

    def clasificar_edad(self, edad):
        if edad < 12:
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 65:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        self.dic_agrupado = {}
        for edad in edades:
            categoria = self.clasificar_edad(edad)
            if categoria in self.dic_agrupado:
                self.dic_agrupado[categoria].append(edad)
            else:
                self.dic_agrupado[categoria] = [edad]
        return self.dic_agrupado

    def edad_promedio_categoria(self, categoria):
        if categoria in self.dic_agrupado:
            lista_edades = self.dic_agrupado[categoria]
            suma_edades = 0
            for edad in lista_edades:
                suma_edades = suma_edades + edad
            promedio = suma_edades / len(lista_edades)
            return promedio
        else:
            return 0.0


# Pruebas Ejercicio 17
ae = AgrupadorEdades()
print("Ej 17 - Agrupado por categoría:", ae.agrupar_por_categoria(5, 15, 30, 70))
print("Ej 17 - Promedio categoría 'adulto':", ae.edad_promedio_categoria("adulto"))


#======================================
# Ej. 18: Matriz de distancias
# Clase CalculadorDistancia que: 
# (1) tenga método distancia_euclidiana(p1, p2) que reciba dos tuplas (x,y) y calcule la distancia; 
# (2) tenga método punto_mas_cercano(referencia, *puntos) que retorne el punto más cercano a referencia; 
# (3) tenga un atributo lista para guardar todas las distancias calculadas.
#======================================
class CalculadorDistancia():
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


# Pruebas Ejercicio 18
cd = CalculadorDistancia()
print("Ej 18 - Distancia entre (0,0) y (3,4):", cd.distancia_euclidiana((0, 0), (3, 4)))
print("Ej 18 - Punto más cercano a (0,0):", cd.punto_mas_cercano((0, 0), (5, 5), (1, 2), (8, 8)))
print("Ej 18 - Lista de distancias calculadas:", cd.lista_distancias)


#======================================
# Ej. 19: Inventario de productos
# Clase Inventario que: 
# (1) tenga método agregar_stock(producto, cantidad) que guarde en un diccionario; 
# (2) tenga método restar_stock(producto, cantidad) que disminuya y retorne True si hay suficiente; 
# (3) tenga método productos_bajo_stock(minimo) que retorne una lista de productos con cantidad < minimo.
#======================================
class Inventario():
    def __init__(self):
        self.dic_stock = {}

    def agregar_stock(self, producto, cantidad):
        if producto in self.dic_stock:
            self.dic_stock[producto] = self.dic_stock[producto] + cantidad
        else:
            self.dic_stock[producto] = cantidad

    def restar_stock(self, producto, cantidad):
        if producto in self.dic_stock:
            cantidad_actual = self.dic_stock[producto]
            if cantidad_actual >= cantidad:
                self.dic_stock[producto] = cantidad_actual - cantidad
                return True
            else:
                return False
        else:
            return False

    def productos_bajo_stock(self, minimo):
        lista_bajos = []
        for producto, cantidad in self.dic_stock.items():
            if cantidad < minimo:
                lista_bajos.append(producto)
        return lista_bajos


# Pruebas Ejercicio 19
inv = Inventario()
inv.agregar_stock("pan", 50)
print("Ej 19 - ¿Resta de stock exitosa?:", inv.restar_stock("pan", 30))
print("Ej 19 - Productos bajo stock (< 25):", inv.productos_bajo_stock(25))


#======================================
# Ej. 20: Analizador de patrones en textos
# Clase AnalizadorPatrones que: 
# (1) tenga método encontrar_palabras(texto, patron) que busque palabras que inicien con el patrón y retorne una lista; 
# (2) tenga método agrupar_por_longitud(texto) que retorne un diccionario {longitud: [palabras]}; 
# (3) tenga método palabras_unicas(texto) usando un conjunto.
#======================================
class AnalizadorPatrones():
    def encontrar_palabras(self, texto, patron):
        lista_palabras = texto.split()
        coincidencias = []
        for palabra in lista_palabras:
            if palabra.startswith(patron):
                coincidencias.append(palabra)
        return coincidencias

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


# Pruebas Ejercicio 20
ap = AnalizadorPatrones()
print("Ej 20 - Palabras que inician con 'es':", ap.encontrar_palabras("el gato está aquí", "est"))
print("Ej 20 - Agrupado por longitud:", ap.agrupar_por_longitud("el gato está aquí"))
print("Ej 20 - Palabras únicas:", ap.palabras_unicas("hola gato hola mundo"))








¡Claro que sí! Aquí tienes la explicación detallada de cada uno de los 11 ejercicios que realizamos. Te desglosaré para qué sirve, cuáles son las líneas de código donde ocurre la "magia" (la lógica principal) y en qué situaciones de la vida real o de otros programas se podría usar esta misma estructura.

---

### Ejercicio 10: Gestor de tareas con prioridad

* **¿Para qué sirve?** Permite guardar información en pares (una tarea y su nivel de urgencia). Luego, permite filtrar esa información para ver solo lo urgente o borrar cosas cuando ya no sirven.
* **Líneas más importantes:**
* `tupla_tarea = (descripcion, prioridad)`: Agrupa los dos datos en una sola cápsula (tupla) para que no se separen.
* `if prioridad == "alta":`: Es el filtro. Como la prioridad está en la posición `[1]` de la tupla, evalúa si dice "alta" para guardar solo esas.
* `if desc == descripcion: self.lista_tareas.remove(tarea)`: Busca la tarea exacta. Una vez que la encuentra, la elimina de la lista principal.


* **¿Para qué más puede servir?**
* Un sistema de tickets de soporte técnico (atender primero las computadoras totalmente dañadas).
* Un filtro de correos electrónicos (separar correos del "Jefe" vs correos de "Publicidad").



### Ejercicio 11: Contador de frecuencia

* **¿Para qué sirve?** Para contar cuántas veces se repite algo dentro de un sistema. En lugar de tener múltiples variables, usa un diccionario donde la "llave" es la palabra y el "valor" es cuántas veces apareció.
* **Líneas más importantes:**
* `if elemento in self.dic_frecuencias:`: Verifica si el elemento ya fue registrado antes.
* `self.dic_frecuencias[elemento] = self.dic_frecuencias[elemento] + 1`: Si ya existe, le suma 1 a su contador. Si no, lo crea con el valor `1`.
* `if conteo > max_conteo:`: Un clásico bucle para encontrar el número mayor. Compara el conteo actual con el más grande que ha visto hasta ahora.


* **¿Para qué más puede servir?**
* Sistemas de votación (contar qué candidato tiene más votos).
* Análisis de ventas (saber qué producto se vende más veces al día).
* Saber qué palabra se usa más en un libro o chat de WhatsApp.



### Ejercicio 12: Selector de rango con tuplas

* **¿Para qué sirve?** Genera listas de números entre dos puntos (inicio y fin) y, lo más importante, junta varios de estos grupos de números eliminando los repetidos.
* **Líneas más importantes:**
* `for num in range(inicio, fin + 1):`: Genera los números paso a paso. Se suma `1` al final para que incluya el último número, ya que el `range` de Python se detiene un número antes.
* `conjunto_unicos.add(num)`: Un `set` (conjunto) en Python **no acepta elementos repetidos**. Al agregar los números aquí, si un número choca con otro igual, simplemente es ignorado, filtrando los duplicados automáticamente.


* **¿Para qué más puede servir?**
* Sistemas de reservas de hoteles (ver qué días están ocupados si varias personas reservan del día 1 al 5 y del 4 al 10).
* Fusión de horarios de disponibilidad de empleados.



### Ejercicio 13: Combinador de listas

* **¿Para qué sirve?** Funciona como cuando barajas cartas, tomando un elemento de una lista, luego de la otra, y así sucesivamente, sin importar si una lista es más larga que la otra.
* **Líneas más importantes:**
* `if largo2 > largo_maximo:`: Descubre cuál es la lista más larga para saber cuántas vueltas (iteraciones) debe dar el bucle `for` como máximo.
* `if i < largo1: resultado.append(lista1[i])`: Esta es la protección. Si la lista 1 tiene 3 elementos, y el bucle va por la vuelta 4, esto evita que el programa colapse por buscar algo que no existe ("Index out of range").


* **¿Para qué más puede servir?**
* Sistemas de turnos (intercalar pacientes de diferentes consultorios en una sola fila).
* Animaciones o videojuegos (intercalar dos secuencias de imágenes).



### Ejercicio 14: Mapeo de estudiantes a notas

* **¿Para qué sirve?** Para relacionar un identificador único (un nombre, ID o cédula) con un valor numérico (una nota) y hacer análisis con esos números, como saber quiénes pasaron y quién es el mejor.
* **Líneas más importantes:**
* `self.dic_notas[estudiante] = nota`: Asocia directamente el nombre con su calificación en el diccionario.
* `if nota >= nota_minima:`: Filtra a los que superan la nota base y los agrega a una nueva lista de aprobados.


* **¿Para qué más puede servir?**
* Encontrar el empleado con el mayor salario de una empresa.
* Tablas de clasificación de videojuegos (Leaderboards) para ver quién tiene el puntaje más alto.
* Filtrar productos de una tienda que cuesten menos de $50.



### Ejercicio 15: Divisores de un número

* **¿Para qué sirve?** Realiza cálculos matemáticos para encontrar qué números pueden dividir a otro exactamente (sin dejar decimales).
* **Líneas más importantes:**
* `if numero % i == 0:`: El operador `%` (módulo) obtiene el residuo de una división. Si el residuo es `0`, significa que la división es exacta, por lo tanto, `i` es un divisor.
* `suma = suma + divisor`: Va acumulando el valor de los divisores para luego compararlo con el número original y saber si es "Perfecto" (como el 6: 1+2+3 = 6).


* **¿Para qué más puede servir?**
* Criptografía y seguridad en internet (se basa muchísimo en buscar divisores y números primos).
* Diseño gráfico o programación de interfaces (calcular cómo dividir una pantalla en columnas perfectas y simétricas).
* Sistemas de empaquetado (saber de cuántas formas exactas puedo dividir 100 cajas en grupos iguales).



### Ejercicio 16: Codificador/Decodificador (César)

* **¿Para qué sirve?** Oculta un texto rodando las letras del abecedario. Por ejemplo, si mueves las letras 1 espacio, la 'A' se vuelve 'B'.
* **Líneas más importantes:**
* `codigo_ascii = ord(letra)`: Convierte la letra a su número de computadora (ASCII). Por ejemplo, 'a' es 97.
* `nueva_posicion = ((codigo_ascii - 97) + desplazamiento) % 26`: Esta es la fórmula mágica. Resta 97 para que la 'a' sea 0. Le suma el desplazamiento, y el `% 26` hace que si te pasas de la 'z', vuelva a empezar en la 'a' (el abecedario inglés tiene 26 letras).
* `letra_codificada = chr(97 + nueva_posicion)`: Convierte el número final de vuelta a texto.


* **¿Para qué más puede servir?**
* Crear contraseñas temporales.
* Ocultar datos sensibles en bases de datos simples.
* Proteger los archivos de un videojuego para que los jugadores no puedan leerlos y hacer trampa fácilmente.



### Ejercicio 17: Grupo de edades

* **¿Para qué sirve?** Clasifica datos numéricos puros y los agrupa en categorías (como "niño" o "adulto"). Luego calcula estadísticas (promedios) por cada grupo.
* **Líneas más importantes:**
* El bloque `if edad < 12: ... elif edad < 18: ...`: Actúa como una cascada. Si el número no cae en el primer escalón, cae al siguiente, hasta clasificar la edad.
* `if categoria in self.dic_agrupado:`: Revisa si ya creaste la categoría en el diccionario; si ya existe, mete la edad en la lista; si no, crea la lista desde cero `[edad]`.
* `promedio = suma_edades / len(lista_edades)`: Fórmula clásica de promedio, la suma de todo dividido para la cantidad de elementos.


* **¿Para qué más puede servir?**
* Marketing: Segmentar clientes por rango de sueldo para saber a quién enviarle anuncios de autos de lujo y a quién promociones de ahorro.
* Clasificar tallas de ropa basadas en centímetros (S, M, L).



### Ejercicio 18: Matriz de distancias

* **¿Para qué sirve?** Utiliza la fórmula matemática de la distancia entre dos puntos (como en un plano cartesiano) y busca cuál de un grupo de puntos está más cerca de ti.
* **Líneas más importantes:**
* `distancia = (diferencia_x + diferencia_y) ** 0.5`: Esta es la raíz cuadrada de la suma de los cuadrados (Teorema de Pitágoras). En Python, elevar a la potencia de `0.5` es lo mismo que sacar raíz cuadrada.
* `distancia_minima = 999999.0`: Se empieza con un número gigante de referencia. Así, cualquier distancia real siempre será menor y empezará a reemplazar a esta variable hasta encontrar la más pequeña verdadera.


* **¿Para qué más puede servir?**
* Aplicaciones como Uber o Google Maps (para encontrar al conductor o la pizzería más cercana a ti).
* Videojuegos (para que un enemigo sepa a cuál jugador debe atacar porque está más cerca).
* Logística (decidir a qué bodega ir por materiales).



### Ejercicio 19: Inventario de productos

* **¿Para qué sirve?** Es un sistema de ingresos y egresos. Asegura que nunca vendas algo que no tienes (evitando saldos negativos) y te avisa cuando te estás quedando sin mercadería.
* **Líneas más importantes:**
* `if cantidad_actual >= cantidad:`: Este es el "guardia de seguridad" de la función. Antes de restar, verifica si tienes suficiente stock. Si alguien pide 50 y tienes 30, este `if` evita la resta y retorna `False`.
* `if cantidad < minimo:`: Un bucle que recorre todos los productos y compara su stock actual contra la alarma que tú le pongas (ej. avísame si hay menos de 25).


* **¿Para qué más puede servir?**
* Cuentas de bancos (retiros y depósitos, evitando que la cuenta quede en negativo).
* Sistemas de salud en videojuegos (restar puntos de vida, y si la vida es menor a un mínimo, la pantalla parpadea en rojo).



### Ejercicio 20: Analizador de patrones en textos

* **¿Para qué sirve?** Desmenuza un texto largo, separándolo por palabras. Luego agrupa las palabras por tamaño o busca palabras que empiecen con ciertas letras, eliminando palabras repetidas.
* **Líneas más importantes:**
* `lista_palabras = texto.split()`: Toma una frase entera y la convierte en una lista cortando por los espacios. "hola mundo" -> `['hola', 'mundo']`.
* `if palabra.startswith(patron):`: Una función muy útil que revisa directamente si las primeras letras de la palabra coinciden con lo que buscas (el patrón).
* `if largo in dic_longitudes:`: Usa el tamaño (`len`) de la palabra como llave del diccionario, agrupando, por ejemplo, todas las palabras de 4 letras juntas.


* **¿Para qué más puede servir?**
* Sistemas de autocompletado en buscadores (cuando escribes "face" y Google te sugiere "facebook", porque busca palabras que inicien con ese patrón).
* Filtros antispam de correos (contar cuántas veces se repite una palabra sospechosa y analizarla).
* Análisis de cadenas de ADN en biología para buscar patrones genéticos.
'''