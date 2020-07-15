-- Script that creates the database hbtn_0d_usa and th etbale cities
-- in the database hbtn_0d_usa on MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE hbtn_0d_usa.cities(
	id INT NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
);
