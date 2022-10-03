-- creates table id_not_null with id set to default value
CREATE TABLE
IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256))
