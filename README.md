
# Crime Investigators
## Working with Crime Data 
You must use Apache Spark for this assignment.
1. Create a Spark session
2. Define the schema for loading the Chicago crime dataset (https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2/data).
3. Load the Chicago crime data (you should get more than a million rows).
4. Clean the data:
- Remove all null values.
- Change 'Date' column data type
- Filter the data for last ten years.
6. Remove all the records with the following crime types:
'NON-CRIMINAL (SUBJECT SPECIFIED)'
'OTHER OFFENSE'
'STALKING'
'NON - CRIMINAL'
'ARSON'
7. Merge the similar crime types.
For example, change 'Primary Type' of cases that have 'Primary Type' as ‘SEX OFFENSE’ or ‘PROSTITUTION’ such that they should have the same 'Primary Type'.
8. Analyze the data and present results:
- Show year-wise trend of the crime for last ten years.
- Find out at which hour of the day crime is highest.
- Find top ten crimes and present them as a bar chart.
