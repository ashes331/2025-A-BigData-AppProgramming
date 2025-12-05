from io import StringIO
import pandas as pd
import requests

user_agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'
}
url = 'https://www.dongyang.ac.kr/dmu/4904/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGZG11JTJGNjc3JTJGYXJ0Y2xMaXN0LmRvJTNG'
'''
# .do, .php, .asp(.aspx), .jsp, .naver, 확장자(x)
# 주소: 물리적인주소 vs 논리적인주소
# protocol -> https
# host(domain) -> www.dongyang.ac.kr
# page name -> /dmu/4904/subview.do
# querystring -> enc=Zm5jdDF8QEB8JTJGYmJzJTJGZG11JTJGNjc3JTJGYXJ0Y2xMaXN0LmRvJTNG
# url(uri)
# get, post, delete, put, fetch

# http -> 프로토콜
# http(80), https(443), ftp(21, 20), smtp(25)
# 네트워크상: 5개: ip(필수), port(필수), instance, account, password
# 동양미래대학교 웹서비스 IP: 203.249.39.43, port: 80(http)
# http://203.249.39.43:80 -----> ? www.dongyang.ac.kr (도메인서비스) : 도메인네임서버
# https://203.249.39.43:443 ---> > a.b.c.d(1~255)(ip-v4) ==> v6
'''
response = requests.get(url, headers=user_agent)

print(response.status_code)
#print(response.headers)
#print(response.text)

raw_html = response.text
raw_data = pd.read_html(StringIO(raw_html))

print(type(raw_data))
print(len(raw_data))

table_data = raw_data[0]
print(type(table_data))

print('-'*50)
print(table_data.info())
print(table_data.head())


