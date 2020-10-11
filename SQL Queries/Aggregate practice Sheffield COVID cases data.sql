/* Finding the week with the greatest decrease in COVID-19 cases in Sheffield */
SELECT TOP 1 Week_Commence, diff
FROM Sheffield_Weekly_Changes
WHERE diff IS NOT NULL
ORDER BY diff ASC
;

/* Finding the week with the greatest increase in COVID-19 cases in Sheffield */
SELECT TOP 1 Week_Commence, diff
FROM Sheffield_Weekly_Changes
WHERE diff IS NOT NULL
ORDER BY diff DESC
;

/* Finding the average weekly change in COVID-19 cases in Sheffield */
SELECT AVG(diff)
FROM Sheffield_Weekly_Changes
WHERE diff IS NOT NULL
;
