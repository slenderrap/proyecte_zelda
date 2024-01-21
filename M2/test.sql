use zelda;




/* Selección por tabla = X */
select * from game;
select * from game_food;
select * from game_weapons;
select * from game_enemies;
select * from game_chests_opened;
select * from game_sanctuaries_opened;
select * from game_trees_fell;

/* insert data */
INSERT INTO game (game_id, user_name, blood_moon_countdown, blood_moon_appearances, hearts, region, created_at, changed_at)
VALUES
(1, 'Link', 0, 0, 3, 'Hyrule', NOW(), NOW());

INSERT INTO game_food (game_id, food_name, quantity, uses, created_at, changed_at)
VALUES
(1, 'Fish', 5, 5, NOW(), NOW());

INSERT INTO game_weapons (game_id, weapon_name, quantity, uses)
VALUES
(1, 'Wood Sword', 23, 23);

INSERT INTO game_enemies (game_id, region, enemy_id, xpos, ypos, xpos2, ypos2, is_dead, lives_remaining)
VALUES
(1, 'Hyrule', 'enemy_2', 50, 50, 50, 50, True, 23);

INSERT INTO game_chests_opened (game_id, region, chest_id, xpos, ypos, is_open, created_at, changed_at)
VALUES
(1, 'Hyrule', 'chest_8', 10, 10, False, NOW(), NOW());

INSERT INTO game_sanctuaries_opened (game_id, region, sanctuary_id, is_open)
VALUES
(1, 'Hyrule', 'sanctuary_1', 1);




