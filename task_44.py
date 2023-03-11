# Задача 44
# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид.
# Сможете ли вы это сделать без get_dummies?

import random
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data)
human = list(map(int, data['whoAmI'].values == 'human'))
robot = list(map(int, data['whoAmI'].values == 'robot'))
data = data.assign(whoAmI_human = human, whoAmI_robot = robot)
data = data.drop(columns='whoAmI')
print(data)
 

