# 4. Variantes de eliminación

Son diseños alternativos para ejercicios independientes. No se mezclan ni se aplican al proyecto existente. Toda variante debe mantener JSON y `self.lista` coherentes.

## 1. Habitual: lógica en el controlador

```python
def eliminar(self, id_registro):
    objeto = self.obtener(id_registro)
    if objeto is None:
        return False, "No existe"
    posicion = self.lista.index(objeto)
    self.lista.remove(objeto)
    if not self.guardar():
        self.lista.insert(posicion, objeto)
        return False, "Falló el guardado; se restauró el registro"
    return True, "Eliminado"
```

El controlador decide reglas, actualiza su colección y usa el booleano de `guardar()`. El menú solo llama `controlador.eliminar(id)` y presenta la tupla.

## 2. Si se exige ejecutar la operación desde main

```python
def quitar_de_lista_y_guardar(controlador, id_registro):
    objeto = controlador.obtener(id_registro)
    if objeto is None:
        return False, "No existe"
    posicion = controlador.lista.index(objeto)
    controlador.lista.remove(objeto)
    if not controlador.guardar():
        controlador.lista.insert(posicion, objeto)
        return False, "Falló el guardado; lista restaurada"
    return True, "Eliminado"

# En la pantalla de main.py:
exito, mensaje = quitar_de_lista_y_guardar(empleados, id_registro)
print(mensaje)
```

Aquí la regla/flujo se traslada a una función de main. Llamar desde main al método habitual (`empleados.eliminar(id)`) **no** traslada la lógica: sigue ejecutándose en views.py. Para esta variante, el controlador necesita exponer `obtener`, `lista` y `guardar`; centralizar fuera puede saltarse validaciones de relaciones.

## 3. Si GestorJSON debe borrar por ID

```python
def eliminar_por_id(self, filas, id_registro):
    restantes = []
    encontrado = False
    for fila in filas:
        if fila.get("id") == id_registro:
            encontrado = True
        else:
            restantes.append(fila)
    if not encontrado:
        return False
    return self.guardar(restantes)
```

El método recibe registros ya serializados, crea una lista de salida y persiste solo si encontró el ID. El controlador coordina memoria y disco:

```python
objeto = self.obtener(id_registro)
if objeto is None:
    return False, "No existe"
filas = []
for registro in self.lista:
    filas.append(registro.a_diccionario())
if not self.gestor.eliminar_por_id(filas, id_registro):
    return False, "No se guardó la eliminación"
self.lista.remove(objeto)
return True, "Eliminado"
```

El JSON se escribe antes de retirar el objeto de memoria; si falla, `self.lista` sigue intacta. GestorJSON no sabe de objetos modelo, reglas relacionadas ni mensajes de usuario. Estas piezas son fragmentos compatibles con el patrón mostrado, pero cada variante se ensaya por separado.
