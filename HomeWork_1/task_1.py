'''
Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) 
'''

i = input('Введите трехзначное число: ')
print(f'Сумма цифр трехзначного числа: {int(i[0])+int(i[1])+int(i[2])}')
