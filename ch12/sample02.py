import matplotlib.pyplot as plt
import pandas as pd

file_name = '../ch11/data_raw.csv'
df_raw = pd.read_csv(file_name)

COL_LANG = 'LanguageHaveWorkedWith'
ds_data = df_raw[COL_LANG]

print('-'*50)
print(ds_data)

ds_data = ds_data.str.split(';')

print('-'*50)
print(ds_data)

ds_data = ds_data.explode()

print('-'*50)
print(ds_data)

ds_data = ds_data.groupby(ds_data).size()

print('-'*50)
print(ds_data)

ds_data.nlargest(20).plot.pie(figsize=(10,10), autopct='%1.2f%%') #인치단위
plt.tight_layout()
# plt.show()

plt.savefig('./lang_info.png')









































