from views import DepartamentoController, EmpleadoController, NominaController

departamentos = DepartamentoController()
empleados = EmpleadoController(departamentos)
nominas = NominaController(empleados)
departamentos.empleados = empleados
empleados.nominas = nominas


def menu(nombre, controlador, campos):
    while True:
        print(f"\n{nombre} | 1 Crear | 2 Listar | 3 Buscar | 4 Ver ID | 5 Actualizar | 6 Eliminar | 0 Volver")
        opcion = input("Opción: ").strip()
        if opcion == "0": return
        if opcion == "1":
            datos = {}
            for campo in campos: datos[campo] = input(f"{campo}: ")
            print(*controlador.crear(datos))
        elif opcion == "2":
            for objeto in controlador.leer(): print(objeto, objeto.a_diccionario())
        elif opcion == "3":
            for objeto in controlador.buscar(input("Texto: ")): print(objeto)
        elif opcion == "4":
            try: objeto = controlador.obtener(int(input("ID: ")))
            except ValueError: objeto = None
            print(objeto if objeto else "No encontrado")
        elif opcion == "5":
            try: id_registro = int(input("ID: "))
            except ValueError: print("ID inválido"); continue
            objeto = controlador.obtener(id_registro)
            if objeto is None: print("No encontrado"); continue
            cambios = {}
            for campo in campos:
                valor = input(f"{campo} [{getattr(objeto, campo)}] (vacío conserva): ").strip()
                if valor: cambios[campo] = valor
            print(*controlador.actualizar(id_registro, cambios))
        elif opcion == "6":
            try: id_registro = int(input("ID: "))
            except ValueError: print("ID inválido"); continue
            respuesta = input("Confirmar eliminación [s/N]: ").strip().lower()
            print(*controlador.eliminar(id_registro)) if respuesta == "s" else print("Cancelado")


def main():
    while True:
        print("\nNÓMINA | 1 Departamentos | 2 Empleados | 3 Nóminas | 0 Salir")
        opcion = input("Opción: ").strip()
        if opcion == "0": return
        if opcion == "1": menu("Departamentos", departamentos, ("nombre",))
        elif opcion == "2": menu("Empleados", empleados, ("nombre", "apellido", "email", "departamento_id"))
        elif opcion == "3": menu("Nóminas", nominas, ("empleado_id", "periodo", "sueldo_base", "bonificacion", "descuento"))


if __name__ == "__main__": main()
