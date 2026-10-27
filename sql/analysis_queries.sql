USE EmployeeDataEngineering;
GO

-- Employee count by department
SELECT
    Department,
    COUNT(*) AS EmployeeCount
FROM dbo.Employees
GROUP BY Department
ORDER BY EmployeeCount DESC;

-- Salary statistics by department
SELECT
    Department,
    COUNT(Salary) AS EmployeesWithSalary,
    CAST(AVG(Salary) AS DECIMAL(12, 2)) AS AverageSalary,
    MIN(Salary) AS MinimumSalary,
    MAX(Salary) AS MaximumSalary
FROM dbo.Employees
GROUP BY Department
ORDER BY AverageSalary DESC;

-- Employee count by country
SELECT
    Country,
    COUNT(*) AS EmployeeCount
FROM dbo.Employees
GROUP BY Country
ORDER BY EmployeeCount DESC;