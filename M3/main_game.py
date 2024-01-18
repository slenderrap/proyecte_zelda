import random
import funciones.inventario

import mapas
import mysql.connector
import os
import diccionarios
import eventos
from funciones.map import current_map
import funciones.dialogos



def LimpiarPantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

def addbottomline_update_map(matriz):
    def update_map_bl():
        # añadimos al mapa los posibles inputs al final
        show_inputs = ""
        for z in range(len(input_variable)):
            show_inputs += input_variable[z] + ", "
        show_inputs = show_inputs[:-2] + " "
        new_map = funciones.inventario.insertar_mapa( map, current_inventory)
        if len(show_inputs) %2 == 0:
            show_inputs += " "

        new_map = new_map[:882] + ("*  " + show_inputs + ("* " * ((76 - len(show_inputs)) // 2)))
        lineas = new_map.strip().split('\n')
        matriz = []
        for linea in lineas:
            fila = [[c] for c in linea]
            matriz.append(fila)
        return matriz

    map = ""
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if j != 78:
                map += matriz[i][j][0]
            else:
                map += matriz[i][j][0] + "\n"
    x, y = current_pos
    input_variable = ["Exit", "Attack", "Go"]
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if (i == x and j != y) or (i != x and j == y):
                # Agregar listado de inputs disponibles
                if diccionarios.player_dict["weapons_inventory"] and "Equip" not in input_variable:
                    input_variable.append("Equip")
                if diccionarios.player_dict["weapons_equipped"] and "Unequip" not in input_variable:
                    input_variable.append("Unequip")
                if diccionarios.player_dict["food_inventory"] and "Eat" not in input_variable:
                    input_variable.append("Eat")
                if matriz[i][j][0] == "C" and "Cook" not in input_variable:
                    input_variable.append("Cook")
                if matriz[i][j][0] == "~" and "Fish" not in input_variable:
                    input_variable.append("Fish")
                if matriz[i][j][0] in ("M", "W","S") and "Open" not in input_variable:
                    input_variable.append("Open")

                matriz = update_map_bl()

    return matriz

# Dividimos el mapa en líneas
lineas = getattr(mapas,(funciones.map.current_map[10:]+"_map")).strip().split('\n')

# Crear una lista de listas
matriz = []
prompt = []

# Procesar cada línea y agregarla a la matriz como una lista de caracteres
for linea in lineas:
    fila = [[c] for c in linea]
    matriz.append(fila)

last_map = ""




#evento Fox
#el 50% de las veces, fox desaparecerá del mapa
if random.randint(1,2) == 1:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == ["F"]:
                # Encontrado, actualiza la matriz
                matriz[i][j] = [" "]
                break


current_pos = []
#actualizamos mapa pre partida
#mapas.update_map_pre_start(matriz)
#funcion para cambiar la posicion inicial del mapa según su ubicacion
def player_change_pos():
    global current_pos
    if "hyrule" in funciones.map.current_map:
        current_pos = [8, 10]
    elif "death" in funciones.map.current_map:
        current_pos = [9,2]
    elif "gerudo" in funciones.map.current_map:
        current_pos = [9,2]
    elif "necluda" in funciones.map.current_map:
        current_pos = [2,2]
    elif "castle" in funciones.map.current_map:
        current_pos = [9,4]


player_change_pos()










command = ""

#funcion que muestra el inventario actual seleccionado
current_inventory = funciones.inventario.player_inventory_main

flag_00 = False #main menu
flag_01 = True #main game
flag_02 = False #death screen
flag_03 = False #castle
flag_04 = False #win screen

while flag_01:
    #INICIO DE ACCION


    #verificamos si hay arboles muertos
    for key, value in getattr(diccionarios,funciones.map.current_map).items():
        if 1 in value:
            for sub_key, sub_value in value[1].items():
                if sub_key.startswith("tree_"):
                    if matriz[sub_value[1][0]][sub_value[1][1]][0] != "T":
                        if sub_value[2] == 0:
                            matriz[sub_value[1][0]][sub_value[1][1]][0] = "T"
                            sub_value[0] = 4
                            sub_value[2] = 10
                        else:
                            if sub_value[0] == 0:
                                sub_value[2] -= 1
                                matriz[sub_value[1][0]][sub_value[1][1]][0] = str(sub_value[2])



    #Variable que almacena el nombre del mapa actual, usando el nombre de diccionario como referencia
    LimpiarPantalla()
    matriz = mapas.agregar_inventario(matriz,current_inventory)
    #fix, agregamos en cada iteracion al jugador en el mapa
    matriz[current_pos[0]][current_pos[1]] = ["X"]

    #mapas.actualizar_mapa(matriz)
    mapas.actualizar_mapa(addbottomline_update_map(matriz))




    #imprimimos la posicion actual
    #print(current_pos)

    if len(prompt) != 0:
        for i in prompt:
            print(i)
    print(current_pos)



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
            #si en el camino a esa casilla hay algun obstaculo, no lo atravesaremos
            for i in range((current_pos[1] - x)):
                if matriz[current_pos[0]][current_pos[1]-(i+1)] != [" "]:
                    x += int(command[command.find(" ", 3) + 1:])
                    break


    elif "go right" in command:
        command.replace(" ", "")
        if command[command.find(" ", 3) + 1:].isdigit():
            x += int(command[command.find(" ", 3) + 1:])
            # si en el camino a esa casilla hay algun obstaculo, no lo atravesaremos
            for i in range((x - current_pos[1])):
                if matriz[current_pos[0]][current_pos[1] + (i+1)] != [" "]:
                    x -= int(command[command.find(" ", 3) + 1:])
                    break

    elif "go up" in command:
        command.replace(" ", "")
        if command[command.find(" ", 3) + 1:].isdigit():
            y -= int(command[command.find(" ", 3) + 1:])
            # si en el camino a esa casilla hay algun obstaculo, no lo atravesaremos
            for i in range((current_pos[0] - y)):
                if matriz[current_pos[0] - (i + 1)][current_pos[1]] != [" "]:
                    y += int(command[command.find(" ", 3) + 1:])
                    break

    elif "go down" in command:
        command.replace(" ", "")
        if command[command.find(" ", 3) + 1:].isdigit():
            y += int(command[command.find(" ", 3) + 1:])
            # si en el camino a esa casilla hay algun obstaculo, no lo atravesaremos
            for i in range((y - current_pos[0])):
                if matriz[current_pos[0] + (i + 1)][current_pos[1]] != [" "]:
                    y -= int(command[command.find(" ", 3) + 1:])
                    break


    elif "go by water" in command:
        new_pos = eventos.move_to_X(matriz, current_pos,["~"])
        y,x = new_pos[0],new_pos[1]

    elif "go by sanctuary" in command:
        new_pos = eventos.move_to_X(matriz, current_pos,["S"])
        y,x = new_pos[0],new_pos[1]

    elif "go by tree" in command:
        new_pos = eventos.move_to_X(matriz, current_pos,["T"])
        y,x = new_pos[0],new_pos[1]

    elif "go by chest" in command:
        new_pos = eventos.move_to_X(matriz, current_pos,["M"])
        y,x = new_pos[0],new_pos[1]

    elif "go by bowl" in command:
        new_pos = eventos.move_to_X(matriz, current_pos,["C"])
        y,x = new_pos[0],new_pos[1]

    elif "show inventory main" in command:
        current_inventory = funciones.inventario.player_inventory_main

    elif "show inventory weapons" in command:
        current_inventory = funciones.inventario.player_inventory_weapons

    elif "show inventory food" in command:
        current_inventory = funciones.inventario.player_inventory_food
    elif "hyrule" in funciones.map.current_map:
        if "go to gerudo" in command:
            funciones.map.current_map = "main_dict_gerudo"
            matriz = mapas.change_map()
            mapas.update_map_pre_start(matriz)
            current_pos = [9,2]
            continue
        if "go to death mountain" in command:
            funciones.map.current_map = "main_dict_death_mountain"
            matriz = mapas.change_map()
            mapas.update_map_pre_start(matriz)
            current_pos = [9,2]
            continue
        if "go to castle" in command:
            current_pos = [9, 4]
            last_map = funciones.map.current_map
            funciones.map.current_map = "main_dict_castle"
            matriz = mapas.change_map()
            flag_03 = True
            flag_01 = False
            continue

    elif "death" in funciones.map.current_map:
        if "go to necluda" in command:
            funciones.map.current_map = "main_dict_necluda"
            matriz = mapas.change_map()
            mapas.update_map_pre_start(matriz)
            current_pos = [2,2]
            continue
        if "go to hyrule" in command:
            funciones.map.current_map = "main_dict_hyrule"
            matriz = mapas.change_map()
            mapas.update_map_pre_start(matriz)
            current_pos = [8,10]
            continue
        if "go to castle" in command:
            current_pos = [9, 4]
            last_map = funciones.map.current_map
            funciones.map.current_map = "main_dict_castle"
            matriz = mapas.change_map()
            flag_03 = True
            flag_01 = False
            continue
    elif "gerudo" in funciones.map.current_map:
        if "go to necluda" in command:
            funciones.map.current_map = "main_dict_necluda"
            matriz = mapas.change_map()
            mapas.update_map_pre_start(matriz)
            current_pos = [2,2]
            continue
        if "go to hyrule" in command:
            funciones.map.current_map = "main_dict_hyrule"
            matriz = mapas.change_map()
            mapas.update_map_pre_start(matriz)
            current_pos = [8,10]
            continue
        if "go to castle" in command:
            current_pos = [9, 4]
            last_map = funciones.map.current_map
            funciones.map.current_map = "main_dict_castle"
            matriz = mapas.change_map()
            flag_03 = True
            flag_01 = False
            continue
    elif "necluda" in funciones.map.current_map:
        if "go to death mountain" in command:
            funciones.map.current_map = "main_dict_death_mountain"
            matriz = mapas.change_map()
            mapas.update_map_pre_start(matriz)
            current_pos = [9,2]
            continue
        if "go to gerudo" in command:
            funciones.map.current_map = "main_dict_gerudo"
            matriz = mapas.change_map()
            mapas.update_map_pre_start(matriz)
            current_pos = [9,2]
            continue
        if "go to castle" in command:
            current_pos = [9, 4]
            last_map = funciones.map.current_map
            funciones.map.current_map = "main_dict_castle"
            matriz = mapas.change_map()
            flag_03 = True
            flag_01 = False
            continue




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

    eventos.interactable_events(matriz,current_pos,prompt,command,getattr(diccionarios,funciones.map.current_map))



    #COMPROBAMOS LA VIDA DEL JUGADOR:
    if diccionarios.player_dict["hearts"] <= 0:
        eventos.historialPrompt(prompt, "You are dead!")
        # AQUI INVOCAMOS PANTALLA DE MUERTE
        flag_02 = True
        flag_01 = False










while flag_03: # GANON

    # INICIO DE ACCION


    # Variable que almacena el nombre del mapa actual, usando el nombre de diccionario como referencia
    LimpiarPantalla()
    matriz = mapas.agregar_inventario(matriz, current_inventory)
    # fix, agregamos en cada iteracion al jugador en el mapa
    matriz[current_pos[0]][current_pos[1]] = ["X"]

    # Desempaquetar la matriz e imprimir el mapa original
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if j != 78:
                print(matriz[i][j][0], end="")
            else:
                print(matriz[i][j][0])
    addbottomline_update_map(matriz)


    if len(prompt) != 0:
        for i in prompt:
            print(i)
    print(current_pos)

    current_pos_original = current_pos.copy()

    # movimiento basico

    y = current_pos[0]
    x = current_pos[1]
    # pedir input
    command = input("Give an Order:")

    if "go left" in command:
        command.replace(" ", "")
        if command[command.find(" ", 3) + 1:].isdigit():
            x -= int(command[command.find(" ", 3) + 1:])
            # si en el camino a esa casilla hay algun obstaculo, no lo atravesaremos
            for i in range((current_pos[1] - x)):
                if matriz[current_pos[0]][current_pos[1] - (i + 1)] != [" "]:
                    x += int(command[command.find(" ", 3) + 1:])
                    break


    elif "go right" in command:
        command.replace(" ", "")
        if command[command.find(" ", 3) + 1:].isdigit():
            x += int(command[command.find(" ", 3) + 1:])
            # si en el camino a esa casilla hay algun obstaculo, no lo atravesaremos
            for i in range((x - current_pos[1])):
                if matriz[current_pos[0]][current_pos[1] + (i + 1)] != [" "]:
                    x -= int(command[command.find(" ", 3) + 1:])
                    break

    elif "go by tree" in command:
        new_pos = eventos.move_to_X(matriz, current_pos, ["T"])
        y, x = new_pos[0], new_pos[1]

    elif "show inventory main" in command:
        current_inventory = funciones.inventario.player_inventory_main

    elif "show inventory weapons" in command:
        current_inventory = funciones.inventario.player_inventory_weapons

    elif "show inventory food" in command:
        current_inventory = funciones.inventario.player_inventory_food

    elif "back" in command and  "necluda" in last_map:
        funciones.map.current_map = "main_dict_necluda"
        matriz = mapas.change_map()
        mapas.update_map_pre_start(matriz)
        current_pos = [2, 2]
        continue
    elif "back" in command and "hyrule" in last_map:
        funciones.map.current_map = "main_dict_hyrule"
        matriz = mapas.change_map()
        mapas.update_map_pre_start(matriz)
        current_pos = [8, 10]
        continue
    elif "back" in command and "death" in last_map:
        funciones.map.current_map = "main_dict_death_mountain"
        matriz = mapas.change_map()
        mapas.update_map_pre_start(matriz)
        current_pos = [9, 2]
        continue
    elif "back" in command and "gerudo" in last_map:
        funciones.map.current_map = "main_dict_gerudo"
        matriz = mapas.change_map()
        mapas.update_map_pre_start(matriz)
        current_pos = [9, 2]
        continue
    elif current_pos[0] == 9 and current_pos[1] == 20:
        if command.lower() == "attack":
            if diccionarios.main_dict_castle["ganon_hearts"] >= 0:
                #si atacamos, quitaremos un corazon a ganon
                diccionarios.main_dict_castle["ganon_hearts"] -= 1
                for i in range(len(matriz)):
                    for j in range(len(matriz[i])):
                        if matriz[i][j] == ['♥']:
                            matriz[i][j] = [' ']
                            break
                #bajamos tambien los corazones del jugador
                diccionarios.player_dict["hearts"] -= 1
                if diccionarios.main_dict_castle["ganon_hearts"] <= 0:
                    diccionarios.player_dict["isganon_dead"] = True
                    flag_04 = True
                    flag_03 = False


            #si ganon tiene menos de 0 vidas, se gana la partida
            else:
                diccionarios.player_dict["isganon_dead"] = True
                flag_04 = True
                flag_03 = False





    # posicion actual del jugador
    matriz[current_pos[0]][current_pos[1]] = [" "]

    current_pos[0] = y
    current_pos[1] = x
    # condiciones limites del mapa

    if current_pos[1] > 57:
        current_pos = current_pos_original
    elif current_pos[1] < 1:
        current_pos = current_pos_original
    elif current_pos[0] > 10:
        current_pos = current_pos_original
    elif current_pos[0] < 1:
        current_pos = current_pos_original

    # ponemos al jugador en el mapa
    try:
        assert matriz[current_pos[0]][current_pos[1]] == [" "]
        matriz[current_pos_original[0]][current_pos_original[1]] = [" "]
        matriz[current_pos[0]][current_pos[1]] = ["X"]

    except AssertionError:
        current_pos = current_pos_original
        matriz[current_pos[0]][current_pos[1]] = ["X"]

    eventos.interactable_events(matriz, current_pos, prompt, command, getattr(diccionarios, funciones.map.current_map))

    # COMPROBAMOS LA VIDA DEL JUGADOR:
    if diccionarios.player_dict["hearts"] <= 0:
        eventos.historialPrompt(prompt, "You are dead!")
        # AQUI INVOCAMOS PANTALLA DE MUERTE
        flag_02 = True
        flag_03 = False


while flag_02:#pantalla de muerte
    LimpiarPantalla()
    funciones.dialogos.generador_menus(funciones.dialogos.death_top, funciones.dialogos.death_end, funciones.dialogos.death_content)
    prompt = input("Give an Order:")



while flag_04:#pantalla de win
    LimpiarPantalla()
    funciones.dialogos.generador_menus(funciones.dialogos.zelda_saved_top, funciones.dialogos.zelda_saved_end, funciones.dialogos.zelda_saved_content)
    prompt = input("Give an Order:")







