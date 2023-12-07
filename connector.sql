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
    ('Aitemir','99'),
    ('Andrew','17'),
    ('Amir','17'),
    ('Atanai','17'),
    ('Akhror','17'),
    ('Arsen','17'),
    ('Aiman','17'),
    ('Alizhan','17'),
    ('Akniyet','17'),
    ('Yunus','17'),
    ('Chyngyz','17'),
    ('Nurmuhammed','16'),
    ('Umar','17');
