-- 5-valid_email
-- checks if email has been changed
delimiter //
CREATE TRIGGER after_email_update
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
        UPDATE users
        SET valid_email = FALSE
        WHERE user_id = NEW.user_id;
    END IF;
END;
//
delimiter ;
