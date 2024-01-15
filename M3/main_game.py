import random
import funciones.inventario

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

# Procesar cada línea y agregarla a la matriz como una lista de caracteres
for linea in lineas:
    fila = [[c] for c in linea]
    matriz.append(fila)

#Variable que almacena las acciones.





#evento Fox
#el 50% de las veces, fox desaparecerá del mapa
if random.randint(1,2) == 1:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == ["F"]:
                # Encontrado, actualiza la matriz
                matriz[i][j] = [" "]
                break



#actualizamos mapa pre partida
mapas.update_map_pre_start(matriz)


current_pos = [8, 10]
command = ""

#funcion que muestra el inventario actual seleccionado
current_inventory = funciones.inventario.player_inventory_main


while True:
    #INICIO DE ACCION
    LimpiarPantalla()
    matriz = mapas.agregar_inventario(matriz,current_inventory)
    mapas.actualizar_mapa(matriz)


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
    if "go by water" in command:
        new_pos = eventos.move_to_X(matriz, current_pos,["~"])
        y,x = new_pos[0],new_pos[1]

    if "go by sanctuary" in command:
        new_pos = eventos.move_to_X(matriz, current_pos,["S"])
        y,x = new_pos[0],new_pos[1]

    if "go by tree" in command:
        new_pos = eventos.move_to_X(matriz, current_pos,["T"])
        y,x = new_pos[0],new_pos[1]

    if "go by tree" in command:
        new_pos = eventos.move_to_X(matriz, current_pos,["T"])
        y,x = new_pos[0],new_pos[1]

    if "show inventory main" in command:
        current_inventory = funciones.inventario.player_inventory_main

    if "show inventory weapons" in command:
        current_inventory = funciones.inventario.player_inventory_weapons

    if "show inventory food" in command:
        current_inventory = funciones.inventario.player_inventory_food

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



    #COMPROBAMOS LA VIDA DEL JUGADOR:
    if diccionarios.player_dict["hearts"] <= 0:
        eventos.historialPrompt(prompt, "You are dead!")
    # AQUI INVOCAMOS PANTALLA DE MUERTE

    LimpiarPantalla()
    #imprimimos el mapa
    mapas.actualizar_mapa(matriz)
    print(current_pos)

    if len(prompt) != 0:
        for i in prompt:
            print(i)
