/* Joining table of cases per week with week numbers with data loaded from a CSV file of 
week numbers against week commence date & creating a new table from join */

SELECT Week_Commence,  new_cases
INTO Sheffield_Cases_Per_Week_v3
FROM Case_week_table
INNER JOIN Week_numbers_2020
ON Week_numbers_2020.Week_num = Case_week_table.week
WHERE week IS NOT NULL
OR new_cases IS NOT NULL;

