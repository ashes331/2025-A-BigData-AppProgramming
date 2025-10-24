import pandas as pd
import matplotlib.pyplot as plt
from ch05.common_function import init_matplotlib

init_matplotlib()

#전달받은 파일명에 해당하는 Data리턴 함수
def get_data(filename):
    kor_df = pd.read_csv(filename)
    index_name = 'date'
    kor_index_df = kor_df.set_index(index_name)
    return kor_index_df['total_cases']
#end-def

kor_data = get_data('../ch05/data/covid_kor.csv')
usa_data = get_data('../ch05/data/covid_usa.csv')
index_data = kor_data.index

df = pd.DataFrame(
    {
        '대한민국': kor_data,
        '미국': usa_data,
    },
    index=index_data
)
df['2022-01-01':'2022-12-31'].plot.line(rot = 45)
plt.show()