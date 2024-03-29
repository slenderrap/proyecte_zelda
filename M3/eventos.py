import diccionarios
import random
import bbdd_changes







def move_to_X(matriz, current_position, casilla):
    x, y = current_position
    target_positions = []

    # Buscar la posición de la casilla con "T"
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == casilla:
                target_positions.append((i, j))

    # Verificar si se encontró una posición con "T"
    if target_positions:
        # Buscar la posición vacía más cercana
        min_distance = float('inf')
        closest_empty_position = (x, y)

        for target_position in target_positions:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    new_x, new_y = target_position[0] + i, target_position[1] + j
                    if (
                        0 <= new_x < len(matriz)
                        and 0 <= new_y < len(matriz[new_x])
                        and matriz[new_x][new_y] == [" "]
                    ):
                        distance = abs(new_x - x) + abs(new_y - y)
                        if distance < min_distance:
                            min_distance = distance
                            closest_empty_position = (new_x, new_y)

        return closest_empty_position

    else:
        return (x, y)



#Variable movimiento npcs
def move_enemy(current_pos, matriz, main_dict, object_id, npc_id, npc_name):
    current_positions = main_dict[object_id][npc_id][npc_name][:2]

    # Derecha = 1
    # Izquierda = 2
    # Arriba = 3
    # Abajo = 4

    #ponemos las posibles direcciones en una lista

    directions = ["derecha","arriba","abajo","izquierda"]

    #mezclamos la lista
    random.shuffle(directions)
    new_positions = current_pos.copy()


    for direction in directions:
        positions_occupied = False
        temp_old_pos = [[current_positions[0][0], current_positions[0][1] + 2],
                        [current_positions[1][0], current_positions[1][1] + 2]].copy()

        # Calcula las nuevas coordenadas según la dirección
        if direction == "arriba":
            new_positions[0][0] -= 1
            new_positions[1][0] -= 1
            temp_old_pos = [[new_positions[0][0] + 1, new_positions[0][1]],
                            [new_positions[1][0] + 1, new_positions[1][1]]]

        elif direction == "abajo":
            new_positions[0][0] += 1
            new_positions[1][0] += 1
            temp_old_pos = [[new_positions[0][0] - 1, new_positions[0][1]],
                            [new_positions[1][0] - 1, new_positions[1][1]]]

        elif direction == "izquierda":
            new_positions[0][1] -= 1
            new_positions[1][1] -= 1

            temp_old_pos = [[new_positions[0][0], new_positions[0][1] + 1],
                            [new_positions[1][0], new_positions[1][1] + 1]]

        elif direction == "derecha":
            new_positions[0][1] += 1
            new_positions[1][1] += 1


            temp_old_pos = [[new_positions[0][0], new_positions[0][1] - 1],
                            [new_positions[1][0], new_positions[1][1] - 1]]

        new_positions = [new_positions[0], new_positions[1]]



        # Verifica si alguna de las nuevas posiciones está ocupada
        for pos in new_positions:
            if matriz[pos[0]][pos[1]] not in ([" "], ["E"], ["1"], ["2"], ["3"], ["4"], ["5"], ["6"], ["7"], ["8"], ["9"]):
                current_pos[0],current_pos[1] = temp_old_pos[0],temp_old_pos[1]
                positions_occupied = True
                break
        #current_pos[0][0],current_pos[0][1],current_pos[1][0],current_pos[1][1], = old_pos[0][0],old_pos[0][1],old_pos[1][0],old_pos[1][1]

        # Si no hay posiciones ocupadas, actualiza las coordenadas y sale del bucle
        if not positions_occupied:

            # Borramos las posiciones anteriores
            matriz[temp_old_pos[0][0]][temp_old_pos[0][1]] = [" "]
            matriz[temp_old_pos[1][0]][temp_old_pos[1][1]] = [" "]

            current_pos[0] = current_positions[0]
            current_pos[1] = current_positions[1]
            return




#VARIABLE PROMPT HISTORIAL
def historialPrompt(prompt,NewLine):
    if "\n" in NewLine:
        NewLine.index("\n")
        NewLine += "\n"
        for i in range(NewLine.count("\n")):
            if i==0:
                inicio=0
                final = NewLine.index("\n")
            else:
                inicio = final + 1
                final = NewLine.find("\n",inicio)
            if len(prompt) == 8:
                prompt[0], prompt[1], prompt[2], prompt[3], prompt[4], prompt[5], prompt[6], prompt[7] = \
                    prompt[1], prompt[2], prompt[3], prompt[4], prompt[5], prompt[6], prompt[7], NewLine[inicio:final].capitalize()
            else:
                prompt.append(NewLine[inicio:final].capitalize())
    else:
        if len(prompt) == 8:
            prompt[0], prompt[1], prompt[2], prompt[3], prompt[4], prompt[5], prompt[6], prompt[7] = \
                prompt[1], prompt[2], prompt[3], prompt[4], prompt[5], prompt[6], prompt[7], NewLine.capitalize()
        else:
            prompt.append(NewLine.capitalize())









def interactable_events(matriz,current_pos,prompt,command,diccionario_mapa):

    #Variable para checkear cofres
    def check_cofre(diccionario, x, y):
        # Comprobamos en el diccionario si el cofre está abierto
        for key, value in diccionario.items():
            # Verificar si la clave 2 existe y es un diccionario
            if 2 in value and type(value[2]) is dict:
                # Iterar sobre todas las claves en el diccionario interno
                for sub_key, sub_value in value[2].items():
                    # Verificar si la clave es un cofre y está abierto
                    if sub_key.startswith("chest_") and "isopen" in sub_value[2]:
                        # Comprobamos si el jugador está cerca del cofre
                        if x == sub_value[1][0] and y == sub_value[1][1]:
                            if sub_value[2]["isopen"]:

                                historialPrompt(prompt,f"{sub_key} is already open." )
                                return True
                            else:
                                if sub_value[0] == 1:

                                    historialPrompt(prompt, "You Got a Sword!")

                                    # AGREGAR SWORD A PLAYER
                                    diccionarios.player_dict["weapons_inventory"][1][2]["quantity"] += 1

                                elif sub_value[0] == 2:
                                    historialPrompt(prompt, "You Got a Shield!")
                                    # AGREGAR SHIELD A PLAYER
                                    diccionarios.player_dict["shields_inventory"][1][2]["quantity"] += 1
                                matriz[x][y][0] = "W"
                                sub_value[2]["isopen"] = True
                                #cuando se abra el cofre, se guarda en la base de datos

                                return True

    def sanctuary_event(diccionario, x, y, matriz, prompt):
        # Comprobamos en el diccionario si el santuario está abierto
        for key, value in diccionario.items():
            # Verificar si la clave 3 existe y es un diccionario
            if 3 in value:
                # Iterar sobre todas las claves en el diccionario interno
                for sub_key, sub_value in value[3].items():
                    # Verificar si la clave es un santuario y está abierto
                    if sub_key.startswith("sanctuary_") and "isopen" in sub_value[3]:
                        # Comprobamos si el jugador está cerca del cofre
                        if (x == sub_value[0][0] and y == sub_value[0][1]) or (
                                x == sub_value[1][0] and y == sub_value[1][1]) or (
                                x == sub_value[2][0] and y == sub_value[2][1]):
                            if sub_value[3]["isopen"]:

                                historialPrompt(prompt, f"{sub_key} is already open.")

                                return True
                            else:

                                historialPrompt(prompt, "You opened the sanctuary, your maximum health has increased by 1")

                                # AGREGAR VIDA AL JUGADOR
                                diccionarios.player_dict["hearts_max"] += 1
                                diccionarios.player_dict["hearts"] = diccionarios.player_dict["hearts_max"]




                                #Borramos el interrogante del mapa
                                if matriz[x][y][0] == "S":
                                    matriz[x][y+2][0] = " "
                                elif str(matriz[x][y][0]).isdigit():
                                    matriz[x][y + 1][0] = " "
                                else:
                                    matriz[x][y][0] = " "

                                sub_value[3]["isopen"] = True
                                #cuando se abra el santuario, se guarda en la base de datos

                                bbdd_changes.guardar_datos_partida(diccionarios.player_dict["game_id"], diccionarios.player_dict["region"])
                                return True


    def enemy_event(diccionario, x, y, matriz, prompt):
        # Comprobamos en el diccionario si el santuario está abierto
        for key, value in diccionario.items():
            # Verificar si la clave 3 existe y es un diccionario
            if 4 in value:
                # Iterar sobre todas las claves en el diccionario interno
                for sub_key, sub_value in value[4].items():
                    # Verificar si la clave es un santuario y está abierto
                    if sub_key.startswith("enemy_") and "isdead" in sub_value[2]:
                        # Comprobamos si el jugador está cerca del enemigo
                        if (x == sub_value[0][0] and y == sub_value[0][1]) or (
                                x == sub_value[1][0] and y == sub_value[1][1]):
                            if diccionarios.player_dict["weapons_equipped"][0][1]["weapon_name"] != "":
                                if sub_value[2]["isdead"]:
                                    historialPrompt(prompt, "Enemy killed!")

                                else:
                                    historialPrompt(prompt, "Brave, keep fighting Link")
                                    move_enemy(sub_value, matriz, getattr(diccionarios,diccionarios.dades[2]["current_map"]),int(key), 4, sub_key)



                                    #Restamos la vida del enemigo en el diccionario
                                    sub_value[2]["current_hearts"] -= 1
                                    #Restamos uno de uso al arma equipada

                                    # restar 1 a espada
                                    if diccionarios.player_dict['weapons_equipped'][0][1]['weapon_name'] == "Sword":
                                        diccionarios.player_dict["weapons_equipped"][0][1]["uses_left_sword"] -= 1
                                    elif diccionarios.player_dict['weapons_equipped'][0][1][
                                        'weapon_name'] == "Wood Sword":
                                        diccionarios.player_dict["weapons_equipped"][0][1]["uses_left_woodsword"] -= 1
                                    # eliminamos las armas si estas se quedan sin usos
                                    if diccionarios.player_dict["weapons_equipped"][0][1]["uses_left_woodsword"] <= 0:
                                        diccionarios.player_dict["weapons_inventory"][0][1]["quantity"] -= 1
                                    elif diccionarios.player_dict["weapons_equipped"][0][1]["uses_left_sword"] <= 0:
                                        diccionarios.player_dict["weapons_inventory"][1][2]["quantity"] -= 1



                                    #Si la vida del enemigo llega a 0, esta se elimina
                                    if matriz[sub_value[1][0]][sub_value[1][1]][0] == "0":
                                        matriz[sub_value[0][0]][sub_value[0][1]][0] = " "
                                        matriz[sub_value[1][0]][sub_value[1][1]][0] = " "

                                        historialPrompt(prompt, "Enemy dead")
                                        sub_value[3]["isdead"] = True


                            else:
                                historialPrompt(prompt, "You have no Sword!")

                                move_enemy(sub_value, matriz,getattr(diccionarios, diccionarios.dades[2]["current_map"]), int(key), 4,sub_key)

                            # el enemigo se movera despues de la interaccion, y atacara al jugador, si se tiene escudo, se restara 1 a escudos
                            if diccionarios.player_dict["weapons_equipped"][1][2]["shield_name"] == "Shield":
                                diccionarios.player_dict["weapons_equipped"][1][2]["uses_left_shield"] -= 1
                                historialPrompt(prompt, "-1 health to shield!")

                            elif diccionarios.player_dict["weapons_equipped"][1][2]["shield_name"] == "Wood_Shield":
                                diccionarios.player_dict["weapons_equipped"][1][2]["uses_left_woodshield"] -= 1
                                historialPrompt(prompt, "-1 health to woodshield!")

                            else:
                                diccionarios.player_dict["hearts"] -= 1
                                # restamos 1 de vida al jugador
                                historialPrompt(prompt,f"Be careful Link, you only have {diccionarios.player_dict['hearts']} hearts ")
                            return




    def tree_event(diccionario, x, y):
        # Comprobamos en el diccionario si el cofre está abierto
        for key, value in diccionario.items():
            if 1 in value:
                for sub_key, sub_value in value[1].items():
                    # Verificar si la clave es un arbol
                    if sub_key.startswith("tree_"):
                        # Comprobar si el jugador está cerca del arbol
                        if x == sub_value[1][0] and y == sub_value[1][1]:
                            #comprobamos si el arbol tiene vida
                            if sub_value[0] >= 1:

                                #comprobamos si el jugador tiene armas equipadas
                                historialPrompt(prompt, "Tree Attacked")

                                if diccionarios.player_dict["weapons_equipped"][0][1]["weapon_name"].isspace():
                                    #probabilidad manzana 20%
                                    if random.randint(1, 10) <= 4:
                                        historialPrompt(prompt, "Tree dropped an Apple")
                                        diccionarios.player_dict["food_inventory"][0][1]["quantity"] += 1
                                        #Aqui se guardaria la manzana
                                        bbdd_changes.guardar_datos_partida(diccionarios.player_dict["game_id"],
                                                                           diccionarios.player_dict["region"])

                                    #probabilidad que caigan objetos 10%
                                    if random.randint(1,10) == 10:
                                        if random.randint(1,2) == 1:
                                            historialPrompt(prompt, "You got a Wood Sword")
                                            diccionarios.player_dict["weapons_inventory"][0][1]["quantity"] += 1

                                        else:

                                            historialPrompt(prompt, "Wood Shield")
                                            #AQUI SE GUARDA EL ESCUDO (Ids en diccionarios.py)
                                            diccionarios.player_dict["shields_inventory"][0][1]["quantity"] += 1
                                        bbdd_changes.guardar_datos_partida(diccionarios.player_dict["game_id"],
                                                                           diccionarios.player_dict["region"])
                                    else:
                                        historialPrompt(prompt, "The tree didn't give you anything")
                                    return


                                else:
                                    # probabilidad manzana 40%
                                    if random.randint(1, 10) <= 4:
                                        historialPrompt(prompt, "Tree Attacked")
                                        # Aqui se guarda la manzana

                                        diccionarios.player_dict["food_inventory"][0][1]["quantity"] += 1



                                    # probabilidad manzana
                                    #probabilidad objeto 20%
                                    if random.randint(1, 5) == 5:

                                        historialPrompt(prompt, "Tree dropped a Wood Sword")


                                        # Aqui se guardarda el objeto
                                        diccionarios.player_dict["weapons_inventory"][0][1]["quantity"] += 1
                                        # probabilidad objeto 20%
                                    elif random.randint(1, 5) == 5:
                                        historialPrompt(prompt, "Tree dropped a Wood Shield")

                                        # Aqui se guardaria el objeto
                                        diccionarios.player_dict["shields_inventory"][0][1]["quantity"] += 1


                                    else:

                                        historialPrompt(prompt, "The tree didn't give you anything")

                                    #AQUI DESGASTAMOS LA ESPADA EN UN USO

                                    #restamos uno de vida al arbol
                                    sub_value[0] -= 1

                                    #si el arbol se queda sin vida, este se destruirá

                                    if sub_value[0] <= 0:
                                        matriz[x][y][0] = "9"
                                        historialPrompt(prompt, "Tree destroyed")
                                    return

                            else:
                                historialPrompt(prompt, "The Tree is not ready yet")


    def fox_event(diccionario, x, y):
        # Comprobamos en el diccionario si el cofre está abierto
        for key, value in diccionario.items():
            if 1 in value:
                for sub_key, sub_value in value[1].items():
                    # Verificar si la clave es un fox
                    if sub_key.startswith("fox_"):
                        # Comprobar si el jugador está cerca del arbol
                        if x == sub_value[1][0] and y == sub_value[1][1]:

                            # comprobamos si el jugador tiene armas equipadas

                            if not diccionarios.player_dict["weapons_equipped"][0][1]["weapon_name"].isspace():
                                historialPrompt(prompt, "Fox Attacked")
                                historialPrompt(prompt, "You got meat!")

                                # Aqui se guarda el objeto
                                diccionarios.player_dict["food_inventory"][2][3]["quantity"] += 1

                                # AQUI DESGASTAMOS EL/LAS ARMAS EQUIPADA EN UN USO
                                if diccionarios.player_dict['weapons_equipped'][0][1]['weapon_name'] == "Sword":
                                    diccionarios.player_dict["weapons_equipped"][0][1]["uses_left_sword"] -= 1
                                elif diccionarios.player_dict['weapons_equipped'][0][1]['weapon_name'] == "Wood Sword":
                                    diccionarios.player_dict["weapons_equipped"][0][1]["uses_left_woodsword"] -= 1
                                    # eliminamos las armas si estas se quedan sin usos
                                if diccionarios.player_dict["weapons_equipped"][0][1]["uses_left_woodsword"] <= 0:
                                    diccionarios.player_dict["weapons_inventory"][0][1]["quantity"] -= 1
                                elif diccionarios.player_dict["weapons_equipped"][0][1]["uses_left_sword"] <= 0:
                                    diccionarios.player_dict["weapons_inventory"][1][2]["quantity"] -= 1


                                # restamos uno de vida al fox
                                sub_value[0] -= 1

                                # si fox se queda sin vida, este desaparecerá

                                if sub_value[0] <= 0:
                                    matriz[x][y][0] = " "
                                    historialPrompt(prompt, "Fox killed")

                                return
                            else:
                                historialPrompt(prompt, "Fox not attacked, no weapon equipped")
                                return

    #FUNCION EAT
    def eat(food, player_dict):
        # Verificar si el comando es para comer y el tipo de comida es válido
        if food.lower() in ["vegetables", "salad", "pescatarian", "roasted", "meat",
                                                         "fish"]:
            food_name = food.lower().capitalize()  # Convertir la comida a formato de título (por ejemplo, "vegetables" a "Vegetables")

            # Buscar la comida en el inventario del jugador
            for item in player_dict['food_inventory']:
                print(player_dict['food_inventory'])
                if item.get(1, {}).get('food_name', '').lower() == food_name.lower():
                    # Verificar si hay suficiente cantidad de esa comida
                    if item[1]["quantity"] > 0:
                        # Restar 1 a la cantidad de esa comida
                        item[1]["quantity"] -= 1

                        # Aumentar los corazones según el tipo de comida
                        if food_name == "Vegetables":
                            player_dict['hearts'] += 1
                        elif food_name == "Salads":
                            player_dict['hearts'] += 2
                        elif food_name == "Pescatarian":
                            player_dict['hearts'] += 3
                        elif food_name == "Roasted":
                            player_dict['hearts'] += 4
                        elif food_name == "Meat":
                            player_dict['hearts'] += 1
                        elif food_name == "Fish":
                            player_dict['hearts'] += 1

                        # Aumentar el uso en el diccionario
                        item[1]["uses"] += 1

                        # Ponemos mensaje de confirmacion al comer
                        historialPrompt(prompt, f"You ate {food_name}!")

                        return player_dict

            # Mostrar mensaje si no se encontró la comida en el inventario
            historialPrompt(prompt, f"You don't have {food_name}!")
            return




    #Variable encargada de llamar a los distintos eventos
    def event_caller(matriz, current_pos, command, diccionario):
        x, y = current_pos
        current_tile = matriz[x][y][0]

        if current_tile == "X":
            for j in range(y - 1, y + 2):
                for i in range(x - 1, x + 2):
                    # Verificar si las coordenadas (i, j) están dentro de los límites del mapa
                    if 0 <= i < len(matriz) and 0 <= j < len(matriz[0]) and (i != x or j != y) and (i == x or j == y):
                        try:
                            # Dependiendo del caso, llamamos a las correspondientes funciones
                            # FUNCION COFRE
                            if matriz[i][j][0] in ("M", "W") and command.lower() == "open chest":
                                check_cofre(diccionario, i, j)
                                bbdd_changes.guardar_datos_partida(diccionarios.player_dict["game_id"], diccionarios.player_dict["region"])
                                return

                            # FUNCION ARBOL
                            if (matriz[i][j][0] == "T"  or matriz[i][j][0] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")) and command.lower() == "attack":
                                tree_event(diccionario, i, j)
                                bbdd_changes.guardar_datos_partida(diccionarios.player_dict["game_id"], diccionarios.player_dict["region"])
                                return


                            # FUNCION SANTUARIOS
                            if (matriz[i][j][0] == "S" or (matriz[i][j][0] == "S" and matriz[i][j+1][0]  in ("0","1","2","3","4","5","6","7","8","9")) or matriz[i][j][0] == "?") and command.lower() == "open sanctuary":
                                if sanctuary_event(diccionario, i, j, matriz, prompt):
                                    return

                            # FUNCION ENEMIGOS

                            #print(f"Coordenadas: {j} {i} Matriz de enemigos:{matriz[i][j][0]}")
                            if (matriz[i][j][0] == "E" or matriz[i][j][0] == "4" ) and command.lower() == "attack":
                                enemy_event(diccionario, i, j, matriz, prompt)
                                return

                            # FUNCION FOX
                            if matriz[i][j][0] == "F" and command.lower() == "attack":
                                fox_event(diccionario, i, j)
                                bbdd_changes.guardar_datos_partida(diccionarios.player_dict["game_id"], diccionarios.player_dict["region"])
                                return


                            # FUNCION EAT
                            if command.lower() == "eat vegetables":
                                eat("vegetables", diccionarios.player_dict)
                                return
                            elif command.lower() == "eat fish":
                                eat("fish", diccionarios.player_dict)
                                return
                            elif command.lower() == "eat meat":
                                eat("meat", diccionarios.player_dict)
                                return
                            elif command.lower() == "eat salad":
                                eat("salad", diccionarios.player_dict)
                                return
                            elif command.lower() == "eat pescatarian":
                                eat("pescatarian", diccionarios.player_dict)
                                return
                            elif command.lower() == "eat roasted":
                                eat("roasted", diccionarios.player_dict)
                                return


                            # FUNCION PESCAR
                            if matriz[i][j][0] == "~" and command.lower() == "fish":
                                #el 20% de las veces,si no se ha pescado ya antes se obtendra un pescado
                                if getattr(diccionarios,(diccionarios.dades[2]["current_map"]))[10][6]["already_fished"]:
                                    historialPrompt(prompt, "You have already fished in this area")
                                    return

                                else:

                                    if random.randint(1,5) == 1:
                                        historialPrompt(prompt, "You got a fish!")

                                        getattr(diccionarios, (diccionarios.dades[2]["current_map"]))[10][6]["already_fished"] = True
                                        diccionarios.player_dict["food_inventory"][0][1]["quantity"] += 1
                                        bbdd_changes.guardar_datos_partida(diccionarios.player_dict["game_id"],
                                                                           diccionarios.player_dict["region"])

                                    else:
                                        historialPrompt(prompt, "You didn't get a fish!")

                                    return

                            # FUNCION CUINAR
                            if matriz[i][j][0] == "C" and "cook" in command.lower():
                                if command.lower() == "cook salad":
                                    #comprobamos si hay vegetables(apple)
                                    if diccionarios.player_dict["food_inventory"][0][1]["quantity"] >= 2:
                                        #restamos ingredientes de diccionario
                                        diccionarios.player_dict["food_inventory"][0][1]["quantity"] -= 2
                                        #cocinamos ensalada
                                        historialPrompt(prompt, "Salad cooked!")
                                        diccionarios.player_dict["food_inventory"][3][4]["quantity"] += 1
                                    else:
                                        #si no hay ingredientes suficientes se añade al prompt un mensaje

                                        if not diccionarios.player_dict["food_inventory"].count(6) == 1:
                                            historialPrompt(prompt, "Not enough Vegetable!")


                                elif command.lower() == "cook pescatarian":
                                    # comprobamos si hay vegetables(apple) y fish
                                    if diccionarios.player_dict["food_inventory"][0][1]["quantity"] >= 1 and diccionarios.player_dict["food_inventory"][1][2]["quantity"] >= 1:
                                        # restamos ingredientes de diccionario
                                        diccionarios.player_dict["food_inventory"][0][1]["quantity"] -= 1
                                        diccionarios.player_dict["food_inventory"][1][2]["quantity"] -= 1

                                        # cocinamos pescatarian
                                        historialPrompt(prompt, "Pescatarian cooked!")
                                        diccionarios.player_dict["food_inventory"][4][5]["quantity"] += 1
                                        bbdd_changes.guardar_datos_partida(diccionarios.player_dict["game_id"],
                                                                           diccionarios.player_dict["region"])

                                    else:
                                        #si no hay ingredientes suficientes se añade al prompt un mensaje

                                        if not diccionarios.player_dict["food_inventory"][0][1]["quantity"] >= 1 and not diccionarios.player_dict["food_inventory"][1][2]["quantity"] >= 1:
                                            historialPrompt(prompt, "Not enough Vegetable and fish!")
                                        else:
                                            if not diccionarios.player_dict["food_inventory"][1][2]["quantity"] >= 1:
                                                historialPrompt(prompt, "Not enough Fish!")

                                            if not diccionarios.player_dict["food_inventory"][0][1]["quantity"] >= 1:
                                                historialPrompt(prompt, "Not enough Vegetable!")

                                elif command.lower() == "cook roasted":
                                    # comprobamos si hay vegetables(apple) y meat
                                    if diccionarios.player_dict["food_inventory"][0][1]["quantity"]>= 1 and \
                                            diccionarios.player_dict["food_inventory"][2][3]["quantity"] >= 1:
                                        # restamos ingredientes de diccionario
                                        diccionarios.player_dict["food_inventory"][0][1]["quantity"] -= 1
                                        diccionarios.player_dict["food_inventory"][2][3]["quantity"] -= 1

                                        # cocinamos pescatarian
                                        historialPrompt(prompt, "Roasted cooked!")
                                        diccionarios.player_dict["food_inventory"][5][6]["quantity"] += 1
                                        bbdd_changes.guardar_datos_partida(diccionarios.player_dict["game_id"],
                                                                           diccionarios.player_dict["region"])

                                    else:
                                        #si no hay ingredientes suficientes se añade al prompt un mensaje

                                        if not diccionarios.player_dict["food_inventory"][0][1]["quantity"] >= 1 and not diccionarios.player_dict["food_inventory"][2][3]["quantity"] >= 1:
                                            historialPrompt(prompt, "Not enough Vegetable and Meat!")
                                        else:
                                            if not diccionarios.player_dict["food_inventory"][2][3]["quantity"] >= 1:
                                                historialPrompt(prompt, "Not enough Meat!")

                                            if not diccionarios.player_dict["food_inventory"][0][1]["quantity"] >= 1:
                                                historialPrompt(prompt, "Not enough Vegetable!")

                            # FUNCION EQUIP
                            if command.lower() == "equip wood sword" :
                                # agregamos la espada de madera
                                if diccionarios.player_dict["weapons_inventory"][0][1]["quantity"] >= 1:
                                    diccionarios.player_dict["weapons_equipped"][0][1]["weapon_name"] = "Wood Sword"
                                    historialPrompt(prompt, "Weapon equipped")
                                    return

                                else:
                                    historialPrompt(prompt, "You have no Wood Sword to equip")
                                    return

                            if command.lower() == "equip sword" :


                                if diccionarios.player_dict["weapons_inventory"][1][2]["quantity"] >= 1:


                                    # agregamos la espada
                                    if diccionarios.player_dict["weapons_inventory"][1][2]["quantity"] >= 1:
                                        diccionarios.player_dict["weapons_equipped"][0][1]["weapon_name"] = "Sword"
                                        historialPrompt(prompt, "Weapon equipped")
                                        return

                                else:
                                    historialPrompt(prompt, "You have no Sword to equip")
                                    return


                            # FUNCION UNEQUIP
                            if "unequip sword" in command.lower() and "sword" in diccionarios.player_dict["weapons_equipped"][0][1]["weapon_name"].lower():
                                #eliminamos la espada
                                diccionarios.player_dict["weapons_equipped"][0][1]["weapon_name"] = " "
                                historialPrompt(prompt,"Weapon unequipped")
                                return

                            if "unequip shield" in command.lower() and "shield" in diccionarios.player_dict["weapons_equipped"][0][1]["weapon_name"].lower():
                                #eliminamos el escudo
                                diccionarios.player_dict["weapons_equipped"][1][2]["weapon_name"] = " "
                                historialPrompt(prompt,"Weapon unequipped")
                                return


                            #Funcion Hierba
                            if matriz[i][j][0] == " " and "attack grass" in command.lower():
                                if diccionarios.player_dict["weapons_equipped"]:
                                    if random.randint(1,10) == 1:
                                        historialPrompt(prompt, "You got a lizard!")

                                        diccionarios.player_dict["food_inventory"][2][3]["quantity"] += 1
                                        bbdd_changes.guardar_datos_partida(diccionarios.player_dict["game_id"],
                                                                           diccionarios.player_dict["region"])


                                        #restar 1 a espada
                                        if diccionarios.player_dict['weapons_equipped'][0][1]['weapon_name'] == "Sword":
                                            diccionarios.player_dict["weapons_equipped"][0][1]["uses_left_sword"] -= 1
                                        elif diccionarios.player_dict['weapons_equipped'][0][1]['weapon_name'] == "Wood Sword":
                                            diccionarios.player_dict["weapons_equipped"][0][1]["uses_left_woodsword"] -= 1
                                        #eliminamos las armas si estas se quedan sin usos
                                        if diccionarios.player_dict["weapons_equipped"][0][1]["uses_left_woodsword"] <= 0:
                                            diccionarios.player_dict["weapons_inventory"][0][1]["quantity"] -= 1
                                        elif diccionarios.player_dict["weapons_equipped"][0][1]["uses_left_sword"] <= 0:
                                            diccionarios.player_dict["weapons_inventory"][1][2]["quantity"] -= 1

                                        return

                        except IndexError:
                            pass

    event_caller(matriz, current_pos, command, diccionario_mapa)