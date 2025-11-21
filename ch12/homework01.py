import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

matplotlib.rcParams['font.family'] = 'Malgun Gothic'

file_name = '../ch11/data_raw.csv'
df_raw = pd.read_csv(file_name)

df_age_filtered = df_raw[df_raw['Age'] == '35-44 years old']

COL_LANG = 'LanguageHaveWorkedWith'

ds_data = df_age_filtered[COL_LANG]

print('-' * 50)
print(ds_data)

ds_data = ds_data.str.split(';')

print('-' * 50)
print(ds_data)

ds_data = ds_data.explode()

print('-' * 50)
print(ds_data)

ds_data = ds_data.groupby(ds_data).size()

print('-' * 50)
print(ds_data)

ds_data.nlargest(5).plot.pie(
    figsize=(10, 10),
    autopct='%1.2f%%',
    startangle=90
)

plt.title('35-44세 개발자가 가장 많이 사용하는 언어 TOP 5')
plt.tight_layout()

# plt.show()
plt.savefig('./lang_top5_35_44.png')
