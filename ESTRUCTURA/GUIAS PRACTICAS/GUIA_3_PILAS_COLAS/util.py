import os

from datetime import datetime

def borrar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")
    
def leer_entero(mensaje, minimo=1):
    while True:
        try:
            numero=int(input(mensaje))
            if numero>= minimo:
                return numero
            print(f"Debe ser un número mayor o igual a {minimo}")
        except ValueError:
            print("  Debe ser un número entero.")
            
def menu(titulo, opciones ):
    print(f"\n-----------{titulo}-----------")
    for opcion in opciones:
        print(f" {opcion}")
        lon= len(opciones)
    return input(f"Opcion [0...{lon}]: ").strip().upper()

def validar_cedula(mensaje):
    while True:
        
        cedula=input(mensaje).strip()
        if cedula.isdigit() and len(cedula)==10:
            return cedula
        print("La cédula debe tener exactamente 10 dígitos.")

def validar_vacio(mensaje):
    while True:
        texto= input(mensaje).strip()
        
        if texto:
            return texto
        print("Este campo no puede quedar vacio")

def fecha_vuelo_valida(mensaje):
    while True:
        fecha = input(mensaje).strip()

        try:
            fecha_convertida = datetime.strptime(fecha, "%Y-%m-%d").date()

            if fecha_convertida >= datetime.today().date():
                return fecha
            print("La fecha de vuelo no puede ser pasada.")
        except ValueError:
            print("Ingresa una fecha válida con el formato AAAA-MM-DD.")

def nombre_destino_con_letras(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto and texto.replace(" ", "").isalpha():
            return texto
        print("El campo no puede quedar vacío y debe contener solo letras y espacios.")

def validar_asiento(mensaje):
    while True:
        asiento = input(mensaje).strip().upper()

        if len(asiento) >= 2 and asiento[:-1].isdigit() and asiento[-1].isalpha():
            return asiento
        print("Formato inválido. Usa números seguidos de una letra, por ejemplo 12A.")

