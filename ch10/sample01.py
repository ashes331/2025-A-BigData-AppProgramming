import os

import pandas as pd


hi_file_name = './hawaii-covid-data.csv'
df_raw = pd.read_csv(hi_file_name)

print('='*50)
print(df_raw.head())
print(type(df_raw))

print('='*50)
print(df_raw.info())

df_raw['date'] = pd.to_datetime(df_raw['submission_date'], format='%m/%d/%Y')

print('='*50)
print(df_raw.info())

print('='*50)
print(df_raw.head())

print('='*50)
print(df_raw['date'].dt.year.unique())

#df_raw에 2021년도 하와이 인구(population)를 대입(저장)!!!!
hi_population = 1441553
df_raw['population'] = hi_population
df_raw['total_cases'] = df_raw['tot_cases']

print('='*50)
print(df_raw.head())

#원하는 데이터(날짜, 감염자수, 인구수)
col_list = ['date', 'total_cases', 'population']
df_raw_filter = df_raw[col_list]

print('='*50)
print(df_raw_filter.head())

df_raw_filter.set_index('date', inplace=True)

print('='*50)
print(df_raw_filter.head())


#파일(csv)로 저장!!!!
hi_data_file = './hi_data.csv'
if os.path.exists(hi_data_file):
    os.remove(hi_data_file)
df_raw_filter.to_csv(hi_data_file)







