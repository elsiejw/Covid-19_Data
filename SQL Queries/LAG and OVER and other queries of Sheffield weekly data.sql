/* Select top 10 weeks of new cases */
SELECT TOP 10 * 
FROM Sheffield_Cases_Per_Week_v3
ORDER BY new_cases DESC;

/* use LAG and OVER to calculate the change for each week from previous week */
ALTER TABLE Sheffield_Cases_Per_Week_v3
ALTER COLUMN new_cases integer

SELECT Week_Commence, new_cases, LAG(new_cases) OVER(ORDER BY (Week_Commence)) AS Previous_week, new_cases - LAG(new_cases) OVER(ORDER BY (Week_Commence)) AS Diff
INTO Sheffield_Weekly_Changes
FROM Sheffield_Cases_Per_Week_v3;


