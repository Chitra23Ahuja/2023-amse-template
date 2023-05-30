import pandas as pd
import sqlite3

csv_url = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-ladesaulen-in-deutschland/exports/csv"
excel_url = "https://www.bundesnetzagentur.de/SharedDocs/Downloads/DE/Sachgebiete/Energie/Unternehmen_Institutionen/E_Mobilitaet/Ladesaeulenregister.xlsx?__blob=publicationFile&v=21"

connection = sqlite3.connect('AMSE_database.sqlite')

csv_df = pd.read_csv(csv_url, delimiter=';', encoding='latin-1')
excel_df = pd.read_excel(excel_url, skiprows=10)

excel_df.fillna(0, inplace=True)
csv_df.fillna(0, inplace=True)
new_columns = [column.lower().replace(' ', '_') for column in excel_df.columns]
excel_df.columns = new_columns

excel_df.rename(mapper={'straße': 'strasse'}, axis=1, inplace=True)
excel_df.rename(mapper={'anzahl ladepunkte': 'anzahl_ladepunkte	'}, axis=1, inplace=True)

# Save the DataFrame to a SQL database
csv_df.to_sql("e_charging stations", connection, if_exists='replace', index=False)
excel_df.to_sql("e_ladesäulenregister", connection, if_exists='replace', index=False)

connection.commit()
connection.close()