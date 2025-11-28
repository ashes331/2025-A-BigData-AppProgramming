# 퇴근시간이 가장 많은 장소 확인
# 츨근시간 9시 이전(9시 포함)
# 최근시간 5시 이후 8시 까지

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

df_raw['timestamp'] = pd.to_datetime(df_raw['timestamp'], errors='coerce')

print('-'*50)
print(df_raw.info())

#data_in = df_raw[df_raw['timestamp'].dt.hour <= 9][['station_code', 'people_in']].groupby('station_code').sum()
data_in = df_raw[df_raw['timestamp'].dt.hour <= 9][['station_code', 'people_out']].groupby('station_code').sum()

# 17 <= hour <= 20



#data_in = df_raw[df_raw['timestamp'].dt.hour <= 9]
#data_in = data_in[['station_code', 'people_in']]
#data_in = data_in.groupby('station_code').sum()

print('-'*50)
print(data_in.head())

print('-'*50)
print(df_station.head())

join_in = data_in.join(df_station)
#join_in = df_station.join(data_in)

print('join_in => ' + '-'*50)
print(join_in.head())

map = folium.Map(location=[37.566621, 126.978208], zoom_start=12)

cols = ['geo.latitude', 'geo.longitude', 'people_out']
HeatMap(data = join_in[cols]).add_to(map)

map.show_in_browser()






























