import random
import diccionarios
import funciones.inventario
from funciones.map import current_map

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
*         X                                     T         *                   *\n\
* OO    OOOO         E1        S1?            T M    F    *                   *\n\
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
*  E1          C                                        OO*                   *\n\
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
*  E1          C                                        OO*                   *\n\
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
* X       E1                         TT            M      *                   *\n\
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
* X       E1                         TT            M      *                   *\n\
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

#Ancho mapa:57
#Ancho inventario:19


# eventos pre-partida

def update_map_pre_start(matriz):
    # Iterar sobre el diccionario

    for key, value in getattr(diccionarios,funciones.map.current_map).items():
        for subkey, subvalue in value.items():
            for subsubkey, subsubvalue in subvalue.items():
                if "enemy_" in subsubkey:
                    #antes de nada, borramos las posiciones del enemigo en el mapa original
                    for i in range(len(matriz)):
                        for j in range(len(matriz[0])):
                            if matriz[i][j][0] == "E":
                                matriz[i][j][0],matriz[i][j+1][0] = " "," "

                    # Cogemos las coordenadas y el número de vidas
                    coordenadas = subsubvalue[1]
                    vidas = str(subsubvalue[2]["current_hearts"])

                    # Reemplazamos las coordenadas en la matriz con el número de vidas en formato str y la E
                    matriz[coordenadas[0]][coordenadas[1]] = [vidas]
                    matriz[coordenadas[0]][coordenadas[1]-1] = ["E"]
                if "chest_" in subsubkey:
                    # Cogemos las coordenadas
                    coordenadas = subsubvalue[1]
                    if subsubvalue [2]["isopen"]:
                        # Reemplazamos las coordenadas con el cofre abierto
                        matriz[coordenadas[0]][coordenadas[1]] = ["W"]

                if "sanctuary_" in subsubkey:
                    # Cogemos las coordenadas
                    coordenadas = subsubvalue[2]
                    if subsubvalue [3]["isopen"]:
                        # Reemplazamos las coordenadas con el cofre abierto
                        matriz[coordenadas[0]][coordenadas[1]] = [" "]

                if "tree_" in subsubkey:
                    if subsubvalue[0] <= 0:
                        # Cogemos las coordenadas
                        coordenadas = subsubvalue[1]
                        # Reemplazamos las coordenadas con el numero de turnos del arbol para aparecer
                        matriz[coordenadas[0]][coordenadas[1]] = [str(subsubvalue[2])]


def agregar_inventario(matriz,inventario):
    map = ""
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if j != 78:
                map += matriz[i][j][0]
            else:
                map += matriz[i][j][0] + "\n"

    new_map = funciones.inventario.insertar_mapa(map, inventario)
    lineas = new_map.strip().split('\n')
    matriz = []
    for linea in lineas:
        fila = [[c] for c in linea]
        matriz.append(fila)
    return matriz


def actualizar_mapa(matriz):
    #actualizamos vida enemigos en mapa
    for key, value in getattr(diccionarios, funciones.map.current_map).items():
        for subkey, subvalue in value.items():
            for subsubkey, subsubvalue in subvalue.items():
                if "enemy_" in subsubkey:
                    # antes de nada, borramos las posiciones del enemigo en el mapa original
                    for i in range(len(matriz)):
                        for j in range(len(matriz[0])):
                            if i < 11 and j < 58:
                                if matriz[i][j][0] == "E":
                                    matriz[i][j][0], matriz[i][j + 1][0] = " ", " "

                    # Cogemos las coordenadas y el número de vidas
                    coordenadas = subsubvalue[1]
                    vidas = str(subsubvalue[2]["current_hearts"])
                    #si el numero de vidas es mayor a 0, se imprimira el enemigo en el mapa, si no, no
                    if  int(vidas) <= 0:
                        # Reemplazamos las coordenadas en la matriz con el número de vidas en formato str y la E
                        matriz[coordenadas[0]][coordenadas[1]] = [" "]
                        matriz[coordenadas[0]][coordenadas[1] - 1] = [" "]
                    else:
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
    if "gerudo" in funciones.map.current_map:
        lineas = gerudo_map.strip().split('\n')
        for linea in lineas:
            fila = [[c] for c in linea]
            matriz.append(fila)

    elif "necluda" in funciones.map.current_map:
        lineas = necluda_map.strip().split('\n')
        for linea in lineas:
            fila = [[c] for c in linea]
            matriz.append(fila)

    elif "death" in funciones.map.current_map:
        lineas = death_mountain_map.strip().split('\n')
        for linea in lineas:
            fila = [[c] for c in linea]
            matriz.append(fila)

    elif "hyrule" in funciones.map.current_map:
        lineas = hyrule_map.strip().split('\n')
        for linea in lineas:
            fila = [[c] for c in linea]
            matriz.append(fila)

    elif "castle" in funciones.map.current_map:
        lineas = castle_map.strip().split('\n')
        for linea in lineas:
            fila = [[c] for c in linea]
            matriz.append(fila)

    return matriz



