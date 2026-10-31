# =====================================================================
#  pasajero.py  —  CLASE DE DOMINIO (ya está terminada, NO la modifiques)
# ---------------------------------------------------------------------
#  Un Pasajero es el "dato" que vamos a guardar en las dos listas.
#  La CÉDULA es la clave: no puede haber dos pasajeros con la misma.
# =====================================================================


class Pasajero:
    """Representa a un pasajero de la aerolínea."""

    def __init__(self, nombre, cedula, carrera):
        self.nombre = nombre      # str  -> "Ana"
        self.cedula = cedula      # str  -> "0912345678"  (clave única)
        self.carrera = carrera          # int  -> 28

    def es_mayor_de_edad(self):
        """Retorna True si el pasajero tiene 18 años o más."""
        return self.edad >= 18

    def __str__(self):
        """Así se ve un pasajero cuando haces print(pasajero)."""
        return f"{self.nombre} | cédula: {self.cedula} | {self.carrera} años"