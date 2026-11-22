#================================================
"""----------------EJERCICIOS DE PRACTICA--------------"""
#================================================
#================================================
#1) Dada ciudades = ["Quito","Guayaquil","Quito","Cuenca","Guayaquil"], 
# obtén una lista sin repetidos respetando el orden de aparición (un set solo no alcanza).
#================================================
class sinRepetidos():
    def quitar_repetidos(self, ciudades):
        visitas=set()
        unicas=[]
        for ciudad in ciudades:
            if ciudad not in unicas:
                visitas.add(ciudad)
                unicas.append(ciudad)
        return unicas    
    
sr=sinRepetidos()
ciudade=sr.quitar_repetidos(["Quito","Guayaquil","Quito","Cuenca","Guayaquil"])
print(ciudade)
#================================================
#2) Con la misma lista, arma un diccionario {"Quito": 2, "Guayaquil": 2, "Cuenca": 1}.
#================================================
ciudades=["Quito","Guayaquil","Quito","Cuenca","Guayaquil"]
contar={}
for ciudad in ciudades:
    contar[ciudad]=contar.get(ciudad, 0)+1
print(contar)
#el mas repetido
mas_repetidas= max(contar, key=contar.get)
print(mas_repetidas)
#================================================
# 3) inscritos_matematica = {"Ana","Luis","Sol","Marco"} y inscritos_ingles = {"Luis","Marco","Ruth"}. 
# Responde con código: ¿quiénes están en las dos?, ¿quiénes solo en matemática?, 
# ¿cuántos estudiantes distintos hay en total?
#================================================
inscritos_matematica = {"Ana","Luis","Sol","Marco"} 
inscritos_ingles = {"Luis","Marco","Ruth"}
ambas= inscritos_matematica & inscritos_ingles
print(ambas)
matematicas= inscritos_matematica - inscritos_ingles
print(matematicas)
distintos= len(inscritos_matematica|inscritos_ingles)
print(distintos)
#================================================
#4) Con clientes = [{"id":1,"nombre":"Ana"},{"id":2,"nombre":"Luis"}], 
# crea un diccionario {id: cliente} para acceder por id sin recorrer la lista. 
# Luego imprime el nombre del id 2.
#================================================
clientes = [{"id":1,"nombre":"Ana"},{"id":2,"nombre":"Luis"}]
indice={}
for cliente in clientes:
    indice[cliente["id"]]=cliente
    
print(indice[2]["nombre"])
#================================================
# 5) Dada ventas = [("enero", 1500), ("febrero", 1800), ("marzo", 1200)], 
# imprime el mes con mayor venta y el total, usando desempaquetado de tuplas.
#================================================
ventas = [("enero", 1500), ("febrero", 1800), ("marzo", 1200)]
mes_mayor, total_mayor= ventas[0]
for mes, total in ventas:
    if total> total_mayor:
        mes_mayor=mes
        total_mayor=total

print(f"Mes con mayor venta: {mes_mayor}")
print(f"Total: ${total_mayor}")
#================================================
# 6) Agrega al Controlador la función clientes_por_ciudad() 
# que devuelva un diccionario {"Guayaquil": ["Ana", "Luis"], "Quito": ["Sol"]}.
#================================================
class Controlador:
    def __init__(self):
        self.clientes = [
            {"nombre": "Ana", "ciudad": "Guayaquil"},
            {"nombre": "Luis", "ciudad": "Guayaquil"},
            {"nombre": "Sol", "ciudad": "Quito"}
        ]

    def clientes_por_ciudad(self):
        resultado = {}

        for cliente in self.clientes:
            ciudad = cliente["ciudad"]
            nombre = cliente["nombre"]

            if ciudad not in resultado:
                resultado[ciudad] = []

            resultado[ciudad].append(nombre)

        return resultado


controlador = Controlador()
print(controlador.clientes_por_ciudad())