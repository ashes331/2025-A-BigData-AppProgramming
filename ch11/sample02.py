import matplotlib.pyplot as plt
import pandas as pd

file_name = './data_raw.csv'
df_raw = pd.read_csv(file_name)

### 개발자 연령대?????

COLUMN_AGE = 'Age'

sr_data = df_raw[COLUMN_AGE]
print('-'*100)
print(sr_data)

print('-'*100)
print(sr_data.unique())

print('-'*100)
print(sr_data.drop_duplicates())

ds_data = df_raw.groupby([COLUMN_AGE]).size()

reindex_column = [
    '65 years or older'
    , '55-64 years old'
    , '45-54 years old'
    , '35-44 years old'
    , '25-34 years old'
    , '18-24 years old'
    , 'Under 18 years old'
    , 'Prefer not to say'
]
ds_data = ds_data.reindex(reindex_column)

#ds_data.plot.line(rot=45)
#ds_data.plot.bar()
ds_data.plot.barh()

plt.tight_layout()
plt.show()