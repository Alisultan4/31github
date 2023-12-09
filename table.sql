-- Create a new database
CREATE DATABASE IF NOT EXISTS mydatabase;
USE mydatabase;

-- Create a table named 'users'
CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    subject VARCHAR(50) NOT NULL,
    mark VARCHAR(100) NOT NULL
);

-- Insert some sample data into the 'users' table
INSERT INTO users (subject, mark) VALUES
    ('English', '5'),
    ('Math','5'),
    ('Geography','5'),
    ('Kyrgyz','4'),
    ('Russian','4'),
    ('ICT','5'),
    ('PE','5'),
    ('',''),
    ('',''),
    ('',''),
    ('',''),
    ('',''),
    ('',''),
    ('','');