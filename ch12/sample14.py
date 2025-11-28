
import matplotlib.pyplot as plt
import pandas as pd
import folium
from folium.plugins import HeatMap

file_name = './data/seoul-metro-2021.logs.csv'
df_raw = pd.read_csv(file_name)

file_name = './data/seoul-metro-station-info.csv'
df_station = pd.read_csv(file_name)
df_station = df_station[['station.code', 'geo.latitude', 'geo.longitude']].set_index('station.code')

print('-'*50)
print(df_raw.info())

df_raw['timestamp'] = pd.to_datetime(df_raw['timestamp'])

print('-'*50)
print(df_raw.info())

data_in = df_raw[df_raw['timestamp'].dt.hour <= 9][['station_code', 'people_in']].groupby('station_code').sum()

#data_in = df_raw[df_raw['timestamp'].dt.hour <= 9]
#data_in = data_in[['station_code', 'people_in']]
#data_in = data_in.groupby('station_code').sum()

print('-'*50)
print(data_in.head())

print('-'*50)
print(df_station.head())

join_in = data_in.join(df_station)

print('-'*50)
print(join_in.head())

map = folium.Map(location=[37.566621, 126.978208], zoom_start=12)
HeatMap(data = join_in[['geo.latitude', 'geo.longitude', 'people_in']]).add_to(map)
map.show_in_browser()






























