import mapas
import mysql.connector
import os
import diccionarios
import eventos




def LimpiarPantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")



# Dividir el mapa en líneas
lineas = mapas.hyrule_map.strip().split('\n')

# Crear una lista de listas
matriz = []
prompt = []

#Variable que almacena las acciones.


# Procesar cada línea y agregarla a la matriz como una lista de caracteres
for linea in lineas:
    fila = [[c] for c in linea]
    matriz.append(fila)



current_pos = [8, 11]
command = ""


print(mapas.hyrule_map)

while True:


    current_pos_original = current_pos.copy()


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

    eventos.interactable_events(matriz,current_pos,prompt,command,diccionarios.main_dict_hyrule)


    LimpiarPantalla()


        # Desempaquetar la matriz e imprimir el mapa original
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if j != 78:
                print(matriz[i][j][0], end="")
            else:
                print(matriz[i][j][0])

    print(current_pos)




# Imprimimos las últimas 8 líneas de la lista prompt
    for line in prompt[-8:]:
        print(line)
    if len(prompt) > 8:
        prompt.remove(prompt[0])

    #Sumamos una accion

    diccionarios.player_dict["action_count"] += 1



