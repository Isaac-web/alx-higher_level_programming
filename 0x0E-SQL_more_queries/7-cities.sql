-- creates a database called hbtn_0d_usa
CREATE DATABASE
IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE
IF NOT EXISTS hbtn_0d_usa.cities(
	id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
	state_id INT FOREIGN KEY REFERENCE KEY(states.id) REFERENCES states(id),
	name VARCHAR(256) NOT NULL
);
