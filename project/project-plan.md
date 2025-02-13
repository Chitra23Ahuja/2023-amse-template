# Project Plan

## Summary
This projects analyzes the availability and usage of electric vehicle charging stations in Germany by answering following questions:

1. Regions with the highest number of charging stations
2. Top 10 cities with the highest number of charging stations
3. Average power capacity of charging stations
4. Average power capacity of charging stations by region
5. Distribution of charging station types
6. Number of charging stations per operator

## Rationale
The analysis provides output that includes comprehensive database of electric vehicle charging stations in Germany, reports on descriptive and usage patterns, trends of charging station demand in different regions.

## Datasources

### Datasource1: Germany: E-charging stations
* Metadata URL: https://mobilithek.info/offers/-2989425250318611078
* Data URL: https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-ladesaulen-in-deutschland/exports/csv
* Data Type: CSV
The data of the charging station map of the Federal Network Agency.Federal Network Agency - charging station map

### Datasource2 : E-Ladesäulenregister
* Metadata URL: https://www.govdata.de/web/guest/daten/-/details/e-ladesaulenregister
* Data URL: https://www.bundesnetzagentur.de/SharedDocs/Downloads/DE/Sachgebiete/Energie/Unternehmen_Institutionen/E_Mobilitaet/Ladesaeulenregister.xlsx?__blob=publicationFile&v=21
* Data Type: xlsx
The static data represent the charging facilities of all operators who have completed the notification procedure of the Federal Network Agency and have consented to publication on the Internet.

## Work Packages
1.  Data Acquistion
2.  Automated Data pipeline
4.	Exploratory Analysis
5.	Automated testing
6.	Implement Continuous Integration
7.	Deploy the project 
8.  Documentation
