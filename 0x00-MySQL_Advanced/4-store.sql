-- 4-store
-- This script that creates a trigger that decreases the quantity of an
-- item after adding a new order.
delimiter //
CREATE TRIGGER after_new_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items
	SET quantity = quantity - NEW.quantity;
END;
//
delimiter ;
