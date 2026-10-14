# Proyecto didáctico de hospital

Ejecute `python main.py` desde esta carpeta. El programa crea los JSON en `data/` al guardar cada tipo de registro.

Estudie `models.py` y después `shared/json_manager.py`, `views.py` y `main.py`. Paciente y Medico heredan sus datos comunes de Persona. Cita recibe los controladores de pacientes y médicos, verifica ambos IDs y evita conflictos de médico o paciente para igual fecha y hora. La fecha debe ser ISO `AAAA-MM-DD` y la hora `HH:MM` válida. Las comprobaciones excluyen la cita que se actualiza.

Supuestos: una cita ocupa exactamente un horario de minuto; no se modelan duración, zonas horarias, disponibilidad laboral ni cancelación lógica. No se elimina un paciente o médico que tenga citas; primero elimine las citas asociadas. Cada guardado fallido revierte la lista/objeto en memoria. Para ensayar datos temporales, pase una ruta temporal a cada constructor del controlador y no use la carpeta `data`.
