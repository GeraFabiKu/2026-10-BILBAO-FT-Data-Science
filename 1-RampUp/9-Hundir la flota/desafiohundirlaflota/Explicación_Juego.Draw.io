┌─────────────────────────┐
│         INICIO          │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ Importar librerías      │
│ y constantes            │
│ random                  │
│ variables.py            │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ Crear estructuras       │
│ principales             │
│                         │
│ tableros                │
│ radares                 │
│ barcos                  │
│ vivas                   │
│ impactos_fila           │
│ mis_resultados          │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ Crear 2 tableros        │
│ Jugador y Máquina       │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ Inicializar todas las   │
│ casillas con AGUA       │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ Colocar barcos          │
│ aleatoriamente          │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ Elegir posición         │
│ aleatoria               │
│                         │
│ fila                    │
│ columna                 │
│ orientación             │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ Calcular todas las      │
│ casillas del barco      │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ ¿Caben en el tablero?   │
│ ¿Están libres?          │
└───────┬─────────┬───────┘
        │No       │Sí
        ▼         ▼
 Elegir otra   Colocar barco
 posición      Guardar barco
               Sumar casillas
               vivas
                     │
                     ▼
┌─────────────────────────┐
│ ¿Quedan barcos          │
│ por colocar?            │
└───────┬─────────┬───────┘
        │Sí       │No
        ▼         ▼
 Repetir      Mostrar reglas
 colocación   del juego
                     │
                     ▼
┌─────────────────────────┐
│ turno = 0               │
│ abandonado = False      │
└───────────┬─────────────┘
            │
            ▼
╔════════════════════════════════╗
║      BUCLE PRINCIPAL           ║
║ vivas[0]>0 y vivas[1]>0        ║
╚══════════════╤═════════════════╝
               │
               ▼
┌─────────────────────────┐
│ ¿Turno jugador?         │
│ turno == 0              │
└───────┬─────────┬───────┘
        │Sí       │No
        ▼         ▼

──────────── RAMA JUGADOR ────────────

┌─────────────────────────┐
│ Mostrar MI RADAR        │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ Mostrar MI FLOTA        │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ Pedir coordenada        │
│ Ej: B7                  │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ ¿Has escrito Q?          │
└───────┬─────────┬───────┘
        │Sí       │No
        ▼         ▼
 abandonado     Validar
 = True         entrada
 break
                  │
                  ▼
┌─────────────────────────┐
│ ¿Formato correcto?      │
└───────┬─────────┬───────┘
        │No       │Sí
        ▼         ▼
 Mostrar     Obtener fila
 error       y columna
 continue
                  │
                  ▼
┌─────────────────────────┐
│ ¿Dentro del tablero?    │
└───────┬─────────┬───────┘
        │No       │Sí
        ▼         ▼
 Mostrar     ¿Ya disparado?
 error
 continue         │
                  ▼
         ┌────────┴─────────┐
         │Sí                │No
         ▼                  ▼
    Mostrar error       Realizar
    continue            disparo

──────────── RAMA MAQUINA ────────────

┌─────────────────────────┐
│ Recorrer radar          │
│ de la máquina           │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ Guardar casillas        │
│ libres                  │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ Elegir una al azar      │
└───────────┬─────────────┘
            │
            ▼
      Realizar disparo

──────── RESOLUCIÓN DEL DISPARO ────────

┌─────────────────────────┐
│ Buscar coordenada en    │
│ barcos enemigos         │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ ¿Pertenece a un barco?  │
└───────┬─────────┬───────┘
        │No       │Sí
        ▼         ▼
 resultado     Eliminar
 = agua        casilla
               del barco
                    │
                    ▼
          vivas[defensor]--
                    │
                    ▼
┌─────────────────────────┐
│ ¿Barco vacío?           │
└───────┬─────────┬───────┘
        │Sí       │No
        ▼         ▼
 resultado   resultado
 hundido     tocado

──────── ACTUALIZACIÓN TABLEROS ───────

┌─────────────────────────┐
│ ¿Resultado agua?        │
└───────┬─────────┬───────┘
        │Sí       │No
        ▼         ▼
 Marcar       Marcar
 FALLO        IMPACTO
 Radar        Radar
 Tablero      Tablero

──────── ESTADÍSTICAS ────────────────

┌─────────────────────────┐
│ ¿Atacante = jugador?    │
└───────┬─────────┬───────┘
        │Sí       │No
        ▼         ▼
 Guardar       Seguir
 resultado
      │
      ▼
┌─────────────────────────┐
│ ¿Impacto?               │
└───────┬─────────┬───────┘
        │Sí       │No
        ▼         ▼
 impactos_fila++
         │
         ▼

──────── CAMBIO DE TURNO ─────────────

┌─────────────────────────┐
│ ¿Resultado agua?        │
└───────┬─────────┬───────┘
        │Sí       │No
        ▼         ▼
 Cambiar     Mostrar
 turno       BOOM
             IMPACTO
                  │
                  ▼
          ¿Hundido?
             │
       ┌─────┴─────┐
       ▼           ▼
   Hundido       Tocado
                  │
                  ▼
        Mismo jugador repite

                  │
                  ▼
        Regresar al bucle

══════════ FIN DE PARTIDA ══════════

┌─────────────────────────┐
│ ¿Abandonó?              │
└───────┬─────────┬───────┘
        │Sí       │No
        ▼         ▼
 Mensaje       ¿Quién ganó?
 salida
                    │
                    ▼
        ┌───────────┴───────────┐
        ▼                       ▼
 Máquina sin barcos      Jugador sin barcos
 Gana jugador            Gana máquina

                    │
                    ▼
┌─────────────────────────┐
│ Mostrar tablero final   │
│ del jugador             │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ Mostrar tablero final   │
│ de la máquina           │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ Calcular informe        │
│                         │
│ disparos                │
│ impactos                │
│ agua                    │
│ hundidos                │
│ precisión               │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ Mostrar impactos        │
│ por fila                │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│           FIN           │
└─────────────────────────┘