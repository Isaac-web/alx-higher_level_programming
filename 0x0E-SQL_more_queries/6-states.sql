-- creates a database and a table inside the database

CREATE DATABASE
IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE
IF NOT EXISTS states (
	id INT NOT NULL AUTO_INCREMENT, 
	name VARCHAR(256) NOT NULL
	);
