
import matplotlib.pyplot as plt
import pandas as pd

file_name = './data/seoul-metro-2021.logs.csv'
df_raw = pd.read_csv(file_name)
columns = ['station_code', 'people_in', 'people_out']
df_raw = df_raw[columns]

file_name = './data/seoul-metro-station-info.csv'
station_raw = pd.read_csv(file_name)
columns = ['station.code', 'geo.latitude', 'geo.longitude']
station_raw = station_raw[columns]
station_raw = station_raw.set_index('station.code')

print('-'*50)
print(df_raw)

ds_data = df_raw.groupby('station_code').sum()

print('-'*50)
print(ds_data)

print('-'*50)
print(station_raw)

join_data = ds_data.join(station_raw)

print('-'*50)
print(join_data)

join_data.to_csv('./seoul-inout.csv')







































