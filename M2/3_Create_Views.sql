
use zelda;

DROP VIEW IF EXISTS show_players;
DROP VIEW IF EXISTS games_played;
DROP VIEW IF EXISTS acquired_weapons;
DROP VIEW IF EXISTS food_eaten;
DROP VIEW IF EXISTS avg_bloodmoons;
DROP VIEW IF EXISTS max_bloodmoons;
DROP VIEW IF EXISTS save_games;


-- 1
CREATE VIEW show_players AS
    select user_name, max(DATE_FORMAT(changed_at, '%d/%m/%y %H:%i:%s')) AS last_save
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
select g.game_id, user_name, weapon_name, quantity,
                        (SELECT g.created_at
                        FROM game g_inner
                            INNER JOIN game_weapons gw_inner ON g_inner.game_id = gw_inner.game_id
                        WHERE g.game_id = g_inner.game_id
                            AND gw_inner.weapon_name = gw.weapon_name
                        ORDER BY gw_inner.quantity DESC
                        LIMIT 1) AS max_count_date
from game g
inner join game_weapons gw
on g.game_id = gw.game_id
group by g.game_id, user_name, weapon_name
order by g.user_name asc, quantity desc;


-- 4
CREATE VIEW food_eaten AS
select g.game_id, user_name, food_name, quantity,
                        (SELECT g.created_at
                        FROM game g_inner
                            INNER JOIN game_food gf_inner ON g_inner.game_id = gf_inner.game_id
                        WHERE g.game_id = g_inner.game_id
                            AND gf_inner.food_name = gf.food_name
                        ORDER BY gf_inner.quantity DESC
                        LIMIT 1) AS max_count_date
from game g
inner join game_food gf
on g.game_id = gf.game_id
group by g.game_id, user_name, food_name, quantity
order by g.user_name asc, quantity desc;


-- 5
CREATE VIEW avg_bloodmoons AS
    select round(avg(blood_moon_appearances), 2) as average_blood_moon_appearances
    from game;

CREATE VIEW max_bloodmoons AS
    select DATE_FORMAT(created_at, '%d/%m/%Y %H:%i:%s') AS created_at, user_name, blood_moon_appearances
    from game
    where blood_moon_appearances = (select max(blood_moon_appearances)
                                    from game)
    order by changed_at
    LIMIT 7;


/* VIEWS CREADAS PARA EL JUEGO */
CREATE VIEW save_games AS
    select game_id, DATE_FORMAT(changed_at, '%d/%m/%Y %H:%i:%s') AS changed_at, user_name, region
    from game
    group by game_id
    order by game_id;
