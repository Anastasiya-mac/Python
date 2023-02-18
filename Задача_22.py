# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений 
# в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

from random import randint

def intersect(n, m):
    A, B = [], []
    for _ in range(n):
        A.append(randint(0, 50))

    for _ in range(m):
        B.append(randint(0, 50))

    A = set(A)
    print(A)
    B = set(B)
    print(B)

    result = list(A & B)
    result.sort()
    return result


n = int(input("Первое множество: "))
m = int(input("Второе множество: "))
print("Пересечение ", intersect(n, m))