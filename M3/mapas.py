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


#Ancho mapa:57
#Ancho inventario:19


# eventos pre-partida

def update_map_pre_start(matriz):
    # Iterar sobre el diccionario

    #HYRULE
    for key, value in getattr(diccionarios,current_map):
        for subkey, subvalue in value.items():
            for subsubkey, subsubvalue in subvalue.items():
                if "enemy" in subsubkey:
                    # Cogemos las coordenadas y el número de vidas
                    coordenadas = subsubvalue[1]
                    vidas = str(subsubvalue[2]["current_hearts"])

                    # Reemplazamos las coordenadas en la matriz con el número de vidas en formato str
                    matriz[coordenadas[0]][coordenadas[1]] = [vidas]
    # RESTO DE MAPAS...


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
    # Desempaquetar la matriz e imprimir el mapa original
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if j != 78:
                print(matriz[i][j][0], end="")
            else:
                print(matriz[i][j][0])





