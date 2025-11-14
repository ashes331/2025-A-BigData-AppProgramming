import matplotlib.pyplot as plt
import pandas as pd

file_name = './data_raw.csv'
df_raw = pd.read_csv(file_name)

ds_data = df_raw.groupby(['Country']).size()

print('-'*100)
print(ds_data)

ds_data.nlargest(20).plot.pie(figsize=(10,10)) #인치단위
plt.tight_layout()
plt.show()

# 그래프 글자 한글로 변경 코드 과제










