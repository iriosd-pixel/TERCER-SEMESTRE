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
Clase AnalizadorTexto que: 
(1) tenga método agregar_palabra(palabra) que agregue
la palabra a un conjunto (para evitar duplicados) y a una lista (para el orden); 
(2) tenga método contar_palabras() que retorne cuántas palabras únicas hay; 
(3) tenga método agregar_multiples(*args) que reutilice agregar_palabra para varios.

'''
class Analizador_texto():
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
            
analizar=Analizador_texto()

analizar.agregar_palabra("python")
analizar.agregar_palabra("Hola")
analizar.agregar_palabra("Hola")

analizar.agregar_multiples("hola", "mundo", "python", "codigo")

print("La lsita de palabras es: ", analizar.lista_palabras)
print( "EL conjutno  palabras es: ", analizar.conjunto)
print("Las palbras total son: ", analizar.contar_palabras())