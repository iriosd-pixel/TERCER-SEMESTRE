"""GUÍA DE PRÁCTICA: PILAS, COLAS Y LISTAS ENLAZADAS (Python).

Ejecuta: python ayuda_leccion.py
No necesita instalar paquetes ni modificar los proyectos de clase.

Esta guía usa la sintaxis de tus archivos mi_pila.py, mi_cola.py y
lista_pasajeros.py: self.datos, self.cantidad, apilar, desapilar, encolar,
desencolar, head, data y next. Aquí los datos son textos o números para que
se vea el movimiento. En los proyectos reales cada dato es un Pasajero:
para buscarlo por número se compara self.datos[i].numero o
actual.data.numero; para modificar se cambian sus atributos.

FUENTES DE ESTUDIO (las instrucciones de estas guías son material didáctico):
  guia_estructuras_datos_python_v4.html: método de 5 pasos, pilas, colas,
    listas enlazadas y talleres.
  TAREA_U3_LISTAS_PASAJEROS (3).html: arreglo fijo, cantidad, recorridos
    y desplazamientos. Esa tarea trata listas de arreglo, NO nodos.
  guia_listas_enlazadas_web (1).html: dibujos y enlaces de nodos; sus
    ejemplos están en JavaScript, traducidos aquí a Python.
  Texto pegado.txt: seguimiento casilla por casilla de desapilar,
    desencolar e insertar/eliminar nodos.

ÍNDICE
  0. Método de estudio y vocabulario.
  1. Pila: construir, apilar, ver tope, desapilar y operaciones extra.
  2. Cola: construir, encolar, ver frente, desencolar y operaciones extra.
  3. Lista enlazada: nodos, recorrido, inserciones, búsqueda, eliminación,
     modificación e inversión.
  4. Ejercicios resueltos y retos para hacer sin mirar.

0. MÉTODO DE 5 PASOS (úsalo en CADA ejercicio)
  1) Entrada / proceso / salida: ¿qué recibo, hago y devuelvo?
  2) Bosquejo: dibuja casillas o nodos con un caso pequeño.
  3) Patrón: descubre qué se repite (for, while, enlaces).
  4) Código: contempla vacío, lleno, primer/último elemento y no encontrado.
  5) Prueba de escritorio: apunta el estado DESPUÉS de cada línea.

  self = «este objeto». self.datos pertenece a una pila/cola concreta.
  capacidad = casillas reservadas; cantidad = casillas activas.
  [None] * 4 crea [None, None, None, None], pero cantidad empieza en 0.
  Con cantidad == 3, las casillas activas son 0, 1 y 2.
  Los índices comienzan en 0; por eso el último activo es cantidad - 1.
  None = no hay dato. False = no se pudo hacer una operación.
  La implementación manual usa índices, for, while e if; no necesita
  append, pop, insert, remove, len, slicing, deque ni comprensiones.

1. PILA = LIFO: el ÚLTIMO en entrar es el PRIMERO en salir.
  Ejemplo: platos o acciones para deshacer. Se entra y sale por el TOPE.
  Fondo [Ana, Beto, Diana, None, None] Tope; cantidad = 3, capacidad = 5.
  Tope = datos[cantidad - 1] = datos[2] = Diana.

  APILAR("Carlos")                    datos                         cantidad
  antes                               [Ana,Beto,Diana,None,None]          3
  datos[cantidad] = "Carlos"          [Ana,Beto,Diana,Carlos,None]        3
  cantidad += 1                       [Ana,Beto,Diana,Carlos,None]        4
  El nuevo tope es Carlos. Antes de escribir: cantidad < capacidad.

  DESAPILAR() desde [Ana,Beto,Diana,None,None], cantidad = 3:
  valor = datos[cantidad - 1]        valor = Diana; arreglo igual; cant. 3
  datos[cantidad - 1] = None         valor = Diana; [Ana,Beto,None,...]; 3
  cantidad -= 1                      valor = Diana; [Ana,Beto,None,...]; 2
  return valor                       sale Diana; ahora el tope es Beto.
  Guardar valor ANTES de limpiar evita perderlo. No se desplaza nada.
  En vacío, desapilar y ver_tope devuelven None. En lleno, apilar da False.

  LISTAR del tope al fondo: range(cantidad - 1, -1, -1).
  Si cantidad = 3, los índices son 2, 1, 0. El límite -1 NO se incluye.
  BUSCAR recorre en ese orden; devuelve índice o -1 si no encuentra.
  MODIFICAR: buscar primero; si devuelve -1, no tocar nada. Si devuelve
  posición, cambiar el dato de esa casilla sin mover los demás.
  LONGITUD devuelve cantidad; ESTA_VACIA comprueba cantidad == 0.
  ELIMINAR UN DATO INTERMEDIO no es la operación básica: usa una pila
  auxiliar, saca hasta hallar el dato y restaura los de encima.
  Ejemplo [Ana,Beto,Diana] quitando Beto:
    desapila Diana -> auxiliar [Diana]; desapila Beto -> descartarlo;
    desapila Diana de auxiliar -> apilarla; queda [Ana,Diana].
  COPIAR: recorre original desde el fondo y apila en otra pila. Copia
  el orden, pero si los elementos son objetos, comparte esos objetos.

2. COLA = FIFO: el PRIMERO en entrar es el PRIMERO en salir.
  Ejemplo: banco, impresora o turnos. Entra por FINAL, sale por FRENTE.
  Frente [Ana, Beto, Diana, None, None] Final; cantidad = 3.
  Frente = datos[0] = Ana; final activo = datos[cantidad - 1] = Diana.

  ENCOLAR("Carlos"): escribir en datos[cantidad], luego cantidad += 1.
  Queda [Ana,Beto,Diana,Carlos,None], cantidad = 4; Ana sigue al frente.

  DESENCOLAR() desde [Ana,Beto,Diana,None,None], cantidad = 3:
  primero = datos[0]                primero = Ana; arreglo igual
  i=0: datos[0] = datos[1]          [Beto,Beto,Diana,None,None]
  i=1: datos[1] = datos[2]          [Beto,Diana,Diana,None,None]
  datos[cantidad - 1] = None        [Beto,Diana,None,None,None]
  cantidad -= 1                     cantidad = 2; return Ana.
  La duplicación durante el for es TEMPORAL: asignar no borra el origen.
  range(cantidad - 1) produce 0, 1 si cantidad era 3.
  Con un único dato, range(0) no ejecuta vueltas; se limpia datos[0].
  En vacío, desencolar y ver_frente devuelven None; en lleno, encolar
  devuelve False. Listar va de 0 a cantidad - 1 con range(cantidad).
  BUSCAR devuelve índice o -1; MODIFICAR cambia el valor en ese índice,
  sin alterar el orden de atención. LONGITUD devuelve cantidad;
  ESTA_VACIA comprueba cantidad == 0. COPIAR encola los datos de 0 a
  cantidad - 1 en otra cola, conservando el frente y el final.

  ELIMINAR UN DATO INTERMEDIO: repite exactamente cantidad_inicial veces:
  desencola uno; si no es el buscado, vuelve a encolarlo.
  [Ana,Beto,Diana], quitar Beto: [Beto,Diana,Ana] -> [Diana,Ana]
  -> [Ana,Diana]. Si repitieras con la cantidad cambiante, fallarías.
  Esta cola desplaza elementos en O(n); la guía amplia muestra deque,
  pero los ejercicios manuales de tu clase usan el arreglo fijo.

3. LISTA ENLAZADA: no hay datos[0], datos[1]... Hay NODOS.
  Cada Nodo guarda data (el dato) y next (referencia al siguiente).
  head -> [Ana|next] -> [Beto|next] -> [Diana|None]; cantidad = 3.
  head es el primer nodo; si head is None, está vacía.
  actual = head; while actual is not None: ...; actual = actual.next
  «Avanzar» cambia la referencia actual; NO desplaza el nodo.
  Si olvidas actual = actual.next, el while nunca termina.

  INSERTAR AL INICIO, partiendo de Ana -> Beto:
    nuevo = Nodo("Diana")       Diana.next = None
    nuevo.next = self.head     Diana -> Ana; head aún es Ana
    self.head = nuevo          head -> Diana -> Ana -> Beto
  La primera flecha debe guardarse ANTES de mover head.

  INSERTAR AL FINAL: si head is None, head = nuevo. Si no, empieza
  en head, avanza mientras actual.next is not None y conecta
  actual.next = nuevo. Con Ana -> Beto, actual termina en Beto.

  INSERTAR EN POSICIÓN 2, desde Ana(0) -> Beto(1) -> Carlos(2):
    anterior = Beto
    nuevo = Nodo("Diana")
    nuevo.next = anterior.next    Diana -> Carlos
    anterior.next = nuevo         Beto -> Diana -> Carlos
  Cambiar anterior.next primero puede perder Carlos y crear un ciclo.
  Posición 0 cambia head. Posición cantidad equivale al final.
  Negativos y posiciones mayores que cantidad son inválidos.

  ELIMINAR Beto desde Ana -> Beto -> Carlos:
    anterior = Ana; actual = Beto
    anterior.next = actual.next   Ana -> Carlos
  Eliminar la cabeza: self.head = self.head.next.
  Eliminar último: el anterior pasa a apuntar a None.
  Solo resta cantidad si realmente encontraste y quitaste el nodo.
  Una variable local que aún apunta al nodo quitado lo mantiene vivo
  hasta que esa referencia deje de usarse; el enlace de la lista ya no.

  BUSCAR: desde head, comparar actual.data, avanzar actual.next; si
  llegas a None, no existe. MODIFICAR cambia data o un atributo de
  actual.data, nunca next. LISTAR visita cada nodo en orden y recoge
  data. LONGITUD puede devolver cantidad sin recorrer. CONTAR recorre
  y suma 1 por nodo; los dos números deben coincidir.

  INVERTIR Ana -> Beto -> Carlos:
    guarda siguiente antes de cambiar cada next; luego haz
    actual.next = anterior; avanza anterior y actual; actualiza head.
  Estado de las flechas: Ana -> None, Beto -> Ana, Carlos -> Beto;
  al terminar head = Carlos. cantidad no cambia.

  DIFERENCIA IMPORTANTE: una list normal accede por índice; en lista
  enlazada se camina desde head para buscar una posición. Insertar al
  inicio requiere cambiar dos referencias; buscar puede recorrer todos
  los nodos. La tarea de listas de pasajeros con arreglo fijo desplaza
  casillas; la AeroLista enlazada cambia enlaces.
"""


class MiPila:
    """Arreglo fijo de práctica. En tu proyecto, cada valor es un Pasajero."""

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def apilar(self, valor):
        if self.cantidad == self.capacidad:
            return False
        self.datos[self.cantidad] = valor
        self.cantidad += 1
        return True

    def desapilar(self):
        if self.esta_vacia():
            return None
        valor = self.datos[self.cantidad - 1]  # 1. conservar el tope
        self.datos[self.cantidad - 1] = None   # 2. liberar su casilla
        self.cantidad -= 1                     # 3. reducir parte activa
        return valor                           # 4. entregar lo guardado

    def ver_tope(self):
        if self.esta_vacia():
            return None
        return self.datos[self.cantidad - 1]   # no cambia cantidad

    def listar(self):
        if self.esta_vacia():
            print("  (pila vacía)")
            return
        for i in range(self.cantidad - 1, -1, -1):
            print(f"  [{i}] {self.datos[i]}")

    def buscar(self, valor):
        for i in range(self.cantidad - 1, -1, -1):
            if self.datos[i] == valor:
                return i
        return -1

    def modificar(self, valor, nuevo_valor):
        posicion = self.buscar(valor)
        if posicion == -1:
            return False
        self.datos[posicion] = nuevo_valor
        return True

    def eliminar_por_valor(self, valor):
        if self.buscar(valor) == -1:
            return False
        auxiliar = MiPila(self.capacidad)
        while not self.esta_vacia():
            actual = self.desapilar()
            if actual == valor:
                break
            auxiliar.apilar(actual)
        while not auxiliar.esta_vacia():
            self.apilar(auxiliar.desapilar())
        return True

    def copiar(self):
        nueva = MiPila(self.capacidad)
        for i in range(self.cantidad):
            nueva.apilar(self.datos[i])
        return nueva

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0


class MiCola:
    """Cola manual: el frente siempre está en datos[0]."""

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def encolar(self, valor):
        if self.cantidad == self.capacidad:
            return False
        self.datos[self.cantidad] = valor
        self.cantidad += 1
        return True

    def desencolar(self):
        if self.esta_vacia():
            return None
        primero = self.datos[0]                 # 1. guardar el frente
        for i in range(self.cantidad - 1):     # 2. correr a la izquierda
            self.datos[i] = self.datos[i + 1]
        self.datos[self.cantidad - 1] = None   # 3. limpiar duplicado final
        self.cantidad -= 1                     # 4. reducir parte activa
        return primero                         # 5. entregar el atendido

    def ver_frente(self):
        if self.esta_vacia():
            return None
        return self.datos[0]

    def listar(self):
        if self.esta_vacia():
            print("  (cola vacía)")
            return
        for i in range(self.cantidad):
            print(f"  [{i}] {self.datos[i]}")

    def buscar(self, valor):
        for i in range(self.cantidad):
            if self.datos[i] == valor:
                return i
        return -1

    def modificar(self, valor, nuevo_valor):
        posicion = self.buscar(valor)
        if posicion == -1:
            return False
        self.datos[posicion] = nuevo_valor
        return True

    def eliminar_por_valor(self, valor):
        if self.buscar(valor) == -1:
            return False
        cantidad_inicial = self.cantidad
        eliminado = False
        for i in range(cantidad_inicial):
            actual = self.desencolar()
            if actual == valor and not eliminado:
                eliminado = True
            else:
                self.encolar(actual)
        return True

    def copiar(self):
        nueva = MiCola(self.capacidad)
        for i in range(self.cantidad):
            nueva.encolar(self.datos[i])
        return nueva

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0


class Nodo:
    """Un nodo como el de AeroLista: data + next."""

    def __init__(self, data):
        self.data = data
        self.next = None


class ListaEnlazada:
    """Misma idea de head y cantidad de ListaPasajeros, con valores simples."""

    def __init__(self):
        self.head = None
        self.cantidad = 0

    def esta_vacia(self):
        return self.head is None

    def longitud(self):
        return self.cantidad

    def ingresar(self, data):
        """Inserta al final, igual que ingresar() en AeroLista."""
        nuevo = Nodo(data)
        if self.head is None:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next is not None:
                actual = actual.next
            actual.next = nuevo
        self.cantidad += 1
        return True

    def insertar_inicio(self, data):
        nuevo = Nodo(data)
        nuevo.next = self.head                  # conservar la cadena vieja
        self.head = nuevo                       # ahora empieza en nuevo
        self.cantidad += 1
        return True

    def insertar_en(self, posicion, data):
        if posicion < 0 or posicion > self.cantidad:
            return False
        if posicion == 0:
            return self.insertar_inicio(data)
        anterior = self.head
        for i in range(posicion - 1):
            anterior = anterior.next
        nuevo = Nodo(data)
        nuevo.next = anterior.next              # primero conservar el resto
        anterior.next = nuevo                   # después enlazar anterior
        self.cantidad += 1
        return True

    def listar(self):
        """Como AeroLista: retorna una list solo para mostrar resultados."""
        resultado = []
        actual = self.head
        while actual is not None:
            resultado.append(actual.data)
            actual = actual.next
        return resultado

    def buscar(self, data):
        """Devuelve el dato o None, como buscar(numero) en AeroLista."""
        actual = self.head
        while actual is not None:
            if actual.data == data:
                return actual.data
            actual = actual.next
        return None

    def buscar_posicion(self, data):
        posicion = 0
        actual = self.head
        while actual is not None:
            if actual.data == data:
                return posicion
            posicion += 1
            actual = actual.next
        return -1

    def modificar(self, data, nuevo_data):
        """Cambia data; los enlaces next no se modifican."""
        actual = self.head
        while actual is not None:
            if actual.data == data:
                actual.data = nuevo_data
                return True
            actual = actual.next
        return False

    def eliminar(self, data):
        """Retorna el dato eliminado o None, igual que AeroLista."""
        if self.head is None:
            return None
        if self.head.data == data:
            eliminado = self.head.data
            self.head = self.head.next
            self.cantidad -= 1
            return eliminado
        anterior = self.head
        actual = self.head.next
        while actual is not None and actual.data != data:
            anterior = actual
            actual = actual.next
        if actual is None:
            return None
        anterior.next = actual.next
        self.cantidad -= 1
        return actual.data

    def contar(self):
        """Recuento por recorrido: permite comprobar self.cantidad."""
        total = 0
        actual = self.head
        while actual is not None:
            total += 1
            actual = actual.next
        return total

    def invertir(self):
        anterior = None
        actual = self.head
        while actual is not None:
            siguiente = actual.next             # si no lo guardas, pierdes resto
            actual.next = anterior              # invierte UNA flecha
            anterior = actual
            actual = siguiente
        self.head = anterior


# 4. EJERCICIOS RESUELTOS: primero escribe entrada/proceso/salida en papel.
# Cada función utiliza las clases manuales de arriba. Son ejemplos pequeños
# para poder observar el arreglo o la cadena de nodos después de cada paso.


def invertir_texto(texto):
    """Pila: 'Hola' -> 'aloH'. Se apilan caracteres, luego se desapilan."""
    capacidad = 0
    for letra in texto:
        capacidad += 1
    pila = MiPila(capacidad)
    for letra in texto:
        pila.apilar(letra)
    resultado = ""
    while not pila.esta_vacia():
        resultado += pila.desapilar()
    return resultado


def parentesis_balanceados(expresion):
    """Pila: reconoce (), [] y {}; ignora letras y espacios."""
    capacidad = 0
    for simbolo in expresion:
        capacidad += 1
    pila = MiPila(capacidad)
    for simbolo in expresion:
        if simbolo == "(" or simbolo == "[" or simbolo == "{":
            pila.apilar(simbolo)
        elif simbolo == ")" or simbolo == "]" or simbolo == "}":
            if pila.esta_vacia():
                return False
            apertura = pila.desapilar()
            if simbolo == ")" and apertura != "(":
                return False
            if simbolo == "]" and apertura != "[":
                return False
            if simbolo == "}" and apertura != "{":
                return False
    return pila.esta_vacia()


def decimal_a_binario(numero):
    """Pila: 13 -> '1101'; residuos 1,0,1,1 se leen al revés."""
    if numero < 0:
        return None
    if numero == 0:
        return "0"
    capacidad = 0
    temporal = numero
    while temporal > 0:
        capacidad += 1
        temporal //= 2
    pila = MiPila(capacidad)
    while numero > 0:
        pila.apilar(numero % 2)
        numero //= 2
    resultado = ""
    while not pila.esta_vacia():
        resultado += str(pila.desapilar())
    return resultado


def atender_banco():
    """Cola: Ana, Beto, Diana -> se atiende Ana y Beto."""
    cola = MiCola(3)
    cola.encolar("Ana")
    cola.encolar("Beto")
    cola.encolar("Diana")
    primero = cola.desencolar()
    segundo = cola.desencolar()
    return primero, segundo, cola.ver_frente()  # Ana, Beto, Diana


def tiempo_impresora():
    """Cola: A(5), B(2), C(10), a 2 s/página -> 34 s."""
    cola = MiCola(3)
    cola.encolar(("A", 5))
    cola.encolar(("B", 2))
    cola.encolar(("C", 10))
    acumulado = 0
    while not cola.esta_vacia():
        documento = cola.desencolar()
        acumulado += documento[1] * 2
    return acumulado


def turnos_rotativos():
    """Cola: cuatro turnos de Ana y Beto -> Ana, Beto, Ana, Beto."""
    cola = MiCola(2)
    cola.encolar("Ana")
    cola.encolar("Beto")
    turnos = [None] * 4
    for i in range(4):
        jugador = cola.desencolar()
        turnos[i] = jugador
        cola.encolar(jugador)
    return turnos


def ejemplo_enlaces():
    """Lista: A -> B -> C; inserta X en 1 y elimina B."""
    lista = ListaEnlazada()
    lista.ingresar("A")
    lista.ingresar("B")
    lista.ingresar("C")
    lista.insertar_en(1, "X")              # A -> X -> B -> C
    lista.eliminar("B")                  # A -> X -> C
    return lista.listar()


# RETOS PARA PRACTICAR (hazlos con estas clases; solución esperada al lado).
# Escribe primero un bosquejo y prueba también vacío, lleno o no encontrado.
#
# PILAS
# P1. Apila 10, 20, 30 en capacidad 3. Anota datos/cantidad tras CADA línea.
#     Verifica tope=30, cuarto apilar=False; salen 30,20,10 y luego None.
# P2. Desde [Ana,Beto,Diana], elimina Beto con auxiliar. Queda Ana,Diana.
# P3. Invierte las PALABRAS de "hola mundo Python" sin invertir las letras.
#     Pista: separa palabras recorriendo caracteres; salida Python mundo hola.
# P4. Comprueba palíndromo "reconocer" comparando original con desapilados.
#     Prueba también "casa": False.
# P5. Historial: hacer A, B, C; deshacer -> C; ver tope -> B.
# P6. Postfija "3 4 + 5 *": apila números; para operador desapila
#     primero el derecho, luego el izquierdo. Resultado 35.
# P7. En la pila real de pasajeros, buscar(numero) debe comparar .numero,
#     y buscar_cedula(cedula), .cedula. Comprueba que no repite ninguno.
#
# COLAS
# C1. Encola 10,20,30. Dibuja los arreglos TEMPORALES al desencolar:
#     [20,20,30], [20,30,30], [20,30,None]; sale 10.
# C2. Elimina Beto de Ana,Beto,Diana con cantidad_inicial; Ana,Diana.
# C3. Tickets: contador empieza en 1; al encolar, guarda (ticket,nombre)
#     y aumenta contador SOLO si hubo espacio. Atender no reinicia contador.
# C4. Encola A,B,C; atiende A; encola D. Orden final B,C,D.
# C5. Cola de prioridad: NO es FIFO normal. Si Dan(3), Isma(3), Ana(1),
#     atiende Dan, Isma, Ana, conservando el orden de llegada en empate.
# C6. Simula dos cajas: cuando una queda libre, desencola el siguiente.
#     Si ambas quedan libres a la vez, asigna primero la caja 1.
# C7. En la cola real, modifica destino/asiento sin cambiar el turno;
#     filtra mayores de edad a otra cola manteniendo el orden.
#
# LISTAS ENLAZADAS
# L1. Dibuja head -> A -> B -> C. Inserta X en posiciones 0, 2 y 4
#     en tres listas INDEPENDIENTES. Revisa head y cantidad.
# L2. Elimina cabeza, medio y final en tres listas independientes.
#     Con una lista vacía, eliminar devuelve None.
# L3. Busca B: retorna el dato; buscar_posicion(B) retorna 1;
#     buscar_posicion(Z) retorna -1. Sin índice directo: recorre next.
# L4. Modifica B a X. Los enlaces y cantidad deben permanecer iguales.
# L5. Invierte A -> B -> C. Esperado C -> B -> A, cantidad = 3.
# L6. En AeroLista, filtrar_por_clase("Económica") recorre con actual;
#     agrega actual.data al resultado si actual.data.clase() coincide.
# L7. Cuenta menores: si actual.data.edad < 18, incrementa contador.
# L8. Detecta un ciclo como reto avanzado: si next vuelve a un nodo
#     anterior, un recorrido hasta None no termina. Usa dos referencias,
#     una que avance 1 enlace y otra 2; si se encuentran, hay ciclo.


def mostrar_ejemplos():
    """Pequeñas pruebas de escritorio ejecutables; no pide input()."""
    pila = MiPila(3)
    for nombre in ("Ana", "Beto", "Diana"):
        pila.apilar(nombre)
    print("PILA antes:", pila.datos, "cantidad:", pila.cantidad)
    print("Tope:", pila.ver_tope(), "Sale:", pila.desapilar())
    print("PILA después:", pila.datos, "cantidad:", pila.cantidad)

    cola = MiCola(3)
    for nombre in ("Ana", "Beto", "Diana"):
        cola.encolar(nombre)
    print("COLA antes:", cola.datos, "cantidad:", cola.cantidad)
    print("Frente:", cola.ver_frente(), "Sale:", cola.desencolar())
    print("COLA después:", cola.datos, "cantidad:", cola.cantidad)

    lista = ListaEnlazada()
    for nombre in ("Ana", "Beto", "Diana"):
        lista.ingresar(nombre)
    print("ENLAZADA antes:", lista.listar(), "cantidad:", lista.cantidad)
    lista.insertar_en(1, "Carlos")
    lista.eliminar("Beto")
    print("ENLAZADA después:", lista.listar(), "cantidad:", lista.cantidad)

    print("Texto:", invertir_texto("Hola"))
    print("Paréntesis:", parentesis_balanceados("([{}])"))
    print("Binario:", decimal_a_binario(13))
    print("Banco:", atender_banco())
    print("Impresora (segundos):", tiempo_impresora())
    print("Turnos:", turnos_rotativos())
    print("Enlaces:", ejemplo_enlaces())


if __name__ == "__main__":
    mostrar_ejemplos()
