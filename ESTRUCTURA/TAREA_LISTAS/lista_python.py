# =====================================================================
#  lista_python.py  —  LISTA 2: con el list de PYTHON (built-in)
# ---------------------------------------------------------------------
#  Mismas operaciones que la Lista 1, pero ahora usamos lo que Python
#  ya trae: append, insert, pop, remove, sort, reverse, copy, len,
#  enumerate, next, bisect ... y LIST COMPREHENSIONS.
#
#      self.pasajeros -> [Pasajero, Pasajero, ...]   (crece sola)
#
#  ✅ OBLIGATORIO usar comprensiones de listas en (mínimo):
#       buscar · buscar_binaria · eliminar_por_valor (versión 2)
#       filtrar_mayores_de_edad · nombres_en_mayusculas
#
#  Recordatorio de la sintaxis:
#       [EXPRESIÓN for ELEMENTO in LISTA]            -> transformar
#       [ELEMENTO  for ELEMENTO in LISTA if COND]    -> filtrar
#       [EXPRESIÓN for ELEMENTO in LISTA if COND]    -> las dos a la vez
#
#  📌 Compara cada método con su gemelo de lista_manual.py:
#     allá eran 10 líneas, aquí casi siempre son 1 o 2.
#  Cuando termines un método, BORRA la línea "pass".
# =====================================================================

from bisect import bisect_left
from pasajero import Pasajero


class ListaPasajerosPython:

    def __init__(self):
        self.pasajeros = []               # list de Python: crece sola

    # -----------------------------------------------------------------
    # 1. AÑADIR  ✅ YA RESUELTO
    # -----------------------------------------------------------------
    def añadir(self, pasajero):
        """Añade al final sin permitir cédulas repetidas."""
        if self.buscar(pasajero.cedula) != -1:
            print("Ya existe un pasajero con esa cédula.")
            return False

        self.pasajeros.append(pasajero)
        return True

    # -----------------------------------------------------------------
    # 2. LISTAR  ✅ YA RESUELTO
    # -----------------------------------------------------------------
    def listar(self):
        """Muestra los pasajeros con su posición usando enumerate()."""
        if not self.pasajeros:                  # lista vacía es False
            print("(lista vacía)")
            return
        for i, p in enumerate(self.pasajeros):
            print(f"[{i}] {p}")

    # -----------------------------------------------------------------
    # 3. LONGITUD
    # -----------------------------------------------------------------
    def longitud(self):
        """
        USA      : len()
        RETORNA  : int.   PRUEBA: datos de prueba -> 5
        """
        return len(self.pasajeros)

    # -----------------------------------------------------------------
    # 4. INSERTAR
    # -----------------------------------------------------------------
    def insertar(self, posicion, pasajero):
        """
        USA      : self.pasajeros.insert(posicion, pasajero)
        VALIDA   : 0 <= posicion <= len(self.pasajeros); si no, mensaje y False.
        PIENSA   : ¿por qué ya no tienes que correr nada a la derecha?
                (Python lo hace por ti... pero lo sigue haciendo: O(n)).
        """

        if posicion < 0 or posicion > len(self.pasajeros):
            print("Posición no válida")
            return False
        
        self.pasajeros.insert(posicion, pasajero)
        return True

    # -----------------------------------------------------------------
    # 5. BUSCAR POR CÉDULA  (con COMPRENSIÓN)
    # -----------------------------------------------------------------
    def buscar(self, cedula):
        """
        RETORNA  : la posición (int) o -1.
        USA      : una comprensión con enumerate que junte las posiciones
                que coinciden:
                    posiciones = [i for i, p in enumerate(self.pasajeros)
                                    if p.cedula == cedula]
                Si la lista 'posiciones' está vacía -> -1,
                si no -> posiciones[0].
        EXTRA    : investiga la versión con next(...):
                next((i for i, p in enumerate(...) if ...), -1)
        PRUEBA   : buscar("0987654321") -> 2 ;  buscar("1111111111") -> -1
        """
        pos = [i for i, pasajero in enumerate(self.pasajeros) if pasajero.cedula == cedula]
        if pos:
            return pos[0]
        return -1
#     return next(
#     (i for i, pasajero in enumerate(self.pasajeros)
#      if pasajero.cedula == cedula),
#     -1
# )

    # -----------------------------------------------------------------
    # 6. BUSCAR BINARIA  (con COMPRENSIÓN + bisect)
    # -----------------------------------------------------------------
    def buscar_binaria(self, cedula):
        """
        ⚠ REQUISITO: lista ordenada por cédula (ordenar_asc antes).
        PASOS    :
        1. cedulas = [p.cedula for p in self.pasajeros]   # COMPRENSIÓN
        2. i = bisect_left(cedulas, cedula)   # dónde "debería" estar
        3. Si i < len(cedulas) y cedulas[i] == cedula -> return i
        4. return -1
        PRUEBA   : datos ordenados -> buscar_binaria("0923456789") -> 2
        """
        cedulas=[p.cedula for p in self.pasajeros]
        i= bisect_left(cedulas, cedula )
        if i<len(cedulas) and cedulas[i]== cedula:
            return i
        return -1       
    # -----------------------------------------------------------------
    # 7. MODIFICAR
    # -----------------------------------------------------------------
    def modificar(self, cedula, nuevo_nombre, nueva_edad):
        """
        PASOS    : pos = self.buscar(cedula); si -1 -> False;
                si no, cambia self.pasajeros[pos].nombre y .edad -> True
        """
        posicion= self.buscar(cedula)
        if posicion==-1:
            print("No existe un pasajero con esa cédula")
            return False
        self.pasajeros[posicion].nombre = nuevo_nombre
        self.pasajeros[posicion].edad = nueva_edad
        return True

    # -----------------------------------------------------------------
    # 8. ELIMINAR POR POSICIÓN
    # -----------------------------------------------------------------
    def eliminar_por_posicion(self, posicion):
        """
        USA      : self.pasajeros.pop(posicion)   (retorna el eliminado)
        VALIDA   : 0 <= posicion < len(...); si no -> mensaje y None
        """
        if posicion < 0 or posicion >= len(self.pasajeros):
            print("Posición no válida")
            return None
        return self.pasajeros.pop(posicion)

    # -----------------------------------------------------------------
    # 9. ELIMINAR POR VALOR (por cédula)  — hazlo de DOS formas
    # -----------------------------------------------------------------
    def eliminar_por_valor(self, cedula):
        """
        FORMA 1 (remove):
            pos = self.buscar(cedula) ... self.pasajeros.remove(self.pasajeros[pos])
        FORMA 2 (COMPRENSIÓN) — la que debe quedar activa:
            antes = len(self.pasajeros)
            self.pasajeros = [p for p in self.pasajeros if p.cedula != cedula]
            return len(self.pasajeros) < antes      # True si eliminó algo
        Deja la FORMA 1 comentada para comparar.
        """
        # pos=self.buscar(cedula)
        # if pos == -1:
        #     print("No existe un pasajero con esa cédula")
        #     return False
        # self.pasajeros.remove(self.pasajeros[pos])
        # return True
    
        antes = len(self.pasajeros)
        antes = len(self.pasajeros)
        self.pasajeros = [p for p in self.pasajeros if p.cedula != cedula]
        return len(self.pasajeros)<antes

    # -----------------------------------------------------------------
    # 10. ORDENAR ASCENDENTE (por cédula)
    # -----------------------------------------------------------------
    def ordenar_asc(self):
        """
        USA      : self.pasajeros.sort(key=lambda p: p.cedula)
        PIENSA   : ¿qué hace key=? ¿qué pasaría sin él? (pruébalo)
        """
        self.pasajeros.sort(key=lambda pasajero: pasajero.cedula)

    # -----------------------------------------------------------------
    # 11. ORDENAR DESCENDENTE (por cédula)
    # -----------------------------------------------------------------
    def ordenar_desc(self):
        """ USA : sort(key=..., reverse=True) """
        self.pasajeros.sort(key=lambda pasajero: pasajero.cedula, reverse=True)

    # -----------------------------------------------------------------
    # 12. REVERSAR
    # -----------------------------------------------------------------
    def reversar(self):
        """ USA : self.pasajeros.reverse()   (no es lo mismo que ordenar_desc) """
        self.pasajeros.reverse()

    # -----------------------------------------------------------------
    # 13. COPIAR
    # -----------------------------------------------------------------
    def copiar(self):
        """
        PASOS    :
        nueva = ListaPasajerosPython()
        nueva.pasajeros = self.pasajeros.copy()    # o self.pasajeros[:]
        return nueva
        ⚠ OJO    : es una copia SUPERFICIAL: las dos listas son distintas,
                pero los objetos Pasajero de adentro son los MISMOS.
                Reversar la copia no afecta al original;
                modificar un pasajero de la copia... ¡sí! Pruébalo.
        """
        nueva=ListaPasajerosPython()
        nueva.pasajeros=self.pasajeros.copy()
        return nueva

    # -----------------------------------------------------------------
    # 14. FILTRAR MAYORES DE EDAD  (COMPRENSIÓN que FILTRA)
    # -----------------------------------------------------------------
    def filtrar_mayores_de_edad(self):
        """
        RETORNA  : una NUEVA ListaPasajerosPython.
        PASOS    :
        nueva = ListaPasajerosPython()
        nueva.pasajeros = [p for p in self.pasajeros if p.es_mayor_de_edad()]
        return nueva
        PRUEBA   : datos de prueba -> todos menos Beto
        """
        nueva= ListaPasajerosPython()
        nueva.pasajeros = [p for p in self.pasajeros if p.es_mayor_de_edad()]
        return nueva

    # -----------------------------------------------------------------
    # 15. NOMBRES EN MAYÚSCULAS  (COMPRENSIÓN que TRANSFORMA)
    # -----------------------------------------------------------------
    def nombres_en_mayusculas(self):
        """
        RETORNA  : list de str ->  [p.nombre.upper() for p in self.pasajeros]
        PRUEBA   : ['DIANA', 'ANA', 'LUIS', 'BETO', 'ELENA']
        """
        return [p.nombre.upper() for p in self.pasajeros]

    def filtrar_por_destino(self, destino):
        return [
            p for p in self.pasajeros
            if p.destino == destino
        ]


    def mayores_de_edad(self):
        return [
            p for p in self.pasajeros
            if p.es_mayor_de_edad()
        ]