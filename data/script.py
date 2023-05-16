import pandas as pd
import csv
import sqlite3


csv_url = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-ladesaulen-in-deutschland/exports/csv"
excel_url = "https://www.bundesnetzagentur.de/SharedDocs/Downloads/DE/Sachgebiete/Energie/Unternehmen_Institutionen/E_Mobilitaet/Ladesaeulenregister.xlsx?__blob=publicationFile&v=21"

connection = sqlite3.connect('AMSE_database.db')
csv_df = pd.read_csv(csv_url, delimiter=';', encoding='latin-1')
excel_df = pd.read_excel(excel_url, skiprows=10)

csv_df.to_sql("E-charging stations", connection, if_exists='replace', index=False)
excel_df.to_sql("E-Ladesäulenregister", connection, if_exists='replace', index=False)
print("CSV Data:")
print(csv_df)
print("\nExcel Data:")
print(excel_df)

connection.commit()
connection.close()
