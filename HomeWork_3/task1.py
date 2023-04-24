
'''
Задача 16: Требуется вычислить, сколько раз встречается некоторое 
число X в массиве A. Пользователь в первой строке вводит натуральное 
число N – количество элементов в массиве. В последующих  строках записаны N 
целых чисел Ai (можно использовать псевдогенерацию). Последняя строка содержит число X.
*Пример:*
5
    7 -2 3 5 1
    3
    -> 1
'''

import random
N = int(input('Введите размер массива: '))
X = int(input('Введите число X: '))
lst = [random.randint(-10, 10) for _ in range(N)]
print (lst)
count = 0
for i in range(N):
    if lst[i] == X:
        count += 1
print(f'Число {X} встречается в списке А {count} раз.')