-- Create Database
CREATE DATABASE StudentDB;

-- Use Database
USE StudentDB;

-- Create Table
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(100),
    Age INT,
    Department VARCHAR(50),
    CGPA DECIMAL(3,2)
);

-- Insert Data
INSERT INTO Students VALUES
(1, 'John', 20, 'Computer Science', 8.50),
(2, 'Alice', 21, 'Information Technology', 9.10),
(3, 'Bob', 19, 'Computer Science', 7.80),
(4, 'Emma', 22, 'Electronics', 8.90),
(5, 'David', 20, 'Mechanical', 7.50);

-- Display All Students
SELECT * FROM Students;

-- Students with CGPA greater than 8
SELECT Name, CGPA
FROM Students
WHERE CGPA > 8;

-- Students from Computer Science
SELECT *
FROM Students
WHERE Department = 'Computer Science';

-- Average CGPA by Department
SELECT Department,
       AVG(CGPA) AS Average_CGPA
FROM Students
GROUP BY Department;

-- Update Student CGPA
UPDATE Students
SET CGPA = 9.20
WHERE StudentID = 1;

-- Delete a Student
DELETE FROM Students
WHERE StudentID = 5;

-- Order Students by CGPA
SELECT *
FROM Students
ORDER BY CGPA DESC;

-- Count Students in Each Department
SELECT Department,
       COUNT(*) AS TotalStudents
FROM Students
GROUP BY Department;
