import matplotlib.pyplot as plt
import pandas as pd

file_name = '../ch11/data_raw.csv'
df_raw = pd.read_csv(file_name)

COL_LANG = 'LanguageHaveWorkedWith'

print('-'*50)
print(df_raw.info())

ds_data = df_raw[COL_LANG]

print('-'*50)
#print(type(ds_data))
print(ds_data)

lang_list = []
lang_set = set()

for c1 in ds_data:
    if type(c1) == str:
        split_data = c1.split(';')
        for c2 in split_data:
            lang_list.append(c2)
            lang_set.add(c2)

print('-'*50)
print(lang_list)

JavaScript_count = 0

for c in lang_list:
    if c == 'JavaScript':
        JavaScript_count += 1

print('-'*50)
print(JavaScript_count)

print('-'*50)
print(lang_set)













































