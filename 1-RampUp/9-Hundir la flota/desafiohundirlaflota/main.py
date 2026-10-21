
import random
from variables import FILAS, COLUMNAS, LETRAS, TAMANOS, AGUA, BARCO, IMPACTO, FALLO

# Indice 0 = yo, indice 1 = la maquina
#Estructuras principales

tableros = [[], []]      # tableros[0] es mio, tableros[1] el de la maquina
radares = [[], []]       # lo que cada uno ha descubierto del otro jugador
barcos = [[], []]        # cada barco es una lista de casillas [fila, columna] sin tocar
vivas = [0, 0]           # casillas de barco que quedan sin tocar en cada tablero
impactos_fila = [0] * FILAS   # mis impactos por fila, para el informe final
mis_resultados = []      # resultado de cada uno de mis disparos



# Creo los dos tableros y coloco los barcos al azar
for jugador in range(2):
    '''Creación de tableros: El bucle for jugador in range(2) crea un tablero para el jugador y otro para la máquina. 
    Cada fila se rellena con AGUA usando [AGUA] * COLUMNAS. 
    Después se guardan en tableros y radares.'''

    tab = []
    rad = []

    for f in range(FILAS):
        tab.append([AGUA] * COLUMNAS)
        rad.append([AGUA] * COLUMNAS)
    tableros[jugador] = tab
    radares[jugador] = rad

    for tamano in TAMANOS:
        '''Colocación aleatoria de barcos: Para cada tamaño en TAMANOS se busca una posición válida. 
        Se elige fila, columna y orientación aleatoria. 
        Se calculan todas las casillas que ocuparía el barco y se verifica que estén dentro de los límites y libres. 
        Si todo es correcto se colocan las piezas, se guarda el barco y se incrementan las casillas vivas.'''
        puesto = False

        while not puesto:
            fila = random.randint(0, FILAS - 1)
            columna = random.randint(0, COLUMNAS - 1)
            horizontal = random.choice([True, False])

            # calculo las casillas que ocuparia el barco
            casillas = []
            for paso in range(tamano):
                if horizontal:
                    casillas.append([fila, columna + paso])
                else:
                    casillas.append([fila + paso, columna])

            # miro si todas caben y estan libres
            ok = True
            for f, c in casillas:
                if f >= FILAS or c >= COLUMNAS:
                    ok = False
                elif tab[f][c] == BARCO:
                    ok = False

            # si todo esta bien, lo coloco!
            if ok:
                for f, c in casillas:
                    tab[f][c] = BARCO
                barcos[jugador].append(casillas)
                vivas[jugador] += tamano
                puesto = True

# Mensajes de inicio
'''Se muestran reglas, símbolos y el título del juego. turno=0 para mí y turno=1 para la maquina.'''

print("=" * 48)
print("       JUEGO HUNDIR LA FLOTA")
print("=" * 48)
print("Juego contra la máquina en un mar de 10 x 10.")
print("Escribo coordenadas tipo B7. Si escribo Q, salgo.")
print("B = mi barco, X = tocado, · = agua, ~ = sin disparar")

turno = 0          # 0 = me toca a mi, 1 = le toca a la maquina
abandonado = False


'''Bucle principal: while vivas[0] > 0 and vivas[1] > 0 mantiene la partida activa mientras ambos jugadores tengan barcos.'''  
while vivas[0] > 0 and vivas[1] > 0:

    if turno == 0:
        
        '''Turno del jugador: Se muestran el radar y la flota. enumerate permite obtener simultáneamente índice y fila. 
        El usuario introduce coordenadas como B7. strip elimina espacios y upper convierte a mayúsculas. 
        LETRAS.index transforma una letra en índice de fila. 
        int convierte el número introducido en índice de columna.'''

        # con esto recorro dos tableros y muestro el titulo correspondiente en mi radar y mi flota
        for titulo, tab in [("MI RADAR (lo que sé de la máquina)", radares[0]),
                            ("MI FLOTA", tableros[0])]:
            
            print("\n--- " + titulo + " ---")
            print("  1 2 3 4 5 6 7 8 9 10")

            for i, fila_texto in enumerate(tab):

                print(LETRAS[i], " ".join(fila_texto))

        entrada = input("\nMi disparo (ej. B7) o Q para salir: ").strip().upper()

        if entrada == "Q":
            abandonado = True
            break

        '''Agunas validaciones: Se controla que la coordenada tenga formato válido, 
        que exista en el tablero y que no haya sido disparada anteriormente.'''
        
        if len(entrada) < 2 or entrada[0] not in LETRAS or not entrada[1:].isdigit():
            print("Eso no sirve. Tiene que ser una letra y un número, como B7.")
            continue

        fila = LETRAS.index(entrada[0])
        columna = int(entrada[1:]) - 1

        if columna < 0 or columna >= COLUMNAS:
            print("Esa casilla no existe en el tablero.")
            continue

        if radares[0][fila][columna] != AGUA:
            print("Ya disparé ahí. Pruebo otra vez.")
            continue

    else:
        # Turno de la maquina: elige al azar una casilla que no haya probado
        '''La máquina construye una lista de casillas libres recorriendo todo el tablero. 
        random.choice selecciona una al azar para disparar.'''

        print("\nLa máquina está pensando...")
        libres = []

        for f in range(FILAS):
            for c in range(COLUMNAS):
                if radares[1][f][c] == AGUA:
                    libres.append((f, c))
        fila, columna = random.choice(libres)

        print("La máquina dispara a " + LETRAS[fila] + str(columna + 1) + ".")

    # el disparo (igual para mi y para la maquina)
    '''Resolución del disparo: atacante indica quién dispara y defensor quién recibe. 
    Se revisan todos los barcos enemigos. Si la coordenada pertenece a un barco se elimina con remove(). 
    También se reduce el contador vivas. Si el barco queda vacío el resultado es hundido; si no, tocado.'''

    atacante = turno
    defensor = 1 - turno
    resultado = "agua"

    for barco in barcos[defensor]:
        if [fila, columna] in barco:
            barco.remove([fila, columna])
            vivas[defensor] -= 1
            if len(barco) == 0:
                resultado = "hundido"
            else:
                resultado = "tocado"
            break

    # Marco el disparo en el radar del que dispara y en el tablero del otro
    '''Actualización de tableros: Los disparos fallidos se marcan con FALLO. 
    Los impactos se marcan con IMPACTO tanto en el radar del atacante como en el tablero real del defensor.'''

    if resultado == "agua":
        radares[atacante][fila][columna] = FALLO
        tableros[defensor][fila][columna] = FALLO
    else:
        radares[atacante][fila][columna] = IMPACTO
        tableros[defensor][fila][columna] = IMPACTO

    # Guardo los datos para el informe (solo de mis disparos)
    '''Estadísticas: Solo los disparos se almacenan en mis_resultados. 
    impactos_fila registra en qué filas se consiguieron impactos.'''

    if atacante == 0:
        mis_resultados.append(resultado)
        if resultado != "agua":
            impactos_fila[fila] += 1

    # Mensajes y cambio de turno
    '''Si el resultado es agua cambia el turno mediante turno = 1 - turno. 
    Cuando el disparo acierta, el mismo jugador vuelve a disparar.'''

    if resultado == "agua":
        print("Agua. Cambia el turno.")
        turno = 1 - turno
    else:
        print(r"""
          .  *  .
       *  \ | /  *
     . --- BOOM --- .
       *  / | \  *
          '  *  '
      ¡IMPACTO CONFIRMADO!
""")
        if resultado == "hundido":
            print("¡Hundido!")
        else:
            print("¡Tocado!")

        if atacante == 0:
            print("Repito turno.")
        else:
            print("La máquina repite turno.")


# Final de la partida!!!!!!!!!!!!!!!!
'''Si abandonado es True se termina la misión. En caso contrario se comprueba quién se quedó sin barcos. 
Después se imprimen ambos tableros y las estadísticas de la partida.'''

if abandonado:
    print("\nHas abandonado la misión. ¡Hasta la próxima!")
else:
    print("\n" + "=" * 48)
    if vivas[1] == 0:
        print("¡He ganado! Hundí toda la flota de la máquina, mi rival.")
    else:
        print("Gana la máquina. Mi flota ha quedado destrozada.")

    print("\nMi tablero al final:")
    for i, fila_texto in enumerate(tableros[0]):
        print(LETRAS[i], " ".join(fila_texto))

    print("\nTablero de la máquina:")
    for i, fila_texto in enumerate(tableros[1]):
        print(LETRAS[i], " ".join(fila_texto))

    # Imprimo el informe final de la partida
    '''Se calculan disparos, impactos, agua, barcos hundidos y precisión. 
    precision = impactos / total * 100 calcula el porcentaje de aciertos. 
    round(precision,1) redondea a un decimal. Finalmente se muestran los impactos por fila usando caracteres #.'''

    print("\n" + "=" * 48)
    print("INFORME DE LA PARTIDA")
    print("=" * 48)

    total = len(mis_resultados)
    impactos = 0
    agua = 0
    hundidos = 0

    for r in mis_resultados:
        if r == "agua":
            agua += 1
        else:
            impactos += 1
        if r == "hundido":
            hundidos += 1

    print("Disparos: " + str(total))
    print("Impactos: " + str(impactos))
    print("Agua: " + str(agua))
    print("Barcos hundidos: " + str(hundidos))

    if total > 0:
        precision = impactos / total * 100
        print('Precisión: ' + str(round(precision, 1)) + "%")

    print("\nImpactos por fila:")

    for i in range(FILAS):
        print(LETRAS[i], "#" * impactos_fila[i], "(" + str(impactos_fila[i]) + ")")

    print("\nOjo: una sola partida no dice que una fila sea más segura.")
