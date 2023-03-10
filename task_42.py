# Узнать какая максимальная households в зоне минимального значения population.
import pandas as pd

df = pd.read_csv('sample_data/california_housing_train.csv')
df_min_pop = df[df['median_house_value'] < df['median_house_value'].quantile(.25)]['population'].max()
print(df_min_pop)