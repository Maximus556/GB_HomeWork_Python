'''
Задача №1
Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.
*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 
'''
A = int(input('введите число: ')) 
B = int(input('введите степень: '))

def degree (A, B):
    if B == 0:
        return 1
    return A * degree(A, B - 1)
print (degree (A, B))