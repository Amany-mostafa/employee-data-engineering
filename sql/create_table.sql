IF DB_ID(N'EmployeeDataEngineering') IS NULL
    CREATE DATABASE EmployeeDataEngineering;
GO

USE EmployeeDataEngineering;
GO

IF OBJECT_ID(N'dbo.Employees', N'U') IS NULL
BEGIN
    CREATE TABLE dbo.Employees (
        Employee_ID INT NOT NULL PRIMARY KEY,
        Age INT,
        Salary DECIMAL(12, 2),
        Gender VARCHAR(20),
        Department VARCHAR(50),
        Experience INT,
        Education VARCHAR(50),
        Performance_Score DECIMAL(5, 2),
        Working_Hours DECIMAL(5, 2),
        City VARCHAR(100),
        Country VARCHAR(100),
        Years_in_Company INT,
        Previous_Company VARCHAR(150),
        Annual_Bonus DECIMAL(12, 2),
        Join_Date DATE,
        Name VARCHAR(150)
    );
END;
GO