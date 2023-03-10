# Работать с файлом california_housing_train.csv, который находится в папке
# sample_data. Определить среднюю стоимость дома (median_house_value), где кол-во людей от 0 до 500 (population).
import pandas as pd

df = pd.read_csv('sample_data/california_housing_train.csv')
print(df[(df['population']<500) & (df['population']>0)]['median_house_value'].head())