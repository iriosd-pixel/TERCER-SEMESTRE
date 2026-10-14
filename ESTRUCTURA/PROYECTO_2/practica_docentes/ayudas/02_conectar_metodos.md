# 2. Cómo se conectan los métodos

```text
main.py ──datos/llamadas──> views.py ──objetos──> models.py
                               │                    │
                               └── filas JSON ──> GestorJSON
```

`main.py` pide datos y presenta resultados. `views.py` valida, coordina listas/relaciones y pide persistencia. `models.py` representa objetos y comportamientos. `GestorJSON` solo convierte JSON a listas de diccionarios y viceversa.

## Crear

```python
datos = {"nombre": "Ana", "apellido": "Paz", "email": "ana@ejemplo.com", "cargo": "Analista"}
exito, mensaje = empleados.crear(datos)
```

`datos` es el argumento enviado al parámetro `datos` de `crear`. El controlador valida; si no hay error construye `Empleado(self.siguiente(), ...)`, agrega el objeto y llama `guardar()`. Guardar prepara una lista con `objeto.a_diccionario()` y llama `self.gestor.guardar(filas)`. Ese método devuelve booleano. Si falla, el controlador revierte su lista. El CRUD devuelve una tupla `(booleano, mensaje)`.

## Consultar

```python
lista = empleados.leer()
empleado = empleados.obtener(1)
coincidencias = empleados.buscar("ana")
```

`leer()` devuelve una lista de objetos; `buscar()` también devuelve lista, posiblemente vacía. `obtener()` devuelve un objeto o `None` cuando el ID no existe. El menú puede usar `if empleado is None` antes de mostrar detalles.

## Actualizar

```python
cambios = {"cargo": "Supervisora", "email": "ana.paz@ejemplo.com"}
exito, mensaje = empleados.actualizar(1, cambios)
```

`cambios` contiene solo campos a reemplazar. `datos.get("cargo", valor_por_defecto)` permite ausencia sin error; `datos["cargo"]` exige que esté presente y produce `KeyError` si no. Antes de modificar, se valida el diccionario completo. `getattr(objeto, campo)` lee un atributo nombrado en una variable y `setattr(objeto, campo, valor)` lo cambia. Se guarda; si falla se restaura el valor anterior. En una actualización mult campo, cada campo enviado debe validarse y todos los cambios forman una operación.

## Eliminar

```python
resultado = empleados.eliminar(1)  # (exito, mensaje)
```

El controlador busca el objeto, lo quita de `self.lista` y guarda el JSON. Si guarda devuelve `False`, reintroduce el objeto. `if not self.guardar()` solo funciona si `guardar()` retorna un booleano de GestorJSON; sin retorno Python produce `None`, que se interpreta como falso aunque la escritura haya funcionado.

## Relaciones y llamadas entre archivos

Importar una clase permite llamar sus métodos: `from views import EmpleadoController`, luego `empleados.crear(datos)`. Para una venta relacionada, `VentaController(clientes, productos)` recibe los **mismos objetos controlador** que usa main. Así `self.clientes.obtener(cliente_id)` consulta la lista vigente. Nómina y hospital aplican el mismo patrón para empleados/departamentos y pacientes/médicos. Un ID relacionado se comprueba antes de guardar; el controlador relacionado devuelve objeto o `None`.
