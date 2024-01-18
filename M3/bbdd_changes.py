from M3 import diccionarios

main_dict_hyrule = {
        1: {1: {"tree_1": [4, [4, 5]]}},
        2: {1: {"tree_2": [4, [8, 48]]}},
        3: {1: {"tree_3": [4, [9, 46]]}},
        4: {2: {"chest_1": [1, [9, 48], {"isopen": False}]}},
        5: {3: {"sanctuary_0": [[6, 44], [9, 45], [9, 45], {"isopen": True}]}},
        6: {3: {"sanctuary_1": [[9, 31], [9, 32], [9, 33], {"isopen": False}]}},
        7: {4: {"enemy_1": [[9, 21], [9, 22], {"isdead": False, "current_hearts": 1}]}},
        8: {4: {"enemy_2": [[5, 36], [5, 37], {"isdead": False, "current_hearts": 9}]}},
        9: {5: {"fox_1": [1, [9, 53]]}},
    }


# Conector MySQL
import mysql.connector

config = {
    'user': 'zelda',
    'password': 'link',
    'host': '4.231.10.226',
    'database': 'zelda',
    'raise_on_warnings': True
}
connection = mysql.connector.connect(**config)
cursor = connection.cursor()


def region_selector(region):
    if region == "Hyrule":
        diccionario = diccionarios.main_dict_hyrule
    elif region == "Death mountain":
        diccionario = diccionarios.main_dict_death_mountain
    elif region == "Gerudo":
        diccionario = diccionarios.main_dict_gerudo
    elif region == "Necluda":
        diccionario = diccionarios.main_dict_necluda
    elif region == "Castle":
        diccionario = diccionarios.main_dict_hyrule

    return diccionario

def insert_data_game(game_id, region):

    # Query MYSQL tabla 'game'
    query = """
    UPDATE game
    SET blood_moon_countdown = %s,
        blood_moon_appearances = %s,
        hearts = %s,
        region = %s
    WHERE game_id = %s
    """

    # Variables que añadiremos
    data = (
        diccionarios.player_dict['blood_moon_countdown'],
        diccionarios.player_dict['blood_moon_appearances'],
        diccionarios.player_dict['hearts'],
        region,
        game_id
    )

    # ALTER TABLE query + data
    cursor.execute(query, data)

    # Guardar cambios en la tabla
    connection.commit()
def insert_data_food(game_id):
    for food_item in diccionarios.player_dict['food_inventory']:
        food_id = list(food_item.keys())[0]
        food_data = food_item[food_id]


        food_name = food_data["food_name"]
        quantity = food_data["quantity"]
        uses = food_data["uses"]

        # Verificar si la fila ya existe en la tabla
        check_query = "SELECT COUNT(*) FROM game_food WHERE food_name = %s AND game_id = %s"
        cursor.execute(check_query, (food_name, game_id))
        row_count = cursor.fetchone()[0]

        if row_count > 0:
            update_query = """
                    UPDATE game_food
                    SET quantity = %s, uses = %s
                    WHERE food_name = %s AND game_id = %s
                """
            cursor.execute(update_query, (quantity, uses, food_name, game_id))
        else:
            insert_query = """
                    INSERT INTO game_food (game_id, food_name, quantity, uses)
                    VALUES (%s, %s, %s, %s)
                """
            cursor.execute(insert_query, (game_id, food_name, quantity, uses))

    connection.commit()
def insert_data_weapons(game_id):

    # Weapons
    for weapon_item in diccionarios.player_dict['weapons_inventory']:
        weapon_id = list(weapon_item.keys())[0]
        weapon_data = weapon_item[weapon_id]

        weapon_name = weapon_data["name"]
        quantity = weapon_data["quantity"]
        uses = weapon_data["uses"]
        lives_remaining = 9

        # Verificar si la fila ya existe en la tabla
        check_query = "SELECT COUNT(*) FROM game_weapons WHERE weapon_name = %s AND game_id = %s"
        cursor.execute(check_query, (weapon_name, game_id))
        row_count = cursor.fetchone()[0]

        if row_count > 0:
            update_query = """
                    UPDATE game_weapons
                    SET quantity = %s, uses = %s, lives_remaining = %s
                    WHERE weapon_name = %s AND game_id = %s
                """
            cursor.execute(update_query, (quantity, uses, lives_remaining, weapon_name, game_id))
        else:
            insert_query = """
                    INSERT INTO game_weapons (game_id, weapon_name, lives_remaining, quantity, uses)
                    VALUES (%s, %s, %s, %s, %s)
                """
            cursor.execute(insert_query, (game_id, weapon_name, lives_remaining, quantity, uses))

    connection.commit()

    # Shields
    for shield_item in diccionarios.player_dict['shields_inventory']:
        shield_id = list(shield_item.keys())[0]
        shield_data = shield_item[shield_id]

        shield_name = shield_data["name"]
        quantity = shield_data["quantity"]
        uses = shield_data["uses"]
        lives_remaining = 5

        # Verificar si la fila ya existe en la tabla
        check_query = "SELECT COUNT(*) FROM game_weapons WHERE weapon_name = %s AND game_id = %s"
        cursor.execute(check_query, (shield_name, game_id))
        row_count = cursor.fetchone()[0]

        if row_count > 0:
            update_query = """
                    UPDATE game_weapons
                    SET quantity = %s, uses = %s, lives_remaining = %s
                    WHERE weapon_name = %s AND game_id = %s
                """
            cursor.execute(update_query, (quantity, uses, lives_remaining, shield_name, game_id))
        else:
            insert_query = """
                    INSERT INTO game_weapons (game_id, weapon_name, quantity, uses, lives_remaining)
                    VALUES (%s, %s, %s, %s, %s)
                """
            cursor.execute(insert_query, (game_id, shield_name, quantity, uses, lives_remaining))

    connection.commit()
def insert_data_enemies(game_id, region):
    diccionario = region_selector(region)
    records_with_key_4 = {key: value for key, value in diccionario.items() if 4 in value}
    for key1, value1 in records_with_key_4.items():
        for key2, value2 in value1.items():
            enemy_id = list(value2.keys())[0]
            current_hearts = value2[enemy_id][2]['current_hearts']
            xpos = value2[enemy_id][0][0]
            ypos = value2[enemy_id][0][1]
            xpos2 = value2[enemy_id][1][0]
            ypos2 = value2[enemy_id][1][1]
            is_dead = value2[enemy_id][2]['isdead']

            check_query = "DELETE FROM game_enemies WHERE enemy_id = %s AND game_id = %s AND region = %s"
            cursor.execute(check_query, (enemy_id, game_id, region))
            insert_query = """
                    INSERT INTO game_enemies (game_id, region, enemy_id, xpos, ypos, xpos2, ypos2, is_dead, lives_remaining)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
            cursor.execute(insert_query, (game_id, region, enemy_id, xpos, ypos, xpos2, ypos2, is_dead, current_hearts))

    connection.commit()
def insert_data_chests(game_id, region):
    diccionario = region_selector(region)
    records_with_key_2 = {key: value for key, value in diccionario.items() if 2 in value}
    for key1, value1 in records_with_key_2.items():
        for key2, value2 in value1.items():
            chest_id = list(value2.keys())[0]
            is_open = value2[chest_id][2]['isopen']

            check_query = "DELETE FROM game_chests_opened WHERE chest_id = %s AND game_id = %s AND region = %s"
            cursor.execute(check_query, (chest_id, game_id, region))
            insert_query = """
                            INSERT INTO game_chests_opened (game_id, region, chest_id, is_open)
                            VALUES (%s, %s, %s, %s)
                            """
            cursor.execute(insert_query, (game_id, region, chest_id, is_open))

        connection.commit()
def insert_data_sanctuaries(game_id, region):
    diccionario = region_selector(region)
    records_with_key_3 = {key: value for key, value in diccionario.items() if 3 in value}
    for key1, value1 in records_with_key_3.items():
        for key2, value2 in value1.items():
            sanctuary_id = list(value2.keys())[0]
            is_open = value2[sanctuary_id][3]['isopen']

            check_query = "DELETE FROM game_sanctuaries_opened WHERE sanctuary_id = %s AND game_id = %s AND region = %s"
            cursor.execute(check_query, (sanctuary_id, game_id, region))
            insert_query = """
                            INSERT INTO game_sanctuaries_opened (game_id, region, sanctuary_id, is_open)
                            VALUES (%s, %s, %s, %s)
                            """
            cursor.execute(insert_query, (game_id, region, sanctuary_id, is_open))

        connection.commit()
def insert_data_trees_fell(game_id, region):
    diccionario = region_selector(region)
    records_with_key_1 = {key: value for key, value in diccionario.items() if 1 in value}
    for key1, value1 in records_with_key_1.items():
        for key2, value2 in value1.items():
            for sub_key, sub_value in value2.items():
                tree_id = sub_key
                durability = sub_value[0]
                if durability == 0:
                    is_cutted = True
                else:
                    is_cutted = False

                check_query = "DELETE FROM game_trees_fell WHERE tree_id = %s AND game_id = %s AND region = %s"
                cursor.execute(check_query, (tree_id, game_id, region))

                insert_query = """
                                INSERT INTO game_trees_fell (game_id, region, tree_id, is_cutted)
                                VALUES (%s, %s, %s, %s)
                                """
                cursor.execute(insert_query, (game_id, region, tree_id, is_cutted))

    connection.commit()


def download_data_mysql(game_id):

    game_data = []
    food_data = []
    weapons_data = []
    enemies_data = []
    chests_data = []
    sanctuaries_data = []
    trees_data = []

    # game table
    game_query = ("SELECT user_name,blood_moon_countdown,blood_moon_appearances,hearts,region FROM game WHERE game_id = %s")
    cursor.execute(game_query, (game_id,))
    game_data = cursor.fetchall()

    user_name, blood_moon_countdown, blood_moon_appearances, hearts, region = game_data[0]
    diccionarios.player_dict['user_name'] = user_name
    diccionarios.player_dict['blood_moon_countdown'] = blood_moon_countdown
    diccionarios.player_dict['blood_moon_appearances'] = blood_moon_appearances
    diccionarios.player_dict['hearts'] = hearts
    diccionarios.player_dict['region'] = region

    # game_food table
    food_query = "SELECT food_name,quantity,uses FROM game_food WHERE game_id = %s"
    cursor.execute(food_query, (game_id,))
    food_data = cursor.fetchall()

    diccionarios.player_dict['food_inventory'] = []
    for item in food_data:
        food_name, quantity, uses = item
        new_food_entry = {
            len(diccionarios.player_dict['food_inventory']) + 1: {"food_name": food_name, "quantity": quantity, "uses": uses}}
        diccionarios.player_dict['food_inventory'].append(new_food_entry)

    # game_weapons table
    weapons_query = "SELECT weapon_name,quantity,uses FROM game_weapons WHERE weapon_name LIKE '%Sword%' and game_id = %s"
    cursor.execute(weapons_query, (game_id,))
    weapons_data = cursor.fetchall()

    diccionarios.player_dict['weapons_inventory'] = []
    for item in weapons_data:
        weapon_name, quantity, uses = item
        new_weapon_entry = {
            len(diccionarios.player_dict['weapons_inventory']) + 1: {"name": weapon_name, "quantity": quantity, "uses": uses}}
        diccionarios.player_dict['weapons_inventory'].append(new_weapon_entry)

    shields_query = "SELECT weapon_name,quantity,uses FROM game_weapons WHERE weapon_name LIKE '%Shield%' and game_id = %s"
    cursor.execute(shields_query, (game_id,))
    shields_data = cursor.fetchall()
    diccionarios.player_dict['shields_inventory'] = []
    for item in shields_data:
        weapon_name, quantity, uses = item
        new_shield_entry = {
            len(diccionarios.player_dict['shields_inventory']) + 1: {"name": weapon_name, "quantity": quantity,
                                                                     "uses": uses}}
        diccionarios.player_dict['shields_inventory'].append(new_shield_entry)

    # game_enemies table
    enemies_query = "SELECT region,enemy_id, xpos, ypos, xpos2, ypos2, is_dead, lives_remaining FROM game_enemies WHERE game_id = %s"
    cursor.execute(enemies_query, (game_id,))
    enemies_data = cursor.fetchall()
    for item in enemies_data:
        region, enemy_id, xpos, ypos, xpos2, ypos2, is_dead, lives_remaining = item
        diccionario = region_selector(region)
        for key, value in diccionario.items():
            if 4 in value:
                for sub_key, sub_value in value[4].items():
                    sub_value[0][0] = xpos
                    sub_value[0][1] = ypos
                    sub_value[1][0] = xpos2
                    sub_value[1][1] = ypos2
                    sub_value[2]["isdead"] = is_dead
                    sub_value[2]["current_hearts"] = lives_remaining

    # game_chests_opened table
    chests_query = "SELECT region, chest_id, is_open FROM game_chests_opened WHERE game_id = %s"
    cursor.execute(chests_query, (game_id,))
    chests_data = cursor.fetchall()
    for item in chests_data:
        region, chest_id, is_open = item
        if is_open == 1:
            is_open = True
        else:
            is_open = False
        diccionario = region_selector(region)
        for key, value in diccionario.items():
            if 2 in value:
                for sub_key, sub_value in value.items():
                    sub_key2 = next(iter(sub_value))
                    sub_value[sub_key2][2]['isopen'] = is_open

    # game_sanctuaries_opened table
    sanctuaries_query = "SELECT game_id, region, sanctuary_id, is_open FROM game_sanctuaries_opened WHERE game_id = %s"
    cursor.execute(sanctuaries_query, (game_id,))
    sanctuaries_data = cursor.fetchall()
    for item in sanctuaries_data:
        game_id, region, sanctuary_id, is_open = item
        if is_open == 1:
            is_open = True
        else:
            is_open = False
        diccionario = region_selector(region)
        for key, value in diccionario.items():
            if 3 in value:
                for sub_key, sub_value in value.items():
                    sub_key2 = next(iter(sub_value))
                    sub_value[sub_key2][3]['isopen'] = is_open

    # game_trees_fell table
    sanctuaries_query = "SELECT game_id, region, tree_id, is_cutted FROM game_trees_fell WHERE game_id = %s"
    cursor.execute(sanctuaries_query, (game_id,))
    trees_data = cursor.fetchall()
    for item in trees_data:
        game_id, region, tree_id, is_cutted = item
        diccionario = region_selector(region)
        for key, value in diccionario.items():
            if 1 in value:
                for sub_key, sub_value in value.items():
                    sub_key2 = next(iter(sub_value))
                    if is_cutted > 0:
                        sub_value[sub_key2][0] = 4
                    else:
                        sub_value[sub_key2][0] = 0



############################################


# GUARDAR DATOS PARTIDA
# insert_data_game(game_id, region)
# insert_data_food(game_id)
# insert_data_weapons(game_id)
# insert_data_enemies(game_id, region)
# insert_data_chests(game_id, region)
# insert_data_sanctuaries(game_id, region)
# insert_data_trees_fell(game_id, region)
#
#
# # CARGAR DATOS PARTIDA
# download_data_mysql(game_id)

