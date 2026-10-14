def confirmar(mensaje):
    respuesta = input(f"{mensaje} [s/N]: ").strip().lower()
    return respuesta == "s"
