# 6. Comparar los proyectos

| Proyecto | Modelo/relación | Reglas que suelen variar |
|---|---|---|
| Ventas | Cliente(Persona), Producto(ModeloBase), Venta(ModeloBase); VentaController recibe clientes y productos. | Email, precio/stock, IDs existentes y disponibilidad; venta conserva el precio del momento y ajusta stock. |
| Sistema académico | Estudiante(Persona), Materia(ModeloBase), Matrícula(ModeloBase); Matrícula recibe estudiante y materia. | Email/carnet, nota y cupos; matrícula impide duplicidad por estudiante/materia/periodo. |
| Empleados | Empleado(Persona); ejemplo sin otra entidad asociada. | Campos requeridos y unicidad de email como regla didáctica simple. |
| Nómina | Empleado(Persona) lleva departamento_id; Nómina recibe controlador de empleados. | Importes finitos y limitados, neto no negativo, un pago por empleado/periodo. |
| Hospital | Paciente y Medico heredan Persona; Cita recibe ambos controladores. | Fecha/hora válidas, IDs existentes y choques de ambos participantes. |

En cada proyecto se conservan el patrón `ModeloBase`, `desde_diccionario()`, `a_diccionario()` en cadena con `super()`, `etiqueta()` polimórfica, `CrudBase`, siete operaciones, `GestorJSON`, menú de diccionarios y utilidades compartidas. Cambian nombres de clases/campos, archivos JSON, reglas propias y controladores relacionados. Las reglas que no aparezcan en el proyecto de referencia son decisiones pedagógicas documentadas, no requisitos del profesor.

Un hijo hereda del controlador base para ofrecer la misma interfaz. Una relación entre entidades se expresa pasando el controlador existente al constructor y consultando su `obtener()`. No se debe instanciar un controlador duplicado dentro de otro: podría contener una lista desactualizada.
