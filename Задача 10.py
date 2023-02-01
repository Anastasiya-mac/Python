# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.

# Пример:
# 5 -> 1 0 1 1 0
# 2

from random import randint

def flip_coins(n):
    list_of_coins = []
    
    for _ in range(n):
        list_of_coins.append(randint(0, 1))

    print(list_of_coins)

    count_heads = 0
    count_tails = 0

    for i in list_of_coins:
        if i == 1:
            count_heads += 1
        else: 
            count_tails += 1

    if count_heads > count_tails:
        res = count_tails
    else:
        res = count_heads
    
    return res

#Управляющий код
n = 5
res = flip_coins(n)
print(f'Нужно перевернуть минимум {res} монеты(у)')

