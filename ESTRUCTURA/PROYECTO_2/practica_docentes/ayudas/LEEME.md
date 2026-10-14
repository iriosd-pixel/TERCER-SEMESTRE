# Ayudas para estudiar CRUD y relaciones

## Orden recomendado

1. `01_agregar_entidad.md`: modelo, controlador, pantallas y persistencia.
2. `02_conectar_metodos.md`: recorrido de datos entre archivos.
3. `03_validaciones.md`: entradas, conversiones, relaciones y duplicados.
4. `04_variantes_eliminar.md`: tres diseños alternativos, como ejercicios separados.
5. `05_pruebas_manuales.md`: guion de comprobación.
6. `06_comparacion_proyectos.md`: qué cambia entre ventas, academia, empleados, nómina y hospital.
7. Ejecutar y leer `ejemplo_empleados`, luego `proyecto_nomina` y `proyecto_hospital`.

Los ejemplos independientes contienen modelos, CRUD, menús, utilidades y JSON propios. Abra una terminal en la carpeta indicada y ejecute `python main.py`. El gestor crea `data/`/JSON al guardar; para pruebas automatizadas se inyectan rutas temporales en los constructores. No inicialice pruebas y menú con datos reales si el objetivo es conservarlos intactos.

`ejemplo_empleados` enseña `Empleado(Persona)`. Nómina presenta departamentos, empleados relacionados y periodos de pago. Hospital presenta personas y citas con reglas de horario. Cada regla adicional está señalada como supuesto pedagógico en el LEEME del proyecto.
