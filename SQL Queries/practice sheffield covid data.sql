
/* Renaming column "date" - run the first time */ 
/* EXEC sp_rename 'data_2020-Oct-03.date', 'Case_date'; */

/* Select all data from Covid cases in Sheffield by date 
from https://coronavirus.data.gov.uk/cases?areaType=ltla&areaName=Sheffield (data up until 3rd Oct 2020*/
SELECT * 
FROM [data_2020-Oct-03];

/* Find the top 10 dates with highest number of cases */
SELECT TOP 10 *
FROM [data_2020-Oct-03]
ORDER BY newCasesBySpecimenDate DESC;



