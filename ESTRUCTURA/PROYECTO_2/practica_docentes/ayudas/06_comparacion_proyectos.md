# 6. Comparar los proyectos

| Proyecto | Modelo/relación | Reglas que suelen variar |
|---|---|---|
| Ventas | Cliente(Persona), Producto(ModeloBase), Venta(ModeloBase); VentaController recibe clientes y productos. | Email, precio/stock, IDs existentes y disponibilidad; venta conserva el precio del momento y ajusta stock. |
| Sistema académico | Estudiante(Persona), Materia(ModeloBase), Matrícula(ModeloBase); Matrícula recibe estudiante y materia. | Email/carnet, nota y cupos; matrícula impide duplicidad por estudiante/materia/periodo. |
| Empleados | Empleado(Persona); ejemplo sin otra entidad asociada. | Campos requeridos y email único en este ejercicio didáctico. |
| Nómina | Empleado(Persona) lleva departamento_id; Nómina recibe controlador de empleados. | Montos finitos y limitados, neto no negativo, un pago por empleado/periodo. |
| Hospital | Paciente y Medico heredan Persona; Cita recibe ambos controladores. | Fechas/horas válidas, IDs existentes y choques de ambos participantes. |

Se conserva el patrón de modelos `ModeloBase`, `desde_diccionario()`, `a_diccionario()` con `super()` y `etiqueta()` polimórfica. Cada controlador concreto hereda directamente de `CrudBase` e implementa los siete métodos; no hay una clase intermedia genérica. También se conservan `GestorJSON`, los menús de diccionarios y las utilidades compartidas.

Los modelos heredan de otro modelo cuando expresan una relación "es una". Los controladores relacionados se reciben por constructor y se consultan con `obtener()`. Las referencias inversas para proteger eliminaciones se conectan de forma explícita: `conectar_empleados`, `conectar_nominas` o `conectar_citas`. Si falta una referencia necesaria para comprobar una eliminación, el método devuelve un error explicativo. No se debe crear un controlador duplicado dentro de otro, porque podría mantener una lista desactualizada.

Cambian los nombres de clases y campos, los archivos JSON y las reglas propias de cada dominio. Las reglas didácticas que no aparecen en el proyecto de referencia están documentadas como supuestos, no como requisitos del profesor.
