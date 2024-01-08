/* Create the database */
CREATE DATABASE IF NOT EXISTS zelda;

/* Switch to the classicmodels database */
USE zelda;

/* Drop existing tables  */
DROP TABLE IF EXISTS game;
DROP TABLE IF EXISTS game_food; 
DROP TABLE IF EXISTS game_weapons;
DROP TABLE IF EXISTS game_enemies;
DROP TABLE IF EXISTS game_chests_opened;
DROP TABLE IF EXISTS game_sanctuaries_opened;

/* Create the tables */

CREATE TABLE IF NOT EXISTS game (
	game_id INT PRIMARY KEY,
	user_name CHAR(50) NOT NULL,
	date_started DATE NOT NULL,
    blood_moon_countdown INT,
    blood_moon_appearances INT,
    region CHAR(20)
);

CREATE TABLE IF NOT EXISTS game_food (
	game_id INT NOT NULL,
	food_name CHAR(15) NOT NULL,
    quantity_remaining INT,
    PRIMARY KEY (game_id, food_name),
    FOREIGN KEY (game_id) REFERENCES game(game_id)
);

CREATE TABLE IF NOT EXISTS game_weapons (
	game_id INT NOT NULL,
	weapon_name CHAR(15) NOT NULL,
    equiped BOOLEAN DEFAULT false,
    lives_remaining INT,
    PRIMARY KEY (game_id, weapon_name),
    FOREIGN KEY (game_id) REFERENCES game(game_id)
);

CREATE TABLE IF NOT EXISTS game_enemies (
	game_id INT NOT NULL,
	region CHAR(20) NOT NULL,
    num INT NOT NULL,
    xpos INT,
    ypos INT,
    lifes_remaining INT,
    PRIMARY KEY (game_id, region, num),
    FOREIGN KEY (game_id) REFERENCES game(game_id)
);

CREATE TABLE IF NOT EXISTS game_sanctuaries_opened (
	game_id INT NOT NULL,
	region CHAR(20) NOT NULL,
    num INT NOT NULL,
    xpos INT,
    ypos INT,
    PRIMARY KEY (game_id, region, num),
    FOREIGN KEY (game_id) REFERENCES game(game_id)
);

CREATE TABLE IF NOT EXISTS game_chests_opened (
	game_id INT NOT NULL,
	region CHAR(20) NOT NULL,
    num INT NOT NULL,
    xpos INT,
    ypos INT,
    PRIMARY KEY (game_id, region, num),
    FOREIGN KEY (game_id) REFERENCES game(game_id)
);


/* INSERTING DATA */

insert into game(region) values ("Hyrule", "Death mountain", "Gerudo", "Necluda", "Castle");
insert into game_food(food_name) values ("Vegetables", "Fish", "Meat", "Salads", "Pescatarian", "Roasted");
insert into game_weapons(weapon_name) values ("Wood Sword", "Sword", "Wood Shield", "Shield");


