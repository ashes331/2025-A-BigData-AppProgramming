import requests

url = 'https://finance.naver.com/item/sise_day.naver?code=005930&page=1'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'

response = requests.get(url, headers={'User-Agent': user_agent})

print(response.status_code)
print(response.text)