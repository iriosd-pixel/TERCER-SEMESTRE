# =====================================================================
# ejercicios.py — EJERCICIOS DE PILAS Y COLAS
# ---------------------------------------------------------------------
# 7 ejercicios de pilas y 7 de colas:
# 3 de taller + 4 propuestos para cada estructura.
#
# Completa primero MiPila y MiCola.
# Utiliza sus métodos añadir, eliminar, consultar, esta_vacia y tamano.
#
# Si necesitas contar caracteres o palabras sin len(), usa un contador.
# Si necesitas separar palabras sin split(), recorre el texto y
# construye cada palabra hasta encontrar un espacio.
#
# Cada función debe leer los datos necesarios y mostrar el resultado.
# =====================================================================



# ============================ PILAS ============================

def pila_invertir_cadena(texto):
    """
OBJETIVO: invertir un texto usando una pila.

PASOS:
1. Leer el texto.
2. Contar sus caracteres con un ciclo.
3. Crear una pila con capacidad suficiente.
4. Añadir cada carácter.
5. Eliminar elementos hasta vaciarla y construir el resultado.

PRUEBA: hola -> aloh
    """
    pila=[]
    for letra in texto:
        pila.append(letra)
    
    resultado =""
    
    while len(pila)>0:
        letra= pila.pop()
        resultado+= letra
    return resultado
print(pila_invertir_cadena("Hola"))



def pila_parentesis_balanceados():
    """
OBJETIVO: comprobar (), [] y {}.

PASOS:
1. Leer la expresión y crear una pila.
2. Apilar cada símbolo de apertura.
3. Al encontrar un cierre:
- Si la pila está vacía, la expresión es incorrecta.
- Retirar una apertura y comprobar que corresponda.
4. Al terminar, la pila debe estar vacía.

Ignorar los caracteres que no sean delimitadores.

PRUEBAS:
([{}]) -> correcto
([)]   -> incorrecto
(()    -> incorrecto
    """
    pass


def pila_decimal_binario(numero):
    """
    OBJETIVO: convertir un entero no negativo a binario.

    PASOS:
    1. Leer y validar el número.
    2. Si es cero, mostrar "0".
    3. Mientras sea mayor que cero:
    - Apilar el residuo numero % 2.
    - Actualizar numero con división entera entre 2.
    4. Desapilar los residuos para formar el resultado.

    Prever capacidad suficiente para todos los residuos.
    PRUEBA: 13 -> 1101
    """
    if numero ==0:
        print ("0")
    else:
        residuo=numero%2
        residuo+= residuo
        numero=numero//2
    pass


def pila_historial():
    """
OBJETIVO: simular deshacer acciones.

Crear un submenú:
1. Hacer acción: leer texto y añadirlo.
2. Deshacer: eliminar y mostrar la última acción.
3. Ver historial: listar.
0. Volver.

Controlar la pila vacía y la capacidad.
    """
    pass


def pila_invertir_palabras():
    """
OBJETIVO: invertir el orden de las palabras, no sus letras.

PASOS:
1. Leer una frase.
2. Identificar sus palabras.
3. Añadir cada palabra a una pila.
4. Retirarlas y construir la frase con espacios.

PRUEBA: "hola mundo Python" -> "Python mundo hola"
    """
    pass


def pila_palindromo():
    """
OBJETIVO: comprobar si una palabra se lee igual al revés.

PASOS:
1. Leer una palabra.
2. Apilar sus caracteres.
3. Recorrer la palabra original comparando cada carácter
con el que se retira de la pila.
4. Si todos coinciden, es palíndromo.

Para una primera versión, comparar exactamente lo escrito.
PRUEBAS: reconocer -> True; casa -> False.
    """
    pass


def pila_postfija():
    """
OBJETIVO: evaluar una expresión postfija con tokens separados
por espacios.

PASOS:
1. Leer la expresión.
2. Si el token es un número, apilarlo.
3. Si es un operador (+, -, *, /):
- Comprobar que existan al menos dos operandos.
- El primer retirado es el operando DERECHO.
- El segundo retirado es el operando IZQUIERDO.
- Calcular y apilar el resultado.
4. Al terminar debe quedar exactamente un resultado.

Validar tokens incorrectos y división por cero.
PRUEBA: "3 4 + 5 *" -> 35.
    """
    pass


# ============================ COLAS ============================

def cola_banco():
    """
OBJETIVO: atender clientes por orden de llegada.

Crear un submenú:
1. Llega un cliente: leer nombre y añadirlo.
2. Atender: eliminar y mostrar al cliente.
3. Mostrar fila.
0. Volver.

PRUEBA: llegan Ana, Dan, Isma -> se atiende Ana primero.
    """
    pass


def cola_impresora():
    """
OBJETIVO: procesar documentos por orden de llegada.

PASOS:
1. Leer documentos: nombre y cantidad de páginas.
2. Guardar cada documento en la cola.
Puedes representar uno con (nombre, paginas).
3. Retirar documentos en orden.
4. Calcular paginas * 2 segundos para cada documento.
5. Mostrar el tiempo individual y el total acumulado.

Validar que las páginas sean positivas.
    """
    pass


def cola_prioridad():
    """
OBJETIVO: atender mayor prioridad primero y conservar el orden
de llegada entre elementos de igual prioridad.

ADAPTACIÓN:
Crear una estructura específica con un arreglo fijo y contador.
Guardar nombre y prioridad de cada elemento.
Al atender, buscar la mayor prioridad.
Si hay empate, elegir el que llegó antes.
Retirarlo y desplazar los elementos necesarios.

No usar sort(), sorted(), append(), pop() ni len().
Esta estructura tiene reglas distintas de la cola FIFO normal.

PRUEBA:
Ana prioridad 1, Dan prioridad 3, Isma prioridad 3.
Salida: Dan, Isma, Ana.
    """
    pass


def cola_tickets():
    """
OBJETIVO: asignar tickets consecutivos.

PASOS:
1. Crear una cola y un contador de tickets desde 1.
2. Al llegar alguien, guardar (ticket, nombre).
3. Aumentar el contador solo si se añadió correctamente.
4. Al atender, retirar al primero y mostrar su ticket.
5. Permitir mostrar la fila y volver al menú.

No reiniciar los tickets cada vez que se atiende a alguien.
    """
    pass


def cola_turnos():
    """
OBJETIVO: mostrar 10 turnos de jugadores.

PASOS:
1. Añadir los jugadores a una cola.
2. Comprobar que exista al menos uno.
3. Repetir 10 veces:
- Retirar al siguiente jugador.
- Mostrar su turno.
- Volver a añadirlo a la cola.

PRUEBA: Ana, Dan, Isma -> Ana, Dan, Isma, Ana...
    """
    pass


def cola_maximo_historico():
    """
OBJETIVO: recordar el mayor número que haya entrado,
aunque después sea eliminado.

ADAPTACIÓN:
Crear una clase derivada de MiCola, o una clase específica,
con un atributo maximo y un método maximo_visto().

PASOS:
1. Inicializar maximo con None.
2. Cada vez que se añade correctamente un número:
- Si maximo es None o el nuevo número es mayor, actualizarlo.
3. Eliminar elementos sin cambiar el máximo histórico.
4. Mostrar el resultado de maximo_visto().

PRUEBA:
Entran 5, 9, 3. Después salen todos.
El máximo histórico sigue siendo 9.
    """
    pass


def cola_cafe():
    """
OBJETIVO: simular 10 clientes en una sola cola y dos cajas.

PASOS:
1. Crear los 10 clientes con tiempos entre 30 y 90 segundos.
Puedes usar random.randint(30, 90).
2. Llevar el tiempo restante de cada caja.
3. En cada instante simulado:
- Si una caja está libre y hay clientes, asignarle el primero.
- Avanzar el tiempo y actualizar las cajas ocupadas.
4. Mostrar quién atiende cada caja y cuándo termina.
5. Finalizar cuando la cola esté vacía y ambas cajas estén libres.

Si ambas cajas están libres, asignar primero la caja 1.
No necesitas esperar segundos reales ni utilizar sleep().
    """
    pass
