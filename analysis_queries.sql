-- CUNY Expenditure Analysis Dashboard
-- SQL queries for analyzing expenditure trends by fiscal year and funding source

-- 1. Total expenditure by fiscal year
SELECT
    fiscal_year,
    SUM(amount) AS total_expenditure
FROM cuny_expenditures
GROUP BY fiscal_year
ORDER BY fiscal_year;

-- 2. Total expenditure by funding source
SELECT
    source,
    SUM(amount) AS total_expenditure
FROM cuny_expenditures
GROUP BY source
ORDER BY total_expenditure DESC;

-- 3. Expenditure trend by fiscal year and source
SELECT
    fiscal_year,
    source,
    SUM(amount) AS total_expenditure
FROM cuny_expenditures
GROUP BY fiscal_year, source
ORDER BY fiscal_year, source;

-- 4. Highest expenditure year
SELECT
    fiscal_year,
    SUM(amount) AS total_expenditure
FROM cuny_expenditures
GROUP BY fiscal_year
ORDER BY total_expenditure DESC
LIMIT 1;
