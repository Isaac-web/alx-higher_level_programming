-- creates a database and a user and grants previleges on the
-- database to the user
CREATE DATABASE 
	IF NOT EXISTS hbtn_0d_2;

CREATE USER
	IF NOT EXISTS user_0d_2@localhost
	IDENTIFIED BY 'user_0d_2_pwd';

GRANT SELECT
	ON hbtn_0d_2d
	TO user_0d_2;
