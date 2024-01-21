import inventario
import bbdd_changes
import mapas
import os
import diccionarios
import eventos
import funciones.dialogos
import prepartida



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
        new_map = inventario.insertar_mapa(map, current_inventory)
        if len(show_inputs) % 2 == 0:
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
    if "castle" in diccionarios.dades[2]["current_map"]:
        input_variable = [ "Attack", "Go", "Back"]
    else:
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


# Definimos las variables principales
matriz = []

#creamos la matriz por primera vez
lineas = getattr(mapas,(diccionarios.dades[2]["current_map"][10:]+"_map")).strip().split('\n')

# Procesamos cada línea y la agregamos a la matriz como una lista de caracteres
for linea in lineas:
    fila = [[c] for c in linea]
    matriz.append(fila)

prompt = []
last_map = "main_dict_hyrule"
current_pos = []
mapas.change_map()
#funcion que muestra el inventario actual seleccionado
current_inventory = inventario.player_inventory_main
flag_0 = True #Flag principal
flag_00 = True #main menu
flag_01 = False #main game
flag_02 = False #death screen
flag_03 = False #castle
flag_04 = False #win screen


#actualizamos mapa pre partida
#funcion para cambiar la posicion inicial del mapa según su ubicacion
def player_change_pos():
    global current_pos
    if "hyrule" in diccionarios.player_dict["region"].lower():
        current_pos = [8, 10]
        diccionarios.dades[2]["current_map"] = "main_dict_hyrule"
    elif "death" in diccionarios.player_dict["region"].lower():
        current_pos = [9,2]
        diccionarios.dades[2]["current_map"] = "main_dict_death_mountain"
    elif "gerudo" in diccionarios.player_dict["region"].lower():
        current_pos = [9,2]
        diccionarios.dades[2]["current_map"] = "main_dict_gerudo"
    elif "necluda" in diccionarios.player_dict["region"].lower():
        current_pos = [2,2]
        diccionarios.dades[2]["current_map"] = "main_dict_necluda"
    elif "castle" in diccionarios.player_dict["region"].lower():
        current_pos = [9,4]
        diccionarios.dades[2]["current_map"] = "main_dict_castle"



#por primera vez y dependiendo del mapa,ubicamos al jugador en su mapa
player_change_pos()






while flag_0:

    while flag_01:
        #INICIO DE ACCION


        #verificamos si hay arboles muertos
        for key, value in getattr(diccionarios,diccionarios.dades[2]["current_map"]).items():
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
        matriz = addbottomline_update_map(matriz)
        matriz = mapas.agregar_inventario(matriz,current_inventory)
        #fix, agregamos en cada iteracion al jugador en el mapa
        matriz[current_pos[0]][current_pos[1]] = ["X"]
        mapas.actualizar_mapa(matriz)








        # comprobamos blood moon
        # primero restamos blood moon countdown
        diccionarios.player_dict["blood_moon_countdown"] -= 1
        if diccionarios.player_dict["blood_moon_countdown"] == 0:
            diccionarios.player_dict["blood_moon_countdown"] = 25
            diccionarios.player_dict["blood_moon_appearances"] += 1
            eventos.historialPrompt(prompt, "The Blood moon rises once again. Please be careful, Link.")
            #se añaden los enemigos al mapa
            for key, value in getattr(diccionarios,diccionarios.dades[2]["current_map"]).items():
                # Verificar si la clave 3 existe y es un diccionario
                if 4 in value:
                    # Iterar sobre todas las claves en el diccionario interno
                    for sub_key, sub_value in value[4].items():
                        #revivimos a todos los enemigos con 4 corazones
                        sub_value[2]["isdead"] = False
                        sub_value[2]["current_hearts"] = 4





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

        if "cheat" in command.lower():
            if "rename player to" in command.lower():
                if command[command.find("to "):].replace(" ", "").isalnum() and 3 <= len(
                        command[command.find("to "):].replace(" ", "")) <= 10:
                    if diccionarios.player_dict["game_id"] == game_id:
                        diccionarios.player_dict["user_name"] = command[command.find("to "):].title()
            elif "add vegetable" in command.lower():
                diccionarios.player_dict.get("food_inventory")[0].get(1)["quantity"] += 1
            elif "add fish" in command.lower():
                diccionarios.player_dict.get("food_inventory")[0].get(2)["quantity"] += 1
            elif "add meat" in command.lower():
                diccionarios.player_dict.get("food_inventory")[0].get(3)["quantity"] += 1
            elif "add cook salad" in command.lower():
                # comprobamos si hay vegetables(apple)
                if diccionarios.player_dict["food_inventory"][0][1]["quantity"] >= 2:
                    # restamos ingredientes de diccionario
                    diccionarios.player_dict["food_inventory"][0][1]["quantity"] -= 2
                    # cocinamos ensalada
                    eventos.historialPrompt(prompt, "Salad cooked!")
                    diccionarios.player_dict["food_inventory"][3][4]["quantity"] += 1
                else:
                    # si no hay ingredientes suficientes se añade al prompt un mensaje

                    if not diccionarios.player_dict["food_inventory"].count(6) == 1:
                        eventos.historialPrompt(prompt, "Not enough Vegetable!")
                diccionarios.player_dict.get("food_inventory")[0].get(1)["quantity"] += 1
            elif "add cook pescatarian" in command.lower():
                # comprobamos si hay vegetables(apple) y fish
                if diccionarios.player_dict["food_inventory"][0][1]["quantity"] >= 1 and \
                        diccionarios.player_dict["food_inventory"][1][2]["quantity"] >= 1:
                    # restamos ingredientes de diccionario
                    diccionarios.player_dict["food_inventory"][0][1]["quantity"] -= 1
                    diccionarios.player_dict["food_inventory"][1][2]["quantity"] -= 1

                    # cocinamos pescatarian
                    eventos.historialPrompt(prompt, "Pescatarian cooked!")
                    diccionarios.player_dict["food_inventory"][4][5]["quantity"] += 1
                else:
                    # si no hay ingredientes suficientes se añade al prompt un mensaje

                    if not diccionarios.player_dict["food_inventory"][0][1]["quantity"] >= 1 and not \
                    diccionarios.player_dict["food_inventory"][1][2]["quantity"] >= 1:
                        eventos.historialPrompt(prompt, "Not enough Vegetable and fish!")
                    else:
                        if not diccionarios.player_dict["food_inventory"][1][2]["quantity"] >= 1:
                            eventos.historialPrompt(prompt, "Not enough Fish!")

                        if not diccionarios.player_dict["food_inventory"][0][1]["quantity"] >= 1:
                            eventos.historialPrompt(prompt, "Not enough Vegetable!")
            elif "add cook roasted" in command.lower():
                if diccionarios.player_dict["food_inventory"][0][1]["quantity"] >= 1 and \
                        diccionarios.player_dict["food_inventory"][2][3]["quantity"] >= 1:
                    # restamos ingredientes de diccionario
                    diccionarios.player_dict["food_inventory"][0][1]["quantity"] -= 1
                    diccionarios.player_dict["food_inventory"][2][3]["quantity"] -= 1

                    # cocinamos pescatarian
                    eventos.historialPrompt(prompt, "Roasted cooked!")
                    diccionarios.player_dict["food_inventory"][5][6]["quantity"] += 1
                else:
                    # si no hay ingredientes suficientes se añade al prompt un mensaje

                    if not diccionarios.player_dict["food_inventory"][0][1]["quantity"] >= 1 and not \
                    diccionarios.player_dict["food_inventory"][2][3]["quantity"] >= 1:
                        eventos.historialPrompt(prompt, "Not enough Vegetable and Meat!")
                    else:
                        if not diccionarios.player_dict["food_inventory"][2][3]["quantity"] >= 1:
                            eventos.historialPrompt(prompt, "Not enough Meat!")

                        if not diccionarios.player_dict["food_inventory"][0][1]["quantity"] >= 1:
                            eventos.historialPrompt(prompt, "Not enough Vegetable!")
            elif "add wood sword" in command.lower():
                eventos.historialPrompt(prompt, "You got a Wood Sword")
                diccionarios.player_dict["weapons_inventory"][0][1]["quantity"] += 1
            elif "add wood shield" in command.lower():
                eventos.historialPrompt(prompt, "You got a Wood Shield")
                # AQUI SE GUARDA EL ESCUDO (Ids en diccionarios.py)
                diccionarios.player_dict["shields_inventory"][0][1]["quantity"] += 1
            elif "add sword" in command.lower():
                eventos.historialPrompt(prompt, "You Got a Sword!")
                # AGREGAR SWORD A PLAYER
                diccionarios.player_dict["weapons_inventory"][1][2]["quantity"] += 1
            elif "add shield" in command.lower():
                eventos.historialPrompt(prompt, "You Got a Sword!")
                # AGREGAR SHIELD A PLAYER
                diccionarios.player_dict["shields_inventory"][1][2]["quantity"] += 1
            elif "open sanctuaries":
                diccionarios_mapa = {
                    "Hyrule": diccionarios.main_dict_hyrule,
                    "Death mountain": diccionarios.main_dict_death_mountain,
                    "Gerudo": diccionarios.main_dict_gerudo,
                    "Necluda": diccionarios.main_dict_necluda
                }

                for region_name, diccionario in diccionarios_mapa.items():
                    for mapa in diccionario.values():
                        for value in mapa.values():
                            for subsubkey, subsubvalue in value.items():
                                if "sanctuary_" in subsubkey and not subsubvalue[3].get("isopen", False):
                                    subsubvalue[3]["isopen"] = True
                                    #guardamos region antigua
                                    old_region = diccionarios.player_dict["region"]
                                    #guardamos region en diccionario
                                    diccionarios.player_dict["region"] = region_name
                                    #guardamos partida con la nueva region
                                    bbdd_changes.guardar_datos_partida(game_id, diccionarios.player_dict["region"])
                                    diccionarios.player_dict["region"] = old_region


                # AGREGAR VIDA AL JUGADOR
                diccionarios.player_dict["hearts_max"] = 9
                diccionarios.player_dict["hearts"] = 9

            elif "game over":
                flag_02 = True
                flag_01 = False
            elif "win game":
                flag_04 = True
                flag_01 = False

            else:
                eventos.historialPrompt(prompt, "That cheat don't exist")


        elif "go left" in command:
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
            eventos.historialPrompt(prompt, str(new_pos))
            y,x = new_pos[0],new_pos[1]

        elif "go by chest" in command:
            new_pos = eventos.move_to_X(matriz, current_pos,["M"])
            y,x = new_pos[0],new_pos[1]

        elif "go by bowl" in command:
            new_pos = eventos.move_to_X(matriz, current_pos,["C"])
            y,x = new_pos[0],new_pos[1]

        elif "show inventory main" in command:
            current_inventory = inventario.player_inventory_main

        elif "show inventory weapons" in command:
            current_inventory = inventario.player_inventory_weapons
        elif "exit" in command:
            flag_00 = True
            flag_01 = False

        elif "show map" in command:
            eventos.historialPrompt(prompt, "show map")
            prompt_add = mapas.mostrarMapa(current_inventory)
            eventos.historialPrompt(prompt, prompt_add)

        elif "back" in command and  "necluda" in last_map:
            diccionarios.dades[2]["current_map"] = "main_dict_necluda"
            matriz = mapas.change_map()
            matriz = mapas.update_map_pre_start(matriz)
            current_pos = [2, 2]
            continue

        elif "show inventory food" in command:
            current_inventory = inventario.player_inventory_food
        elif "hyrule" in diccionarios.dades[2]["current_map"]:
            if "go to gerudo" in command:
                bbdd_changes.guardar_datos_partida(game_id, diccionarios.player_dict["region"])
                diccionarios.dades[2]["current_map"] = "main_dict_gerudo"
                diccionarios.player_dict["region"] = "Gerudo"
                bbdd_changes.guardar_datos_partida(game_id, diccionarios.player_dict["region"])
                matriz = mapas.change_map()
                matriz = mapas.update_map_pre_start(matriz)
                current_pos = [9,2]
                continue
            if "go to death mountain" in command:
                bbdd_changes.guardar_datos_partida(game_id, diccionarios.player_dict["region"])
                diccionarios.player_dict["region"] = "Death mountain"
                diccionarios.dades[2]["current_map"] = "main_dict_death_mountain"
                bbdd_changes.guardar_datos_partida(game_id, diccionarios.player_dict["region"])
                matriz = mapas.change_map()
                matriz = mapas.update_map_pre_start(matriz)
                current_pos = [9,2]
                continue
            if "go to castle" in command:
                bbdd_changes.guardar_datos_partida(game_id, diccionarios.player_dict["region"])
                current_pos = [9, 4]
                last_map = diccionarios.dades[2]["current_map"]
                diccionarios.player_dict["region"] = "Castle"
                diccionarios.dades[2]["current_map"] = "main_dict_castle"
                matriz = mapas.change_map()
                bbdd_changes.guardar_datos_partida(game_id, diccionarios.player_dict["region"])
                flag_03 = True
                flag_01 = False
                continue

        elif "death" in diccionarios.dades[2]["current_map"]:
            if "go to necluda" in command:
                diccionarios.dades[2]["current_map"] = "main_dict_necluda"
                bbdd_changes.guardar_datos_partida(game_id, diccionarios.player_dict["region"])
                diccionarios.player_dict["region"] = "Necluda"
                matriz = mapas.change_map()
                matriz = mapas.update_map_pre_start(matriz)
                current_pos = [2,2]
                bbdd_changes.guardar_datos_partida(game_id, diccionarios.player_dict["region"])
                continue
            if "go to hyrule" in command:
                bbdd_changes.guardar_datos_partida(game_id, diccionarios.player_dict["region"])
                diccionarios.dades[2]["current_map"] = "main_dict_hyrule"
                diccionarios.player_dict["region"] = "Hyrule"
                bbdd_changes.guardar_datos_partida(game_id, diccionarios.player_dict["region"])
                matriz = mapas.change_map()
                matriz = mapas.update_map_pre_start(matriz)
                current_pos = [8,10]
                continue
            if "go to castle" in command:
                current_pos = [9, 4]
                last_map = diccionarios.dades[2]["current_map"]
                bbdd_changes.guardar_datos_partida(game_id, diccionarios.player_dict["region"])
                diccionarios.player_dict["region"] = "Castle"
                diccionarios.dades[2]["current_map"] = "main_dict_castle"
                matriz = mapas.change_map()
                bbdd_changes.guardar_datos_partida(game_id, diccionarios.player_dict["region"])
                flag_03 = True
                flag_01 = False
                continue
        elif "gerudo" in diccionarios.dades[2]["current_map"]:
            if "go to necluda" in command:
                diccionarios.dades[2]["current_map"] = "main_dict_necluda"
                bbdd_changes.guardar_datos_partida(game_id, diccionarios.player_dict["region"])
                diccionarios.player_dict["region"] = "Necluda"
                matriz = mapas.change_map()
                matriz = mapas.update_map_pre_start(matriz)
                current_pos = [2,2]
                bbdd_changes.guardar_datos_partida(game_id, diccionarios.player_dict["region"])
                continue
            if "go to hyrule" in command:
                diccionarios.dades[2]["current_map"] = "main_dict_hyrule"
                bbdd_changes.guardar_datos_partida(game_id, diccionarios.player_dict["region"])
                diccionarios.player_dict["region"] = "Hyrule"
                matriz = mapas.change_map()
                matriz = mapas.update_map_pre_start(matriz)
                current_pos = [8,10]
                bbdd_changes.guardar_datos_partida(game_id, diccionarios.player_dict["region"])
                continue
            if "go to castle" in command:
                current_pos = [9, 4]
                last_map = diccionarios.dades[2]["current_map"]
                bbdd_changes.guardar_datos_partida(game_id, diccionarios.player_dict["region"])
                diccionarios.player_dict["region"] = "Castle"
                diccionarios.dades[2]["current_map"] = "main_dict_castle"
                matriz = mapas.change_map()
                bbdd_changes.guardar_datos_partida(game_id, diccionarios.player_dict["region"])
                flag_03 = True
                flag_01 = False
                continue
        elif "necluda" in diccionarios.dades[2]["current_map"]:
            if "go to death mountain" in command:
                diccionarios.dades[2]["current_map"] = "main_dict_death_mountain"
                bbdd_changes.guardar_datos_partida(game_id, diccionarios.player_dict["region"])
                diccionarios.player_dict["region"] = "Death mountain"
                matriz = mapas.change_map()
                matriz = mapas.update_map_pre_start(matriz)
                current_pos = [9,2]
                bbdd_changes.guardar_datos_partida(game_id, diccionarios.player_dict["region"])
                continue
            if "go to gerudo" in command:
                diccionarios.dades[2]["current_map"] = "main_dict_gerudo"
                bbdd_changes.guardar_datos_partida(game_id, diccionarios.player_dict["region"])
                diccionarios.player_dict["region"] = "Gerudo"
                matriz = mapas.change_map()
                matriz = mapas.update_map_pre_start(matriz)
                current_pos = [9,2]
                bbdd_changes.guardar_datos_partida(game_id, diccionarios.player_dict["region"])
                continue
            if "go to castle" in command:
                current_pos = [9, 4]
                last_map = diccionarios.dades[2]["current_map"]
                bbdd_changes.guardar_datos_partida(game_id, diccionarios.player_dict["region"])
                diccionarios.player_dict["region"] = "Castle"
                diccionarios.dades[2]["current_map"] = "main_dict_castle"
                matriz = mapas.change_map()
                bbdd_changes.guardar_datos_partida(game_id, diccionarios.player_dict["region"])
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

        eventos.interactable_events(matriz,current_pos,prompt,command,getattr(diccionarios,diccionarios.dades[2]["current_map"]))


        #COMPROBAMOS LA VIDA DEL JUGADOR:
        if diccionarios.player_dict["hearts"] <= 0:
            eventos.historialPrompt(prompt, "You are dead!")
            # AQUI INVOCAMOS PANTALLA DE MUERTE
            flag_02 = True
            flag_01 = False










    while flag_03: # GANON

        # INICIO DE ACCION

        # verificamos si hay arboles muertos
        for key, value in getattr(diccionarios, diccionarios.dades[2]["current_map"]).items():
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


        # Variable que almacena el nombre del mapa actual, usando el nombre de diccionario como referencia
        LimpiarPantalla()
        matriz = addbottomline_update_map(matriz)
        matriz = mapas.agregar_inventario(matriz, current_inventory)
        # fix, agregamos en cada iteracion al jugador en el mapa
        matriz[current_pos[0]][current_pos[1]] = ["X"]
        mapas.actualizar_mapa(matriz)



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




        if "cheat" in command.lower():
            if "rename player to" in command.lower():
                if command[command.find("to "):].replace(" ", "").isalnum() and 3 <= len(
                        command[command.find("to "):].replace(" ", "")) <= 10:
                    if diccionarios.player_dict["game_id"] == game_id:
                        diccionarios.player_dict["user_name"] = command[command.find("to "):].title()
            elif "add vegetable" in command.lower():
                diccionarios.player_dict.get("food_inventory")[0].get(1)["quantity"] += 1
            elif "add fish" in command.lower():
                diccionarios.player_dict.get("food_inventory")[0].get(2)["quantity"] += 1
            elif "add meat" in command.lower():
                diccionarios.player_dict.get("food_inventory")[0].get(3)["quantity"] += 1
            elif "add cook salad" in command.lower():
                # comprobamos si hay vegetables(apple)
                if diccionarios.player_dict["food_inventory"][0][1]["quantity"] >= 2:
                    # restamos ingredientes de diccionario
                    diccionarios.player_dict["food_inventory"][0][1]["quantity"] -= 2
                    # cocinamos ensalada
                    eventos.historialPrompt(prompt, "Salad cooked!")
                    diccionarios.player_dict["food_inventory"][3][4]["quantity"] += 1
                else:
                    # si no hay ingredientes suficientes se añade al prompt un mensaje

                    if not diccionarios.player_dict["food_inventory"].count(6) == 1:
                        eventos.historialPrompt(prompt, "Not enough Vegetable!")
                diccionarios.player_dict.get("food_inventory")[0].get(1)["quantity"] += 1
            elif "add cook pescatarian" in command.lower():
                # comprobamos si hay vegetables(apple) y fish
                if diccionarios.player_dict["food_inventory"][0][1]["quantity"] >= 1 and \
                        diccionarios.player_dict["food_inventory"][1][2]["quantity"] >= 1:
                    # restamos ingredientes de diccionario
                    diccionarios.player_dict["food_inventory"][0][1]["quantity"] -= 1
                    diccionarios.player_dict["food_inventory"][1][2]["quantity"] -= 1

                    # cocinamos pescatarian
                    eventos.historialPrompt(prompt, "Pescatarian cooked!")
                    diccionarios.player_dict["food_inventory"][4][5]["quantity"] += 1
                else:
                    # si no hay ingredientes suficientes se añade al prompt un mensaje

                    if not diccionarios.player_dict["food_inventory"][0][1]["quantity"] >= 1 and not \
                    diccionarios.player_dict["food_inventory"][1][2]["quantity"] >= 1:
                        eventos.historialPrompt(prompt, "Not enough Vegetable and fish!")
                    else:
                        if not diccionarios.player_dict["food_inventory"][1][2]["quantity"] >= 1:
                            eventos.historialPrompt(prompt, "Not enough Fish!")

                        if not diccionarios.player_dict["food_inventory"][0][1]["quantity"] >= 1:
                            eventos.historialPrompt(prompt, "Not enough Vegetable!")
            elif "add cook roasted" in command.lower():
                if diccionarios.player_dict["food_inventory"][0][1]["quantity"] >= 1 and \
                        diccionarios.player_dict["food_inventory"][2][3]["quantity"] >= 1:
                    # restamos ingredientes de diccionario
                    diccionarios.player_dict["food_inventory"][0][1]["quantity"] -= 1
                    diccionarios.player_dict["food_inventory"][2][3]["quantity"] -= 1

                    # cocinamos pescatarian
                    eventos.historialPrompt(prompt, "Roasted cooked!")
                    diccionarios.player_dict["food_inventory"][5][6]["quantity"] += 1
                else:
                    # si no hay ingredientes suficientes se añade al prompt un mensaje

                    if not diccionarios.player_dict["food_inventory"][0][1]["quantity"] >= 1 and not \
                    diccionarios.player_dict["food_inventory"][2][3]["quantity"] >= 1:
                        eventos.historialPrompt(prompt, "Not enough Vegetable and Meat!")
                    else:
                        if not diccionarios.player_dict["food_inventory"][2][3]["quantity"] >= 1:
                            eventos.historialPrompt(prompt, "Not enough Meat!")

                        if not diccionarios.player_dict["food_inventory"][0][1]["quantity"] >= 1:
                            eventos.historialPrompt(prompt, "Not enough Vegetable!")
            elif "add wood sword" in command.lower():
                eventos.historialPrompt(prompt, "You got a Wood Sword")
                diccionarios.player_dict["weapons_inventory"][0][1]["quantity"] += 1
            elif "add wood shield" in command.lower():
                eventos.historialPrompt(prompt, "You got a Wood Shield")
                # AQUI SE GUARDA EL ESCUDO (Ids en diccionarios.py)
                diccionarios.player_dict["shields_inventory"][0][1]["quantity"] += 1
            elif "add sword" in command.lower():
                eventos.historialPrompt(prompt, "You Got a Sword!")
                # AGREGAR SWORD A PLAYER
                diccionarios.player_dict["weapons_inventory"][1][2]["quantity"] += 1
            elif "add shield" in command.lower():
                eventos.historialPrompt(prompt, "You Got a Sword!")
                # AGREGAR SHIELD A PLAYER
                diccionarios.player_dict["shields_inventory"][1][2]["quantity"] += 1
            elif "open sanctuaries":
                diccionarios_mapa = [diccionarios.main_dict_hyrule, diccionarios.main_dict_death_mountain,
                                     diccionarios.main_dict_gerudo, diccionarios.main_dict_necluda]
                for i in range(4):
                    diccionario = bbdd_changes.region_selector(diccionarios_mapa[i])
                    records_with_key_3 = {key: value for key, value in diccionario.items() if 3 in value}
                    for key1, value1 in records_with_key_3.items():
                        for key2, value2 in value1.items():
                            sanctuary_id = list(value2.keys())[0]
                            is_open = value2[sanctuary_id][3]['isopen']
            elif "game over":
                flag_02 = True
                flag_01 = False
            elif "win game":
                flag_04 = True
                flag_01 = False

            else:
                eventos.historialPrompt(prompt, "That cheat don't exist")


        elif "go left" in command:
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
            new_pos = [9,4]
            y, x = new_pos[0], new_pos[1]

        elif "show inventory main" in command:
            current_inventory = inventario.player_inventory_main

        elif "show inventory weapons" in command:
            current_inventory = inventario.player_inventory_weapons

        elif "exit" in command:
            flag_00 = True
            flag_01 = False

        elif "show inventory food" in command:
            current_inventory = inventario.player_inventory_food
        elif "show map" in command:
            eventos.historialPrompt(prompt, "show map")
            prompt_add = mapas.mostrarMapa(current_inventory)
            eventos.historialPrompt(prompt, prompt_add)

        elif "back" in command and  "necluda" in last_map:
            diccionarios.dades[2]["current_map"] = "main_dict_necluda"
            matriz = mapas.change_map()
            matriz = mapas.update_map_pre_start(matriz)
            current_pos = [2, 2]
            flag_01 = True
            flag_03 = False
        elif "back" in command and "hyrule" in last_map:
            diccionarios.dades[2]["current_map"] = "main_dict_hyrule"
            matriz = mapas.change_map()
            matriz = mapas.update_map_pre_start(matriz)
            current_pos = [8, 10]
            flag_01 = True
            flag_03 = False
        elif "back" in command and "death" in last_map:
            diccionarios.dades[2]["current_map"] = "main_dict_death_mountain"
            matriz = mapas.change_map()
            matriz = mapas.update_map_pre_start(matriz)
            current_pos = [9, 2]
            flag_01 = True
            flag_03 = False
        elif "back" in command and "gerudo" in last_map:
            diccionarios.dades[2]["current_map"] = "main_dict_gerudo"
            matriz = mapas.change_map()
            matriz = mapas.update_map_pre_start(matriz)
            current_pos = [9, 2]
            flag_01 = True
            flag_03 = False


        elif current_pos[0] == 9 and current_pos[1] == 20:
            if command.lower() == "attack":
                #si tenemos un arma equipada, podremos atacar
                if diccionarios.player_dict['weapons_equipped'][0][1]["weapon_name"] != "" :
                    if diccionarios.main_dict_castle[2][11]["ganon_hearts"] >= 0:
                        #si atacamos, quitaremos un corazon a ganon
                        diccionarios.main_dict_castle[2][11]["ganon_hearts"] -= 1
                        for i in range(len(matriz)):
                            for j in range(len(matriz[i])):
                                if matriz[i][j] == ['♥']:
                                    matriz[i][j] = [' ']
                                    break

                        if diccionarios.main_dict_castle[2][11]["ganon_hearts"] <= 0:
                            diccionarios.main_dict_castle[2][11]["isdead"] = True
                            flag_04 = True
                            flag_03 = False

                        #bajamos tambien los corazones del jugador
                        diccionarios.player_dict["hearts"] -= 1

                #si no tienes arma equipada, sale el siguiente mensaje
                else:
                    eventos.historialPrompt(prompt, "You have no weapon equipped!")

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

        eventos.interactable_events(matriz, current_pos, prompt, command, getattr(diccionarios, diccionarios.dades[2]["current_map"]))
        # COMPROBAMOS LA VIDA DEL JUGADOR:
        if diccionarios.player_dict["hearts"] <= 0:
            eventos.historialPrompt(prompt, "You are dead!")
            # AQUI INVOCAMOS PANTALLA DE MUERTE
            flag_02 = True
            flag_03 = False


    while flag_02:  # pantalla de muerte
                LimpiarPantalla()
                funciones.dialogos.generador_menus(funciones.dialogos.death_top, funciones.dialogos.death_end,funciones.dialogos.death_content)
                for i in prompt:
                    print(i)
                prompt = input("Type 'Continue' to continue: ").capitalize()
                if prompt != "Continue":
                    eventos.historialPrompt(prompt, "Invalid action")
                else:
                    LimpiarPantalla()
                    flag_02=False
                    flag_00=True



    while flag_04:#pantalla de win
        LimpiarPantalla()
        funciones.dialogos.generador_menus(funciones.dialogos.zelda_saved_top, funciones.dialogos.zelda_saved_end, funciones.dialogos.zelda_saved_content)
        prompt = input("Give an Order:")
        if prompt == "continue":
            flag_00 = True
            flag04 = False

    while flag_00:
        game_id, region = prepartida.PantallaPrincipal()
        diccionarios.player_dict["game_id"] = game_id
        diccionarios.dades["current_map"] = str(bbdd_changes.region_selector(region))
        if not (game_id and region):
            print("Come back soon...")
            flag_00 = False
            flag_0 = False
        else:
            LimpiarPantalla()
            bbdd_changes.download_data_mysql(game_id)
            bbdd_changes.load_all_data(game_id)
            player_change_pos()
            matriz = mapas.update_map_pre_start(mapas.change_map())
            eventos.historialPrompt(prompt,str(diccionarios.player_dict["region"]))
            if "castle" in diccionarios.dades[2]["current_map"]:
                flag_00 = False
                flag_03 = True
            else:
                flag_00 = False
                flag_01 = True








