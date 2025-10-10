import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib import rc

from ch05.common_function import get_font_name
from ch05.sample01 import index_name






kor_file = './data/covid_kor.csv'
kor_df = pd.read_csv(kor_file)

print('='*50)
print(kor_df.head())

index_name = 'data'
kor_index_df = kor_df.set_index(index_name)

print('='*50)
print(kor_index_df.head())




