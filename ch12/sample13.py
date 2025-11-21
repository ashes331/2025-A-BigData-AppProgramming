
import matplotlib.pyplot as plt
import pandas as pd
import folium
from folium.plugins import HeatMap
from ch12.sample12 import columns

file_name = './seoul-inout.csv'
df_raw = pd.read_csv(file_name)
df_raw = df_raw.set_index('station_code')

print('-'*50)
print(df_raw)

columns = ['geo.latitude', 'geo.longitude', 'people_in']
data_in = df_raw[columns]

print('-'*50)
print(data_in)

map = folium.Map(location=[37.566621, 126.978208], zoom_start=12)

HeatMap(data = data_in).add_to(map)

map.show_in_browser()





































