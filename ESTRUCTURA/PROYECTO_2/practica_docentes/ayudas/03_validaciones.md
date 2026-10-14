# 3. Validaciones

Validar significa comprobar entradas antes de cambiar un objeto o persistirlo. Los ejemplos usan las reglas de emails, campos obligatorios, IDs y relaciones que aparecen en ventas/académico cuando corresponde. Rangos de salario, teléfono solo numérico, fechas ISO y unicidad de ciertas parejas son **supuestos didácticos de cada ejemplo**, no requisitos atribuidos al docente.

## Obligatorios y campos permitidos

```python
for campo in ("nombre", "apellido", "email"):
    if str(datos.get(campo, "")).strip() == "":
        return f"{campo} es obligatorio"
desconocidos = set(datos) - permitidos
if desconocidos:
    return False, f"Campos no válidos: {sorted(desconocidos)}"
```

Al crear se requieren todos los campos necesarios. Al actualizar solo se revisan los enviados, pero un campo enviado no puede quedar vacío si es obligatorio. `get()` ofrece valor por defecto para un campo opcional; los conjuntos detectan campos ajenos.

## Convertir y limitar números

```python
try:
    monto = float(datos["sueldo_base"])
except (TypeError, ValueError):
    return "El sueldo debe ser numérico"
if not math.isfinite(monto) or not 0 <= monto <= LIMITE:
    return "Monto fuera de rango"
```

La entrada de consola es texto. `try/except` maneja texto no convertible. `isfinite` rechaza `NaN` e infinito, que no cumplen comparaciones ordinarias de límites.

## Unicidad y excluir el registro actual

```python
emails_usados = set()
for persona in self.lista:
    if persona.id != id_actual:
        emails_usados.add(persona.email.lower())
if email.lower() in emails_usados:
    return "Email repetido"
```

En creación `id_actual` es `None`, así se consideran todos. Al actualizar se excluye el propio registro para que conservar su valor no se detecte como duplicado. Una duplicidad compuesta se comprueba con todos sus campos:

```python
for nomina in self.lista:
    if nomina.id != id_actual and nomina.empleado_id == empleado_id and nomina.periodo == periodo:
        return "Ya existe nómina en ese periodo"
```

## Relaciones y orden seguro

```python
if self.empleados.obtener(empleado_id) is None:
    return "No existe el empleado"
```

Se consulta el controlador recibido; un ID desconocido no debe guardarse como relación válida. En actualización primero se combinan valores enviados con los actuales para revisar el resultado final. Solo después se aplican cambios y se intenta guardar. En fallos, se restaura la memoria. Ejemplos de nómina y hospital bloquean eliminar padres con hijos para no dejar referencias huérfanas.
