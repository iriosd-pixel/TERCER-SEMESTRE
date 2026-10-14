# 1. Agregar una entidad

## Modelo: elegir padre y construir atributos

```python
class Empleado(Persona):
    def __init__(self, id_registro, nombre, apellido, email, cargo):
        super().__init__(id_registro, nombre, apellido, email)
        self.cargo = cargo
```

`Empleado` hereda de `Persona` si **es una persona** y comparte nombre, apellido y email. El ID se guarda en `ModeloBase`, padre indirecto de Persona. Una entidad que no sea persona (producto, departamento, cita) hereda directamente de `ModeloBase`. `self` es el objeto actual; por eso `self.cargo` pertenece a cada instancia. El orden y nombres de parámetros expresan los datos requeridos al construirla. `super().__init__(...)` ejecuta el inicializador de Persona: este a su vez envía `id_registro` a ModeloBase y guarda `nombre`, `apellido`, `email`.

```python
def a_diccionario(self):
    datos = super().a_diccionario()
    datos["cargo"] = self.cargo
    return datos

def etiqueta(self):
    return f"{super().etiqueta()} · {self.cargo}"
```

El padre prepara los campos comunes y el hijo añade el suyo. `etiqueta()` también extiende la etiqueta de Persona. El `__str__()` heredado de ModeloBase llama a `self.etiqueta()`; Python elige la versión de Empleado en tiempo de ejecución: eso es polimorfismo. `desde_diccionario()` está heredado como método de clase: usa `cls` para construir la clase concreta. Copiar y quitar `id` del diccionario permite llamar `cls(id_registro, **datos)`. Por eso cada clave restante debe coincidir con el nombre de un parámetro del constructor.

## Controlador y persistencia

```python
from models import Empleado
from shared.json_manager import GestorJSON

class EmpleadoController(CrudBase):
    def __init__(self, archivo):
        self.gestor = GestorJSON(archivo)
        self.lista = []
        for datos in self.gestor.leer():
            self.lista.append(Empleado.desde_diccionario(datos))
```

`views.py` importa el modelo. El parámetro `archivo` permite elegir el JSON. Cada diccionario leído se reconstruye como objeto. El controlador hereda de `CrudBase` para **cumplir** su interfaz; no recibe otro controlador por esa razón. Implementa `leer`, `obtener`, `buscar`, `siguiente`, `crear`, `actualizar`, `eliminar`. `guardar()` serializa todos los objetos usando `a_diccionario()` y delega la escritura a GestorJSON. `validar(datos, id_actual=None)` revisa reglas antes de tocar la lista.

```python
def siguiente(self):
    mayor = 0
    for empleado in self.lista:
        if empleado.id > mayor:
            mayor = empleado.id
    return mayor + 1
```

`self.lista` viene del JSON al iniciar y contiene los objetos actuales. El bucle encuentra el mayor ID; devuelve el siguiente entero.

Las siete operaciones de `CrudBase` tienen estos contratos sencillos:

- `leer()` devuelve `self.lista` (lista de objetos).
- `obtener(id_registro)` recorre con `for`, devuelve el objeto coincidente o `None`.
- `buscar(texto)` normaliza texto, recorre campos y devuelve una lista de coincidencias.
- `siguiente()` devuelve mayor ID + 1.
- `crear(datos)` valida, construye el modelo con `siguiente()`, agrega y guarda; devuelve `(exito, mensaje)`.
- `actualizar(id_registro, datos)` busca, rechaza campos desconocidos, valida antes de usar `setattr`, guarda y devuelve `(exito, mensaje)`.
- `eliminar(id_registro)` busca, quita, guarda y revierte la lista si falla; devuelve `(exito, mensaje)`.

Además de esos métodos, cada controlador normalmente tiene `guardar()` y `validar()`. La validación devuelve un mensaje de error o `None`; `guardar()` debe devolver el booleano de GestorJSON para que el controlador sepa si confirma o revierte la operación.

## Conectar pantalla y menú

```python
from views import EmpleadoController
empleados = EmpleadoController("data/empleados.json")

def crear_empleado():
    datos = {"nombre": input("Nombre: "), "apellido": input("Apellido: "),
             "email": input("Email: "), "cargo": input("Cargo: ")}
    exito, mensaje = empleados.crear(datos)
    print(mensaje)

MENU = {"1": ("Crear empleado", crear_empleado), "0": ("Volver", None)}
```

`main.py` importa e instancia una sola vez el controlador. La pantalla obtiene texto del usuario, forma un diccionario y muestra la tupla `(exito, mensaje)`. Añada funciones de listar, buscar, ver, actualizar y eliminar y conéctelas a las opciones del menú, como los menús de ventas.

El JSON vive bajo `data` del ejemplo y cada registro almacena `id`, `nombre`, `apellido`, `email`, `cargo`. El archivo puede comenzar como lista vacía. Para una entidad relacionada, por ejemplo `VentaController(clientes, productos)`, se reciben las instancias que ya creó main y se consultan con `clientes.obtener(id)`; no se crea otra lista desconectada.

Configurar JSON consiste en escoger una ruta anclada al ejemplo, por ejemplo `os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "empleados.json")`, crear `GestorJSON(ruta)` y llamar `leer()`/`guardar()`. Así ejecutar desde otra carpeta no redirige accidentalmente el archivo de datos.

## Herencia frente a recibir un controlador

`Empleado(Persona)` expresa que empleado **es una** persona y reutiliza atributos/comportamiento del padre. `VentaController(clientes, productos)` expresa que el controlador **usa** otros controladores para validar IDs o consultar datos. Esa relación es composición/colaboración: no convierte una venta en cliente ni en producto.
