-- 7-average_score
-- The script creates a stored procedure ComputeAverageScoreForUser that
-- computes and store the average score for a student.

delimiter //

CREATE PROCEDURE ComputeAverageScoreForUser(
	IN user_id INT
)
BEGIN
	DECLARE avg_score DECIMAL(5,2);

	SELECT AVG(score) INTO avg_score
	FROM corrections
	WHERE user_id = user_id;

	UPDATE users
	SET average_score = avg_score
	WHERE id = user_id;
END//
delimiter ;
