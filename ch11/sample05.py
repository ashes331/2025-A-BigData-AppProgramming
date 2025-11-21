# 개발자의 나이가 '35-44 years old' 인 데이터 중에서 개발자가 가장 많이 사용하는 언어 5가지를 파이 차트로 표시 과제 (12 주차)

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

matplotlib.rcParams['font.family'] = 'Malgun Gothic'

# 데이터 파일 로드
file_name = './data_raw.csv'
df_raw = pd.read_csv(file_name)

# '35-44 years old'인 데이터 필터링
df_age_filtered = df_raw[df_raw['Age'] == '35-44 years old']

# 사용 국가별로 그룹화하여 각 국가의 빈도 계산
country_counts = df_age_filtered['Country'].value_counts()

# 가장 많이 사용되는 국가 5개 선택
top_5_countries = country_counts.nlargest(5)

# 국가명 영어 -> 한글 매핑 딕셔너리 (예시, 실제로는 전체 국가명에 대해 매핑이 필요함)
country_translation = {
    'United States of America': '미국',
    'India': '인도',
    'Germany': '독일',
    'Canada': '캐나다',
    'United Kingdom of Great Britain and Northern Ireland': '영국 및 북아일랜드',
    # 여기 더 많은 국가들을 추가해야 합니다...
}

# 국가명 영어를 한글로 변환
top_5_countries_kr = top_5_countries.index.map(country_translation)

# 파이 차트로 시각화
plt.figure(figsize=(10, 10))
top_5_countries.plot.pie(labels=top_5_countries_kr, autopct='%1.1f%%', startangle=90)

# 제목 설정
plt.title('35-44세 개발자가 가장 많이 사용하는 국가')

# 차트 레이아웃 정리
plt.tight_layout()

# 차트 표시
plt.show()









