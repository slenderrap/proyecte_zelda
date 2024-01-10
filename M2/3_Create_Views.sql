DROP VIEW IF EXISTS show_players;
DROP VIEW IF EXISTS games_played;
DROP VIEW IF EXISTS acquired_weapons;
DROP VIEW IF EXISTS food_eaten;
DROP VIEW IF EXISTS avg_bloodmoons;
DROP VIEW IF EXISTS max_bloodmoons;


-- 1
CREATE VIEW show_players AS
	select user_name, max(changed_at) as last_save
    from game
    group by user_name, changed_at
    order by last_save;
    
-- 2
CREATE VIEW games_played AS
	select user_name, count(game_id) as times_played
    from game
    group by user_name
    order by times_played;

-- 3
CREATE VIEW acquired_weapons AS
	select user_name, weapon_name, count(weapon_name) as times_achieved, g.created_at
    from game g
    inner join game_weapons gw
    on g.game_id = gw.game_id
    group by user_name, weapon_name, g.created_at
    order by g.user_name, times_achieved desc;
    
-- 4
CREATE VIEW food_eaten AS
	select user_name, food_name, count(food_name) as times_eated, g.created_at
    from game g
    inner join game_food gf
    on g.game_id = gf.game_id
    group by user_name, food_name, g.created_at
	order by g.user_name, times_eated desc;
    
-- 5
CREATE VIEW avg_bloodmoons AS
	select round(avg(blood_moon_appearances), 2) as average_blood_moon_appearances
    from game;

CREATE VIEW max_bloodmoons AS
	select created_at, user_name, blood_moon_appearances
    from game
    where blood_moon_appearances = (select max(blood_moon_appearances)
									from game)
	LIMIT 8;