from io import StringIO
import pandas as pd
import requests

# 737

user_agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'
}

all_table_data = pd.DataFrame()
total_page = 737

for index in range(1, total_page + 1):
    print('-'*50, f'{index}/{total_page}')

    url = f'https://finance.naver.com/item/sise_day.naver?code=005930&page={index}'
    response = requests.get(url, headers=user_agent)

    print(response.status_code)
    raw_html = response.text
    raw_data = pd.read_html(StringIO(raw_html))
    table_data = raw_data[0]

    print('-' * 50)
    print(table_data.head())

    all_table_data = pd.concat([all_table_data, table_data])
#end-for

all_table_data.dropna(inplace=True)

print(all_table_data.head())
all_table_data.to_csv('./stock_005930.csv')



