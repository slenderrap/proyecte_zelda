import random
#MAPAS

hyrule_map_original = ("*Hyrule * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n\
*                                    ~~~~~~~~~~~~~~~~~~OOO*                   *\n\
*                                    ~~~~~~~~~~~~~OO~OOOO~*                   *\n\
*              C                           ~~~~~~   ~~~~~~*                   *\n\
*    T                                                 ~~~*                   *\n\
*                                   E9                    *                   *\n\
*                                           S0            *                   *\n\
*                                                         *                   *\n\
*         !X                                    T         *                   *\n\
* OO    OOOO         E1        S1?            T M    F    *                   *\n\
*OOOOOOOOOOO                                              *                   *\n\
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")



hyrule_map = ("*Hyrule * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n\
*                                    ~~~~~~~~~~~~~~~~~~OOO*                   *\n\
*                                    ~~~~~~~~~~~~~OO~OOOO~*                   *\n\
*              C                           ~~~~~~   ~~~~~~*                   *\n\
*    T                                                 ~~~*                   *\n\
*                                   E9                    *                   *\n\
*                                           S0            *                   *\n\
*                                                         *                   *\n\
*         !X                                    T         *                   *\n\
* OO    OOOO         E1        S1?            T M    F    *                   *\n\
*OOOOOOOOOOO                                              *                   *\n\
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")

#Ancho mapa:57
#Ancho inventario:19

# Dividir el mapa en líneas
lineas = hyrule_map.strip().split('\n')

# Crear una lista de listas
matriz = []

# Procesar cada línea y agregarla a la matriz como una lista de caracteres
for linea in lineas:
    fila = [[c] for c in linea]
    matriz.append(fila)

# Imprimir la matriz
#matriz[4][4]="P"

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if j != 78:
            print(matriz[i][j][0], end="")
        else:
            print(matriz[i][j][0])

current_pos = [8, 11]

while True:

#movimiento basico
    current_pos_original=current_pos.copy()




    y = current_pos[0]
    x = current_pos[1]
    #pedir input
    command = input("Give an Order:")

    if "go left" in command:
        command.replace(" ","")
        if command[command.find(" ",3)+1:].isdigit():
            x -= int(command[command.find(" ",3)+1:])

    if "go right" in command:
        command.replace(" ","")
        if command[command.find(" ", 3)+1:].isdigit():
            x += int(command[command.find(" ", 3)+1:])

    if "go up" in command:
        command.replace(" ", "")
        if command[command.find(" ", 3)+1:].isdigit():
            y -= int(command[command.find(" ", 3)+1:])


    if "go down" in command:
        command.replace(" ", "")
        if command[command.find(" ", 3)+1:].isdigit():
            y += int(command[command.find(" ", 3)+1:])

    #posicion actual del jugador


    current_pos[0] = y
    current_pos[1] = x

    #condiciones limites del mapa

    if current_pos[1]>57:
        current_pos = current_pos_original
    elif current_pos[1] < 1:
        current_pos = current_pos_original
    elif current_pos[0]>10:
        current_pos = current_pos_original
    elif current_pos[0]<1:
        current_pos = current_pos_original



    #ponemos al jugador en el mapa
    try:
        assert matriz[current_pos[0]][current_pos[1]] == [" "]
        matriz[current_pos_original[0]][current_pos_original[1]] = [" "]
        matriz[current_pos[0]][current_pos[1]] = ["X"]

    except AssertionError:
        current_pos = current_pos_original



    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if j != 78:
                print(matriz[i][j][0], end="")
            else:
                print(matriz[i][j][0])


