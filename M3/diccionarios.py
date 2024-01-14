import os

#HYRULE

#Sintaxis del diccionario:
#1:Arboles
#2:Cofres (1 es espada, 2 es escudo)
#3:Santuarios
#4:Enemigos

#Arboles: Primera Posicion


dades = {}

# localitzacions = {{
#     1: {1: {"tree_1": [4,[4,5]]}},
#     2: {1: {"tree_2": [4,[8,48]]}},
#     3: {1: {"tree_3": [4,[9,46]]}},
#     4: {2: {"chest_1": [1,[9,48]]}},
#     5: {3: {"sanctuary_0": [[6,44],[9,45],[9,45]]}},
#     6: {3: {"sanctuary_1": [[9,31],[9,32],[9,33]]}},
#
# },#copia de resto de diccionarios de mundo
# }

#player{armas equipadas,armas en inventario,corazones}
#wood sword = 1
#sword = 2
#wood shield = 3
#shield = 4

#IDS de objetos
#Meat = 1
#Fish = 2


#REVISAR WEAPONS INVENTORY, puede ser innecesario
player_dict = {'weapons_equipped': [{1:{"uses_og":5,"uses_left":5}}], 'weapons_inventory': [], 'hearts': 3 , 'action_count': 0, 'food_inventory': [] }


#composicion diccionarios:
#primera clave: ID General (Unica),
#Segunda clave en diccionario: (Id del objeto, mirar arriba, este no es unico)
#Los demas valores dependiendo del elemento variaran
#Ejemplo: [1, {"isopen": False}]
#          ^
#          |
#Objeto que ofrecerá (1: Espada, 2: Cofre)
#Tree: primera posicion, vida, segunda, posicion arbol



main_dict_hyrule = {
    1: {1: {"tree_1": [4,[4,5]]}},
    2: {1: {"tree_2": [4,[8,48]]}},
    3: {1: {"tree_3": [4,[9,46]]}},
    4: {2: {"chest_1": [1,[9,48], {"isopen": False}]}},
    5: {3: {"sanctuary_0": [[6,44],[9,45],[9,45],{"isopen": True}]}},
    6: {3: {"sanctuary_1": [[9,31],[9,32],[9,33],{"isopen": False}]}},
    7: {4: {"enemy_1": [[9,21],[9,22],{"isdead": False,"current_hearts" : 1 }]}},
    8: {4: {"enemy_2": [[5,36],[5,37],{"isdead": False,"current_hearts" : 9 }]}},
    9: {1: {"fox_1": [1,[9,53]]}},



}




