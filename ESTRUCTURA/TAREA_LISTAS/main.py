from pasajero import Pasajero
from lista_manual import ListaPasajerosManual
from lista_python import ListaPasajerosPython
from ejercicios import menu_ejercicios

lista1 = ListaPasajerosManual(10)
lista2 = ListaPasajerosPython()


# ------------------------- funciones de apoyo ✅ -------------------------
def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ser un número entero.")


def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha_vuelo = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha_vuelo, destino, asiento)


def cargar_datos_prueba(lista):
    lista.añadir(Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito", "12A"))
    lista.añadir(Pasajero(1002, "Ana", "0912345678", 28, "2026-11-15", "Lima", "03C"))
    lista.añadir(Pasajero(1009, "Luis", "0987654321", 35, "2026-11-20", "Bogotá", "18F"))
    lista.añadir(Pasajero(1004, "Beto", "0934567890", 16, "2026-11-20", "Quito", "07B"))
    lista.añadir(Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima", "01A"))
    print("  OK: Datos de prueba cargados")


def mostrar_opciones(titulo, extras=False):
    print(f"\n========== {titulo} ==========")
    print(" 1. Añadir           2. Listar            3. Insertar en posición")
    print(" 4. Buscar por cédula (lineal)  5. Buscar por cédula (binaria)  6. Modificar")
    print(" 7. Eliminar por posición                 8. Eliminar por cédula")
    print(" 9. Ordenar asc     10. Ordenar desc     11. Reversar")
    print("12. Copiar          13. Longitud")
    if extras:
        print("14. Filtrar mayores de edad              15. Nombres en mayúsculas")
    print(" C. Cargar datos de prueba                0. Volver")


# ---------------------- MENÚ 1 · MiLista ----------------------
def menu_lista1():
    while True:
        mostrar_opciones("MENÚ 1 · MiLista")
        op = input("Opción: ").strip().upper()

        if op == "1":                                  # ✅ ejemplo resuelto
            pasajero = leer_pasajero()                 # 1. LEER
            if lista1.añadir(pasajero):                # 2. LLAMAR
                print("  OK: Pasajero añadido")          # 3. MOSTRAR
        elif op == "2":
            lista1.listar()
        elif op == "C":
            cargar_datos_prueba(lista1)
        elif op == "4":
            cedula = input("Cédula que buscas: ").strip()
            posicion = lista1.buscar(cedula)
            if posicion == -1:
                print("No existe un pasajero con esa cédula")
            else:
                print(f"Encontrado en [{posicion}]: {lista1.datos[posicion]}")
        elif op == "5":
            print("Recuerda ordenar primero la lista por cédula (opción 9).")
            cedula = input("Cédula que buscas: ").strip()
            posicion = lista1.buscar_binaria(cedula)
            if posicion == -1:
                print("No existe un pasajero con esa cédula")
            else:
                print(f"Encontrado en [{posicion}]: {lista1.datos[posicion]}")
        elif op == "6":
            cedula = input("Cédula del pasajero: ").strip()
            nuevo_nombre = input("Nuevo nombre: ").strip()
            nueva_edad = leer_entero("Nueva edad: ")
            if lista1.modificar(cedula, nuevo_nombre, nueva_edad):
                print("Pasajero modificado")
        elif op == "9":
            lista1.ordenar_asc()
            lista1.listar()

        # ✍ TODO: opciones 3 a 13 con el patrón LEER → LLAMAR → MOSTRAR

        elif op == "0":
            break
        else:
            print("  Opción no válida")


# ---------------------- MENÚ 2 · list de Python ----------------------
def menu_lista2():
    while True:
        mostrar_opciones("MENÚ 2 · list de Python", extras=True)
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()
            if lista2.añadir(pasajero):
                print("Pasajero añadido")
        elif op == "2":
            lista2.listar()
        elif op == "C":
            cargar_datos_prueba(lista2)
        elif op == "4":
            cedula = input("Cédula que buscas: ").strip()
            posicion = lista2.buscar(cedula)
            if posicion == -1:
                print("No existe un pasajero con esa cédula")
            else:
                print(f"Encontrado en [{posicion}]: {lista2.pasajeros[posicion]}")
        elif op == "5":
            print("Recuerda ordenar primero la lista por cédula (opción 9).")
            cedula = input("Cédula que buscas: ").strip()
            posicion = lista2.buscar_binaria(cedula)
            if posicion == -1:
                print("No existe un pasajero con esa cédula")
            else:
                print(f"Encontrado en [{posicion}]: {lista2.pasajeros[posicion]}")
        elif op == "6":
            cedula = input("Cédula del pasajero: ").strip()
            nuevo_nombre = input("Nuevo nombre: ").strip()
            nueva_edad = leer_entero("Nueva edad: ")
            if lista2.modificar(cedula, nuevo_nombre, nueva_edad):
                print("Pasajero modificado")
        elif op == "9":
            lista2.ordenar_asc()
            lista2.listar()
        elif op == "0":
            break
        else:
            print("Opción todavía no implementada")


# ---------------------- MENÚ PRINCIPAL ✅ ----------------------
def main():
    while True:
        print("\n===== TAREA LISTAS - PASAJEROS =====")
        print("1. Menú 1 · MiLista")
        print("2. Menú 2 · list de Python")
        print("3. Listar ejercicios")
        print("4. Salir")
        op = input("Opción: ").strip()
        if op == "1":
            menu_lista1()
        elif op == "2":
            menu_lista2()
        elif op == "3":
            menu_ejercicios()
        elif op == "4":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
