-- Creating Departments table
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(50) NOT NULL
);

-- Creating JobRoles table
CREATE TABLE JobRoles (
    JobRoleID INT PRIMARY KEY,
    JobRoleName VARCHAR(50) NOT NULL
);

-- Creating Employees table
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    Age INT,
    Gender VARCHAR(10),
    MonthlyIncome DECIMAL(10, 2),
    JobLevel INT,
    DepartmentID INT,
    JobRoleID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID),
    FOREIGN KEY (JobRoleID) REFERENCES JobRoles(JobRoleID)
);

-- Creating Attrition table
CREATE TABLE Attrition (
    EmployeeID INT,
    AttritionStatus VARCHAR(10),
    PRIMARY KEY (EmployeeID),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

-- Insert into Employee table
INSERT INTO Employee (EmployeeID, Name, Age, Gender, MaritalStatus, BusinessTravel, 
DistanceFromHome, YearStartedAtCompany, YearStartedCurrentRole, LastManagerChangeDate, 
LastPromotionDate, TotalWorkingYears, DepartmentID, WorkLocationID, HomeLocationID, 
FinancialsID, SatisfactionID, ManagerID, JobID)
VALUES (101, 'John Doe', 35, 'M', 'Single', 'Travel_Rarely', 10, 2010, 2015, '2020-01-01', 
'2019-01-01', 10, 1, 1, 1, 1, 1, 201, 1);

-- Insert into Job table
INSERT INTO Job (JobID, JobTitle, JobLevel, JobInvolvement, Description)
VALUES (1, 'Sales Representative', 1, 1, 'Responsible for sales activities');

-- Insert into Financials table
INSERT INTO Financials (FinancialsID, EmployeeID, MonthlyIncome, DailyRate, HourlyRate, 
TotalIncomeOverYears, IncomePerJobLevel, PercentSalaryHike, StockLevelOption)
VALUES (1, 101, 4000, 200, 20, 48000, 4000, 15, 2);

-- Insert into Satisfaction table
INSERT INTO Satisfaction (SatisfactionID, EmployeeID, JobSatisfaction, 
EnvironmentSatisfaction, RelationshipSatisfaction, WorkLifeSatisfaction)
VALUES (1, 101, 4, 3, 4, 3);

-- Insert into Department table
INSERT INTO Department (DepartmentID, DepartmentName, ManagerID)
VALUES (1, 'Sales', 201);

-- Insert into WorkLocation table
INSERT INTO WorkLocation (WorkLocationID, City, Country)
VALUES (1, 'New York', 'USA');

-- Insert into HomeLocation table
INSERT INTO HomeLocation (HomeLocationID, City, Country)
VALUES (1, 'Brooklyn', 'USA');


-- Extract Description for Specific Criteria:
SELECT e.Name, e.Description
FROM Employee e
JOIN Job j ON e.JobID = j.JobID
WHERE e.JobInvolvement = 1 AND e.JobLevel = 1 AND j.JobTitle = 'Sales Representative';

-- Extract Average Monthly Income for Each Job Role:
SELECT j.JobTitle, AVG(f.MonthlyIncome) AS AverageMonthlyIncome
FROM Employee e
JOIN Job j ON e.JobID = j.JobID
JOIN Financials f ON e.EmployeeID = f.EmployeeID
GROUP BY j.JobTitle;

