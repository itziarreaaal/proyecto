CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `admin2`@`%` 
    SQL SECURITY DEFINER
VIEW `ranking1` AS
    SELECT 
        `pg`.`player_id` AS `player_id`,
        SUM((`pg`.`ending_points` - `pg`.`starting_points`)) AS `Earnings`,
        COUNT(`pg`.`player_id`) AS `Games Played`,
        SUM(TIMESTAMPDIFF(MINUTE,
            `cg`.`start_hour`,
            `cg`.`end_hour`)) AS `Minutes Played`
    FROM
        (`player_game` `pg`
        JOIN `cardgame` `cg` ON ((`cg`.`cardgame_id` = `pg`.`cardgame_id`)))
    GROUP BY `pg`.`player_id`
    ORDER BY COUNT(`pg`.`player_id`) DESC