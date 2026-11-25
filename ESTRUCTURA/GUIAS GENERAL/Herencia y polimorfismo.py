#=======================================================================
# EJEMPLOS DE EXPLICACIÓN DE LA GUÍA
# Cada ejemplo se puede ejecutar llamando a su función.
#=======================================================================
# Ejemplo de explicación 1
def ejemplo_explicacion_1():
    class Persona:
        def __init__(self, nombre, cedula):
            self.nombre = nombre
            self.cedula = cedula

        def presentarse(self):
            print(f"Soy {self.nombre}, cédula {self.cedula}")

        def __str__(self):
            return f"{self.nombre} ({self.cedula})"


    class Pasajero(Persona):                    # HEREDA de Persona
        def __init__(self, nombre, cedula, codigo_reserva):
            super().__init__(nombre, cedula)    # llama al __init__ del padre
            self.codigo_reserva = codigo_reserva
            self.millas = 0

        def sumar_millas(self, m):
            self.millas += m

        # Sobrescribimos __str__ (polimorfismo)
        def __str__(self):
            return f"Pasajero {self.nombre} [reserva: {self.codigo_reserva}]"


    class Empleado(Persona):                    # HEREDA de Persona
        def __init__(self, nombre, cedula, codigo_emp, salario):
            super().__init__(nombre, cedula)
            self.codigo_emp = codigo_emp
            self.salario = salario

        def aumentar_salario(self, porcentaje):
            self.salario *= (1 + porcentaje/100)


    # --- Uso ---
    p = Pasajero("Ana", "0912...", "AB-1234")
    e = Empleado("Luis", "0987...", "EMP-01", 1200)

    p.presentarse()                             # HEREDADO del padre
    e.presentarse()                             # HEREDADO del padre

    p.sumar_millas(500)                         # propio de Pasajero
    e.aumentar_salario(10)                      # propio de Empleado

    print(p)                                    # __str__ sobrescrito de Pasajero
    print(e)                                    # __str__ heredado (Luis (0987...))

# Ejemplo de explicación 2
def ejemplo_explicacion_2():
    class Animal:
        def hablar(self):
            print("(algún sonido)")

    class Perro(Animal):
        def hablar(self):                       # sobrescribe
            print("¡Guau!")

    class Gato(Animal):
        def hablar(self):                       # sobrescribe
            print("Miau")

    class Vaca(Animal):
        def hablar(self):
            print("Muuu")

    # El "misterio" del polimorfismo:
    animales = [Perro(), Gato(), Vaca()]
    for a in animales:
        a.hablar()                              # cada uno responde distinto
    # ¡Guau! / Miau / Muuu

#=======================================================================
#EJEMPLOS PUESTOS POR LA IA MAS CAMBIOS
#=======================================================================
#=======================================================================
# TALLER — 2 ejercicios paso a paso
# 1) Modela una empresa aérea con Persona como clase base
# y Pasajero y Empleado como hijas. Cada hija añade 
# su propio atributo y método.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: los datos de una persona más los específicos
# Proceso: clase base con lo común, hijas con lo específico
# Salida: presentación adaptada a cada tipo
# Ejemplo de entrada (guía): Pasajero Ana con reserva AB1
# Salida esperada (guía): Pasajero Ana [reserva: AB1] · 500 millas

#-------- 2. BOSQUEJO A MANO ------------
# Persona(nombre, cedula)
#    ├── Pasajero(nombre, cedula, codigo_reserva)
#    │    métodos: sumar_millas()
#    │
#    └── Empleado(nombre, cedula, codigo_emp, salario)
#         métodos: aumentar_salario()

#-------- 3. DESCUBRIR EL PATRÓN --------
# Las clases hijas reutilizan los datos de su clase padre con super().
# Después, cada hija guarda sus propios datos y puede tener sus propios métodos.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
class Persona:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def presentarse(self):
        print(f"Soy {self.nombre}, cédula {self.cedula}")

    def __str__(self):
        return f"{self.nombre} ({self.cedula})"


class Pasajero(Persona):
    def __init__(self, nombre, cedula, codigo_reserva):
        super().__init__(nombre, cedula)         # inicializa lo del padre
        self.codigo_reserva = codigo_reserva
        self.millas = 0

    def sumar_millas(self, m):
        self.millas += m

    def __str__(self):
        return f"Pasajero {self.nombre} [reserva: {self.codigo_reserva}] · {self.millas} millas"


class Empleado(Persona):
    def __init__(self, nombre, cedula, codigo_emp, salario):
        super().__init__(nombre, cedula)
        self.codigo_emp = codigo_emp
        self.salario = salario

    def aumentar_salario(self, porcentaje):
        self.salario *= (1 + porcentaje / 100)

    def __str__(self):
        return f"Empleado {self.nombre} [{self.codigo_emp}] · ${self.salario:.2f}"


# --- Uso ---
p = Pasajero("Ana", "0912345678", "AB-1234")
e = Empleado("Luis", "0987654321", "EMP-01", 1200)

p.sumar_millas(500)
e.aumentar_salario(10)

# Ambos heredan presentarse():
p.presentarse()                                   # Soy Ana, cédula 0912345678
e.presentarse()                                   # Soy Luis, cédula 0987...

# Pero __str__ es distinto en cada uno:
print(p)                                          # Pasajero Ana [reserva: AB-1234] · 500 millas
print(e)                                          # Empleado Luis [EMP-01] · $1320.00

#-------- 5. PRUEBA DE ESCRITORIO -------
# Acción                 | Datos                         | Resultado
# ---------------------- | ----------------------------- | -------------------------------
# sumar_millas(500)      | Pasajero Ana                  | 500 millas
# aumentar_salario(10)   | Empleado Luis, salario $1200  | salario $1320

#CAMBIO

# Añade una clase Tripulante(Empleado) con rol (piloto, copiloto, azafata)
# y un método que muestre sus horas de vuelo.
class Tripulante(Empleado):
    def __init__(self, nombre, cedula, codigo_emp, salario, rol, horas):
        super().__init__(nombre, cedula, codigo_emp, salario)
        self.rol = rol
        self.horas = horas

    def horas_vuelo(self):
        return self.horas

# --- Uso ---
tripulante = Tripulante("Marta", "0911122233", "EMP-02", 1800, "piloto", 120)
print(f"{tripulante.nombre} es {tripulante.rol}")
print(f"Horas de vuelo: {tripulante.horas_vuelo()}")
# Prueba del cambio: horas_vuelo() de Marta → 120.

#=======================================================================
# 2) Clase base Figura con método area(). 
# Clases hijas Rectangulo, Circulo, Triangulo que 
# la implementan.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: figuras de distinta forma
# Proceso: una lista mixta de figuras
# Salida: las áreas de todas, con un mismo bucle
# Ejemplo de entrada (guía): 3 figuras distintas
# Salida esperada (guía): Áreas: 15, 78.54, 6

#-------- 2. BOSQUEJO A MANO ------------
# figuras = [Rectangulo(5,3), Circulo(5), Triangulo(4,3)]
#
# for f in figuras:
#    print(f.area())
#
#   → 15, 78.54, 6   (cada una calcula distinto)

#-------- 3. DESCUBRIR EL PATRÓN --------
# Cada figura implementa area() con sus propias medidas.
# El mismo bucle puede llamar area() sin preguntar qué clase recibió.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
import math

class Figura:
    def area(self):
        raise NotImplementedError("Cada figura debe implementar area()")

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return math.pi * self.radio ** 2

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return (self.base * self.altura) / 2

# --- Uso polimórfico ---
figuras = [
    Rectangulo(5, 3),
    Circulo(5),
    Triangulo(4, 3)
]

for f in figuras:
    print(f"{type(f).__name__}: {f.area():.2f}")

# Rectangulo: 15.00
# Circulo: 78.54
# Triangulo: 6.00

# Y podemos sumar todas
total = sum(f.area() for f in figuras)
print(f"Área total: {total:.2f}")

#-------- 5. PRUEBA DE ESCRITORIO -------
# Figura      | Entrada | Área
# Rectangulo  | 5 y 3   | 15
# Circulo     | radio 5 | 78.54
# Triangulo   | 4 y 3   | 6
# Suma de áreas de las tres figuras: 99.54

#CAMBIO
#Añade el método perimetro() a las tres. Añade una nueva figura: Cuadrado (que hereda de Rectángulo).

class RectanguloConPerimetro(Rectangulo):
    def perimetro(self):
        return 2 * (self.base + self.altura)


class CirculoConPerimetro(Circulo):
    def perimetro(self):
        return 2 * math.pi * self.radio


class TrianguloConPerimetro(Triangulo):
    def perimetro(self):
        # En este ejemplo, base y altura son los catetos.
        hipotenusa = (self.base ** 2 + self.altura ** 2) ** 0.5
        return self.base + self.altura + hipotenusa


class Cuadrado(RectanguloConPerimetro):
    def __init__(self, lado):
        # En un cuadrado, la base y la altura son iguales.
        super().__init__(lado, lado)

    def perimetro(self):
        # Paso 1: sumar los cuatro lados iguales.
        return 4 * self.base

# --- Uso del cambio ---
for figura in [RectanguloConPerimetro(5, 3),
               CirculoConPerimetro(5), TrianguloConPerimetro(4, 3)]:
    print(f"{type(figura).__name__}: perímetro {figura.perimetro():.2f}")
cuadrado = Cuadrado(4)
print(f"Cuadrado: área {cuadrado.area()}, perímetro {cuadrado.perimetro()}")

# Prueba del cambio: perímetros 16, 31.42, 12 y 16.


#=======================================================================
# EJERCICIOS PROPUESTOS
#=======================================================================
#=======================================================================
# 1) Base Vehiculo(marca, modelo). Hija Auto con puertas. Hija Moto con cilindraje. Ambas tienen __str__ propio.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: marca y modelo del vehículo.
#          Auto también recibe la cantidad de puertas.
#          Moto también recibe el cilindraje.
# Proceso: guardar los datos comunes en Vehiculo y los propios en cada hija.
# Salida: mostrar una descripción distinta para el auto y la moto.

# Ejemplo de entrada (guía): auto = Auto('Toyota', 'Corolla', 4)
# Salida esperada (guía): Toyota Corolla — 4 puertas

#-------- 2. BOSQUEJO A MANO ------------
# Auto: Toyota, Corolla, 4 puertas -> Toyota Corolla — 4 puertas.
# Moto: Honda, CBR, 600 cc -> Honda CBR — 600cc.

#-------- 3. DESCUBRIR EL PATRÓN --------
# Marca y modelo son datos comunes, por eso van en la clase Vehiculo.
# Auto y Moto heredan esos datos y cada una personaliza cómo se muestra.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"{self.marca} {self.modelo}"

class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def __str__(self):
        return f"{self.marca} {self.modelo} — {self.puertas} puertas"

class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindraje):
        super().__init__(marca, modelo)
        self.cilindraje = cilindraje

    def __str__(self):
        return f"{self.marca} {self.modelo} — {self.cilindraje}cc"

# --- Uso ---
auto = Auto("Toyota", "Corolla", 4)
moto = Moto("Honda", "CBR", 600)
for v in [auto, moto]:
    print(v)

#-------- 5. PRUEBA DE ESCRITORIO -------
# Objeto | Datos                         | Pantalla
# ------ | ----------------------------- | -------------------------------
# auto   | Toyota, Corolla, 4 puertas    | Toyota Corolla — 4 puertas
# moto   | Honda, CBR, 600 cc            | Honda CBR — 600cc
    
#=======================================================================
# 2) Base Animal(nombre) con método hablar() que dice «(sonido)». Cada hija sobrescribe con su propio sonido.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: el nombre de cada animal.
# Proceso: cada tipo de animal usa su propio sonido.
# Salida: mostrar el nombre y el sonido correspondiente.

# Ejemplo de entrada (guía): para 3 animales
# Salida esperada (guía): Rex: Guau, Felix: Miau, Piolín: Pío

#-------- 2. BOSQUEJO A MANO ------------
# Perro Rex -> Rex: ¡Guau!
# Gato Felix -> Felix: Miau
# Ave Piolín -> Piolín: Pío pío

#-------- 3. DESCUBRIR EL PATRÓN --------
# Animal tiene un método hablar() general.
# Perro, Gato y Ave reemplazan ese método con su sonido.
# Así, el mismo llamado hablar() produce resultados distintos.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre}: (sonido)")

class Perro(Animal):
    def hablar(self):
        print(f"{self.nombre}: ¡Guau!")

class Gato(Animal):
    def hablar(self):
        print(f"{self.nombre}: Miau")

class Ave(Animal):
    def hablar(self):
        print(f"{self.nombre}: Pío pío")

# Uso polimórfico
animales = [Perro("Rex"), Gato("Felix"), Ave("Piolín")]
for a in animales:
    a.hablar()

#-------- 5. PRUEBA DE ESCRITORIO -------
# Objeto       | Método llamado | Pantalla
# ------------ | -------------- | ----------------
# Perro("Rex") | hablar()       | Rex: ¡Guau!
# Gato("Felix")| hablar()       | Felix: Miau
# Ave("Piolín")| hablar()       | Piolín: Pío pío

#=======================================================================
# 3) Base Empleado(nombre) con método abstracto sueldo_mensual(). EmpleadoPorHoras calcula sueldo por horas trabajadas × tarifa. EmpleadoFijo tiene sueldo fijo.
#=======================================================================
#-------- 1. ENTENDER EL PROBLEMA --------
# Entrada: nombre y datos para calcular el sueldo.
# Proceso: el empleado por horas multiplica horas por tarifa.
#          el empleado fijo usa el sueldo indicado.
# Salida: mostrar el sueldo de cada empleado y el total de la nómina.

# Ejemplo de entrada (guía): por_horas: 160h × 8, fijo: 1500
# Salida esperada (guía): 1280.00, 1500.00

#-------- 2. BOSQUEJO A MANO ------------
# Ana: 160 horas × $8 = $1280.
# Luis: sueldo fijo de $1500.
# Total de la nómina: $1280 + $1500 = $2780.

#-------- 3. DESCUBRIR EL PATRÓN --------
# La clase Empleado define que cada tipo debe calcular sueldo_mensual().
# Cada clase hija aplica su propia forma de calcularlo.
# El programa puede sumar los sueldos sin preguntar qué tipo de empleado es.

#-------- 4. ESCRIBIR EL CÓDIGO ---------
class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def sueldo_mensual(self):
        raise NotImplementedError

    def __str__(self):
        return f"{self.nombre}: ${self.sueldo_mensual():.2f}"


class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, horas, tarifa):
        super().__init__(nombre)
        self.horas = horas
        self.tarifa = tarifa

    def sueldo_mensual(self):
        return self.horas * self.tarifa


class EmpleadoFijo(Empleado):
    def __init__(self, nombre, sueldo):
        super().__init__(nombre)
        self.sueldo = sueldo

    def sueldo_mensual(self):
        return self.sueldo


# Nómina polimórfica
empleados = [
    EmpleadoPorHoras("Ana", 160, 8),
    EmpleadoFijo("Luis", 1500)
]

nomina = 0
for e in empleados:
    print(e)
    nomina += e.sueldo_mensual()

print(f"Total nómina: ${nomina:.2f}")

#-------- 5. PRUEBA DE ESCRITORIO -------
# Empleado          | Cálculo          | Sueldo
# ----------------- | ---------------- | --------
# Ana por horas     | 160 × $8         | $1280
# Luis fijo         | sueldo indicado  | $1500
# Total de nómina   | $1280 + $1500    | $2780
