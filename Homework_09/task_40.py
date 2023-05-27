#Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)

import pandas as pd

df = pd.read_csv('california_housing_train.csv')

df1 = df.loc[(df.population >= 0) & (df.population <= 500)]
#print(df1) - 1605 записей
print(df1.median_house_value.mean())

