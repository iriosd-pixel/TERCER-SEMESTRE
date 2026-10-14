def confirmar(mensaje):
    return input(f"{mensaje} [s/N]: ").strip().lower() == "s"
