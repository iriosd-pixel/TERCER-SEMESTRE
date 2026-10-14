from views import EmpleadoController
from shared.herramientas import confirmar

empleados = EmpleadoController()


def ejecutar():
    while True:
        print("\nEMPLEADOS | 1 Crear | 2 Listar | 3 Buscar | 4 Ver ID | 5 Actualizar | 6 Eliminar | 0 Salir")
        opcion = input("Opción: ").strip()
        if opcion == "0": break
        if opcion == "1":
            datos = {"nombre": input("Nombre: "), "apellido": input("Apellido: "), "email": input("Email: "), "cargo": input("Cargo: ")}
            print(*empleados.crear(datos))
        elif opcion == "2":
            for empleado in empleados.leer(): print(empleado)
        elif opcion == "3":
            for empleado in empleados.buscar(input("Buscar: ")): print(empleado)
        elif opcion == "4":
            try: empleado = empleados.obtener(int(input("ID: ")))
            except ValueError: empleado = None
            print(empleado if empleado else "No encontrado")
        elif opcion == "5":
            try: id_registro = int(input("ID: "))
            except ValueError: print("ID inválido"); continue
            empleado = empleados.obtener(id_registro)
            if empleado is None: print("No encontrado"); continue
            cambios = {}
            for campo in ("nombre", "apellido", "email", "cargo"):
                valor = input(f"{campo} [{getattr(empleado, campo)}] (vacío conserva): ").strip()
                if valor: cambios[campo] = valor
            print(*empleados.actualizar(id_registro, cambios))
        elif opcion == "6":
            try: id_registro = int(input("ID: "))
            except ValueError: print("ID inválido"); continue
            if confirmar("¿Confirma eliminar?"): print(*empleados.eliminar(id_registro))
            else: print("Operación cancelada")
        else: print("Opción inválida")


if __name__ == "__main__": ejecutar()
