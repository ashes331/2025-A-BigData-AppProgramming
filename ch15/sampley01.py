# pip install prophet

import pandas as pd
from prophet import Prophet
from matplotlib import pyplot as plt
from prophet.plot import plot_plotly

file_name = '../ch14/stock_005930_data.csv'
df_raw = pd.read_csv(file_name)

df_raw['ds'] = pd.to_datetime(df_raw['date'])
df_raw['y'] = df_raw['end_price']
print(df_raw.info())

# 년도를 2021년 이후
df_raw = df_raw[df_raw['ds'].dt.year >= 2021]

df_data = df_raw[['ds', 'y']]
print('-'*50)
print(df_data.info())

# 프로핏 모델 객체 생성
model = Prophet()

# df_data를 학습
print('-'*50)
print('데이터학습!')
model.fit(df_data)

#예측 데이터 설정
future = model.make_future_dataframe(periods=365)
print('-'*50)
print(future.tail())

#예측하기
forecast = model.predict(future)

print('-'*50)
print(forecast.info())

print('-'*50)
print(forecast.tail())

fig1 = model.plot(forecast)
plt.show()

fig2 = model.plot_components(forecast)
plt.show()
