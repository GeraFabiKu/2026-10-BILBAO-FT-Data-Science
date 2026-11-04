# EJERCICIO SQL: CERVEZAS

---

## 1. Tablas de la Base de Datos

### CERVEZAS
| CodC | Envase | Capacidad | Stock |
| :--- | :--- | :--- | :--- |
| 01 | Botella | 0.2 | 3600 |
| 02 | Botella | 0.33 | 1200 |
| 03 | Lata | 0.33 | 2400 |
| 04 | Botella | 1 | 288 |
| 05 | Barril | 60 | 30 |

### BARES
| CodB | Cif | Nombre | Localidad |
| :--- | :--- | :--- | :--- |
| 001 | 11111111X | Stop | Villa Botijo |
| 002 | 22222222Y | Las Vegas | Villa Botijo |
| 003 | - | Club Social | Las Ranas |
| 004 | 33333333Z | Otra Ronda | La Esponja |

### EMPLEADOS
| CodE | Nombre | Sueldo |
| :--- | :--- | :--- |
| 1 | Prudencio Caminero | 120000 |
| 2 | Vicente Merario | 110000 |
| 3 | Valentin Siempre | 100000 |

### REPARTO
| CodE | CodB | CodC | Fecha | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| 1 | 001 | 01 | 10/21/05 | 240 |
| 1 | 001 | 02 | 10/21/05 | 48 |
| 1 | 002 | 03 | 10/22/05 | 60 |
| 1 | 004 | 05 | 10/22/05 | 4 |
| 2 | 002 | 03 | 10/22/05 | 48 |
| 2 | 002 | 05 | 10/23/05 | 2 |
| 2 | 004 | 01 | 10/23/05 | 480 |
| 2 | 004 | 02 | 10/24/05 | 72 |
| 3 | 003 | 03 | 10/24/05 | 48 |
| 3 | 003 | 04 | 10/25/05 | 20 |

---

## 2. Enunciados de los Ejercicios

1. Obtener el nombre de los empleados que hayan repartido al bar **Stop** durante la semana del 17 al 23 de octubre de 2005.
2. Obtener el Cif y nombre de los bares a los que se ha repartido cerveza de tipo **Botella** y capacidad inferior a 1 litro, ordenados por localidad.
3. Obtener los repartos (nombre del bar, envase y capacidad de la bebida, fecha y cantidad) realizados por **Prudencio Caminero**.
4. Obtener los bares a los que se les ha repartido envases de tipo **botella** y capacidad 0.2 ó 0.33.
5. Nombre de los empleados que han repartido a los bares **"Stop"** y **"Las Vegas"** cervezas con envase botella. 
6. Obtener el nombre y número de viajes que ha realizado cada empleado fuera de **Villa Botijo**.
7. Obtener el nombre y localidad del bar que más litros de cerveza ha comprado.
8. Obtener los bares que han adquirido todos los tipos de cerveza con envase de botella y capacidad menor que 1 litro.
9. Subir un 5% el sueldo del empleado que más días haya trabajado.
10. Insertar un nuevo reparto del empleado **"Vicente Merario"** al bar **"Stop"** de 48 cervezas de tipo lata el día 10/26/05.