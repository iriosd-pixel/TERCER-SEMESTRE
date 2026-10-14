# Proyecto didáctico de nómina

Desde esta carpeta ejecute `python main.py`. Cada CRUD almacena sus datos en su propio JSON dentro de `data/`; los archivos se crean cuando se realiza el primer guardado.

Orden sugerido: `models.py` (base, Persona, Empleado y sus diccionarios), `shared/json_manager.py`, `views.py` (CRUD y validaciones) y `main.py` (menús). Los empleados tienen `departamento_id`; Nómina recibe el controlador de empleados para verificar cada vínculo. Los departamentos se protegen de eliminación mientras tengan empleados, y los empleados mientras tengan nóminas. Primero elimine las nóminas y reasigne o elimine los empleados para retirar un departamento.

El neto didáctico es sueldo base + bonificación - descuento. Todos los importes son finitos, entre 0 y 1 000 000 000 y el neto no puede ser negativo. Se supone un periodo como texto no vacío; se impide más de un registro por pareja empleado/periodo. No se modelan impuestos ni legislación laboral. Actualizar admite solo campos enviados y valida el resultado combinado; el ID y relaciones no se pueden borrar en cascada. Si falla el guardado se restaura la lista o el objeto en memoria.

Para pruebas aisladas, cree los controladores con rutas temporales distintas y arranque cada proceso con el directorio del ejemplo en `PYTHONPATH`/directorio actual; el JSON de datos real no hace falta modificarlo.
