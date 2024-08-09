-- 100-average_weighted_score
-- The script that creates a stored procedure
-- ComputeAverageWeightedScoreForUser that computes and store the average
-- weighted score for a student.

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE total_weight INT;
    DECLARE weighted_sum DECIMAL(10,2);
    DECLARE avg_weighted_score DECIMAL(5,2);

    -- Compute the total weight and weighted sum
    SELECT SUM(score * weight), SUM(weight) INTO weighted_sum, total_weight
    FROM corrections
    WHERE user_id = user_id;

    -- Compute the average weighted score
    SET avg_weighted_score = weighted_sum / total_weight;

    -- Update the average weighted score in the users table
    UPDATE users
    SET average_weighted_score = avg_weighted_score
    WHERE id = user_id;

END//

DELIMITER ;

