from pasajero import Pasajero
from lista_manual import ListaPasajerosManual
from lista_python import ListaPasajerosPython
from ejercicios import menu_ejercicios

lista1 = ListaPasajerosManual(10)
lista2 = ListaPasajerosPython()


# ------------------------- FUNCIONES DE APOYO -------------------------
def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ser un número entero.")


def leer_pasajero():
    numero = leer_entero("N.º de pasajero: ")
    nombre = input("Nombre: ").strip()
    cedula = input("Cédula: ").strip()
    edad = leer_entero("Edad: ")
    fecha_vuelo = input("Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("Destino: ").strip()
    asiento = input("Asiento: ").strip().upper()

    return Pasajero(
        numero, nombre, cedula, edad,
        fecha_vuelo, destino, asiento
    )


def cargar_datos_prueba(lista):
    lista.añadir(
        Pasajero(1005, "Diana", "0923456789", 22,
                 "2026-11-15", "Quito", "12A")
    )
    lista.añadir(
        Pasajero(1002, "Ana", "0912345678", 28,
                 "2026-11-15", "Lima", "03C")
    )
    lista.añadir(
        Pasajero(1009, "Luis", "0987654321", 35,
                 "2026-11-20", "Bogotá", "18F")
    )
    lista.añadir(
        Pasajero(1004, "Beto", "0934567890", 16,
                 "2026-11-20", "Quito", "07B")
    )
    lista.añadir(
        Pasajero(1001, "Elena", "0901234567", 41,
                 "2026-11-22", "Lima", "01A")
    )
    print("Carga de datos de prueba finalizada.")


def mostrar_opciones(titulo, extras=False):
    print(f"\n========== {titulo} ==========")
    print(" 1. Añadir pasajero")
    print(" 2. Listar pasajeros")
    print(" 3. Insertar en una posición")
    print(" 4. Buscar por cédula (lineal)")
    print(" 5. Buscar por cédula (binaria)")
    print(" 6. Modificar nombre y edad")
    print(" 7. Eliminar por posición")
    print(" 8. Eliminar por cédula")
    print(" 9. Ordenar ascendente por cédula")
    print("10. Ordenar descendente por cédula")
    print("11. Reversar")
    print("12. Copiar lista")
    print("13. Longitud")
    print("14. Filtrar mayores de edad")
    print("15. Nombres en mayúsculas")

    if extras:
        print("16. Filtrar por destino")
        print("17. Mayores de edad")

    print(" C. Cargar datos de prueba")
    print(" 0. Volver")


# ---------------------- MENÚ 1 · LISTA MANUAL ----------------------
def menu_lista1():
    while True:
        mostrar_opciones("MENÚ 1 · Lista manual")
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()
            if lista1.añadir(pasajero):
                print("Pasajero añadido.")

        elif op == "2":
            lista1.listar()

        elif op == "3":
            posicion = leer_entero("Posición para insertar: ")
            pasajero = leer_pasajero()

            if lista1.insertar(posicion, pasajero):
                print("Pasajero insertado.")

        elif op == "4":
            cedula = input("Cédula que buscas: ").strip()
            posicion = lista1.buscar(cedula)

            if posicion == -1:
                print("No existe un pasajero con esa cédula.")
            else:
                print(
                    f"Encontrado en [{posicion}]: "
                    f"{lista1.datos[posicion]}"
                )

        elif op == "5":
            print("Recuerda ordenar primero por cédula (opción 9).")
            cedula = input("Cédula que buscas: ").strip()
            posicion = lista1.buscar_binaria(cedula)

            if posicion == -1:
                print("No se encontró esa cédula. Comprueba el orden.")
            else:
                print(
                    f"Encontrado en [{posicion}]: "
                    f"{lista1.datos[posicion]}"
                )

        elif op == "6":
            cedula = input("Cédula del pasajero: ").strip()
            nuevo_nombre = input("Nuevo nombre: ").strip()
            nueva_edad = leer_entero("Nueva edad: ")

            if lista1.modificar(cedula, nuevo_nombre, nueva_edad):
                print("Pasajero modificado.")

        elif op == "7":
            posicion = leer_entero("Posición que quieres eliminar: ")
            eliminado = lista1.eliminar_por_posicion(posicion)

            if eliminado is not None:
                print(f"Eliminado: {eliminado}")

        elif op == "8":
            cedula = input("Cédula que quieres eliminar: ").strip()

            if lista1.eliminar_por_valor(cedula):
                print("Pasajero eliminado.")

        elif op == "9":
            lista1.ordenar_asc()
            lista1.listar()

        elif op == "10":
            lista1.ordenar_desc()
            lista1.listar()

        elif op == "11":
            lista1.reversar()
            lista1.listar()

        elif op == "12":
            copia = lista1.copiar()
            copia.reversar()

            print("\n--- COPIA REVERSADA ---")
            copia.listar()

            print("\n--- ORIGINAL ---")
            lista1.listar()

        elif op == "13":
            print(f"Hay {lista1.longitud()} pasajeros.")

        elif op == "14":
            mayores = lista1.filtrar_mayores_de_edad()
            print("\n--- MAYORES DE EDAD ---")
            mayores.listar()

        elif op == "15":
            nombres = lista1.nombres_en_mayusculas()
            print(nombres)

        elif op == "C":
            cargar_datos_prueba(lista1)

        elif op == "0":
            break

        else:
            print("Opción no válida.")


# ---------------------- MENÚ 2 · LIST DE PYTHON ----------------------
def menu_lista2():
    while True:
        mostrar_opciones("MENÚ 2 · list de Python", extras=True)
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()
            if lista2.añadir(pasajero):
                print("Pasajero añadido.")

        elif op == "2":
            lista2.listar()

        elif op == "3":
            posicion = leer_entero("Posición para insertar: ")
            pasajero = leer_pasajero()

            if lista2.insertar(posicion, pasajero):
                print("Pasajero insertado.")

        elif op == "4":
            cedula = input("Cédula que buscas: ").strip()
            posicion = lista2.buscar(cedula)

            if posicion == -1:
                print("No existe un pasajero con esa cédula.")
            else:
                print(
                    f"Encontrado en [{posicion}]: "
                    f"{lista2.pasajeros[posicion]}"
                )

        elif op == "5":
            print("Recuerda ordenar primero por cédula (opción 9).")
            cedula = input("Cédula que buscas: ").strip()
            posicion = lista2.buscar_binaria(cedula)

            if posicion == -1:
                print("No se encontró esa cédula. Comprueba el orden.")
            else:
                print(
                    f"Encontrado en [{posicion}]: "
                    f"{lista2.pasajeros[posicion]}"
                )

        elif op == "6":
            cedula = input("Cédula del pasajero: ").strip()
            nuevo_nombre = input("Nuevo nombre: ").strip()
            nueva_edad = leer_entero("Nueva edad: ")

            if lista2.modificar(cedula, nuevo_nombre, nueva_edad):
                print("Pasajero modificado.")

        elif op == "7":
            posicion = leer_entero("Posición que quieres eliminar: ")
            eliminado = lista2.eliminar_por_posicion(posicion)

            if eliminado is not None:
                print(f"Eliminado: {eliminado}")

        elif op == "8":
            cedula = input("Cédula que quieres eliminar: ").strip()

            if lista2.eliminar_por_valor(cedula):
                print("Pasajero eliminado.")
            else:
                print("No existe un pasajero con esa cédula.")

        elif op == "9":
            lista2.ordenar_asc()
            lista2.listar()

        elif op == "10":
            lista2.ordenar_desc()
            lista2.listar()

        elif op == "11":
            lista2.reversar()
            lista2.listar()

        elif op == "12":
            copia = lista2.copiar()
            copia.reversar()

            print("\n--- COPIA REVERSADA ---")
            copia.listar()

            print("\n--- ORIGINAL ---")
            lista2.listar()

        elif op == "13":
            print(f"Hay {lista2.longitud()} pasajeros.")

        elif op == "14":
            mayores = lista2.filtrar_mayores_de_edad()
            print("\n--- MAYORES DE EDAD ---")
            mayores.listar()

        elif op == "15":
            nombres = lista2.nombres_en_mayusculas()
            print(nombres)

        elif op == "16":
            destino = input("Destino que quieres buscar: ").strip()
            pasajeros = lista2.filtrar_por_destino(destino)

            if not pasajeros:
                print("No hay pasajeros con ese destino.")
            else:
                print(f"\n--- PASAJEROS CON DESTINO A {destino} ---")
                for pasajero in pasajeros:
                    print(pasajero)

        elif op == "17":
            pasajeros = lista2.mayores_de_edad()

            if not pasajeros:
                print("No hay pasajeros mayores de edad.")
            else:
                print("\n--- MAYORES DE EDAD ---")
                for pasajero in pasajeros:
                    print(pasajero)

        elif op == "C":
            cargar_datos_prueba(lista2)

        elif op == "0":
            break

        else:
            print("Opción no válida.")


# ---------------------- MENÚ PRINCIPAL ----------------------
def main():
    while True:
        print("\n===== TAREA LISTAS - PASAJEROS =====")
        print("1. Menú 1 · Lista manual")
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
            print("Opción no válida.")


if __name__ == "__main__":
    main()