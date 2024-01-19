# Funcion que se encarga de mostrar los diferentes inventarios haciendo querys a la BBDD

# COSAS ARREGLAR
# en bbdd name_user = max length(11)
# Arreglar name_user, hearts, blood moon
# Solo puede tener dos armas
# Añadir maximo 99 armas
# Añadir maximo 99 food
# guardar usos arma equipada si se cambia

import diccionarios




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
    inventory = inventory[:78] + f"{diccionarios.player_dict['blood_moon_countdown']}".rjust(3) + inventory[78 + 1:]

    # Inventory - equipment
    # weapon_1 = 106
    if diccionarios.player_dict['weapons_equipped'][0][1]['weapon_name'] in ("Wood Sword", "Sword"):
        weapon_1 = diccionarios.player_dict['weapons_equipped'][0][1]['weapon_name']
        inventory = inventory[:106] + f"{weapon_1}".rjust(17) + inventory[106 + 1:]
    else:
        inventory = inventory[:106] + "".rjust(17) + inventory[106 + 1:]

    # weapon_2 (shield) = 127
    if diccionarios.player_dict['weapons_equipped'][1][2]['shield_name'] in ("Wood Shield", "Shield"):
        weapon_2 = diccionarios.player_dict['weapons_equipped'][1][2]['shield_name']
        inventory = inventory[:127] + f"{weapon_2}".rjust(17) + inventory[127 + 1:]
    else:
        inventory = inventory[:127] + "".rjust(17) + inventory[127 + 1:]

    # food = 174
    food_remaining = sum(next(iter(item.values()))["quantity"] for item in diccionarios.player_dict['food_inventory'])
    inventory = inventory[:174] + f"{food_remaining}".rjust(12) + inventory[174 + 1:]

    # weapons = 198
    weapons_remaining = sum(
        next(iter(item.values()))["quantity"] for item in diccionarios.player_dict['weapons_inventory'])
    inventory = inventory[:198] + f"{weapons_remaining}".rjust(9) + inventory[198 + 1:]

    return inventory


def inv_weapons(player_id):
    # Inventory
    inventory = inventory_weapons

    # wood_sword = 75
    # wood_sword equiped = 86
    if diccionarios.player_dict['weapons_equipped'][0][1]['weapon_name'] == "Wood Sword":
        lives_current_woodsword = diccionarios.player_dict['weapons_equipped'][0][1]['uses_left_woodsword']
        total_woodsword = diccionarios.player_dict['weapons_inventory'][0][1]['quantity']
        inventory = inventory[:75] + f"{lives_current_woodsword}/{total_woodsword}".rjust(6) + inventory[75 + 1:]
        inventory = inventory[:86] + "(equiped)".ljust(16) + inventory[86 + 1:]
    if not diccionarios.player_dict['weapons_equipped'][0][1]['weapon_name'] == "Wood Sword":
        lives_current_woodsword = diccionarios.player_dict['weapons_equipped'][0][1]['uses_left_woodsword']
        total_woodsword = diccionarios.player_dict['weapons_inventory'][0][1]['quantity']
        inventory = inventory[:75] + f"{lives_current_woodsword}/{total_woodsword}".rjust(6) + inventory[75 + 1:]
        inventory = inventory[:86] + "".ljust(16) + inventory[86 + 1:]



    # sword = 112
    # sword equiped = 128
    if diccionarios.player_dict['weapons_equipped'][0][1]['weapon_name'] == "Sword":
        lives_current_sword = diccionarios.player_dict['weapons_equipped'][0][1]['uses_left_sword']
        total_sword = diccionarios.player_dict['weapons_inventory'][1][2]['quantity']
        inventory = inventory[:112] + f"{lives_current_sword}/{total_sword}".rjust(11) + inventory[112 + 1:]
        inventory = inventory[:128] + "(equiped)".ljust(16) + inventory[128 + 1:]
    if not diccionarios.player_dict['weapons_equipped'][0][1]['weapon_name'] == "Sword":
        lives_current_sword = diccionarios.player_dict['weapons_equipped'][0][1]['uses_left_sword']
        total_sword = diccionarios.player_dict['weapons_inventory'][1][2]['quantity']
        inventory = inventory[:112] + f"{lives_current_sword}/{total_sword}".rjust(11) + inventory[112 + 1:]
        inventory = inventory[:128] + "".ljust(16) + inventory[128 + 1:]


    # wood_shield = 160
    # wood_shield equiped = 170
    if diccionarios.player_dict['weapons_equipped'][1][2]['shield_name'] == "Wood Shield":
        lives_current_woodshield = diccionarios.player_dict['weapons_equipped'][1][2]['uses_left_woodshield']
        total_woodshield = diccionarios.player_dict['shields_inventory'][0][1]['quantity']
        inventory = inventory[:160] + f"{lives_current_woodshield}/{total_woodshield}".rjust(5) + inventory[160 + 1:]
        inventory = inventory[:170] + "(equiped)".ljust(16) + inventory[170 + 1:]
    if not diccionarios.player_dict['weapons_equipped'][1][2]['shield_name'] == "Wood Shield":
        lives_current_woodshield = diccionarios.player_dict['weapons_equipped'][1][2]['uses_left_woodshield']
        total_woodshield = diccionarios.player_dict['shields_inventory'][0][1]['quantity']
        inventory = inventory[:160] + f"{lives_current_woodshield}/{total_woodshield}".rjust(5) + inventory[160 + 1:]
        inventory = inventory[:170] + "".ljust(16) + inventory[170 + 1:]


    # shield = 197
    # shield equiped = 212
    if diccionarios.player_dict['weapons_equipped'][1][2]['shield_name'] == "Shield":
        lives_current_shield = diccionarios.player_dict['weapons_equipped'][1][2]['uses_left_shield']
        total_shield = diccionarios.player_dict['shields_inventory'][1][2]['quantity']
        inventory = inventory[:197] + f"{lives_current_shield}/{total_shield}".rjust(10) + inventory[197 + 1:]
        inventory = inventory[:212] + "(equiped)".ljust(16) + inventory[212 + 1:]
    if not diccionarios.player_dict['weapons_equipped'][1][2]['shield_name'] == "Shield":
        lives_current_shield = diccionarios.player_dict['weapons_equipped'][1][2]['uses_left_shield']
        total_shield = diccionarios.player_dict['shields_inventory'][1][2]['quantity']
        inventory = inventory[:197] + f"{lives_current_shield}/{total_shield}".rjust(10) + inventory[197 + 1:]
        inventory = inventory[:212] + "".ljust(16) + inventory[212 + 1:]


    return inventory


def inv_food(player_id):
    # Inventory
    inventory = inventory_food

    # vegetables i=76
    vegetables_int = diccionarios.player_dict['food_inventory'][0][1]['quantity']
    inventory = inventory[:76] + f"{vegetables_int}".rjust(5) + inventory[76 + 1:]
    # fish i=97
    fish_int = diccionarios.player_dict['food_inventory'][1][2]['quantity']
    inventory = inventory[:97] + f"{fish_int}".rjust(5) + inventory[97 + 1:]
    # meat i=120
    meat_int = diccionarios.player_dict['food_inventory'][2][3]['quantity']
    inventory = inventory[:118] + f"{meat_int}".rjust(5) + inventory[118 + 1:]
    # salad i=160
    salad_int = diccionarios.player_dict['food_inventory'][3][4]['quantity']
    inventory = inventory[:160] + f"{salad_int}".rjust(5) + inventory[160 + 1:]
    # pescatarian i=181
    pescatarian_int = diccionarios.player_dict['food_inventory'][4][5]['quantity']
    inventory = inventory[:181] + f"{pescatarian_int}".rjust(5) + inventory[181 + 1:]
    # roasted i=202
    roasted_int = diccionarios.player_dict['food_inventory'][5][6]['quantity']
    inventory = inventory[:202] + f"{roasted_int}".rjust(5) + inventory[202 + 1:]



    return inventory


# Funcion insertar inventario dentro de cualquier mapa
def insertar_mapa(mapa, inventario):
    #actualizamos mapas
    if "Inventory" in inventario :
        inventario = inv_main(diccionarios.player_dict["game_id"])
    elif " * * * * * *  Food" in inventario:
        inventario = inv_food(diccionarios.player_dict["game_id"])
    elif "* Weapons" in inventario:
        inventario = inv_weapons(diccionarios.player_dict["game_id"])




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