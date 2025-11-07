import pandas as pd
import matplotlib.pyplot as plt
from ch05.common_function import init_matplotlib

init_matplotlib()

#전달받은 파일명에 해당하는 Data리턴 함수
def get_data(iso_code, rate_yn):
    file_path = './data/covid_common.csv'
    common_df = pd.read_csv(file_path)

    #기준이되는 인구수(USA)
    common_population_sr = common_df[common_df['iso_code'] == 'USA']['population']
    common_population_value = common_population_sr.iat[0]

    #현재 iso_code에 해당하는 인구수
    cur_population_sr = common_df[common_df['iso_code'] == iso_code]['population']
    cur_population_value = cur_population_sr.iat[0]

    rate = round(common_population_value / cur_population_value, 2)

    filter_df = common_df[common_df['iso_code'] == iso_code]
    # date컬럼을 인덱스로 지정
    index_name = 'date'
    index_df = filter_df.set_index(index_name)

    if rate_yn:
        return index_df['total_cases'] * rate
    else:
        return index_df['total_cases']
#end-def

kor_data = get_data('KOR', False)
usa_data = get_data('USA', False)
fra_data = get_data('FRA', False)
gbr_data = get_data('GBR', False)
pol_data = get_data('POL', False)
index_data = kor_data.index

data = {
    'KOR': kor_data,
    'USA': usa_data,
    'FRA': fra_data,
    'GBR': gbr_data,
    'POL': pol_data
}

df = pd.DataFrame(data, index=index_data)
df[:].plot.line(rot = 45)
#plt.show()

kor_data = get_data('KOR', True)
usa_data = get_data('USA', True)
fra_data = get_data('FRA', True)
gbr_data = get_data('GBR', True)
pol_data = get_data('POL', True)
index_data = kor_data.index

data = {
    'KOR': kor_data,
    'USA': usa_data,
    'FRA': fra_data,
    'GBR': gbr_data,
    'POL': pol_data
}

df = pd.DataFrame(data, index=index_data)
df[:].plot.line(rot = 45)
plt.show()