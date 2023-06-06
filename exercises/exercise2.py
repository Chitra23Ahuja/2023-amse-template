import pandas as pd
from sqlalchemy import types, create_engine

d_types = {
    'EVA_NR': types.BIGINT,
    'DS100': types.TEXT,
    'IFOPT': types.TEXT,
    'NAME': types.TEXT,
    'Verkehr': types.TEXT,
    'Laenge': types.FLOAT,
    'Breite': types.FLOAT,
    'Betreiber_Name': types.TEXT,
    'Betreiber_Nr': types.BIGINT}

# Read the CSV file
df = pd.read_csv("https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV", sep=';', decimal=',')

# Drop the "Status" column
df = df.drop("Status", axis=1)
# Filter out rows with invalid values
valid_verkehr_values = ["FV", "RV", "nur DPN"]
df = df[df["Verkehr"].isin(valid_verkehr_values)]
df = df[(df['Laenge'] >= -90) & (df['Laenge'] <= 90)]
df = df[(df['Breite'] >= -90) & (df['Breite'] <= 90)]
pattern = r'^[A-Za-z]{2}:\d+:\d+(?::\d+)?$'
df = df[df['IFOPT'].str.contains(pattern, na=False)]
df.dropna(inplace=True)

# Load the transformed data into the "trainstops" table
engine = create_engine("sqlite:///trainstops.sqlite")
df.to_sql("trainstops", engine, if_exists="replace", index=False, dtype= d_types)




