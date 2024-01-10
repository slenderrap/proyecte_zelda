/* ALTER TABLEs */

ALTER TABLE game
    ADD PRIMARY KEY (game_id),
    MODIFY user_name CHAR(50) NOT NULL,
    MODIFY date_started DATE NOT NULL,
    ADD CONSTRAINT check_region
    CHECK (region IN ('Hyrule', 'Death mountain', 'Gerudo', 'Necluda', 'Castle')),
    MODIFY created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    MODIFY changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;


ALTER TABLE game_food
    ADD PRIMARY KEY (game_id, food_name),
    ADD CONSTRAINT check_food_name
    CHECK (food_name IN ('Vegetables', 'Fish', 'Meat', 'Salads', 'Pescatarian', 'Roasted')),
    ADD CONSTRAINT fk_game_gameFood
    FOREIGN KEY (game_id)
    REFERENCES game(game_id),
    MODIFY created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    MODIFY changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;

    
ALTER TABLE game_weapons
    ADD PRIMARY KEY (game_id, weapon_name),
    ADD CONSTRAINT check_weapon_name
    CHECK (weapon_name IN ('Wood Sword', 'Sword', 'Wood Shield', 'Shield')),
    MODIFY equiped BOOLEAN DEFAULT false,
    ADD CONSTRAINT fk_game_gameWeapons
    FOREIGN KEY (game_id)
    REFERENCES game (game_id),
    MODIFY created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    MODIFY changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;

    
ALTER TABLE game_enemies
    ADD PRIMARY KEY (game_id, region, num),
    ADD CONSTRAINT fk_game_gameEnemies
	FOREIGN KEY (game_id)
	REFERENCES game (game_id),
    MODIFY created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    MODIFY changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;

ALTER TABLE game_sanctuaries_opened
    ADD PRIMARY KEY (game_id, region, num),
    ADD CONSTRAINT fk_game_sanctuariesOpened
	FOREIGN KEY (game_id)
	REFERENCES game (game_id),
    MODIFY created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    MODIFY changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;
    
ALTER TABLE game_chests_opened
    ADD PRIMARY KEY (game_id, region, num),
    ADD CONSTRAINT fk_game_chestsOpened
	FOREIGN KEY (game_id)
	REFERENCES game (game_id),
    MODIFY created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    MODIFY changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;

