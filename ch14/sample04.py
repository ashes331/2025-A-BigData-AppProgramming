from io import StringIO
import pandas as pd
import requests
from matplotlib import pyplot as plt

file_name = './stock_005930_data.csv'
df_raw = pd.read_csv(file_name)

df_raw['date_time'] = pd.to_datetime(df_raw['date'])
df_raw = df_raw[df_raw['date_time'].dt.year >= 2025]
df_raw.drop(columns=['date_time'], inplace=True)

#월단위로
df_raw['date_month'] = df_raw['date'].str[:7]
df_raw.set_index('date', inplace=True)

#중앙값(중간값)

low_price = 5
hi_price = 11
# 6,7,8,9,10 -> 8
# 5,6,7,8,9,10,11 -> 8
# 11 - ((11 - 5) / 2)
# hi_price - ((hi_price - low_price) / 2)
df_raw['middle_price'] = df_raw['hi_price'] - ((df_raw['hi_price'] - df_raw['low_price']) / 2)


print('-'*50)
print(df_raw.info())
print(df_raw.head())

#df_raw.plot.line()
#plt.show()

df_raw.boxplot(column='middle_price', by=['date_month'])
plt.show()