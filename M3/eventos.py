import diccionarios
import random


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
                                    prompt.append("You Got a Shield!")
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
                                prompt.append(f"{sub_key} is already open.")
                                return True
                            else:
                                #prompt.append("You opened the sanctuary!")
                                print()
                                # AGREGAR RECOMPENSA AL JUGADOR
                                if matriz[x][y][0] != "?":
                                    matriz[x][y+2][0] = " "
                                else:
                                    matriz[x][y][0] = " "

                                sub_value[3]["isopen"] = True

                                return True
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

                                #restamos uno de vida al abrol
                                sub_value[0] -= 1
                                
                                #si el arbol se queda sin vida, este se destruirá

                                if sub_value[0] <= 0:
                                    matriz[x][y][0] = " "
                                    prompt.append("Tree destroyed")

                                return True


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


                        except IndexError:
                            pass



    event_caller(matriz, current_pos, command, diccionario_mapa)