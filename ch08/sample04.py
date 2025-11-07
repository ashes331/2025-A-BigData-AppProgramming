import pandas as pd
import os

#코로나 원 데이터파일
covid_file_name = '../ch04/data/owid-covid-data.csv'
raw_df = pd.read_csv(covid_file_name, sep=',')

#데이터분석에 필요한 컬러만 사용
selected_columns = ['iso_code','location','date','total_cases','population']
selected_df = raw_df[selected_columns]

#date컬럼을 index로 지정
index_name = 'date'
selected_index_df = selected_df.set_index(index_name)

#코로나데이터 저장
covid_common_file_name = './data/covid_common.csv'
if os.path.exists(covid_common_file_name):
    os.remove(covid_common_file_name)
selected_index_df.to_csv(covid_common_file_name)

