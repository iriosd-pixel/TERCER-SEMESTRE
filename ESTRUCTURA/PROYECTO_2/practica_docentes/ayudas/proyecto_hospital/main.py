from views import PacienteController, MedicoController, CitaController

pacientes = PacienteController()
medicos = MedicoController()
citas = CitaController(pacientes, medicos)
pacientes.citas = citas
medicos.citas = citas


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
            for obj in controlador.leer(): print(obj, obj.a_diccionario())
        elif opcion == "3":
            for obj in controlador.buscar(input("Texto: ")): print(obj)
        elif opcion == "4":
            try: obj = controlador.obtener(int(input("ID: ")))
            except ValueError: obj = None
            print(obj if obj else "No encontrado")
        elif opcion == "5":
            try: id_registro = int(input("ID: "))
            except ValueError: print("ID inválido"); continue
            obj = controlador.obtener(id_registro)
            if obj is None: print("No encontrado"); continue
            cambios = {}
            for campo in campos:
                valor = input(f"{campo} [{getattr(obj, campo)}] (vacío conserva): ").strip()
                if valor: cambios[campo] = valor
            print(*controlador.actualizar(id_registro, cambios))
        elif opcion == "6":
            try: id_registro = int(input("ID: "))
            except ValueError: print("ID inválido"); continue
            if input("Confirmar eliminación [s/N]: ").strip().lower() == "s": print(*controlador.eliminar(id_registro))
            else: print("Cancelado")


def main():
    while True:
        print("\nHOSPITAL | 1 Pacientes | 2 Médicos | 3 Citas | 0 Salir")
        opcion = input("Opción: ").strip()
        if opcion == "0": return
        if opcion == "1": menu("Pacientes", pacientes, ("nombre", "apellido", "email", "telefono"))
        elif opcion == "2": menu("Médicos", medicos, ("nombre", "apellido", "email", "especialidad"))
        elif opcion == "3": menu("Citas", citas, ("paciente_id", "medico_id", "fecha", "hora"))


if __name__ == "__main__": main()
