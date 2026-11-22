"""PRÁCTICA 1: LISTAS EN PYTHON, EXPLICADAS PASO A PASO

tarea_listas/
├── pasajero.py      ✅ terminado
├── mi_lista.py      ✍ Lista 1: completar métodos
├── lista_python.py  ✍ Lista 2: completar métodos
└── main.py          ✍ completar los dos menús


La primera parte construye MiLista para entender qué ocurre al añadir,
insertar, buscar, eliminar y ordenar elementos. Después hay ejemplos de la
lista incorporada de Python (`list`) y ejercicios del módulo de la guía.

Idea clave de MiLista: los elementos ocupan siempre los índices desde 0 hasta
cantidad - 1, sin espacios vacíos en medio. La capacidad es fija.
"""


class MiLista:
    """Lista educativa de capacidad fija, implementada con una lista de Python."""

    def __init__(self, capacidad=10):
        """Prepara los espacios vacíos y sus contadores.

        `self` es el objeto que se está creando. `capacidad` es el máximo de
        elementos que caben. Si no se especifica, usamos 10.
        """
        # Creamos los cajones. None significa que el espacio está disponible.
        # Con capacidad 5, al inicio queda [None, None, None, None, None].
        self.datos = [None] * capacidad

        # Número total de cajones disponibles.
        self.capacidad = capacidad

        # Número de cajones que tienen un elemento guardado.
        self.cantidad = 0

    def añadir(self, valor):
        """Guarda un valor al final. Avisa si ya se ocuparon todos los espacios."""
        # Cuando cantidad y capacidad son iguales, no queda un cajón libre.
        if self.cantidad >= self.capacidad:
            print("La lista está llena")
            return

        # cantidad señala el primer índice libre. Por ejemplo, con dos valores,
        # los índices ocupados son 0 y 1, así que el índice libre es 2.
        self.datos[self.cantidad] = valor

        # Actualizamos la cantidad porque ahora guardamos un elemento más.
        self.cantidad += 1

    def insertar(self, posicion, valor):
        """Inserta un valor y desplaza a la derecha los que estaban después."""
        # Comprobamos primero que haya espacio para el nuevo valor.
        if self.cantidad >= self.capacidad:
            print("La lista está llena")
            return

        # Para insertar, la posición puede ir desde 0 hasta cantidad.
        # cantidad significa insertar al final. No se permiten índices negativos
        # ni saltarse posiciones vacías.
        if posicion < 0 or posicion > self.cantidad:
            print("Posición no válida")
            return

        # Empezamos por el primer cajón vacío. Si hay 3 elementos, i empieza en 3.
        i = self.cantidad

        # Avanzamos hacia la izquierda, copiando cada elemento un lugar a la
        # derecha. Empezar por el final evita pisar datos que aún necesitamos.
        while i > posicion:
            self.datos[i] = self.datos[i - 1]
            i -= 1

        # Ya quedó libre el lugar solicitado; ponemos allí el valor nuevo.
        self.datos[posicion] = valor

        # La cantidad de elementos aumentó en uno.
        self.cantidad += 1

    def buscar(self, valor):
        """Búsqueda lineal: devuelve el índice o -1 si no encuentra el valor."""
        # range(cantidad) recorre únicamente los espacios ocupados:
        # 0, 1, 2, ..., cantidad - 1. No revisamos los None libres.
        for i in range(self.cantidad):
            if self.datos[i] == valor:
                return i  # Encontramos el valor; devolvemos su posición.

        # Si llegamos aquí, comparamos todos los valores y ninguno coincidió.
        return -1

    def buscar_binaria(self, valor):
        """Busca en una MiLista ordenada y devuelve el índice o -1.

        La búsqueda binaria solo funciona si los elementos están ordenados de
        menor a mayor. En cada paso descarta aproximadamente la mitad restante.
        """
        izquierda = 0
        derecha = self.cantidad - 1  # El último índice ocupado, no la capacidad.

        # Mientras quede un intervalo que revisar, seguimos buscando.
        while izquierda <= derecha:
            # // es división entera: el resultado es un índice sin decimales.
            medio = (izquierda + derecha) // 2

            if self.datos[medio] == valor:
                return medio  # El elemento del centro es el que buscábamos.
            elif self.datos[medio] < valor:
                # El centro es menor; el valor solo podría estar a su derecha.
                izquierda = medio + 1
            else:
                # El centro es mayor; el valor solo podría estar a su izquierda.
                derecha = medio - 1

        return -1  # El intervalo se acabó y el valor no apareció.

    def modificar(self, viejo, nuevo):
        """Reemplaza la primera coincidencia de `viejo` por `nuevo`."""
        # Reutilizamos buscar para obtener la posición del elemento anterior.
        posicion = self.buscar(viejo)

        if posicion == -1:
            print(viejo, "no existe")
            return

        # Sustituimos el contenido en el mismo cajón; la cantidad no cambia.
        self.datos[posicion] = nuevo

    def eliminar_por_posicion(self, posicion):
        """Elimina un elemento por índice y devuelve el valor eliminado."""
        # El último índice ocupado es cantidad - 1, por eso cantidad no es válido.
        if posicion < 0 or posicion >= self.cantidad:
            print("Posición no válida")
            return None

        # Guardamos el valor para poder devolverlo después de mover los demás.
        valor_eliminado = self.datos[posicion]

        # Corremos a la izquierda los elementos que estaban después del borrado.
        # Así cerramos el hueco y los elementos siguen juntos desde el índice 0.
        for i in range(posicion, self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]

        # El índice que antes tenía el último valor ahora queda libre.
        self.datos[self.cantidad - 1] = None

        # Hay un elemento activo menos. Devolvemos el que quitamos.
        self.cantidad -= 1
        return valor_eliminado

    def eliminar_por_valor(self, valor):
        """Busca un valor y elimina su primera coincidencia."""
        posicion = self.buscar(valor)

        if posicion == -1:
            print(valor, "no existe")
            return

        # El método por posición ya sabe desplazar los valores y ajustar cantidad.
        return self.eliminar_por_posicion(posicion)

    def ordenar_asc(self):
        """Ordena los elementos ocupados de menor a mayor usando burbuja."""
        n = self.cantidad

        # Cada vuelta completa deja uno de los valores mayores al final.
        for vuelta in range(n - 1):
            # En cada vuelta quedan menos pares por comparar.
            for i in range(n - 1 - vuelta):
                # Comparamos vecinos. Si están en orden contrario, los cambiamos.
                if self.datos[i] > self.datos[i + 1]:
                    auxiliar = self.datos[i]  # Guardamos uno para no perderlo.
                    self.datos[i] = self.datos[i + 1]
                    self.datos[i + 1] = auxiliar

    def reversar(self):
        """Invierte el orden actual; no ordena los valores por magnitud."""
        izquierda = 0
        derecha = self.cantidad - 1

        # Intercambiamos los extremos y nos acercamos al centro.
        while izquierda < derecha:
            auxiliar = self.datos[izquierda]
            self.datos[izquierda] = self.datos[derecha]
            self.datos[derecha] = auxiliar
            izquierda += 1
            derecha -= 1

    def copiar(self):
        """Crea otra MiLista con los mismos elementos y la misma capacidad."""
        nueva = MiLista(self.capacidad)

        # Copiamos solo los elementos activos, no los None que marcan espacios.
        for i in range(self.cantidad):
            nueva.añadir(self.datos[i])

        return nueva

    def longitud(self):
        """Devuelve cuántos elementos hay guardados (no la capacidad)."""
        return self.cantidad

    def listar(self):
        """Imprime cada elemento activo junto con su índice."""
        if self.cantidad == 0:
            print("Lista vacía")
            return

        for i in range(self.cantidad):
            print(f"[{i}] {self.datos[i]}")

    def __str__(self):
        """Permite mostrar los elementos al escribir print(mi_lista)."""
        # Mostramos únicamente los elementos activos; listar() muestra índices.
        return str(self.datos[:self.cantidad])


# ---------------------------------------------------------------------------
# Parte B: ejemplos con la lista incorporada de Python (list)
# ---------------------------------------------------------------------------

def ejemplo_listas_python():
    """Muestra las operaciones de listas nativas que explica la guía."""
    estudiantes = ["Ana", "Luis", "Diana"]

    # Los índices empiezan en cero. El índice -1 significa el último elemento.
    print("Primer estudiante:", estudiantes[0])
    print("Último estudiante:", estudiantes[-1])

    # append agrega al final; insert coloca el valor en una posición concreta.
    estudiantes.append("Carlos")
    estudiantes.insert(1, "Beto")

    # Se puede cambiar un valor asignando en su índice.
    estudiantes[2] = "Roberto"

    # in comprueba pertenencia. index obtiene el índice (si existe).
    if "Diana" in estudiantes:
        posicion = estudiantes.index("Diana")
        print("Diana está en el índice:", posicion)

    # remove recibe el valor y elimina su primera coincidencia.
    estudiantes.remove("Beto")

    # pop recibe un índice, elimina ese elemento y también lo devuelve.
    eliminado = estudiantes.pop(0)
    print("Eliminado con pop:", eliminado)
    print("Cantidad de estudiantes:", len(estudiantes))

    # Un for visita los valores. enumerate entrega índice y valor en cada vuelta.
    for indice, estudiante in enumerate(estudiantes):
        print(f"Índice {indice}: {estudiante}")

    numeros = [8, 3, 10, 5]

    # sort modifica la lista original; reverse=True la ordena de mayor a menor.
    numeros.sort()
    print("Orden ascendente:", numeros)
    numeros.sort(reverse=True)
    print("Orden descendente:", numeros)

    # reverse solo invierte el orden que ya tenía; no compara los números.
    numeros.reverse()
    print("Orden invertido:", numeros)

    # sorted crea una lista ordenada aparte; no modifica numeros.
    ordenada = sorted(numeros)
    print("Copia ordenada:", ordenada)

    # copy crea otra lista. Agregar a la copia no cambia la lista original.
    copia = numeros.copy()
    copia.append(99)
    print("Original:", numeros)
    print("Copia:", copia)

    # Slicing obtiene una parte: incluye el inicio y excluye el final.
    valores = [10, 20, 30, 40, 50]
    print("Índices 1 hasta antes del 4:", valores[1:4])
    print("Copia invertida con slicing:", valores[::-1])

    # Comprensión de listas: crea una lista filtrando valores con una condición.
    notas = [8, 6, 10, 7, 5]
    aprobadas = [nota for nota in notas if nota >= 7]
    print("Notas aprobadas:", aprobadas)

    # También transforma cada elemento. ** 2 significa elevar al cuadrado.
    cuadrados = [numero ** 2 for numero in [1, 2, 3, 4]]
    print("Cuadrados:", cuadrados)


# ---------------------------------------------------------------------------
# Ejercicios de práctica de la guía
# ---------------------------------------------------------------------------

def estadisticas_notas(notas, nombres=None, nota_minima=7):
    """Calcula promedio, máximo, mínimo y aprobados de una lista de notas.

    `nombres` es opcional. Si se proporciona, debe tener un nombre por nota y
    se informa quién obtuvo la nota más alta.
    """
    if len(notas) == 0:
        # No se puede dividir por cero ni pedir máximo/mínimo de una lista vacía.
        return None

    suma = 0
    aprobados = 0
    mayor = notas[0]  # Empezamos suponiendo que la primera nota es la mayor.
    menor = notas[0]  # También la usamos como primera candidata a la menor.
    indice_mejor = 0

    # Recorremos las notas para acumular su suma y contar las aprobadas.
    for indice, nota in enumerate(notas):
        suma += nota
        if nota >= nota_minima:
            aprobados += 1

        # Guardamos el índice de la nota más alta para encontrar su nombre.
        if nota > mayor:
            mayor = nota
            indice_mejor = indice

        if nota < menor:
            menor = nota

    promedio = suma / len(notas)

    mejor_estudiante = None
    if nombres is not None and len(nombres) == len(notas):
        # Las dos listas se relacionan por posición: nombre[i] corresponde a nota[i].
        mejor_estudiante = nombres[indice_mejor]

    return {
        "promedio": promedio,
        "maxima": mayor,
        "minima": menor,
        "aprobados": aprobados,
        "mejor_estudiante": mejor_estudiante,
    }


def ordenar_burbuja(valores):
    """Devuelve una copia ordenada ascendentemente con el método burbuja."""
    resultado = valores.copy()  # No modificamos la lista que recibió la función.
    n = len(resultado)

    for vuelta in range(n - 1):
        for i in range(n - 1 - vuelta):
            if resultado[i] > resultado[i + 1]:
                # Intercambio de dos vecinos usando una variable auxiliar.
                auxiliar = resultado[i]
                resultado[i] = resultado[i + 1]
                resultado[i + 1] = auxiliar

    return resultado


def contar_apariciones(valores, buscado):
    """Cuenta manualmente cuántas veces aparece un valor en una lista."""
    contador = 0

    for valor in valores:
        if valor == buscado:
            contador += 1

    return contador


def invertir_lista(valores):
    """Devuelve una copia con los elementos en el orden opuesto."""
    resultado = []

    # Visitamos los índices desde el último hasta el primero.
    for i in range(len(valores) - 1, -1, -1):
        resultado.append(valores[i])

    return resultado


def quitar_duplicados(valores):
    """Devuelve los valores únicos conservando el orden de su primera aparición."""
    resultado = []

    for valor in valores:
        # Solo añadimos el valor la primera vez que aparece.
        if valor not in resultado:
            resultado.append(valor)

    return resultado


def segundo_mayor(valores):
    """Devuelve el segundo valor más grande y distinto, o None si no existe."""
    unicos = quitar_duplicados(valores)

    if len(unicos) < 2:
        return None

    # Ordenamos una copia y tomamos el penúltimo valor.
    ordenados = ordenar_burbuja(unicos)
    return ordenados[-2]


def fusionar_ordenadas(lista_a, lista_b):
    """Combina dos listas ya ordenadas en una nueva lista también ordenada."""
    resultado = []
    i = 0  # Índice actual en la primera lista.
    j = 0  # Índice actual en la segunda lista.

    # Mientras haya valores en ambas listas, añadimos el menor de los dos.
    while i < len(lista_a) and j < len(lista_b):
        if lista_a[i] <= lista_b[j]:
            resultado.append(lista_a[i])
            i += 1
        else:
            resultado.append(lista_b[j])
            j += 1

    # Si quedaron elementos en una lista, los agregamos al final.
    while i < len(lista_a):
        resultado.append(lista_a[i])
        i += 1

    while j < len(lista_b):
        resultado.append(lista_b[j])
        j += 1

    return resultado


class Pasajero:
    """Representa un pasajero con nombre y cédula para el ejercicio CRUD."""

    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def __str__(self):
        # Este formato se usa al imprimir directamente el objeto.
        return f"{self.nombre} ({self.cedula})"


def buscar_por_cedula(pasajeros, cedula):
    """Devuelve el primer pasajero con esa cédula o None si no está."""
    for pasajero in pasajeros:
        if pasajero.cedula == cedula:
            return pasajero
    return None


def menu_pasajeros():
    """Ejercicio CRUD interactivo: crear, leer, actualizar y borrar pasajeros.

    Llama esta función cuando quieras practicar el menú. No se inicia sola al
    abrir el archivo para que puedas estudiar o ejecutar primero los ejemplos.
    """
    pasajeros = []

    while True:
        print("\n--- MENÚ DE PASAJEROS ---")
        print("1. Agregar  2. Listar  3. Buscar  4. Modificar  5. Eliminar  6. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre: ").strip()
            cedula = input("Cédula: ").strip()

            # Evitamos guardar dos pasajeros con la misma cédula.
            if buscar_por_cedula(pasajeros, cedula) is not None:
                print("Ya existe un pasajero con esa cédula")
            else:
                pasajeros.append(Pasajero(nombre, cedula))
                print("Pasajero agregado")

        elif opcion == "2":
            if not pasajeros:
                print("No hay pasajeros")

            # enumerate entrega el índice y el pasajero en cada repetición.
            for indice, pasajero in enumerate(pasajeros):
                print(f"[{indice}] {pasajero}")

        elif opcion == "3":
            cedula = input("Cédula que deseas buscar: ").strip()
            pasajero = buscar_por_cedula(pasajeros, cedula)
            print(pasajero if pasajero is not None else "No existe")

        elif opcion == "4":
            cedula = input("Cédula del pasajero: ").strip()
            pasajero = buscar_por_cedula(pasajeros, cedula)

            if pasajero is None:
                print("No existe")
            else:
                pasajero.nombre = input("Nuevo nombre: ").strip()
                print("Pasajero modificado")

        elif opcion == "5":
            cedula = input("Cédula del pasajero: ").strip()
            pasajero = buscar_por_cedula(pasajeros, cedula)

            if pasajero is None:
                print("No existe")
            else:
                # remove recibe el objeto encontrado y lo quita de la lista.
                pasajeros.remove(pasajero)
                print("Pasajero eliminado")

        elif opcion == "6":
            print("Fin del menú")
            break  # Sale del while y termina el menú.

        else:
            print("Opción no válida")


def ejemplos_milista():
    """Demostración de los métodos de MiLista de la primera parte de la guía."""
    mi = MiLista(capacidad=10)
    mi.añadir("Ana")
    mi.añadir("Carlos")
    mi.añadir("Diana")
    mi.insertar(1, "Beto")

    print("Elementos de MiLista:")
    mi.listar()
    print("Longitud:", mi.longitud())

    # buscar devuelve un índice o -1 si no encuentra el texto.
    print("Índice de Carlos:", mi.buscar("Carlos"))
    print("Índice de Zoe:", mi.buscar("Zoe"))

    mi.modificar("Beto", "Roberto")
    quitado = mi.eliminar_por_posicion(0)
    print("Eliminado por posición:", quitado)
    mi.eliminar_por_valor("Diana")

    mi.añadir("Eva")
    mi.ordenar_asc()  # Orden alfabético porque los elementos son textos.
    print("Ordenada:", mi)
    mi.reversar()
    print("Reversada:", mi)

    copia = mi.copiar()
    print("Copia:", copia)

    # La búsqueda binaria requiere que los datos estén ordenados.
    mi.ordenar_asc()
    print("Búsqueda binaria de Carlos:", mi.buscar_binaria("Carlos"))


def ejemplos_ejercicios():
    """Ejemplos pequeños de los algoritmos propuestos en el módulo de listas."""
    notas = [8, 6, 10, 7, 5]
    nombres = ["Ana", "Luis", "Diana", "Beto", "Eva"]
    print("Estadísticas:", estadisticas_notas(notas, nombres))

    print("Burbuja:", ordenar_burbuja([8, 3, 10, 5]))
    print("Apariciones de 2:", contar_apariciones([2, 1, 2, 3, 2], 2))
    print("Invertida:", invertir_lista([10, 20, 30]))
    print("Sin duplicados:", quitar_duplicados([3, 1, 3, 2, 1]))
    print("Segundo mayor distinto:", segundo_mayor([8, 3, 10, 10, 5]))
    print("Fusión ordenada:", fusionar_ordenadas([1, 4, 8], [2, 3, 9]))


if __name__ == "__main__":
    # Estas demostraciones se ejecutan al correr este archivo directamente.
    # El menú interactivo se inicia por separado con menu_pasajeros().
    ejemplos_milista()
    print("\n--- Ejemplos con list de Python ---")
    ejemplo_listas_python()
    print("\n--- Ejercicios de práctica ---")
    ejemplos_ejercicios()
