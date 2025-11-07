import pandas as pd
import matplotlib.pyplot as plt
from ch05.common_function import init_matplotlib
from ch08.sample02 import kor_population

init_matplotlib()


#전달받은 파일명에 해당하는 Data리턴 함수
def get_data(filename):
    df_raw = pd.read_csv(filename)
    df_raw.set_index('date', inplace=True)

    #TODO: 소통용 주석
    population = df_raw['population'].iat[0]

    return {
        'population': population,
        'sr': df_raw['total_cases']
    }
#end-def

# 2020-01-01 ~ 2020-12-31
kor_data = get_data('../ch05/data/covid_kor.csv')
kor_sr  = kor_data['sr']
kor_population = kor_data['population']
kor_index = kor_sr.index

# 2020-03-01 ~ 2021-12-31
hi_data = get_data('./hi_data.csv')
hi_sr = hi_data['sr']
hi_population = hi_data['population']
hi_index = hi_sr.index

# -> 2020-01-01 ~ 2021-12-31
data_index = kor_index.union(hi_index)

#인구비율구하기!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

rate = round(kor_population / hi_population, 2)

df = pd.DataFrame(
    {
        '대한민국': kor_sr,
        '하와이': hi_sr * rate,
    },
    index=data_index
)

df.plot.line()
plt.show()















