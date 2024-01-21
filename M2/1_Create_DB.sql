use zelda;

/* Create the database */
CREATE DATABASE IF NOT EXISTS zelda;

/* Drop tables */
DROP TABLE IF EXISTS game_food;
DROP TABLE IF EXISTS game_weapons;
DROP TABLE IF EXISTS game_enemies;
DROP TABLE IF EXISTS game_sanctuaries_opened;
DROP TABLE IF EXISTS game_chests_opened;
DROP TABLE IF EXISTS game_trees_fell;
DROP TABLE IF EXISTS game;


/* Create the tables */
CREATE TABLE IF NOT EXISTS game (
	game_id INT,
	user_name CHAR(50),
    blood_moon_countdown INT,
    blood_moon_appearances INT,
    hearts INT,
    region CHAR(20),
    created_at TIMESTAMP,
    changed_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS game_food (
	game_id INT,
	food_name CHAR(15),
    quantity INT,
    uses INT,
    created_at TIMESTAMP,
    changed_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS game_weapons (
	game_id INT,
	weapon_name CHAR(15),
    equipped BOOLEAN,
    quantity INT,
    uses INT,
    uses_left INT,
    created_at TIMESTAMP,
    changed_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS game_enemies (
	game_id INT,
	region CHAR(20),
    enemy_id CHAR(7),
    xpos INT,
    ypos INT,
    xpos2 INT,
    ypos2 INT,
    is_dead BOOLEAN,
    lives_remaining INT,
    created_at TIMESTAMP,
    changed_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS game_sanctuaries_opened (
	game_id INT,
	region CHAR(20),
    sanctuary_id CHAR(11),
    is_open BOOLEAN,
    created_at TIMESTAMP,
    changed_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS game_chests_opened (
	game_id INT,
	region CHAR(20),
    chest_id CHAR(7),
    is_open BOOLEAN,
    created_at TIMESTAMP,
    changed_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS game_trees_fell (
	game_id INT,
	region CHAR(20),
    tree_id CHAR(6),
    is_cutted BOOLEAN,
    created_at TIMESTAMP,
    changed_at TIMESTAMP
);
