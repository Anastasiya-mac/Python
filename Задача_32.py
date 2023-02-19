# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

def find_idx(list_of_input, min_, max_):
    res = []
    for i in range(len(list_of_input)):
        if list_of_input[i] <= max_ and list_of_input[i] >= min_:
            res.append(i)

    return res

list_of_input = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_ = 7
max_ = 10
print(find_idx(list_of_input, min_, max_))