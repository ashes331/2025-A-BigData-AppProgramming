import pandas as pd

covid_file_name = './data/owid-covid-data.csv'
# covid_file_name = './data/sample_kr.csv'
# raw_df = pd.read_csv(covid_file_name, sep='|', encoding='euc-kr')
raw_df = pd.read_csv(covid_file_name, sep=',')

# print(dir(raw_df))
# print(type(raw_df))
# print(raw_df)

print('='*50)
print(raw_df.info())


print('='*50)
print(raw_df.head())


selected_columns = ['iso_code', 'location', 'date', 'total_cases', 'population']
selected_df = raw_df[selected_columns]
print('='*50)
print(selected_df)

# 데이터에서 국기를 확인
# locations = raw_df['location']
locations = selected_df['location']

print('='*50)
print(locations)

print('='*50)
print(locations.unique())
print(locations.unique().size)

kor_df = selected_df[selected_df['location']=='South Korea']
print('='*50)
print(kor_df)





