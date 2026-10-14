# Ejemplo independiente de empleados

Abra una terminal en esta carpeta y ejecute `python main.py`. El JSON persistente está en `data/empleados.json`; `GestorJSON` crea el directorio si hace falta.

Orden de estudio: `models.py`, `shared/json_manager.py`, `views.py` y `main.py`. `Empleado(Persona)` hereda ID, nombre, apellido y email; `super()` inicializa los campos comunes. `a_diccionario()` extiende el diccionario de Persona y `etiqueta()` personaliza el texto usado por el `__str__()` heredado. `desde_diccionario()` se hereda de `ModeloBase`; las claves del JSON coinciden con los parámetros del constructor.

`EmpleadoController` hereda directamente de `CrudBase` e implementa `leer`, `obtener`, `buscar`, `siguiente`, `crear`, `actualizar` y `eliminar`. Los métodos `guardar` y `validar` son auxiliares. Las pantallas de `main.py` piden valores, forman `datos`/`cambios` y muestran la tupla `(exito, mensaje)` que devuelven las operaciones de escritura.

Para probar con otro JSON, cree `EmpleadoController(archivo=ruta_temporal)`. Al incorporar empleados a ventas o al sistema académico, importe y reutilice el `ModeloBase`, `Persona`, `CrudBase`, gestor y utilidades existentes del proyecto destino; añada la clase concreta, su controlador, menú y archivo propio sin duplicar las bases.
