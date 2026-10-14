# 5. Pruebas manuales

Realice en una carpeta temporal o ejemplo desechable. Resultado esperado:

1. **Crear y listar:** crear entidad con campos válidos; aparece confirmación y el mismo registro al listar.
2. **Buscar y obtener:** buscar por parte del nombre/etiqueta devuelve coincidencias; consultar el ID devuelve el objeto.
3. **ID inexistente:** consultar o actualizar un ID que no existe devuelve `None` o `(False, mensaje)` sin excepción ni cambio.
4. **Datos inválidos/duplicados:** probar campo vacío, texto en monto, monto fuera de rango, relación inexistente y duplicidad; todos se rechazan antes de guardar.
5. **Actualizar varios campos:** enviar dos campos; ambos cambian y siguen correctos tras volver a listar.
6. **Eliminar/cancelar:** cancelar desde menú no cambia nada; confirmar elimina y luego la búsqueda por ID da `None`.
7. **Persistencia:** cerrar, volver a iniciar con el mismo directorio de datos y confirmar que altas, cambios y bajas permanecen.
8. **Relaciones nómina:** crear departamento, empleado asociado y nómina; intentar IDs que no existen y periodo duplicado; se rechazan. El pago neto concuerda con base + bono - descuento. Eliminar departamento/empleado relacionado se bloquea.
9. **Relaciones hospital:** crear paciente y médico, luego cita; intentar ID inexistente, fecha/hora inválida, choque del médico, choque del paciente y actualización que colisiona con otra cita. Son rechazados. Crear una cita a `09:00:00` y otra equivalente a `09:00` debe detectar el duplicado. La misma cita puede conservar su horario al actualizar otro campo permitido.
10. **Nombre de departamento:** crear `Ventas`, actualizarlo a ` Ventas ` y probar crear otro `Ventas`; el segundo departamento debe rechazarse y el primero conservar el mismo ID.

Para automatizar, ejecute cada ejemplo en un proceso separado con su carpeta como directorio actual y pase rutas temporales diferentes a cada constructor. Así no se mezclan importaciones genéricas (`models`, `views`) ni se toca JSON real.
