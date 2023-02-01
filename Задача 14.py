# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2**k), не превосходящие числа N.

# Пример:
# 10 -> 1 2 4 8

def exponentiation(N):
    i = 1
    k = 1
    result = []
    while i <= N:
        for k in range(N):
            if 2**k == i:
                result.append(i)
        i+=1
    
    return result


N = 1024
print(exponentiation(N))