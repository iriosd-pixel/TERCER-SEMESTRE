#================================================
#EJEMPLOS PUESTOS POR LA IA MAS CAMBIOS
#================================================

#================================================
# 1)Crear la clase Pasajero con nombre, cédula y edad. Crear tres instancias y mostrarlas.
#================================================
class Pasajero:
    def __init__(self, nombre, cedula, edad):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} ({self.cedula}) - {self.edad} años"

# --- Programa principal ---
p1 = Pasajero("Ana", "0912345678", 28)
p2 = Pasajero("Luis", "0987654321", 35)
p3 = Pasajero("Diana", "0923456789", 22)

print(p1)
print(p2)
print(p3)
#CAMBIO
#Añade un método cumplir_anios() que sume 1 a la edad.
class Pasajero:
    def __init__(self, nombre, cedula, edad):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} ({self.cedula}) - {self.edad} años"

    def cumplir_anios(self):
        self.edad += 1


# --- Programa principal ---
p1 = Pasajero("Ana", "0912345678", 28)
p2 = Pasajero("Luis", "0987654321", 35)
p3 = Pasajero("Diana", "0923456789", 22)

print("Antes de cumplir años:")
print(p1)
print(p2)
print(p3)

# Cada pasajero cumple un año más
p1.cumplir_anios()
p2.cumplir_anios()
p3.cumplir_anios()

print("\nDespués de cumplir años:")
print(p1)
print(p2)
print(p3)

#================================================
# 2) Crear CuentaBancaria con métodos depositar, retirar, saldo y __str__.
# El saldo empieza en 0. No se puede retirar más de lo que hay.
#================================================
class CuentaBancaria:
    def __init__(self, numero):
        self.numero = numero
        self._saldo = 0                # el _ indica "atributo interno"

    def depositar(self, monto):
        if monto <= 0:
            print("Monto inválido"); return
        self._saldo += monto
        print(f"Depósito de ${monto}. Saldo: ${self._saldo}")

    def retirar(self, monto):
        if monto <= 0:
            print("Monto inválido"); return
        if monto > self._saldo:
            print(f"Saldo insuficiente (tiene ${self._saldo})"); return
        self._saldo -= monto
        print(f"Retiro de ${monto}. Saldo: ${self._saldo}")

    def saldo(self):
        return self._saldo

    def __str__(self):
        return f"Cuenta {self.numero}: ${self._saldo}"

# --- Uso ---
c = CuentaBancaria("001")
c.depositar(100)         # Depósito de $100. Saldo: $100
c.retirar(30)            # Retiro de $30. Saldo: $70
c.retirar(200)           # Saldo insuficiente (tiene $70)
print(c)                 # Cuenta 001: $70
print(c.saldo())         # 70
#CAMBIO
#Añade historial: una lista donde cada operación añade un string tipo '+100', '-30'. 
# Método ver_historial().
class CuentaBancaria:
    def __init__(self, numero):
        self.numero = numero
        self._saldo = 0
        self.historial = []

    def depositar(self, monto):
        if monto <= 0:
            print("Monto inválido")
            return

        self._saldo += monto
        self.historial.append(f"+{monto}")
        print(f"Depósito de ${monto}. Saldo: ${self._saldo}")

    def retirar(self, monto):
        if monto <= 0:
            print("Monto inválido")
            return

        if monto > self._saldo:
            print(f"Saldo insuficiente (tiene ${self._saldo})")
            return

        self._saldo -= monto
        self.historial.append(f"-{monto}")
        print(f"Retiro de ${monto}. Saldo: ${self._saldo}")

    def saldo(self):
        return self._saldo

    def ver_historial(self):
        return self.historial

    def __str__(self):
        return f"Cuenta {self.numero}: ${self._saldo}"


# --- Uso ---
c = CuentaBancaria("001")
c.depositar(100)
c.retirar(30)
c.retirar(200)

print(c)
print(c.saldo())
print(c.ver_historial())

#================================================
# 3) Clase Producto con nombre, precio y stock. Métodos: vender(cantidad) 
# (reduce stock si hay), reabastecer(cantidad), valor_inventario() (precio × stock).
#================================================
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if cantidad > self.stock:
            print(f"Sin stock suficiente ({self.stock} disponibles)"); return False
        self.stock -= cantidad
        print(f"Vendidas {cantidad} de {self.nombre}. Stock: {self.stock}")
        return True

    def reabastecer(self, cantidad):
        self.stock += cantidad
        print(f"Nuevo stock de {self.nombre}: {self.stock}")

    def valor_inventario(self):
        return self.precio * self.stock

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f} - stock: {self.stock}"

# --- Uso ---
leche = Producto("Leche", 1.20, 10)
pan = Producto("Pan", 0.50, 30)

print(leche)                     # Leche - $1.20 - stock: 10
leche.vender(3)                  # Vendidas 3
print(f"Valor: ${leche.valor_inventario():.2f}")  # Valor: $8.40
leche.vender(20)                 # Sin stock suficiente
leche.reabastecer(5)             # Nuevo stock: 12
#CAMBIO
#Amplíalo con un método de clase total_inventario(productos) que sume los valores de una lista de productos.
#================================================
# 3) Clase Producto con nombre, precio y stock.
#================================================
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if cantidad > self.stock:
            print(f"Sin stock suficiente ({self.stock} disponibles)")
            return False

        self.stock -= cantidad
        print(f"Vendidas {cantidad} de {self.nombre}. Stock: {self.stock}")
        return True

    def reabastecer(self, cantidad):
        self.stock += cantidad
        print(f"Nuevo stock de {self.nombre}: {self.stock}")

    def valor_inventario(self):
        return self.precio * self.stock

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f} - stock: {self.stock}"

    # CAMBIO: sumar el valor del inventario de varios productos
    @classmethod
    def total_inventario(cls, productos):
        total = 0
        for producto in productos:
            total += producto.valor_inventario()
        return total


# --- Uso ---
leche = Producto("Leche", 1.20, 10)
pan = Producto("Pan", 0.50, 30)

print(leche)
leche.vender(3)
print(f"Valor: ${leche.valor_inventario():.2f}")
leche.vender(20)
leche.reabastecer(5)

# Lista de productos y cálculo del total
productos = [leche, pan]
total = Producto.total_inventario(productos)

print(f"Valor total del inventario: ${total:.2f}")


#================================================
# ------------------------------------------------------TAREA-------------------------------------------
#================================================

#================================================
# 1) Clase Rectangulo con base y altura. Métodos area(), perimetro() y __str__.
#================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: base y altura del rectángulo (5 y 3 en este ejemplo)
# Proceso: multiplicar base por altura para el área y sumar las medidas
#          para calcular el perímetro
# Salida: mostrar el rectángulo, su área y su perímetro

#-------- 2. BOSQUEJO A MANO ------------
# base = 5, altura = 3
# área = 5 * 3 = 15
# perímetro = 2 * (5 + 3) = 16

#-------- 3. DESCUBRIR EL PATRÓN --------
# El área siempre se obtiene multiplicando base por altura.
# El perímetro suma los cuatro lados: dos bases y dos alturas.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

    def __str__(self):
        return f"Rectángulo {self.base}×{self.altura}, área={self.area()}, perímetro={self.perimetro()}"

r = Rectangulo(5, 3)
print(r)
print(r.area())

#-------- 5. PRUEBA DE ESCRITORIO -------
# Línea                 | base | altura | área | perímetro | Pantalla
# --------------------- | ---: | -----: | ---: | --------: | -----------------------------------------------
# Crear Rectangulo      |    5 |      3 |    — |         — | —
# area()                |    5 |      3 |   15 |         — | —
# perimetro()           |    5 |      3 |   15 |        16 | —
# print(r)              |    5 |      3 |   15 |        16 | Rectángulo 5×3, área=15, perímetro=16
# print(r.area())       |    5 |      3 |   15 |        16 | 15

#---------- EJERCICIO SIMILAR: CUADRADO ----------
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: medida de un lado del cuadrado (4 en este ejemplo)
# Proceso: multiplicar el lado por sí mismo para obtener el área;
#          multiplicarlo por 4 para obtener el perímetro
# Salida: mostrar las medidas calculadas

#-------- 2. BOSQUEJO A MANO ------------
# lado = 4
# área = 4 * 4 = 16
# perímetro = 4 * 4 = 16

#-------- 3. DESCUBRIR EL PATRÓN --------
# Como los cuatro lados del cuadrado son iguales, basta guardar una medida.
# Esa medida se usa en ambas fórmulas.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

    def perimetro(self):
        return 4 * self.lado

    def __str__(self):
        return f"Cuadrado de lado {self.lado}, área={self.area()}, perímetro={self.perimetro()}"

cuadrado = Cuadrado(4)
print(cuadrado)
print(f"Área del cuadrado: {cuadrado.area()}")

#-------- 5. PRUEBA DE ESCRITORIO -------
# Línea                   | lado | área | perímetro | Pantalla
# ----------------------- | ---: | ---: | --------: | ----------------------------------------------
# Crear Cuadrado          |    4 |    — |         — | —
# area()                  |    4 |   16 |         — | —
# perimetro()             |    4 |   16 |        16 | —
# print(cuadrado)         |    4 |   16 |        16 | Cuadrado de lado 4, área=16, perímetro=16
# print(cuadrado.area())  |    4 |   16 |        16 | Área del cuadrado: 16

#================================================
# 2) Clase con radio y métodos area() (π·r²) y circunferencia() (2·π·r). Usa math.pi.
#================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: radio del círculo (5 en este ejemplo)
# Proceso: calcular el área con π * radio² y la circunferencia con 2 * π * radio
# Salida: mostrar el área y la circunferencia con 2 decimales

#-------- 2. BOSQUEJO A MANO ------------
# radio = 5
# área = π * 5² = 25π ≈ 78.54
# circunferencia = 2 * π * 5 = 10π ≈ 31.42

#-------- 3. DESCUBRIR EL PATRÓN --------
# Las dos fórmulas usan el radio y el valor de π que proporciona math.pi.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def circunferencia(self):
        return 2 * math.pi * self.radio

    def __str__(self):
        return f"Círculo r={self.radio}, área={self.area():.2f}"

c = Circulo(5)
print(c)                         # Círculo r=5, área=78.54
print(f"Circunferencia: {c.circunferencia():.2f}")

#-------- 5. PRUEBA DE ESCRITORIO -------
# Línea                 | radio | cálculo                 | resultado | Pantalla
# --------------------- | ----: | ----------------------- | --------: | --------------------------------
# Crear Circulo         |     5 | —                       |         — | —
# area()                |     5 | math.pi * 5 ** 2        |     78.54 | —
# circunferencia()      |     5 | 2 * math.pi * 5         |     31.42 | —
# print(c)              |     5 | —                       |     78.54 | Círculo r=5, área=78.54
# print(circunferencia) |     5 | —                       |     31.42 | Circunferencia: 31.42

#---------- EJERCICIO SIMILAR: ESFERA ----------

#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: radio de una esfera (3 en este ejemplo)
# Proceso: calcular el área de la superficie y el volumen con fórmulas
#          que usan el radio y math.pi
# Salida: mostrar ambas medidas redondeadas a 2 decimales

#-------- 2. BOSQUEJO A MANO ------------
# radio = 3
# área = 4 * π * 3² = 36π ≈ 113.10
# volumen = (4 / 3) * π * 3³ = 36π ≈ 113.10

#-------- 3. DESCUBRIR EL PATRÓN --------
# Guardamos el radio una sola vez y lo usamos en dos métodos distintos:
# uno calcula la superficie y el otro calcula el espacio que ocupa la esfera.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
class Esfera:
    def __init__(self, radio):
        self.radio = radio

    def area_superficie(self):
        return 4 * math.pi * self.radio ** 2

    def volumen(self):
        return (4 / 3) * math.pi * self.radio ** 3

esfera = Esfera(3)
print(f"Área de la esfera: {esfera.area_superficie():.2f}")
print(f"Volumen de la esfera: {esfera.volumen():.2f}")

#-------- 5. PRUEBA DE ESCRITORIO -------
# Línea                    | radio | cálculo                  | resultado | Pantalla
# ------------------------ | ----: | ------------------------ | --------: | --------------------------------
# Crear Esfera             |     3 | —                        |         — | —
# area_superficie()        |     3 | 4 * math.pi * 3 ** 2     |    113.10 | —
# volumen()                |     3 | (4 / 3) * math.pi * 3**3 |    113.10 | —
# print(area_superficie)   |     3 | —                        |    113.10 | Área de la esfera: 113.10
# print(volumen)           |     3 | —                        |    113.10 | Volumen de la esfera: 113.10

#================================================
# 3) Clase Estudiante con nombre y una lista de notas. Métodos: agregar_nota(n), 
# promedio(), aprobado() (True si promedio ≥ 7).
#================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: nombre del estudiante y sus notas (8, 6 y 9 en este ejemplo)
# Proceso: guardar cada nota, sumar las notas y dividir para saber el promedio;
#          comprobar si el promedio es mayor o igual a 7
# Salida: mostrar el nombre, las notas, el promedio y si aprobó

#-------- 2. BOSQUEJO A MANO ------------
# notas = [8, 6, 9]
# suma = 8 + 6 + 9 = 23
# promedio = 23 / 3 ≈ 7.67
# ¿7.67 >= 7? Sí, está aprobado.

#-------- 3. DESCUBRIR EL PATRÓN --------
# Se agregan las notas a una lista. El promedio es la suma dividida
# para la cantidad de notas; aprobado() compara ese resultado con 7.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []          # lista vacía inicial

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def aprobado(self):
        return self.promedio() >= 7

    def __str__(self):
        return f"{self.nombre}: {self.notas} → prom={self.promedio():.2f}"

# --- Uso ---
ana = Estudiante("Ana")
for n in [8, 6, 9]:
    ana.agregar_nota(n)
print(ana)
print(f"Aprobado: {ana.aprobado()}")

#-------- 5. PRUEBA DE ESCRITORIO -------
# Línea                  | notas       | suma | promedio | ¿promedio >= 7? | Pantalla
# ---------------------- | ----------- | ---: | -------: | --------------- | --------------------------------
# Crear Estudiante       | []          |    — |        — | —               | —
# agregar_nota(8)        | [8]         |    8 |        — | —               | —
# agregar_nota(6)        | [8, 6]      |   14 |        — | —               | —
# agregar_nota(9)        | [8, 6, 9]   |   23 |        — | —               | —
# promedio()             | [8, 6, 9]   |   23 |     7.67 | —               | —
# aprobado()             | [8, 6, 9]   |   23 |     7.67 | True            | —
# print(ana)             | [8, 6, 9]   |   23 |     7.67 | True            | Ana: [8, 6, 9] → prom=7.67
# print(aprobado)        | [8, 6, 9]   |   23 |     7.67 | True            | Aprobado: True

#---------- EJERCICIO SIMILAR: JUGADOR ----------
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: nombre del jugador y los puntos obtenidos en varios partidos
#          (12, 8 y 10 en este ejemplo)
# Proceso: guardar los puntajes, calcular su promedio y comprobar si llega a 10
# Salida: mostrar los puntajes, el promedio y si alcanzó el objetivo

#-------- 2. BOSQUEJO A MANO ------------
# puntajes = [12, 8, 10]
# promedio = (12 + 8 + 10) / 3 = 10
# ¿10 >= 10? Sí, alcanzó el objetivo.

#-------- 3. DESCUBRIR EL PATRÓN --------
# Igual que una lista de notas, cada puntaje se agrega a una lista.
# Luego se divide la suma por la cantidad de partidos y se compara el promedio
# con el objetivo definido para este jugador.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntajes = []

    def agregar_puntaje(self, puntaje):
        self.puntajes.append(puntaje)

    def promedio(self):
        if not self.puntajes:
            return 0
        return sum(self.puntajes) / len(self.puntajes)

    def alcanzo_objetivo(self):
        return self.promedio() >= 10

    def __str__(self):
        return f"{self.nombre}: puntajes={self.puntajes}, promedio={self.promedio():.2f}"

jugador = Jugador("Luis")
for puntaje in [12, 8, 10]:
    jugador.agregar_puntaje(puntaje)
print(jugador)
print(f"Alcanzó el objetivo: {jugador.alcanzo_objetivo()}")

#-------- 5. PRUEBA DE ESCRITORIO -------
# Línea                      | puntajes       | suma | promedio | ¿llegó a 10? | Pantalla
# -------------------------- | -------------- | ---: | -------: | ------------ | ----------------------------------------
# Crear Jugador              | []             |    — |        — | —            | —
# agregar_puntaje(12)        | [12]           |   12 |        — | —            | —
# agregar_puntaje(8)         | [12, 8]        |   20 |        — | —            | —
# agregar_puntaje(10)        | [12, 8, 10]    |   30 |        — | —            | —
# promedio()                 | [12, 8, 10]    |   30 |    10.00 | —            | —
# alcanzo_objetivo()         | [12, 8, 10]    |   30 |    10.00 | True         | —
# print(jugador)             | [12, 8, 10]    |   30 |    10.00 | True         | Luis: puntajes=[12, 8, 10], promedio=10.00
# print(alcanzo_objetivo)    | [12, 8, 10]    |   30 |    10.00 | True         | Alcanzó el objetivo: True


#================================================
# 4) Clase Vehiculo con marca, modelo y km recorridos (inicialmente 0). 
# Método recorrer(km) que suma al odómetro. Método necesita_mantenimiento() que retorna True cada 10 000 km.
#================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: marca y modelo; distancia recorrida (15 000 km en este ejemplo)
# Proceso: sumar la distancia al odómetro y comparar los kilómetros desde
#          el último mantenimiento con 10 000
# Salida: mostrar los kilómetros y si necesita mantenimiento

#-------- 2. BOSQUEJO A MANO ------------
# El vehículo comienza con 0 km y 0 km desde el último mantenimiento.
# Después de recorrer 15 000 km: 15 000 - 0 = 15 000 km.
# Como 15 000 >= 10 000, necesita mantenimiento.
# Después del mantenimiento: 15 000 - 15 000 = 0 km; ya no lo necesita.

#-------- 3. DESCUBRIR EL PATRÓN --------
# recorrer() aumenta el odómetro. El mantenimiento guarda el kilometraje
# actual como referencia para contar de nuevo desde cero.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.km = 0
        self._ultimo_mantenimiento = 0

    def recorrer(self, distancia):
        self.km += distancia

    def necesita_mantenimiento(self):
        return (self.km - self._ultimo_mantenimiento) >= 10000

    def hacer_mantenimiento(self):
        self._ultimo_mantenimiento = self.km
        print(f"Mantenimiento hecho a los {self.km} km")

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.km} km"

auto = Vehiculo("Toyota", "Corolla")
auto.recorrer(15000)
print(auto)                                       # Toyota Corolla - 15000 km
print(f"Necesita mantenimiento: {auto.necesita_mantenimiento()}")
auto.hacer_mantenimiento()                        # se resetea el contador
print(f"Necesita mantenimiento: {auto.necesita_mantenimiento()}")

#-------- 5. PRUEBA DE ESCRITORIO -------
# Línea                  | km actual | último mantenimiento | diferencia | ¿necesita? | Pantalla
# ---------------------- | --------: | -------------------: | ----------: | ---------- | -----------------------------------
# Crear Vehiculo         |         0 |                    0 |           0 | No         | —
# recorrer(15000)        |     15000 |                    0 |       15000 | Sí         | —
# print(auto)            |     15000 |                    0 |       15000 | Sí         | Toyota Corolla - 15000 km
# necesita_mantenimiento |     15000 |                    0 |       15000 | Sí         | Necesita mantenimiento: True
# hacer_mantenimiento()  |     15000 |                15000 |           0 | No         | Mantenimiento hecho a los 15000 km
# necesita_mantenimiento |     15000 |                15000 |           0 | No         | Necesita mantenimiento: False

#---------- EJERCICIO SIMILAR: MAQUINA ----------
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: nombre de la máquina y horas de trabajo (620 horas en este ejemplo)
# Proceso: acumular las horas y verificar si han pasado 500 horas desde
#          el último servicio
# Salida: indicar si la máquina necesita servicio y actualizar la referencia
#         cuando se le da mantenimiento

#-------- 2. BOSQUEJO A MANO ------------
# La máquina comienza con 0 horas y 0 horas desde el último servicio.
# Después de trabajar 620 horas: 620 - 0 = 620 horas.
# Como 620 >= 500, necesita servicio.
# Después del servicio: 620 - 620 = 0 horas; ya no lo necesita.

#-------- 3. DESCUBRIR EL PATRÓN --------
# La máquina acumula horas de uso, igual que un vehículo acumula kilómetros.
# Al realizar el servicio guardamos el total actual para empezar un nuevo conteo.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
class Maquina:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horas = 0
        self._horas_ultimo_servicio = 0

    def trabajar(self, horas):
        self.horas += horas

    def necesita_servicio(self):
        return (self.horas - self._horas_ultimo_servicio) >= 500

    def hacer_servicio(self):
        self._horas_ultimo_servicio = self.horas
        print(f"Servicio realizado a las {self.horas} horas")

    def __str__(self):
        return f"{self.nombre} - {self.horas} horas de uso"

maquina = Maquina("Excavadora")
maquina.trabajar(620)
print(maquina)
print(f"Necesita servicio: {maquina.necesita_servicio()}")
maquina.hacer_servicio()
print(f"Necesita servicio: {maquina.necesita_servicio()}")

#-------- 5. PRUEBA DE ESCRITORIO -------
# Línea                    | horas actuales | horas del último servicio | diferencia | ¿necesita? | Pantalla
# ------------------------ | -------------: | ------------------------: | ---------: | ---------- | ------------------------------------
# Crear Maquina            |              0 |                         0 |          0 | No         | —
# trabajar(620)            |            620 |                         0 |        620 | Sí         | —
# print(maquina)           |            620 |                         0 |        620 | Sí         | Excavadora - 620 horas de uso
# necesita_servicio()      |            620 |                         0 |        620 | Sí         | Necesita servicio: True
# hacer_servicio()         |            620 |                       620 |          0 | No         | Servicio realizado a las 620 horas
# necesita_servicio()      |            620 |                       620 |          0 | No         | Necesita servicio: False