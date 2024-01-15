# Funcion que se encarga de mostrar los diferentes inventarios haciendo querys a la BBDD

# COSAS ARREGLAR
# en bbdd name_user = max length(11)
# Arreglar name_user, hearts, blood moon
# Solo puede tener dos armas
# Añadir maximo 99 armas
# Añadir maximo 99 food

import mapas
import diccionarios

# Conector MySQL
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

# Strings inventarios
inventory_main = \
(" * * * * Inventory *\n\
                   *\n\
 X ♥ X/X *\n\
 Blood moon in X *\n\
 Equipment         *\n\
 X *\n\
 X *\n\
                   *\n\
 Food X *\n\
 Weapons X *\n\
                   *\n\
 * * * * * * * * * *")
inventory_weapons = \
(" * * * * * Weapons *\n\
                   *\n\
                   *\n\
 Wood Sword X *\n\
  X *\n\
 Sword X *\n\
  X *\n\
 Wood Shield X *\n\
  X *\n\
 Shield X *\n\
  X *\n\
 * * * * * * * * * * ")
inventory_food = \
(" * * * * * *  Food *\n\
                   *\n\
                   *\n\
 Vegetables  X *\n\
 Fish        X *\n\
 Meat        X *\n\
                   *\n\
 Salads      X *\n\
 Pescatarian X *\n\
 Roasted     X *\n\
                   *\n\
 * * * * * * * * * *")


# Funciones generar inventario
def inv_main(player_id):

    # Inventory
    inventory = inventory_main
    # name_user=43
    inventory = inventory[:43] + f"{diccionarios.player_dict['user_name']}".ljust(11) + inventory[43 + 1:]


    # Inventory - health
    # current_hearts i= 57
    inventory = inventory[:57] + f"{diccionarios.player_dict['hearts']}" + inventory[57 + 1:]

    # full_hearts i=59
    inventory = inventory[:59] + f"{diccionarios.player_dict['hearts_max']}" + inventory[59 + 1:]

    # Inventory - Blood moon
    inventory = inventory[:78] + f"{diccionarios.player_dict['action_count']}".rjust(3) + inventory[78 + 1:]


    # Inventory - equipment
    # weapon_1 = 106
    consulta = "SELECT weapon_name FROM game_weapons WHERE game_id = %s AND equiped=1 AND weapon_name LIKE '%Sword%'"
    cursor.execute(consulta, (player_id,))
    weapon_1 = cursor.fetchall()
    if len(weapon_1) > 0:
        inventory = inventory[:106] + f"{weapon_1[0][0]}".rjust(17) + inventory[106 + 1:]
    else:
        inventory = inventory[:106] + "".rjust(17) + inventory[106 + 1:]
    # weapon_2 = 127
    consulta = "SELECT weapon_name FROM game_weapons WHERE game_id = %s AND equiped=1 AND weapon_name LIKE '%Shield%'"
    cursor.execute(consulta, (player_id,))
    weapon_2 = cursor.fetchall()
    if len(weapon_2) > 0:
        inventory = inventory[:127] + f"{weapon_2[0][0]}".rjust(1) + inventory[127 + 1:]
    else:
        inventory = inventory[:127] + "".rjust(17) + inventory[127 + 1:]

    # food = 174
    consulta = "SELECT SUM(quantity_remaining) FROM game_food WHERE game_id = %s GROUP BY game_id"
    cursor.execute(consulta, (player_id,))
    food_remaining = cursor.fetchall()
    inventory = inventory[:174] + f"{food_remaining[0][0]}".rjust(12) + inventory[174 + 1:]
    # weapons = 198
    consulta = "SELECT count(*) FROM game_weapons WHERE game_id = %s GROUP BY game_id"
    cursor.execute(consulta, (player_id,))
    weapons_remaining = cursor.fetchall()
    inventory = inventory[:198] + f"{weapons_remaining[0][0]}".rjust(9) + inventory[198 + 1:]


    return inventory
def inv_weapons(player_id):
    # Inventory
    inventory = inventory_weapons


    # wood_sword = 75
    consulta = "SELECT lives_remaining FROM game_weapons WHERE game_id = %s and equiped=1 and weapon_name='Wood Sword'"
    cursor.execute(consulta, (player_id,))
    lives_current_woodsword = cursor.fetchone()
    consulta = "SELECT count(*) FROM game_weapons WHERE game_id = %s and weapon_name='Wood Sword'"
    cursor.execute(consulta, (player_id,))
    total_woodsword = cursor.fetchone()
    if total_woodsword[0] >= 1:
        inventory = inventory[:75] + f"{lives_current_woodsword[0]}/{total_woodsword[0]}".rjust(6) + inventory[75 + 1:]
    else:
        inventory = inventory[:75] + "0/0".rjust(6) + inventory[75 + 1:]
    # wood_sword equiped = 86
    consulta = "SELECT equiped FROM game_weapons WHERE game_id = %s and equiped=1 and weapon_name='Wood Sword'"
    cursor.execute(consulta, (player_id,))
    woodsword_equiped = cursor.fetchone()
    if woodsword_equiped:
        inventory = inventory[:86] + "(equiped)".ljust(16) + inventory[86 + 1:]
    else:
        inventory = inventory[:86] + "".ljust(16) + inventory[86 + 1:]

    # sword = 112
    consulta = "SELECT lives_remaining FROM game_weapons WHERE game_id = %s and equiped=1 and weapon_name='Sword'"
    cursor.execute(consulta, (player_id,))
    lives_current_sword = cursor.fetchone()
    consulta = "SELECT count(*) FROM game_weapons WHERE game_id = %s and weapon_name='Sword'"
    cursor.execute(consulta, (player_id,))
    total_sword = cursor.fetchone()
    if total_sword[0] >= 1:
        inventory = inventory[:112] + f"{lives_current_sword[0]}/{total_sword[0]}".rjust(11) + inventory[112 + 1:]
    else:
        inventory = inventory[:112] + "0/0".rjust(11) + inventory[112 + 1:]
    # sword equiped = 128
    consulta = "SELECT equiped FROM game_weapons WHERE game_id = %s and equiped=1 and weapon_name='Sword'"
    cursor.execute(consulta, (player_id,))
    sword_equiped = cursor.fetchone()
    if sword_equiped:
        inventory = inventory[:128] + "(equiped)".ljust(16) + inventory[128 + 1:]
    else:
        inventory = inventory[:128] + "".rjust(16) + inventory[128 + 1:]

    # wood_shield = 160
    consulta = "SELECT lives_remaining FROM game_weapons WHERE game_id = %s and equiped=1 and weapon_name='Wood Shield'"
    cursor.execute(consulta, (player_id,))
    lives_current_woodshield = cursor.fetchone()
    consulta = "SELECT count(*) FROM game_weapons WHERE game_id = %s and weapon_name='Wood Shield'"
    cursor.execute(consulta, (player_id,))
    total_woodshield = cursor.fetchone()
    if total_sword[0] >= 1:
        inventory = inventory[:160] + f"{lives_current_woodshield[0]}/{total_woodshield[0]}".rjust(5) + inventory[160 + 1:]
    else:
        inventory = inventory[:160] + "0/0".rjust(5) + inventory[160 + 1:]
    # wood_shield equiped = 170
    consulta = "SELECT equiped FROM game_weapons WHERE game_id = %s and equiped=1 and weapon_name='Wood Shield'"
    cursor.execute(consulta, (player_id,))
    woodshield_equiped = cursor.fetchone()
    if woodshield_equiped:
        inventory = inventory[:170] + "(equiped)".ljust(16) + inventory[170 + 1:]
    else:
        inventory = inventory[:170] + "".rjust(16) + inventory[170 + 1:]

    # shield = 197
    consulta = "SELECT lives_remaining FROM game_weapons WHERE game_id = %s and equiped=1 and weapon_name='Sword'"
    cursor.execute(consulta, (player_id,))
    lives_current_shield = cursor.fetchone()
    consulta = "SELECT count(*) FROM game_weapons WHERE game_id = %s and weapon_name='Sword'"
    cursor.execute(consulta, (player_id,))
    total_shield = cursor.fetchone()
    if total_sword[0] >= 1:
        inventory = inventory[:197] + f"{lives_current_shield}/{total_shield}".rjust(10) + inventory[197 + 1:]
    else:
        inventory = inventory[:197] + "0/0".rjust(10) + inventory[197 + 1:]
    # shield equiped = 212
    consulta = "SELECT equiped FROM game_weapons WHERE game_id = %s and equiped=1 and weapon_name='Sword'"
    cursor.execute(consulta, (player_id,))
    sword_equiped = cursor.fetchone()
    if sword_equiped:
        inventory = inventory[:212] + "(equiped)".ljust(16) + inventory[212 + 1:]
    else:
        inventory = inventory[:212] + "".rjust(16) + inventory[212 + 1:]


    return inventory
def inv_food(player_id):
    # Inventory
    inventory = inventory_food

    # vegetables i=76
    consulta = "SELECT count(*) FROM game_food WHERE game_id = %s and food_name='Vegetables'"
    cursor.execute(consulta, (player_id,))
    vegetables_int = cursor.fetchone()
    inventory = inventory[:76] + f"{vegetables_int[0]}".rjust(5) + inventory[76 + 1:]
    # fish i=97
    consulta = "SELECT count(*) FROM game_food WHERE game_id = %s and food_name='Fish'"
    cursor.execute(consulta, (player_id,))
    fish_int = cursor.fetchone()
    inventory = inventory[:97] + f"{fish_int[0]}".rjust(5) + inventory[97 + 1:]
    # meat i=120
    consulta = "SELECT count(*) FROM game_food WHERE game_id = %s and food_name='Meat'"
    cursor.execute(consulta, (player_id,))
    meat_int = cursor.fetchone()
    inventory = inventory[:118] + f"{meat_int[0]}".rjust(5) + inventory[118 + 1:]
    # salad i=160
    consulta = "SELECT count(*) FROM game_food WHERE game_id = %s and food_name='Salad'"
    cursor.execute(consulta, (player_id,))
    salad_int = cursor.fetchone()
    inventory = inventory[:160] + f"{salad_int[0]}".rjust(5) + inventory[160 + 1:]
    # pescatarian i=181
    consulta = "SELECT count(*) FROM game_food WHERE game_id = %s and food_name='Pescatarian'"
    cursor.execute(consulta, (player_id,))
    pescatarian_int = cursor.fetchone()
    inventory = inventory[:181] + f"{pescatarian_int[0]}".rjust(5) + inventory[181 + 1:]
    # roasted i=202
    consulta = "SELECT count(*) FROM game_food WHERE game_id = %s and food_name='Roasted'"
    cursor.execute(consulta, (player_id,))
    roasted_int = cursor.fetchone()
    inventory = inventory[:202] + f"{roasted_int[0]}".rjust(5) + inventory[202 + 1:]

    for i, char in enumerate(inventory):
        if char == "X":
            print(f"Posiciones i: {i}")

    return inventory

# Funcion insertar inventario dentro de cualquier mapa
def insertar_mapa(mapa, inventario):

    # Dividir cada string en líneas
    lineas_inv = inventario.split('\n')
    lineas_map = mapa.split('\n')

    resultado = ""
    for i in range(12):
        resultado += lineas_map[i][:59] + lineas_inv[i] + '\n'

    return resultado



# Funcion menu main
player_inventory_main = inv_main(diccionarios.player_dict["game_id"])
# Funcion menu weapons
player_inventory_weapons = inv_weapons(diccionarios.player_dict["game_id"])
# Funcion menu food
player_inventory_food = inv_food(diccionarios.player_dict["game_id"])

# Funcion insertar inv
map_solved = insertar_mapa(mapas.hyrule_map, player_inventory_main)
