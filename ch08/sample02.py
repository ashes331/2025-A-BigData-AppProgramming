import pandas as pd
import matplotlib.pyplot as plt
from ch05.common_function import init_matplotlib

init_matplotlib()

#전달받은 파일명에 해당하는 Data리턴 함수
def get_data(filename):
    raw_df = pd.read_csv(filename)
    index_name = 'date'
    raw_index_df = raw_df.set_index(index_name)
    return raw_index_df
#end-def

kor_data = get_data('../ch05/data/covid_kor.csv')
kor_data_population = kor_data['population']
kor_population = kor_data_population['2020-01-05']
print('대한민국 인구수:', kor_population)

usa_data = get_data('../ch05/data/covid_usa.csv')
usa_population = usa_data['population']['2020-01-05']
print('미국의 인구수: ', usa_population)

rate = usa_population / kor_population
print('비율: ', rate)

rate = round(usa_population / kor_population, 2)
print('비율: ', rate)