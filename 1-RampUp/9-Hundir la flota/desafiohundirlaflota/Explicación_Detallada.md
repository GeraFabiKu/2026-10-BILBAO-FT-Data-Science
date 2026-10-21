# HUNDIR LA FLOTA
## Documentación y explicación del proyecto

Autor: Fabiano

---

# 1. Objetivo del proyecto

El objetivo del programa es recrear el juego clásico *Hundir la Flota* en consola utilizando Python.

La partida enfrenta a dos jugadores:

- Jugador humano.
- Máquina.

Ambos disponen de un tablero con barcos colocados aleatoriamente.

El objetivo es hundir toda la flota enemiga antes de perder la propia.

---

# 2. Estructuras principales

## Tableros

```python
tableros = [[], []]
```

```text
tableros
│
├── tableros[0] → Jugador
│
└── tableros[1] → Máquina
```

Cada posición almacena:

```text
~
B
X
·
```

donde:

| Símbolo | Significado |
|----------|--------------|
| ~ | Casilla desconocida |
| B | Barco |
| X | Impacto |
| · | Agua |

---

## Radares

```python
radares = [[], []]
```

```text
radares
│
├── radares[0]
│   └── Lo que conozco de la máquina
│
└── radares[1]
    └── Lo que conoce la máquina de mí
```

---

## Barcos

```python
barcos = [[], []]
```

```text
barcos
│
├── barcos[0]
│   ├── barco_1
│   ├── barco_2
│   └── barco_n
│
└── barcos[1]
```

Cada barco almacena las coordenadas que todavía siguen vivas.

Ejemplo:

```python
[[2,3],[2,4],[2,5]]
```

---

## Contador de vidas

```python
vivas = [0,0]
```

```text
vivas[0] → casillas de mis barcos
vivas[1] → casillas de los barcos enemigos
```

---

# 3. Creación de tableros

## Código principal

```python
for jugador in range(2):

    tab = []
    rad = []

    for f in range(FILAS):
        tab.append([AGUA] * COLUMNAS)
        rad.append([AGUA] * COLUMNAS)

    tableros[jugador] = tab
    radares[jugador] = rad
```

## Explicación

El programa crea:

- Un tablero para el jugador.
- Un tablero para la máquina.
- Un radar para cada participante.

Representación:

```text
~ ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ ~ ~
...
```

---

# 4. Colocación aleatoria de barcos

## Código

```python
fila = random.randint(0, FILAS - 1)
columna = random.randint(0, COLUMNAS - 1)

horizontal = random.choice([True, False])
```

---

## Flujo

```text
Elegir posición
       │
       ▼
Elegir orientación
       │
       ▼
Calcular casillas
       │
       ▼
¿Caben?
 ├── No → volver a intentar
 └── Sí
       │
       ▼
¿Están libres?
 ├── No → volver a intentar
 └── Sí
       │
       ▼
Colocar barco
```

---

# 5. Inicio de la partida

## Código

```python
print("=" * 48)
print("JUEGO HUNDIR LA FLOTA")
```

Se muestran:

- Reglas.
- Símbolos.
- Tamaño del tablero.
- Cómo disparar.
- Cómo abandonar la partida.

---

# 6. Flujo general del programa

```text
INICIO
│
├─ Crear estructuras
│
├─ Crear tableros
│
├─ Colocar barcos
│
├─ Mostrar instrucciones
│
├─ BUCLE PRINCIPAL
│
└─ Informe final
```

---

# 7. Bucle principal

## Código

```python
while vivas[0] > 0 and vivas[1] > 0:
```

## Explicación

La partida continúa mientras ambos jugadores tengan barcos.

```text
¿Quedan barcos?
        │
    ┌───┴───┐
    │       │
   Sí       No
    │       │
    ▼       ▼
 Seguir    Fin
 jugando
```

---

# 8. Turno del jugador

## Código

```python
for titulo, tab in [
    ("MI RADAR", radares[0]),
    ("MI FLOTA", tableros[0])
]:
```

---

## Desempaquetado de tuplas

```text
("MI RADAR", radares[0])

      │            │
      │            └─ tablero mostrado
      │
      └─ título mostrado
```

```text
("MI FLOTA", tableros[0])

      │            │
      │            └─ tablero mostrado
      │
      └─ título mostrado
```

Esto evita repetir código.

---

# 9. Validación de coordenadas

## Código

```python
if len(entrada) < 2:
```

```python
if entrada[0] not in LETRAS:
```

```python
if not entrada[1:].isdigit():
```

---

## Flujo

```text
Entrada usuario
       │
       ▼
¿Formato correcto?
       │
   ┌───┴───┐
   │       │
  No      Sí
   │       │
   ▼       ▼
 Error  Convertir
         coordenada
```

---

# 10. Turno de la máquina

## Código

```python
libres = []

for f in range(FILAS):
    for c in range(COLUMNAS):
        if radares[1][f][c] == AGUA:
            libres.append((f,c))
```

---

## Funcionamiento

```text
Recorrer tablero
       │
       ▼
Guardar libres
       │
       ▼
random.choice()
       │
       ▼
Disparar
```

La máquina utiliza una estrategia completamente aleatoria.

---

# 11. Resolución del disparo

## Código

```python
for barco in barcos```

```python
if [fila, columna] in barco:
```

---

## Flujo

```text
Disparo
   │
   ▼
¿Hay barco?
   │
 ┌─┴─┐
 │   │
No  Sí
 │   │
 ▼   ▼
Agua Tocado
      │
      ▼
 ¿Quedan piezas?
      │
   ┌──┴──┐
   │     │
  Sí    No
   │     │
   ▼     ▼
Tocado Hundido
```

---

# 12. Actualización de tableros

## Código

```python
if resultado == "agua":
```

---

## Agua

```text
Radar   → FALLO
Tablero → FALLO
```

---

## Impacto

```text
Radar   → IMPACTO
Tablero → IMPACTO
```

---

# 13. Estadísticas

## Código

```python
mis_resultados.append(resultado)
```

```python
impactos_fila[fila] += 1
```

---

## Información guardada

- Disparos realizados.
- Impactos.
- Hundidos.
- Agua.
- Impactos por fila.

---

# 14. Cambio de turno

## Código

```python
if resultado == "agua":
```

---

## Lógica

```text
¿Resultado?
      │
 ┌────┴────┐
 │         │
Agua    Impacto
 │         │
 ▼         ▼
Cambia   Repite
turno    turno
```

---

# 15. Animación de explosión

## Código

```python
print(r"""
      .  *  .
   *  \ | /  *
 . --- BOOM --- .
   *  / | \  *
      '  *  '
""")
```

---

## Representación

```text
IMPACTO
   │
   ▼
 BOOM
   │
   ▼
Tocado o Hundido
```

---

# 16. Fin de la partida

```text
¿Abandonó?
 │
 ├── Sí → Mensaje de salida
 │
 └── No
       │
       ▼
¿Quién ganó?
       │
 ┌─────┴─────┐
 │           │
Yo      Máquina
```

---

# 17. Informe final

## Código

```python
precision = impactos / total * 100
```

```python
round(precision,1)
```

---

## Datos mostrados

- Disparos realizados.
- Impactos.
- Agua.
- Barcos hundidos.
- Precisión.
- Impactos por fila.

---

# Capturas con CodeSnap


### 1. Creación de tableros

![Creación de tableros](Img_CodeSnap/codesnap_creacion_tableros.png)


---

### 2. Colocación aleatoria de barcos

![Colocación de barcos](Img_CodeSnap/codesnap_colocacion_barcos.png)

---

### 3. Mostrar radar y flota

![Mostrar radar y flota](Img_CodeSnap/codesnap_radar_flota.png)

---

### 4. Validación de coordenadas

![Validación de coordenadas](Img_CodeSnap/codesnap_validacion.png)

---

### 5. Resolución del disparo

![Disparo](Img_CodeSnap/codesnap_disparo.png)

---

### 6. Actualización de tableros

![Actualización de tableros](Img_CodeSnap/codesnap_actualizacion_tablero.png)


---

### 7. Cálculo del informe final

![Informe final](Img_CodeSnap/codesnap_estadisticas.png)

---

# Diagrama completo del programa

```text
INICIO
 │
 ▼
Crear estructuras
 │
 ▼
Crear tableros
 │
 ▼
Colocar barcos
 │
 ▼
Mostrar reglas
 │
 ▼
BUCLE PRINCIPAL
 │
 ├─ Turno jugador
 │
 ├─ Turno máquina
 │
 ├─ Resolver disparo
 │
 ├─ Actualizar tableros
 │
 └─ Cambiar turno
 │
 ▼
¿Fin?
 │
 ├─ No → volver al bucle
 │
 └─ Sí
      │
      ▼
Informe final
      │
      ▼
FIN
```

---

# Conclusión

Este proyecto aplica los principales conceptos trabajados en clase:

- Variables.
- Listas y listas anidadas.
- Bucles.
- Condicionales.
- Funciones de la librería `random`.
- Validación de entradas.
- Manipulación de matrices.
- Estadísticas básicas.
- Diseño de lógica de juego por turnos.

