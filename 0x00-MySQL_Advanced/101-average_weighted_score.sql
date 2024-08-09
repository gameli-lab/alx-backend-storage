-- 101-average_weighted_score
-- SQL script that creates a stored procedure
-- ComputeAverageWeightedScoreForUsers that computes and store the average
-- weighted score for all students.

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE user_id INT;
    DECLARE total_weight INT;
    DECLARE weighted_sum DECIMAL(10,2);
    DECLARE avg_weighted_score DECIMAL(5,2);
    DECLARE user_cursor CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN user_cursor;

    read_loop: LOOP
        FETCH user_cursor INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Compute the total weight and weighted sum for the current user
        SELECT SUM(score * weight), SUM(weight) INTO weighted_sum, total_weight
        FROM corrections
        WHERE user_id = user_id;

        -- Compute the average weighted score
        IF total_weight > 0 THEN
            SET avg_weighted_score = weighted_sum / total_weight;
        ELSE
            SET avg_weighted_score = NULL;
        END IF;

        -- Update the average weighted score in the users table
        UPDATE users
        SET average_weighted_score = avg_weighted_score
        WHERE id = user_id;
    END LOOP;

    CLOSE user_cursor;
END//

DELIMITER ;

