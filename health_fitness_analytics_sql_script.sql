
-- Step 1: Create tables

CREATE TABLE Athletes (
    Athlete_ID INT PRIMARY KEY,
    Age INT,
    Gender VARCHAR(10),
    Training_Intensity VARCHAR(10),
    Diet_Quality VARCHAR(10),
    Rest_Hours FLOAT
);

CREATE TABLE Performance (
    Athlete_ID INT,
    Performance_Score FLOAT,
    Injury_Risk INT,
    FOREIGN KEY (Athlete_ID) REFERENCES Athletes(Athlete_ID)
);

-- Step 2: Insert sample data into Athletes and Performance tables

-- Example insert statement (bulk insert would be used in a real setup)
-- INSERT INTO Athletes (Athlete_ID, Age, Gender, Training_Intensity, Diet_Quality, Rest_Hours)
-- VALUES (1, 25, 'Male', 'High', 'Good', 7.5);

-- INSERT INTO Performance (Athlete_ID, Performance_Score, Injury_Risk)
-- VALUES (1, 85.5, 0);

-- Step 3: Queries

-- Query 1: Average performance score by training intensity
SELECT 
    Training_Intensity, 
    AVG(Performance_Score) AS Avg_Performance
FROM 
    Athletes A
JOIN 
    Performance P ON A.Athlete_ID = P.Athlete_ID
GROUP BY 
    Training_Intensity;

-- Query 2: Correlate injury risk with rest hours
SELECT 
    Rest_Hours, 
    AVG(Injury_Risk) AS Avg_Injury_Risk
FROM 
    Athletes A
JOIN 
    Performance P ON A.Athlete_ID = P.Athlete_ID
GROUP BY 
    Rest_Hours;

-- Query 3: Analyze the relationship between diet quality and performance
SELECT 
    Diet_Quality, 
    AVG(Performance_Score) AS Avg_Performance
FROM 
    Athletes A
JOIN 
    Performance P ON A.Athlete_ID = P.Athlete_ID
GROUP BY 
    Diet_Quality;
