# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X

# 5
# 1 2 3 4 5
# 6
# -> 5

import random

n = int(input("Введите количество чисел в массиве: "))

array_of_numbers = []

for i in range (n):
    number = random.randint(1, 100)
    array_of_numbers.append(number)

print(array_of_numbers)

x = int(input("Введите искомое число: "))
min = abs(x - array_of_numbers[0])  
index = 0
for i in range(n):
    diff_number = abs(x - array_of_numbers[i])
    if diff_number < min:
        min = diff_number
        index = i

if diff_number == 0:
    print("Введённое число присутствует в массиве")
else:
    print(f'Число {array_of_numbers[index]} наиболее близко по величине к числу {x}')      


