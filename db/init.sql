CREATE DATABASE IF NOT EXISTS users_db;
USE users_db;

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(255),
  encrypted_password TEXT
);