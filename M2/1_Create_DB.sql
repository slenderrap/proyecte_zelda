/* Create the database */
CREATE DATABASE IF NOT EXISTS zelda;

/* Switch to the classicmodels database */
USE zelda;

/* Create the tables */
CREATE TABLE IF NOT EXISTS game (
	game_id INT,
	user_name CHAR(50),
	date_started DATE,
    blood_moon_countdown INT,
    blood_moon_appearances INT,
    region CHAR(20),
    created_at TIMESTAMP,
    changed_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS game_food (
	game_id INT,
	food_name CHAR(15),
    quantity_remaining INT,
    created_at TIMESTAMP,
    changed_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS game_weapons (
	game_id INT,
	weapon_name CHAR(15),
    equiped BOOLEAN,
    lives_remaining INT,
    created_at TIMESTAMP,
    changed_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS game_enemies (
	game_id INT,
	region CHAR(20),
    num INT,
    xpos INT,
    ypos INT,
    lifes_remaining INT,
    created_at TIMESTAMP,
    changed_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS game_sanctuaries_opened (
	game_id INT,
	region CHAR(20),
    num INT,
    xpos INT,
    ypos INT,
    created_at TIMESTAMP,
    changed_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS game_chests_opened (
	game_id INT,
	region CHAR(20),
    num INT,
    xpos INT,
    ypos INT,
    created_at TIMESTAMP,
    changed_at TIMESTAMP
);
