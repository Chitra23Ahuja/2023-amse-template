import zipfile
import urllib.request
import pandas as pd
import sqlite3

# Step 1: Download and unzip the data
zip_file_url = 'https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip'
zip_file_path = 'mowesta-dataset.zip'
data_file_name = 'data.csv'

# Download the ZIP file
urllib.request.urlretrieve(zip_file_url, zip_file_path)

# Unzip the ZIP file and extract the data.csv file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extract(data_file_name)

# Step 2: Reshape the data
columns_to_keep = ['Geraet', 'Hersteller', 'Model', 'Monat', 'Temperatur in °C (DWD)', 'Batterietemperatur in °C', 'Geraet aktiv']

data = pd.read_csv(data_file_name, delimiter=';', index_col=False, usecols=columns_to_keep)
data.rename(columns={'Temperatur in °C (DWD)': 'Temperatur', 'Batterietemperatur in °C': 'Batterietemperatur'}, inplace=True)

#handling data types
data["Temperatur"] = data["Temperatur"].apply(lambda x: float(x.replace(',', '.')))
data["Batterietemperatur"] = data["Batterietemperatur"].apply(lambda x: float(x.replace(',', '.')))
data = data.astype({'Geraet': 'int64' , 'Monat' : 'int64' ,  'Temperatur' : 'float64' , 'Batterietemperatur' : 'float64' })

# Step 3: Transform temperatures from Celsius to Fahrenheit
data['Temperatur'] = (data['Temperatur'] * 9/5) + 32
data['Batterietemperatur'] = (data['Batterietemperatur'] * 9/5) + 32

# Step 4: Validate data
data = data.dropna()
data = data[data['Geraet'] > 0]

valid_temp_range = (-459.67, 212)
temp_valid = data["Temperatur"].between(*valid_temp_range)
data = data[temp_valid]
valid_battery_range = data["Batterietemperatur"].between(*valid_temp_range)
data = data[valid_battery_range]

# Step 5: Write data to SQLite database
db_path = 'temperatures.sqlite'
table_name = 'temperatures'

conn = sqlite3.connect(db_path)
data.to_sql(table_name, conn, if_exists='replace', index=False)

# Close the database connection
conn.close()