import diccionarios
import random


#mover jugador a water
def move_to_X(matriz, current_position,casilla):
    x, y = current_position
    position = None

    # Buscar la posición de la casilla con "~"
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == casilla:
                position = (i, j)
                break

    # Verificar si se encontró una posición con "~"
    if position:
        # Buscar la posición vacía más cercana
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_x, new_y = position[0] + i, position[1] + j
                if 0 <= new_x < len(matriz) and 0 <= new_y < len(matriz[new_x]) and matriz[new_x][new_y] == [" "]:
                    return (new_x, new_y)

        # Si no se encuentra una posición vacía, devolvemos la posición original
        return (x, y)
    else:
        return (x, y)











#Variable movimiento npcs
def move_enemy(current_pos,matriz,main_dict,object_id,npc_id, npc_name,prompt):
    current_positions = main_dict[object_id][npc_id][npc_name][:2]
    old_pos = current_positions.copy()

    #Derecha = 1
    #Izquierda = 2
    #Arriba = 3
    #Abajo = 4

    directions = ["derecha", "arriba", "izquierda", "abajo"]
    #print(random.shuffle(directions))
    random.shuffle(directions)



    new_positions = current_pos.copy()
    for direction in directions:
        positions_occupied = False
        # Calcula las nuevas coordenadas según la dirección

        if direction == "arriba":
            new_positions[0][0] -= 1
            new_positions[1][0] -= 1
            old_pos = [[new_positions[0][0]+1,new_positions[0][1]],[new_positions[1][0]+1,new_positions[1][1]]]

        elif direction == "abajo":
            new_positions[0][0] += 1
            new_positions[1][0] += 1
            old_pos = [[new_positions[0][0]-1,new_positions[0][1]],[new_positions[1][0]-1,new_positions[1][1]]]

        elif direction == "izquierda":
            new_positions[0][1] -= 2
            new_positions[1][1] -= 2
            old_pos = [[new_positions[0][0],new_positions[0][1]+2],[new_positions[1][0],new_positions[1][1]+2]]

        elif direction == "derecha":
            new_positions[0][1] += 2
            new_positions[1][1] += 2
            old_pos = [[new_positions[0][0],new_positions[0][1]-2],[new_positions[1][0],new_positions[1][1]-2]]




        new_positions = [new_positions[0],new_positions[1]]
        # Verifica si alguna de las nuevas posiciones está ocupada
        for pos in new_positions:
            print("--")
            if positions_occupied:
                new_positions = old_pos.copy()
                continue
            print(new_positions)
            if matriz[pos[0]][pos[1]] != [" "] :
                print("Pos occupied")
                positions_occupied = True




        # Si no hay posiciones ocupadas, actualiza las coordenadas y sale del bucle
        if not positions_occupied:
            #print(current_pos[0][0], (current_pos[0][1])-1)
            #main_dict[7][npc_id][npc_name][:2] = new_positions
            char_1 = matriz[old_pos[0][0]][old_pos[0][1]]
            char_2 = matriz[old_pos[1][0]][old_pos[1][1]]

            #imprimimos la nueva posicion del npc en la matriz
            matriz[new_positions[0][0]][new_positions[0][1]] = char_1
            matriz[new_positions[1][0]][new_positions[1][1]] = char_2

            print(matriz[old_pos[0][0]][old_pos[0][1]])
            #borramos las posiciones anteriores
            matriz[old_pos[0][0]][old_pos[0][1]] = [" "]
            matriz[old_pos[1][0]][old_pos[1][1]] = [" "]

            historialPrompt(prompt,f"Enemy '{npc_name}' moved to positions {current_positions}")

            current_pos[0] = current_positions[0]
            current_pos[1] = current_positions[1]
            return

    # Si todas las posiciones están ocupadas, imprime un mensaje
    else:
        print(f"All positions occupied, enemy '{npc_name}' can't move.")









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
                                #prompt.append(f"{sub_key} is already open.")
                                historialPrompt(prompt,f"{sub_key} is already open." )
                                return True
                            else:
                                if sub_value[0] == 1:
                                    #prompt.append("You Got a Sword!")
                                    historialPrompt(prompt, "You Got a Sword!")

                                    # AGREGAR SWORD A PLAYER
                                elif sub_value[0] == 2:
                                    historialPrompt(prompt, "You Got a Shield!")
                                    #prompt.append("You Got a Shield!")
                                    # AGREGAR SHIELD A PLAYER
                                matriz[x][y][0] = "W"
                                sub_value[2]["isopen"] = True
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
                                #prompt.append(f"{sub_key} is already open.")
                                historialPrompt(prompt, f"{sub_key} is already open.")

                                return True
                            else:
                                #prompt.append("You opened the sanctuary!")
                                historialPrompt(prompt, "You opened the sanctuary!")

                                # AGREGAR RECOMPENSA AL JUGADOR
                                diccionarios.player_dict["hearts"] += 1



                                #Borramos el interrogante del mapa
                                if matriz[x][y][0] == "S":
                                    matriz[x][y+2][0] = " "
                                elif str(matriz[x][y][0]).isdigit():
                                    matriz[x][y + 1][0] = " "
                                else:
                                    matriz[x][y][0] = " "

                                sub_value[3]["isopen"] = True

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
                            if diccionarios.player_dict["weapons_equipped"]:
                                if sub_value[2]["isdead"]:
                                    historialPrompt(prompt, "Enemy killed!")

                                else:
                                    historialPrompt(prompt, "Enemy encountered!")
                                    move_enemy(sub_value, matriz, diccionarios.main_dict_hyrule,int(key), 4, sub_key, prompt)

                                    print(sub_value[1][0])
                                    print(matriz[x][y][0])

                                    #Restamos en el juego la vida del enemigo
                                    matriz[sub_value[1][0]][sub_value[1][1]][0] = str(
                                        int(matriz[sub_value[1][0]][sub_value[1][1]][0]) - 1)
                                    #Restamos la vida del enemigo en el diccionario
                                    sub_value[2]["current_hearts"] -= 1

                                    #Si la vida del enemigo llega a 0, esta se elimina
                                    if matriz[sub_value[1][0]][sub_value[1][1]][0] == "0":
                                        matriz[sub_value[0][0]][sub_value[0][1]][0] = " "
                                        matriz[sub_value[1][0]][sub_value[1][1]][0] = " "

                                        historialPrompt(prompt, "Enemy dead")
                                        sub_value[3]["isdead"] = True


                            else:
                                historialPrompt(prompt, "You have no Sword!")
                                move_enemy(sub_value, matriz, diccionarios.main_dict_hyrule, int(key), 4, "enemy_1", prompt)

                            # el enemigo se movera despues de la interaccion
                            diccionarios.player_dict["hearts"] -= 1
                            # restamos 1 de vida al jugador
                            historialPrompt(prompt, "-1 health!")
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

                            #comprobamos si el jugador tiene armas equipadas
                            #prompt.append("Tree Attacked")
                            historialPrompt(prompt, "Tree Attacked")
                            if not diccionarios.player_dict["weapons_equipped"]:

                                #probabilidad manzana 20%
                                if random.randint(1, 10) <= 4:
                                    #prompt.append("Tree dropped an Apple")
                                    historialPrompt(prompt, "Tree dropped an Apple")
                                    #Aqui se guardaria la manzana
                                #probabilidad que caigan objetos 10%
                                if random.randint(1,10) == 10:
                                    if random.randint(1,2) == 1:
                                        #prompt.append("Tree dropped a Wood Sword")
                                        historialPrompt(prompt, "Wood Sword")
                                        #AQUI SE GUARDA LA ESPADA (Ids en diccionarios.py)
                                        diccionarios.player_dict["weapons_inventory"].append(1)
                                    else:
                                        #prompt.append("Tree dropped a Wood Shield")
                                        historialPrompt(prompt, "Wood Shield")
                                        #AQUI SE GUARDA EL ESCUDO (Ids en diccionarios.py)
                                        diccionarios.player_dict["weapons_inventory"].append(2)
                            else:
                                # probabilidad manzana 40%
                                if random.randint(1, 10) <= 4:
                                    #prompt.append("Tree dropped an Apple")
                                    historialPrompt(prompt, "Tree Attacked")
                                    # Aqui se guardaria la manzana

                                    # probabilidad manzana
                                #probabilidad objeto 20%
                                if random.randint(1, 5) == 5:
                                    prompt.append("Tree dropped an Wood Sword")
                                    # Aqui se guardaria el objeto
                                    # probabilidad objeto 20%
                                elif random.randint(1, 5) == 5:
                                    prompt.append("Tree dropped an Wood Shield")
                                    # Aqui se guardaria el objeto

                                #AQUI DESGASTAMOS LA ESPADA EN UN USO

                                #restamos uno de vida al arbol
                                sub_value[0] -= 1
                                
                                #si el arbol se queda sin vida, este se destruirá

                                if sub_value[0] <= 0:
                                    matriz[x][y][0] = " "
                                    #prompt.append("Tree destroyed")
                                    historialPrompt(prompt, "Tree destroyed")

                                return True

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
                            # prompt.append("Tree Attacked")

                            if diccionarios.player_dict["weapons_equipped"]:
                                historialPrompt(prompt, "Fox Attacked")
                                prompt.append("You got meat")
                                # Aqui se guarda el objeto
                                diccionarios.player_dict["food_inventory"].append(1)

                                # AQUI DESGASTAMOS EL/LAS ARMAS EQUIPADA EN UN USO
                                for weapon in diccionarios.player_dict['weapons_equipped']:
                                    # Iterar sobre las armas equipadas y restar uno a uses_left
                                    for key, value in weapon.items():
                                        value['uses_left'] -= 1

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

                            # FUNCION ARBOL
                            if matriz[i][j][0] == "T" and command.lower() == "attack":
                                tree_event(diccionario, i, j)

                            # FUNCION SANTUARIOS
                            if (matriz[i][j][0] == "S" or matriz[i][j][0] in ("0","1","2","3","4","5","6","7","8","9") or matriz[i][j][0] == "?") and command.lower() == "open":
                                if sanctuary_event(diccionario, i, j, matriz, prompt):
                                    return

                            # FUNCION ENEMIGOS
                            if (matriz[i][j][0] == "E" or matriz[i][j][0] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")) and command.lower() == "attack":
                                enemy_event(diccionario, i, j, matriz, prompt)

                            # FUNCION FOX
                            if matriz[i][j][0] == "F" and command.lower() == "attack":
                                fox_event(diccionario, i, j)


                        except IndexError:
                            pass

    event_caller(matriz, current_pos, command, diccionario_mapa)