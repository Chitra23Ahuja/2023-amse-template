
import os
import pandas as pd
import script

def test_data_load():
    """ Test if the data loading works and both datasets are an object of class pandas.DataFrame """
    assert isinstance(script.csv_df, pd.DataFrame)
    assert isinstance(script.excel_df, pd.DataFrame)

def test_dataframe_shape():
    """ Test if the shapes of both dataframes are correct as expected """
    csv_df_expected_shape = (36770, 20) # expected shape of the dataframe 1
    excel_df_expected_shape = (42995, 26) # expected shape of the dataframe 2

    csv_df_actual_shape = script.csv_df.shape # actual shape of the dataframe 1
    excel_df_actual_shape = script.excel_df.shape # actual shape of the dataframe 2
    # check if the shape is correct
    assert len(csv_df_actual_shape) == 2
    assert len(excel_df_actual_shape) == 2 
    assert csv_df_expected_shape[0] == csv_df_actual_shape[0] 
    assert csv_df_expected_shape[1] == csv_df_actual_shape[1]
    assert excel_df_expected_shape[0] == excel_df_actual_shape[0]
    assert excel_df_expected_shape[1] == excel_df_actual_shape[1]

def test_dataframe_columns():
    """ Test if the columns of both dataframes are correct as expected """
    csv_df_expected_columns = ['betreiber','art_der_ladeeinrichung','anzahl_ladepunkte','anschlussleistung','steckertypen1','steckertypen2','steckertypen3','steckertypen4','p1_kw','p2_kw','p3_kw','p4_kw','kreis_kreisfreie_stadt','ort','postleitzahl','strasse','hausnummer','adresszusatz','inbetriebnahmedatum','koordinaten'] # expected columns of dataframe 1
    excel_df_expected_columns = ['betreiber', 'strasse', 'hausnummer', 'adresszusatz', 'postleitzahl',
       'ort', 'bundesland', 'kreis/kreisfreie_stadt', 'breitengrad',
       'längengrad', 'inbetriebnahmedatum', 'anschlussleistung',
       'art_der_ladeeinrichung', 'anzahl_ladepunkte', 'steckertypen1',
       'p1_[kw]', 'public_key1', 'steckertypen2', 'p2_[kw]', 'public_key2',
       'steckertypen3', 'p3_[kw]', 'public_key3', 'steckertypen4', 'p4_[kw]',
       'public_key4'] 
    csv_df_actual_columns = script.csv_df.columns # actual columns of dataframe 1
    excel_df_actual_columns = script.excel_df.columns # actual columns of dataframe 2
    # check if the columns are correct
    assert len(csv_df_actual_columns) == len(csv_df_expected_columns)
    assert all([a == b for a, b in zip(csv_df_actual_columns, csv_df_expected_columns)])
    assert len(excel_df_actual_columns) == len(excel_df_expected_columns)
    assert all([a == b for a, b in zip(excel_df_actual_columns, excel_df_expected_columns)])

def test_output_exists():
    """ Test if after the execution of the pipeline, both datasets are safed in an sqlite database file in the data directory """
    directory_path = os.path.join(os.getcwd(), './data') # get directory path
    print(directory_path)
    assert os.path.exists(os.path.join(directory_path,"e_charging_stations.sqlite"))
    assert os.path.exists(os.path.join(directory_path,"e_ladesäulenregister.sqlite"))

def test_pipeline():
    """ Test if the pipeline script works as expected """
    test_output_exists()
    test_data_load()
    test_dataframe_shape()
    test_dataframe_columns()

if __name__ == "__main__":
    print("Start testing pipeline ...")
    test_pipeline()
    print("Test done!")