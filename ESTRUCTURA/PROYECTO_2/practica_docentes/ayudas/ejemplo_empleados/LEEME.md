# Ejemplo independiente de empleados

Ejecute `python main.py` desde esta carpeta. Los datos persisten en `data/empleados.json`, creado al guardar el primer registro. Para probar sin tocar datos del ejercicio, instancie `EmpleadoController(archivo=ruta_temporal)`.

`Empleado(Persona)` hereda `id`, nombre, apellido y email. Su constructor envía a `super()` los cuatro datos de Persona y guarda `cargo`; `a_diccionario()` extiende el diccionario padre. La clase base convierte el JSON al modelo con `desde_diccionario()`: las claves `nombre`, `apellido`, `email` y `cargo` deben coincidir con los parámetros del constructor.

`views.py` hereda `CrudBase`, implementa sus siete operaciones y devuelve `(exito, mensaje)` para cambios. Al añadir empleados a ventas o al sistema académico se reutilizan sus `ModeloBase`, `Persona`, `CrudBase`, gestor y utilidades; se agrega el modelo/controlador y menú propios, se instancia desde `main.py` y se configura el archivo de datos. Se importan esas bases del proyecto y no se copian.
