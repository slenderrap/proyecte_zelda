import diccionarios

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

    # Variables que aÃ±adiremos
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
        equipped = 0

        # Verificar si la fila ya existe en la tabla
        check_query = "SELECT COUNT(*) FROM game_weapons WHERE weapon_name = %s AND game_id = %s"
        cursor.execute(check_query, (weapon_name, game_id))
        row_count = cursor.fetchone()[0]

        if row_count > 0:
            update_query = """
                    UPDATE game_weapons
                    SET equipped = %s, quantity = %s, uses = %s
                    WHERE weapon_name = %s AND game_id = %s
                """
            cursor.execute(update_query, (equipped, quantity, uses, weapon_name, game_id))
        else:
            insert_query = """
                    INSERT INTO game_weapons (game_id, weapon_name, equipped, quantity, uses)
                    VALUES (%s, %s, %s, %s, %s)
                """
            cursor.execute(insert_query, (game_id, weapon_name, equipped, quantity, uses))

    connection.commit()

    # Shields
    for shield_item in diccionarios.player_dict['shields_inventory']:
        shield_id = list(shield_item.keys())[0]
        shield_data = shield_item[shield_id]

        shield_name = shield_data["name"]
        quantity = shield_data["quantity"]
        uses = shield_data["uses"]
        equipped = 0

        # Verificar si la fila ya existe en la tabla
        check_query = "SELECT COUNT(*) FROM game_weapons WHERE weapon_name = %s AND game_id = %s"
        cursor.execute(check_query, (shield_name, game_id))
        row_count = cursor.fetchone()[0]

        if row_count > 0:
            update_query = """
                    UPDATE game_weapons
                    SET equipped = %s, quantity = %s, uses = %s
                    WHERE weapon_name = %s AND game_id = %s
                """
            cursor.execute(update_query, (equipped, quantity, uses, shield_name, game_id))
        else:
            insert_query = """
                    INSERT INTO game_weapons (game_id, weapon_name, equipped, quantity, uses)
                    VALUES (%s, %s, %s, %s, %s)
                """
            cursor.execute(insert_query, (game_id, shield_name, equipped, quantity, uses))
    connection.commit()

    # Weapon equipped
    for weapon_slot in diccionarios.player_dict['weapons_equipped']:
        for slot_id, weapon_info in weapon_slot.items():
            if 'weapon_name' in weapon_info:
                weapon_name = weapon_info['weapon_name']
                uses_left_key = f'uses_left_{weapon_name.lower().replace(" ", "")}'
                uses_left = weapon_info.get(uses_left_key, 0)
                equipped = 1

                update_query = """
                                UPDATE game_weapons
                                SET equipped = %s, uses_left = %s
                                WHERE weapon_name = %s AND game_id = %s
                                """
                cursor.execute(update_query, (equipped, uses_left, weapon_name, game_id))

            elif 'shield_name' in weapon_info:
                shield_name = weapon_info['shield_name']
                uses_left_key = f'uses_left_{shield_name.lower().replace(" ", "")}'
                uses_left = weapon_info.get(uses_left_key, 0)

                equipped = 1

                update_query = """
                                    UPDATE game_weapons
                                    SET equipped = %s, uses_left = %s
                                    WHERE weapon_name = %s AND game_id = %s
                                    """
                cursor.execute(update_query, (equipped, uses_left, shield_name, game_id))
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
    weapons_equipped_data = []
    weapons__uses_equipped_data = []
    weapons_data = []
    shields_data = []
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
    game_query = ("select count(*) from game_sanctuaries_opened where game_id = %s and is_open=1")
    cursor.execute(game_query, (game_id,))
    hearts_max_data = cursor.fetchone()
    diccionarios.player_dict['hearts_max'] = hearts_max_data[0] + 2
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

    # weapons_equipped_data
    weapons_uses_equipped_query = "SELECT weapon_name, uses_left FROM game_weapons WHERE game_id = %s"
    cursor.execute(weapons_uses_equipped_query, (game_id,))
    weapons_uses_equipped_data = cursor.fetchall()
    for item in weapons_uses_equipped_data:
        weapon_name, uses_left = item
        if uses_left is None:
            if "Wood" in weapon_name:
                uses_left = 5
            else:
                uses_left = 9
        if weapon_name == "Wood Sword":
            diccionarios.player_dict['weapons_equipped'][0][1]['uses_left_woodsword'] = uses_left
        elif weapon_name == "Sword":
            diccionarios.player_dict['weapons_equipped'][0][1]['uses_left_sword'] = uses_left
        elif weapon_name == "Wood Shield":
            diccionarios.player_dict['weapons_equipped'][1][2]['uses_left_woodshield'] = uses_left
        elif weapon_name == "Shield":
            diccionarios.player_dict['weapons_equipped'][1][2]['uses_left_shield'] = uses_left

    weapons_equipped_query = "SELECT weapon_name FROM game_weapons WHERE equipped = 1 AND game_id = %s"
    cursor.execute(weapons_equipped_query, (game_id,))
    weapons_equipped_data = cursor.fetchall()
    for weapon_equipped_name, in weapons_equipped_data:
        if "Sword" in weapon_equipped_name:
            diccionarios.player_dict['weapons_equipped'][0][1]['weapon_name'] = weapon_equipped_name
        if "Shield" in weapon_equipped_name:
            diccionarios.player_dict['weapons_equipped'][1][2]['shield_name'] = weapon_equipped_name


    # game_enemies table
    enemies_query = "SELECT enemy_id, xpos, ypos, xpos2, ypos2, is_dead, lives_remaining FROM game_enemies WHERE game_id = %s and region = %s ORDER BY enemy_id"
    cursor.execute(enemies_query, (game_id, region))
    enemies_data = cursor.fetchall()
    diccionario = region_selector(region)
    # print("Diccionario 1")
    # print(diccionario)
    for key, value in diccionario.items():
        if 4 in value:
            if isinstance(value[4], dict):
                for enemy_key, enemy_data in value[4].items():
                    if enemy_key == "enemy_1":
                        enemy_data[0][0] = enemies_data[0][1]
                        enemy_data[0][1] = enemies_data[0][2]
                        enemy_data[1][0] = enemies_data[0][3]
                        enemy_data[1][1] = enemies_data[0][4]
                        if enemies_data[0][5] == 0:
                            enemy_data[2]["isdead"] = False
                        else:
                            enemy_data[2]["isdead"] = True
                        enemy_data[2]["current_hearts"] = enemies_data[0][6]
                    elif enemy_key == "enemy_2":
                        # Datos SQL
                        enemy_data[0][0] = enemies_data[1][1]
                        enemy_data[0][1] = enemies_data[1][2]
                        enemy_data[1][0] = enemies_data[1][3]
                        enemy_data[1][1] = enemies_data[1][4]
                        if enemies_data[1][5] == 0:
                            enemy_data[2]["isdead"] = False
                        else:
                            enemy_data[2]["isdead"] = True
                        enemy_data[2]["current_hearts"] = enemies_data[1][6]
    # print()
    # print(diccionario)
    # input()


    # game_chests_opened table
    chests_query = "SELECT chest_id, is_open FROM game_chests_opened WHERE game_id = %s and region = %s"
    cursor.execute(chests_query, (game_id, region))
    chests_data = cursor.fetchall()
    diccionario = region_selector(region)

    # print("Diccionario antes")
    # print(diccionario)
    for row in chests_data:
        chest_id, is_open = row
        if is_open == 1:
            is_open = True
        else:
            is_open = False
        for key, value in diccionario.items():
            if 2 in value:
                if isinstance(value[2], dict):
                    for chest_key, chest_value in value[2].items():
                        if chest_key == chest_id:
                            chest_value[2]['isopen'] = is_open
                            if not is_open:
                                chest_value[0] = 1
                            else:
                                chest_value[0] = 0
    # print("Diccionario despues")
    # print(diccionario)
    # input()


    # game_sanctuaries_opened table
    sanctuaries_query = "SELECT sanctuary_id, is_open FROM game_sanctuaries_opened WHERE game_id = %s"
    cursor.execute(sanctuaries_query,  (game_id,))
    sanctuaries_data = cursor.fetchall()
    diccionario = region_selector(region)

    # print("Diccionario antes")
    # print(diccionario)
    for row in sanctuaries_data:
        sanctuary_id, is_open = row
        if is_open == 1:
            is_open = True
        else:
            is_open = False
        for key, value in diccionario.items():
            if 3 in value:
                if isinstance(value[3], dict):
                    for sanctuary_key, sanctuary_value in value[3].items():
                        if sanctuary_id ==  sanctuary_key:
                            sanctuary_value[3]['isopen'] = is_open


    # print("Diccionario despues")
    # print(diccionario)
    # input()




    # game_trees_fell table
    sanctuaries_query = "SELECT tree_id, is_cutted FROM game_trees_fell WHERE game_id = %s AND region = %s"
    cursor.execute(sanctuaries_query, (game_id, region))
    trees_data = cursor.fetchall()

    # print("Diccionario antes")
    # print(diccionario)
    for row in trees_data:
        tree_id, is_cutted = row
        if is_cutted == 1:
            is_cutted = True
        else:
            is_cutted = False

        for key, value in diccionario.items():
            if 1 in value:
                if isinstance(value[1], dict):
                    for tree_key, tree_value in value[1].items():
                        if tree_id == tree_key:
                            if is_cutted:
                                tree_value[0] = 0
                            else:
                                tree_value[0] = 4

    # print("Diccionario 2")
    # print(diccionario)
    # input()
def guardar_datos_partida(game_id, region):
    insert_data_game(game_id, region)
    insert_data_food(game_id)
    insert_data_weapons(game_id)
    insert_data_enemies(game_id, region)
    insert_data_chests(game_id, region)
    insert_data_sanctuaries(game_id, region)
    insert_data_trees_fell(game_id, region)

def guardar_datos_new_game(game_id, region):
    insert_data_game(game_id, region)
    insert_data_food(game_id)
    insert_data_enemies(game_id, region)
    insert_data_chests(game_id, region)
    insert_data_sanctuaries(game_id, region)
    insert_data_trees_fell(game_id, region)

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

#download_data_mysql(game_id)


def download_all_data_mysql(game_id, region):

    game_data = []
    food_data = []
    weapons_equipped_data = []
    weapons__uses_equipped_data = []
    weapons_data = []
    shields_data = []
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

    game_query = ("select count(*) from game_sanctuaries_opened where game_id = %s and is_open=1")
    cursor.execute(game_query, (game_id,))
    hearts_max_data = cursor.fetchone()
    diccionarios.player_dict['hearts_max'] = hearts_max_data[0] +2


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

    # weapons_equipped_data
    weapons_uses_equipped_query = "SELECT weapon_name, uses_left FROM game_weapons WHERE game_id = %s"
    cursor.execute(weapons_uses_equipped_query, (game_id,))
    weapons_uses_equipped_data = cursor.fetchall()
    for item in weapons_uses_equipped_data:
        weapon_name, uses_left = item
        if uses_left is None:
            if "Wood" in weapon_name:
                uses_left = 5
            else:
                uses_left = 9
        if weapon_name == "Wood Sword":
            diccionarios.player_dict['weapons_equipped'][0][1]['uses_left_woodsword'] = uses_left
        elif weapon_name == "Sword":
            diccionarios.player_dict['weapons_equipped'][0][1]['uses_left_sword'] = uses_left
        elif weapon_name == "Wood Shield":
            diccionarios.player_dict['weapons_equipped'][1][2]['uses_left_woodshield'] = uses_left
        elif weapon_name == "Shield":
            diccionarios.player_dict['weapons_equipped'][1][2]['uses_left_shield'] = uses_left

    weapons_equipped_query = "SELECT weapon_name FROM game_weapons WHERE equipped = 1 AND game_id = %s"
    cursor.execute(weapons_equipped_query, (game_id,))
    weapons_equipped_data = cursor.fetchall()
    for weapon_equipped_name, in weapons_equipped_data:
        if "Sword" in weapon_equipped_name:
            diccionarios.player_dict['weapons_equipped'][0][1]['weapon_name'] = weapon_equipped_name
        if "Shield" in weapon_equipped_name:
            diccionarios.player_dict['weapons_equipped'][1][2]['shield_name'] = weapon_equipped_name



    # game_enemies table
    enemies_query = "SELECT enemy_id, xpos, ypos, xpos2, ypos2, is_dead, lives_remaining FROM game_enemies WHERE game_id = %s and region = %s ORDER BY enemy_id"
    cursor.execute(enemies_query, (game_id, region))
    enemies_data = cursor.fetchall()
    diccionario = region_selector(region)
    # print("Diccionario 1")
    # print(diccionario)
    for key, value in diccionario.items():
        if 4 in value:
            if isinstance(value[4], dict):
                for enemy_key, enemy_data in value[4].items():
                    if enemy_key == "enemy_1":
                        enemy_data[0][0] = enemies_data[0][1]
                        enemy_data[0][1] = enemies_data[0][2]
                        enemy_data[1][0] = enemies_data[0][3]
                        enemy_data[1][1] = enemies_data[0][4]
                        if enemies_data[0][5] == 0:
                            enemy_data[2]["isdead"] = False
                        else:
                            enemy_data[2]["isdead"] = True
                        enemy_data[2]["current_hearts"] = enemies_data[0][6]
                    elif enemy_key == "enemy_2":
                        # Datos SQL
                        enemy_data[0][0] = enemies_data[1][1]
                        enemy_data[0][1] = enemies_data[1][2]
                        enemy_data[1][0] = enemies_data[1][3]
                        enemy_data[1][1] = enemies_data[1][4]
                        if enemies_data[1][5] == 0:
                            enemy_data[2]["isdead"] = False
                        else:
                            enemy_data[2]["isdead"] = True
                        enemy_data[2]["current_hearts"] = enemies_data[1][6]
    # print()
    # print(diccionario)
    # input()


    # game_chests_opened table
    chests_query = "SELECT chest_id, is_open FROM game_chests_opened WHERE game_id = %s and region = %s"
    cursor.execute(chests_query, (game_id, region))
    chests_data = cursor.fetchall()
    diccionario = region_selector(region)

    # print("Diccionario antes")
    # print(diccionario)
    for row in chests_data:
        chest_id, is_open = row
        if is_open == 1:
            is_open = True
        else:
            is_open = False
        for key, value in diccionario.items():
            if 2 in value:
                if isinstance(value[2], dict):
                    for chest_key, chest_value in value[2].items():
                        if chest_key == chest_id:
                            chest_value[2]['isopen'] = is_open
                            if not is_open:
                                chest_value[0] = 1
                            else:
                                chest_value[0] = 0
    # print("Diccionario despues")
    # print(diccionario)
    # input()


    # game_sanctuaries_opened table
    sanctuaries_query = "SELECT sanctuary_id, is_open FROM game_sanctuaries_opened WHERE game_id = %s and region = %s"
    cursor.execute(sanctuaries_query, (game_id,))
    sanctuaries_data = cursor.fetchall()
    diccionario = region_selector(region)
    # print(diccionario)
    # print("Diccionario antes")
    # print(diccionario)
    for row in sanctuaries_data:
        sanctuary_id, is_open = row
        if is_open == 1:
            is_open = True
        else:
            is_open = False
        for key, value in diccionario.items():
            if 3 in value:
                if isinstance(value[3], dict):
                    for sanctuary_key, sanctuary_value in value[3].items():
                        if sanctuary_id ==  sanctuary_key:
                            sanctuary_value[3]['isopen'] = is_open


    # print("Diccionario despues")
    # print(diccionario)
    # input()




    # game_trees_fell table
    sanctuaries_query = "SELECT tree_id, is_cutted FROM game_trees_fell WHERE game_id = %s AND region = %s"
    cursor.execute(sanctuaries_query, (game_id, region))
    trees_data = cursor.fetchall()

    # print("Diccionario antes")
    # print(diccionario)
    for row in trees_data:
        tree_id, is_cutted = row
        if is_cutted == 1:
            is_cutted = True
        else:
            is_cutted = False

        for key, value in diccionario.items():
            if 1 in value:
                if isinstance(value[1], dict):
                    for tree_key, tree_value in value[1].items():
                        if tree_id == tree_key:
                            if is_cutted:
                                tree_value[0] = 0
                            else:
                                tree_value[0] = 4

    # print("Diccionario 2")
    # print(diccionario)
    # input()




def load_all_data(game_id):
    regiones = ['Hyrule', 'Death mountain', 'Gerudo', 'Necluda', 'Castle']
    for i in range (4):
        region = regiones[i]
        download_all_data_mysql(game_id, region)