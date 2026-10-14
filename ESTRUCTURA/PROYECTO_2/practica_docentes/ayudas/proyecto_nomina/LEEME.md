# Proyecto didáctico de nómina

Desde esta carpeta, ejecute `python main.py`. Los JSON se guardan en `data/` junto al código. El cálculo es didáctico: sueldo base + bonificación - descuento; no incluye impuestos ni legislación laboral. Los importes deben ser finitos, estar entre 0 y 1 000 000 000 y producir un neto no negativo. El periodo es texto no vacío y solo se permite una nómina por empleado y periodo.

Lea `models.py`, después `shared/json_manager.py`, `views.py` y `main.py`. Cada clase concreta (`DepartamentoController`, `EmpleadoController`, `NominaController`) hereda **directamente** de `CrudBase` e implementa los siete métodos CRUD. No hay clase intermedia ni fábrica genérica de modelos. Los modelos heredan `desde_diccionario()` y agregan campos a `a_diccionario()` mediante `super()`.

## Conectar los controladores

`EmpleadoController` requiere el controlador de departamentos; `NominaController` requiere el de empleados. Para proteger las relaciones al borrar, conecte también las referencias inversas antes de utilizar el menú:

```python
departamentos = DepartamentoController()
empleados = EmpleadoController(departamentos)
nominas = NominaController(empleados)
departamentos.conectar_empleados(empleados)
empleados.conectar_nominas(nominas)
```

Si falta la referencia inversa, eliminar departamento o empleado devuelve un mensaje que exige conectar el controlador; no omite la validación ni lanza `AttributeError`. Un departamento asignado a empleados no se elimina, y un empleado con nóminas tampoco. Elimine primero las nóminas y luego los empleados para poder retirar el departamento. Las actualizaciones validan el resultado completo y restauran valores anteriores si falla el guardado.

Los nombres de departamento se normalizan al crear y actualizar, se colapsan espacios y se comparan sin distinguir mayúsculas. Para probar sin modificar JSON del ejemplo, pase rutas temporales a los constructores de los tres controladores.
