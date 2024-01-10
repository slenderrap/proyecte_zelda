import mapas
import mysql.connector

# Dividir el mapa en líneas
lineas = mapas.hyrule_map.strip().split('\n')

# Crear una lista de listas
matriz = []

# Procesar cada línea y agregarla a la matriz como una lista de caracteres
for linea in lineas:
    fila = [[c] for c in linea]
    matriz.append(fila)


def interactable_events():
    # Definir la distancia máxima para considerar que el jugador está cerca
    max_distance = 1
    # Obtener el contenido de la casilla actual
    current_tile = matriz[current_pos[0]][current_pos[1]][0]
    # Variable de control para verificar si se ha abierto el cofre
    chest_opened = False

    # Verificamos si el jugador está cerca de un cofre y escribe "open"
    if current_tile == "X":
        for i in range(current_pos[0] - max_distance, current_pos[0] + max_distance + 1):
            for j in range(current_pos[1] - max_distance, current_pos[1] + max_distance + 1):
                try:
                    # Verificar si la casilla contiene un cofre y si el jugador escribe "open"
                    if matriz[i][j][0] == "T" and command.lower() == "open" and not chest_opened:
                        print("Chest opened!")
                        chest_opened = True
                except IndexError:
                    pass


print(matriz[8][11])

current_pos = [8, 11]

while True:
    current_pos_original = current_pos.copy()

    interactable_events()



#movimiento basico

    y = current_pos[0]
    x = current_pos[1]
    # pedir input
    command = input("Give an Order:")

    if "go left" in command:
        command.replace(" ", "")
        if command[command.find(" ", 3) + 1:].isdigit():
            x -= int(command[command.find(" ", 3) + 1:])

    if "go right" in command:
        command.replace(" ", "")
        if command[command.find(" ", 3) + 1:].isdigit():
            x += int(command[command.find(" ", 3) + 1:])

    if "go up" in command:
        command.replace(" ", "")
        if command[command.find(" ", 3) + 1:].isdigit():
            y -= int(command[command.find(" ", 3) + 1:])

    if "go down" in command:
        command.replace(" ", "")
        if command[command.find(" ", 3) + 1:].isdigit():
            y += int(command[command.find(" ", 3) + 1:])

    #posicion actual del jugador
    matriz[current_pos[0]][current_pos[1]] = [" "]

    current_pos[0] = y
    current_pos[1] = x

    #condiciones limites del mapa

    if current_pos[1] > 57:
        current_pos = current_pos_original
    elif current_pos[1] < 1:
        current_pos = current_pos_original
    elif current_pos[0] > 10:
        current_pos = current_pos_original
    elif current_pos[0] < 1:
        current_pos = current_pos_original



        #ponemos al jugador en el mapa
    try:
        assert matriz[current_pos[0]][current_pos[1]] == [" "]
        matriz[current_pos_original[0]][current_pos_original[1]] = [" "]
        matriz[current_pos[0]][current_pos[1]] = ["X"]

    except AssertionError:
        current_pos = current_pos_original
        matriz[current_pos[0]][current_pos[1]] = ["X"]



        # Desempaquetar la matriz e imprimir el mapa original
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if j != 78:
                print(matriz[i][j][0], end="")
            else:
                print(matriz[i][j][0])

    print(current_pos)