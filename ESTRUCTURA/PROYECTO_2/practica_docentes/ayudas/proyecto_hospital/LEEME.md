# Proyecto didáctico de hospital

Ejecute `python main.py` desde esta carpeta. Los datos JSON se guardan en su subcarpeta `data/`. Paciente y Medico heredan de Persona; Cita guarda sus IDs relacionados, fecha y hora.

Cada controlador concreto hereda directamente de `CrudBase` e implementa explícitamente las siete operaciones. `models.py` contiene los objetos; `views.py` valida relaciones, fechas, horas y duplicados; `main.py` presenta funciones de pantalla y submenús con el patrón de ventas.

## Construcción y conexiones

`CitaController` recibe obligatoriamente las instancias de pacientes y médicos. Para que sus eliminaciones protejan las citas, conecte sus referencias inversas:

```python
pacientes = PacienteController()
medicos = MedicoController()
citas = CitaController(pacientes, medicos)
pacientes.conectar_citas(citas)
medicos.conectar_citas(citas)
```

Si se intenta eliminar un paciente o médico antes de conectar CitaController, la operación devuelve un error explicativo; no ignora la relación ni produce `AttributeError`. Tampoco se permite eliminar una persona que tenga citas. Elimine primero las citas asociadas.

La fecha se normaliza a `AAAA-MM-DD`. La hora se convierte a formato canónico: `09:00` y `09:00:00` se guardan y comparan como `09:00`. Las reglas impiden que un paciente o médico tenga dos citas en el mismo horario y excluyen la cita actual al actualizar. Para probar, suministre una ruta temporal a cada constructor y no use los JSON habituales.
