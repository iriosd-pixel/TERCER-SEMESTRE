from pasajero import Pasajero
from mi_pila import MiPila
from mi_cola import MiCola
from util import (
    borrar_pantalla,
    leer_entero,
    menu,
    validar_cedula,
    validar_vacio,
    fecha_vuelo_valida,
    nombre_destino_con_letras,
    validar_asiento
)

pila = MiPila(10)
cola = MiCola(10)


# ------------------------- funciones de apoyo ✅ -------------------------



def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = nombre_destino_con_letras("  Nombre: ")
    cedula = validar_cedula("  Cédula: ")
    edad = leer_entero("  Edad: ")
    fecha = fecha_vuelo_valida("  Fecha de vuelo (AAAA-MM-DD): ")
    destino = nombre_destino_con_letras("  Destino: ")
    asiento = validar_asiento("  Asiento: ").upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def datos_prueba():
    """Los 5 pasajeros de prueba en ORDEN DE LLEGADA (Diana llega primero, Elena última)."""
    return [
        Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito",  "12A"),
        Pasajero(1002, "Ana",   "0912345678", 28, "2026-11-15", "Lima",   "03C"),
        Pasajero(1009, "Luis",  "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto",  "0934567890", 16, "2026-11-20", "Quito",  "07B"),
        Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima",   "01A"),
    ]



# ---------------------- MENÚ 1 · PILA ----------------------
def menu_pila():
    while True:
        borrar_pantalla()
        op = menu(
            "MENÚ 1 · PILA (LIFO)",
            [
                "1. Apilar",
                "2. Listar",
                "3. Desapilar",
                "4. Ver tope",
                "5. Buscar por número",
                "6. Modificar destino y asiento",
                "7. Eliminar por número",
                "8. Copiar",
                "9. Longitud / ¿vacía?",
                "10. Cargar datos de prueba",
                "11. Volver",
            ],
        )

        if op == "1":
            pasajero = leer_pasajero()
            if pila.apilar(pasajero):
                print("✓ Apilado: ahora es el tope")
        elif op == "2":
            pila.listar()
        elif op == "3":
            pasajero= pila.desapilar()
            
            if pasajero is not None:
                print(f"✓ Pasajero desapilado: {pasajero}")
                
        elif op == "4":
            pasajero= pila.ver_tope()
            if pasajero is None:
                print("La pila está vacía.")
            else:
                print(f"Pasajero en el tope: {pasajero}")
                
        elif op == "5":
            numero= leer_entero("Numero de pasajero")
            posicion= pila.buscar(numero)
            
            if posicion==-1:
                print(f"NO se encontro el pasajero con el numero {numero}")
            else:
                print(f"Encontrado en la posicion {posicion}")
                print(pila.datos[posicion])
        
        elif op == "6":
            numero = leer_entero("Número del pasajero a modificar: ")
            nuevo_destino = nombre_destino_con_letras("Nuevo destino: ")
            nuevo_asiento = validar_asiento("Nuevo asiento: ")

            if pila.modificar(numero, nuevo_destino, nuevo_asiento):
                print("✓ Destino y asiento actualizados.")
        
        elif op == "7":
            numero=leer_entero("Numero del pasajero que desea eliminar: ")
            if pila.eliminar_por_numero(numero):
                print(f" Pasjero {numero} eliminado")
        
        elif op == "8":
            copia=pila.copiar()
            print(" Copia de la pila: ")
            copia.listar()
        
        elif op == "9":
            print(f"Longitud de la pila {pila.longitud()}")
            
            if pila.esta_vacia():
                print("La pila esta vacía")
            else:
                print("La pila no esta vacia")
        
        elif op == "10":
            for pasajero in datos_prueba():
                pila.apilar(pasajero)
            print("✓ Datos de prueba apilados")
        elif op == "11":
            break
        else:
            print("Opción no válida")
        input("\nPresiona Enter para continuar...")


# ---------------------- MENÚ 2 · COLA ----------------------
def menu_cola():
    while True:
        borrar_pantalla()
        op = menu(
            "MENÚ 2 · COLA (FIFO)",
            [
                "1. Encolar",
                "2. Listar",
                "3. Desencolar",
                "4. Ver frente",
                "5. Buscar por número",
                "6. Modificar destino y asiento",
                "7. Eliminar por número",
                "8. Copiar",
                "9. Longitud / ¿vacía?",
                "10. Filtrar mayores de edad",
                "11. Nombres en mayúsculas",
                "12. Cargar datos de prueba",
                "13. Volver",
            ],
        )

        if op == "1":
            pasajero = leer_pasajero()
            if cola.encolar(pasajero):
                print("✓ Encolado: está al final")

        elif op == "2":
            cola.listar()

        elif op == "3":
            pasajero = cola.desencolar()
            if pasajero is not None:
                print(f"✓ Pasajero desencolado: {pasajero}")

        elif op == "4":
            pasajero = cola.ver_frente()
            if pasajero is None:
                print("La cola está vacía.")
            else:
                print(f"Pasajero al frente: {pasajero}")

        elif op == "5":
            numero = leer_entero("Numero del pasajero")
            posicion = cola.buscar(numero)
            if posicion == -1:
                print(f"No se encontró al pasajero {numero}.")
            else:
                print(f"Encontrado en la posición {posicion}:")
                print(cola.datos[posicion])

        elif op == "6":
            numero = leer_entero("Número de pasajero a modificar: ")
            nuevo_destino = nombre_destino_con_letras("Nuevo destino: ")
            nuevo_asiento = validar_asiento("Nuevo asiento: ").upper()
            if cola.modificar(numero, nuevo_destino, nuevo_asiento):
                print("✓ Destino y asiento actualizados.")

        elif op == "7":
            numero = leer_entero("Número de pasajero que deseas eliminar: ")
            if cola.eliminar_por_numero(numero):
                print(f"✓ Pasajero {numero} eliminado.")

        elif op == "8":
            copia = cola.copiar()
            print("✓ Copia de la cola:")
            copia.listar()

        elif op == "9":
            print(f"Longitud de la cola: {cola.longitud()}")
            if cola.esta_vacia():
                print("La cola está vacía.")
            else:
                print("La cola no está vacía.")

        elif op == "10":
            mayores = cola.filtrar_mayores_de_edad()
            print("Pasajeros mayores de edad:")
            mayores.listar()

        elif op == "11":
            nombres = cola.nombres_en_mayusculas()
            print("Nombres en mayúsculas:")
            for i in range(cola.longitud()):
                print(nombres[i])

        elif op == "12":
            for pasajero in datos_prueba():
                cola.encolar(pasajero)
            print("✓ Datos de prueba encolados")

        elif op == "13":
            break

        else:
            print("Opción no válida")

        input("\nPresiona Enter para continuar...")


# ---------------------- MENÚ PRINCIPAL ✅ ----------------------
def main():
    while True:
        borrar_pantalla()
        op = menu("Menú Principal", ["1) Pila", "2) Cola", "3) Salir"])
        if op == "1":
            menu_pila()
        elif op == "2":
            menu_cola()
        elif op == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()