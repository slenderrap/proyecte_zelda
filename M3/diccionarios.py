import os
import mysql.connector



config = {
    'user': 'zelda',
    'password': 'link',
    'host': '4.231.10.226',
    'database': 'zelda_pre',
    'raise_on_warnings': True
}

connection = mysql.connector.connect(**config)
cursor = connection.cursor()


#Diccionarios de cada arma
wood_sword = {1:{"uses_og":5,"uses_left":5}}
sword = {2:{"uses_og":9,"uses_left":9}}
wood_shield = {1:{"uses_og":5,"uses_left":5}}
shield = {2:{"uses_og":9,"uses_left":9}}







#HYRULE

#Sintaxis del diccionario:
#1:Arboles
#2:Cofres (1 es espada, 2 es escudo)
#3:Santuarios
#4:Enemigos

#Arboles: Primera Posicion


dades = {1 : {"blood_moon_count":25},2 :{"current_map":"main_dict_hyrule"} }

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
#Salad = 3 (2 hearts)
#Pescatarian = 4(3 hearts)
#Roasted = 5(4 hearts)
#Apple = 6


#REVISAR WEAPONS INVENTORY, puede ser innecesario
player_dict = {'game_id':1,'user_name':'Player 1','hearts': 3,"hearts_max": 5, 'region':'Hyrule',
               'weapons_equipped': [{1:{'weapon_name':'Wood Sword',"uses_og":5,"uses_left":5}},
                                    {2:{'shield_name':'Shield',"uses_og":9,"uses_left":5}}],
               'weapons_inventory': [{1:{"name":"Wood Sword","quantity":4,'uses':0}},
                                     {2:{"name":"Sword","quantity":2,'uses':0}}],
               'shields_inventory': [{1:{"name":"Wood Shield","quantity":4,'uses':0}},
                                     {2:{"name":"Shield","quantity":3,'uses':0}}],
               'food_inventory': [{1:{"food_name":"Vegetables","quantity":1,'uses':0}},
                                  {2:{"food_name":"Fish","quantity":2,'uses':0}},
                                  {3:{"food_name":"Meat","quantity":3,'uses':0}},
                                  {4:{"food_name":"Salad","quantity":4,'uses':0}},
                                  {5:{"food_name":"Pescatarian","quantity":5,'uses':0}},
                                  {6:{"food_name":"Roasted","quantity":6,'uses':0}}],
               'blood_moon_countdown': 0, 'blood_moon_appearances':0,}

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
    1: {1: {"tree_1": [4,[4,5],10]}},
    2: {1: {"tree_2": [4,[8,48],10]}},
    3: {1: {"tree_3": [4,[9,46],10]}},
    4: {2: {"chest_1": [1,[9,48], {"isopen": False}]}},
    5: {3: {"sanctuary_0": [[6,44],[9,45],[9,45],{"isopen": True}]}},
    6: {3: {"sanctuary_1": [[9,31],[9,32],[9,33],{"isopen": False}]}},
    7: {4: {"enemy_1": [[9,21],[9,22],{"isdead": False,"current_hearts" : 1 }]}},
    8: {4: {"enemy_2": [[5,36],[5,37],{"isdead": False,"current_hearts" : 9 }]}},
    9: {5: {"fox_1": [1,[9,53]]}},
    10: {6: {"already_fished" : False}}

}

main_dict_death_mountain = {
    1: {1: {"tree_1": [4,[7,19],10]}},
    2: {1: {"tree_2": [4,[8,18],10]}},
    3: {1: {"tree_3": [4,[9,18],10]}},
    4: {2: {"chest_1": [2,[8,36], {"isopen": False}]}},
    5: {3: {"sanctuary_2": [[3,6],[3,7],[3,8],{"isopen": False}]}},
    6: {3: {"sanctuary_3": [[9,50],[9,51],[9,52],{"isopen": False}]}},
    7: {4: {"enemy_1": [[4,13],[4,14],{"isdead": False,"current_hearts" : 2 }]}},
    8: {4: {"enemy_2": [[3,51],[5,52],{"isdead": False,"current_hearts" : 2 }]}},
    9: {5: {"fox_1": [1,[2,30]]}},
    10: {6: {"already_fished" : False}}

}

main_dict_gerudo = {
    1: {1: {"tree_1": [4,[2,29],10]}},
    2: {1: {"tree_2": [4,[2,30],10]}},
    3: {1: {"tree_3": [4,[2,31],10]}},
    4: {1: {"tree_4": [4,[3,31],10]}},
    5: {1: {"tree_5": [4,[3,32],10]}},
    6: {1: {"tree_6": [4,[8,5],10]}},
    7: {2: {"chest_1": [1,[1,51], {"isopen": False}]}},
    8: {2: {"chest_2": [1,[9,8], {"isopen": False}]}},
    9: {3: {"sanctuary_4": [[3,45],[3,46],[3,47],{"isopen": False}]}},
    10: {4: {"enemy_1": [[4,3],[4,4],{"isdead": False,"current_hearts" : 1 }]}},
    11: {4: {"enemy_2": [[6,37],[6,38],{"isdead": False,"current_hearts" : 2 }]}},
    12: {5: {"fox_1": [1,[8,47]]}},
    13: {6: {"already_fished" : False}}

}


main_dict_necluda = {
    1: {1: {"tree_1": [4,[2, 37],10]}},
    2: {1: {"tree_2": [4,[2, 37],10]}},
    3: {1: {"tree_3": [4,[3, 35],10]}},
    4: {1: {"tree_4": [4,[3, 36],10]}},
    5: {1: {"tree_5": [4,[6, 15],10]}},
    6: {1: {"tree_6": [4,[7, 14],10]}},
    7: {1: {"tree_7": [4,[7, 15],10]}},
    8: {1: {"tree_8": [4,[8, 15],10]}},
    9: {1: {"tree_9": [4,[8, 16],10]}},
    10: {2: {"chest_1": [2,[1, 22], {"isopen": False}]}},
    11: {2: {"chest_2": [2,[2, 51], {"isopen": False}]}},
    12: {2: {"chest_3": [2,[9, 23], {"isopen": False}]}},
    13: {3: {"sanctuary_5": [[6, 51],[6, 52],[6, 53],{"isopen": False}]}},
    14: {3: {"sanctuary_6": [[9, 33],[9, 34],[9, 33],{"isopen": False}]}},
    15: {4: {"enemy_1": [[2,10],[2,11],{"isdead": False,"current_hearts" : 2 }]}},
    16: {4: {"enemy_2": [[6,38],[6,39],{"isdead": False,"current_hearts" : 2 }]}},
    17: {5: {"fox_1": [1,[7,6]]}},
    18: {6: {"already_fished" : False}}

}











