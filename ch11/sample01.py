
import pandas as pd


file_name = './survey_results_public1.csv'
df_raw = pd.read_csv(file_name)

print('-'*100)
print(df_raw.head())

print('-'*100)
print(df_raw.info())

columns = ['LearnCode', 'LanguageHaveWorkedWith', 'Age', 'Country', 'Gender']
df_raw = df_raw[columns]

print('-'*100)
print(df_raw.head())

df_raw.to_csv('./data_raw.csv')












