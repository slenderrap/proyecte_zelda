import diccionarios
import inventario
import os
import random




def LimpiarPantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")
#MAPAS




hyrule_map_original = ("*Hyrule * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n\
*                                    ~~~~~~~~~~~~~~~~~~OOO*                   *\n\
*                                    ~~~~~~~~~~~~~OO~OOOO~*                   *\n\
*              C                           ~~~~~~   ~~~~~~*                   *\n\
*    T                                                 ~~~*                   *\n\
*                                   E9                    *                   *\n\
*                                           S0            *                   *\n\
*                                                         *                   *\n\
*         X                                     T         *                   *\n\
* OO    OOOO         E2        S1?            T M    F    *                   *\n\
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
*         X                                     T         *                   *\n\
* OO    OOOO         E2        S1?            T M    F    *                   *\n\
*OOOOOOOOOOO                                              *                   *\n\
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")


death_mountain_map_original = ("* Death Mountain  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n\
* O                OOOO                                   *                   *\n\
* O                 OOOO      F                           *                   *\n\
* ~~  S2?            OOOO                           E2    *                   *\n\
* ~~~        E2      OOOO      OOOO                       *                   *\n\
* O~~~~~~~~            OOOO  OO    OOOOOOOO               *                   *\n\
* ~~~~~~~~~             OOOOOO           OOOO             *                   *\n\
*    ~~~           T        OOOO           OO             *                   *\n\
*                 T          OO     M                     *                   *\n\
* !   C           T          OO                   S3?     *                   *\n\
*                                                         *                   *\n\
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")

death_mountain_map = ("* Death Mountain  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n\
* O                OOOO                                   *                   *\n\
* O                 OOOO      F                           *                   *\n\
* ~~  S2?            OOOO                           E2    *                   *\n\
* ~~~        E2      OOOO      OOOO                       *                   *\n\
* O~~~~~~~~            OOOO  OO    OOOOOOOO               *                   *\n\
* ~~~~~~~~~             OOOOOO           OOOO             *                   *\n\
*    ~~~           T        OOOO           OO             *                   *\n\
*                 T          OO     M                     *                   *\n\
* X   C           T          OO                   S3?     *                   *\n\
*                                                         *                   *\n\
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")

gerudo_map_original = ("\
* Gerudo  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n\
*OOOOOOOOOOOOOOOO                                   M     *                   *\n\
*  OOOOO  OOOOO              TTT                          *                   *\n\
*                              TT             S4?        O*                   *\n\
*  E2          C                                        OO*                   *\n\
*                                                       OO*                   *\n\
*             AAAAAA                  E2                  *                   *\n\
*             AAAAAAAA                                    *                   *\n\
*    T       AAAAAAA                 OOOOO      F       ~~*                   *\n\
* X     M      AAA        OOOOO    OOOOO              ~~~~*                   *\n\
*                OOOOOOOOOOOOOOOOOOOO              ~~~~~~~*                   *\n\
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")

gerudo_map = ("\
* Gerudo  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n\
*OOOOOOOOOOOOOOOO                                   M     *                   *\n\
*  OOOOO  OOOOO              TTT                          *                   *\n\
*                              TT             S4?        O*                   *\n\
*  E2          C                                        OO*                   *\n\
*                                                       OO*                   *\n\
*             AAAAAA                  E2                  *                   *\n\
*             AAAAAAAA                                    *                   *\n\
*    T       AAAAAAA                 OOOOO      F       ~~*                   *\n\
* X     M      AAA        OOOOO    OOOOO              ~~~~*                   *\n\
*                OOOOOOOOOOOOOOOOOOOO              ~~~~~~~*                   *\n\
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")

necluda_map_original = ("\
* Necluda * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n\
*                     M                                   *                   *\n\
* X       E2                         TT            M      *                   *\n\
*OO                C               TT                ~~~~~*                   *\n\
*OOOOO                                           ~~~~~~~~~*                   *\n\
*OOOO                                              ~~~~~~~*                   *\n\
*              T                      E2           S5?~~~~*                   *\n\
*     F       TT                                ~~~~~~~~~~*                   *\n\
*~~            TT                                  ~~~~~~~*                   *\n\
*~~~~~~~~              M         S6?         ~~~~~~~~~~~~~*                   *\n\
*~~~~~~~~~~~~                           ~~~~~~~~~~~~~~~~~~*                   *\n\
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")

necluda_map = ("\
* Necluda * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n\
*                     M                                   *                   *\n\
* X       E2                         TT            M      *                   *\n\
*OO                C               TT                ~~~~~*                   *\n\
*OOOOO                                           ~~~~~~~~~*                   *\n\
*OOOO                                              ~~~~~~~*                   *\n\
*              T                      E2           S5?~~~~*                   *\n\
*     F       TT                                ~~~~~~~~~~*                   *\n\
*~~            TT                                  ~~~~~~~*                   *\n\
*~~~~~~~~              M         S6?         ~~~~~~~~~~~~~*                   *\n\
*~~~~~~~~~~~~                           ~~~~~~~~~~~~~~~~~~*                   *\n\
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")



castle_map_original = ("\
* Castle  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n\
*                                                         *                   *\n\
*        \ /                            Ganon ♥♥♥♥♥♥♥♥   *                   *\n\
*      -- O --                                            *                   *\n\
*        / \                                              *                   *\n\
*                             |>  v-v-v-v   |>            *                   *\n\
*                     ,   ,  /_\  |     |  /_\            *                   *\n\
*                     |\_/|  | |'''''''''''| |            *                   *\n\
*                     (q p),-| | ||  _  || | |'-._  |\    *                   *\n\
* OT!                  \_/_(/| |    |#|    | |    '-//    *                   *\n\
* OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO*                   *\n\
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")

castle_map = ("\
* Castle  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n\
*                                                         *                   *\n\
*        \ /                            Ganon ♥♥♥♥♥♥♥♥    *                   *\n\
*      -- O --                                            *                   *\n\
*        / \                                              *                   *\n\
*                             |>  v-v-v-v   |>            *                   *\n\
*                     ,   ,  /_\  |     |  /_\            *                   *\n\
*                     |\_/|  | |'''''''''''| |            *                   *\n\
*                     (q p),-| | ||  _  || | |'-._  |\    *                   *\n\
* OTX                  \_/_(/| |    |#|    | |    '-//    *                   *\n\
* OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO*                   *\n\
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")

show_map = ("\
* Map * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n\
*                                                         *                   *\n\
*  Hyrule       S0{}                       Death mountain  *                   *\n\
*                               S2{}                       *                   *\n\
*        S1{}                                       S3{}    *                   *\n\
*                                                         *                   *\n\
*                         Castle                          *                   *\n\
*                                                         *                   *\n\
*                 S4{}                                 S5{} *                   *\n\
*  Gerudo                               S6{}      Necluda  *                   *\n\
*                                                         *                   *\n\
* Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")

#Ancho mapa:57
#Ancho inventario:19


# eventos pre-partida

def update_map_pre_start(matriz):
    # Borramos las posiciones de todos los enemigos en el mapa original
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j][0] == "E":
                matriz[i][j][0], matriz[i][j+1][0] = " ", " "




    # Iterar sobre el diccionario
    for key, value in getattr(diccionarios, diccionarios.dades[2]["current_map"]).items():
        for subkey, subvalue in value.items():
            for subsubkey, subsubvalue in subvalue.items():
                if "enemy_" in subsubkey:
                    # Cogemos las coordenadas y el número de vidas
                    coordenadas = subsubvalue[1]
                    vidas = str(subsubvalue[2]["current_hearts"])

                    # Reemplazamos las coordenadas en la matriz con el número de vidas en formato str y la E
                    matriz[coordenadas[0]][coordenadas[1]] = [vidas]
                    matriz[coordenadas[0]][coordenadas[1]-1] = ["E"]


                if "chest_" in subsubkey:
                    # Cogemos las coordenadas
                    coordenadas = subsubvalue[1]
                    if subsubvalue[2]["isopen"]:
                        # Reemplazamos las coordenadas con el cofre abierto
                        matriz[coordenadas[0]][coordenadas[1]] = ["W"]

                if "sanctuary_" in subsubkey:
                    # Cogemos las coordenadas
                    coordenadas = subsubvalue[2]
                    if subsubvalue[3]["isopen"]:
                        # Reemplazamos las coordenadas con el cofre abierto
                        matriz[coordenadas[0]][coordenadas[1]] = [" "]

                if "tree_" in subsubkey:
                    if subsubvalue[0] <= 0:
                        # Cogemos las coordenadas
                        coordenadas = subsubvalue[1]
                        # Reemplazamos las coordenadas con el numero de turnos del arbol para aparecer
                        matriz[coordenadas[0]][coordenadas[1]] = [str(subsubvalue[2])]


    # Devolvemos la matriz resultante después de las modificaciones
    return matriz





def agregar_inventario(matriz,inventario_1):
    map = ""
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if j != 78:
                map += matriz[i][j][0]
            else:
                map += matriz[i][j][0] + "\n"

    new_map = inventario.insertar_mapa(map, inventario_1)
    lineas = new_map.strip().split('\n')
    matriz = []
    for linea in lineas:
        fila = [[c] for c in linea]
        matriz.append(fila)
    return matriz


def actualizar_mapa(matriz):

    #actualizamos armas, si se gastan todos los usos de un arma, se sube un uso para la bdd y se suma 5 al nuevo numero de usos si hay otro arma
    if diccionarios.player_dict["weapons_equipped"][0][1]["uses_left_woodsword"] <= 0:
        if diccionarios.player_dict["weapons_inventory"][0][1]["quantity"] > 0:
            diccionarios.player_dict["weapons_equipped"][0][1]["uses_left_woodsword"] = 5
        else:
            if diccionarios.player_dict["weapons_inventory"][1][2]["quantity"] > 0:
                diccionarios.player_dict["weapons_equipped"][0][1]["weapon_name"] = "Sword"
        diccionarios.player_dict["weapons_inventory"][0][1]["uses"] += 1
    if diccionarios.player_dict["weapons_equipped"][0][1]["uses_left_sword"] <= 0:
        if diccionarios.player_dict["weapons_inventory"][1][2]["quantity"] > 0:
            diccionarios.player_dict["weapons_equipped"][0][1]["uses_left_sword"] = 5
        else:
            if diccionarios.player_dict["weapons_inventory"][0][1]["quantity"] > 0:
                diccionarios.player_dict["weapons_equipped"][0][1]["weapon_name"] = "Wood Sword"


        diccionarios.player_dict["weapons_inventory"][1][2]["uses"] += 1

        # Borramos las posiciones de todos los enemigos en el mapa original
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            #si las casillas e pertenecen al tablero y no fuera:
            if i >=10 and j >=57:
                if matriz[i][j][0] == "E":
                    matriz[i][j][0], matriz[i][j + 1][0] = " ", " "

        # Iterar sobre el diccionario
    for key, value in getattr(diccionarios, diccionarios.dades[2]["current_map"]).items():
        for subkey, subvalue in value.items():
            for subsubkey, subsubvalue in subvalue.items():
                if "enemy_" in subsubkey:
                    # Cogemos las coordenadas y el número de vidas
                    coordenadas = subsubvalue[1]
                    vidas = str(subsubvalue[2]["current_hearts"])

                    # Reemplazamos las coordenadas en la matriz con el número de vidas en formato str y la E
                    matriz[coordenadas[0]][coordenadas[1]] = [vidas]
                    matriz[coordenadas[0]][coordenadas[1] - 1] = ["E"]



    # Desempaquetar la matriz e imprimir el mapa original
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if j != 78:
                print(matriz[i][j][0], end="")
            else:
                print(matriz[i][j][0])


def change_map():
    matriz = []
    if "gerudo" in diccionarios.dades[2]["current_map"]:
        lineas = gerudo_map.strip().split('\n')
        for linea in lineas:
            fila = [[c] for c in linea]
            matriz.append(fila)

    elif "necluda" in diccionarios.dades[2]["current_map"]:
        lineas = necluda_map.strip().split('\n')
        for linea in lineas:
            fila = [[c] for c in linea]
            matriz.append(fila)

    elif "death" in diccionarios.dades[2]["current_map"]:
        lineas = death_mountain_map.strip().split('\n')
        for linea in lineas:
            fila = [[c] for c in linea]
            matriz.append(fila)

    elif "hyrule" in diccionarios.dades[2]["current_map"]:
        lineas = hyrule_map.strip().split('\n')
        for linea in lineas:
            fila = [[c] for c in linea]
            matriz.append(fila)

    elif "castle" in diccionarios.dades[2]["current_map"]:
        lineas = castle_map.strip().split('\n')
        for linea in lineas:
            fila = [[c] for c in linea]
            matriz.append(fila)


    # evento Fox
    # el 50% de las veces, fox desaparecerá del mapa
    if random.randint(1, 2) == 1:
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] == ["F"]:
                    # Encontrado, actualiza la matriz
                    matriz[i][j] = [" "]
                    break

    return matriz


def mostrarMapa(inventario):
    prompt_add = ""
    while True:
        LimpiarPantalla()
        count = 0
        matriz = []
        santuaries = sanctuariesOpened()
        lineas = show_map.strip().split('\n')
        for linea in lineas:
            str = ""
            if "{}" in linea:
                for i in range(linea.count("{}")):
                    if len(matriz) == 4:
                        if santuaries[count + 1]:
                            str += " "
                            count += 1
                        else:
                            str += "?"
                            count += 1
                    elif len(matriz) == 5:
                        for j in range(1):
                            if santuaries[count - 1]:
                                str += " "
                                count += 1
                            else:
                                str += "?"
                                count += 1
                        if santuaries[count]:
                            str += " "
                            count += 1
                        else:
                            str += "?"
                            count += 1

                    else:

                        if santuaries[count]:
                            str += " "
                            count += 1
                        else:
                            str += "?"
                            count += 1
                if i == 0:
                    fila = [[c] for c in linea.format(str)]
                else:
                    fila = [[c] for c in linea.format(str[0], str[1])]
                matriz.append(fila)


            else:
                fila = [[c] for c in linea]
                matriz.append(fila)

        matriz = agregar_inventario(matriz, inventario)

        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if j != 78:
                    print(matriz[i][j][0], end="")
                else:
                    print(matriz[i][j][0])
        if len(prompt_add) > 0:
            print(prompt_add)

        opc = input("Give an Order:").capitalize()
        if opc != "Back":
            if len(prompt_add) != 0:
                prompt_add = prompt_add + "\nInvalid action"
            else:
                prompt_add = "Invalid action"
        else:
            prompt_add += "\nBacK"
            return prompt_add


def sanctuariesOpened():
    count = 0
    sanctuaries = []
    for clave, valor in diccionarios.main_dict_hyrule.items():
        if valor.get(3):
            sanctuaries.append(valor.get(3)["sanctuary_{}".format(count)][3].get("isopen"))
            count += 1
    for clave, valor in diccionarios.main_dict_death_mountain.items():
        if valor.get(3):
            sanctuaries.append(valor.get(3)["sanctuary_{}".format(count)][3].get("isopen"))
            count += 1
    for clave, valor in diccionarios.main_dict_gerudo.items():
        if valor.get(3):
            sanctuaries.append(valor.get(3)["sanctuary_{}".format(count)][3].get("isopen"))
            count += 1
    for clave, valor in diccionarios.main_dict_necluda.items():
        if valor.get(3):
            sanctuaries.append(valor.get(3)["sanctuary_{}".format(count)][3].get("isopen"))
            count += 1
    return sanctuaries
