import random
#MAPAS

hyrule_map_original = ("*Hyrule * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n\
*                                    ~~~~~~~~~~~~~~~~~~OOO*                   *\n\
*                                    ~~~~~~~~~~~~~OO~OOOO~*                   *\n\
*              C                           ~~~~~~   ~~~~~~*                   *\n\
*    T                                                 ~~~*                   *\n\
*                                   E9                    *                   *\n\
*                                           S0            *                   *\n\
*                                                         *                   *\n\
*         !X                                    T         *                   *\n\
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
*         !X                                    T         *                   *\n\
* OO    OOOO         E1        S1?            T M    F    *                   *\n\
*OOOOOOOOOOO                                              *                   *\n\
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")


#Ancho mapa:57
#Ancho inventario:19

# Dividir el mapa en líneas
lineas = hyrule_map.strip().split('\n')

# Crear una lista de listas
matriz = []

# Procesar cada línea y agregarla a la matriz como una lista de caracteres
for linea in lineas:
    fila = [[c] for c in linea]
    matriz.append(fila)

# Imprimir la matriz
for fila in range(len(matriz)):
    for columna in range(len(matriz)):
        print(matriz[fila][columna])

