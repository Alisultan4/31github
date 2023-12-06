-- Create a new database
CREATE DATABASE IF NOT EXISTS mydatabase;
USE mydatabase;

-- Create a table named 'users'
CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    age VARCHAR(100) NOT NULL
);

-- Insert some sample data into the 'users' table
INSERT INTO users (name, age) VALUES
    ('Alisultan', '16'),
    ('Bekturgan', '17'),
    ('Aitemir','99');
