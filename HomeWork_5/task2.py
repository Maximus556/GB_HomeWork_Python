'''
Задача 28: Напишите рекурсивную функцию sum(a, b), 
возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. 
Также нельзя использовать циклы.
*Пример:*

2 2
    4 
'''
A = int(input('введите число №1: ')) 
B = int(input('введите число №2: '))

def sum_rec (A, B):
    if A == 0:
        return B
    return sum_rec(A - 1, B + 1)
print (sum_rec (A, B))