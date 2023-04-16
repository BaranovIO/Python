# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

import random

n = int(input("Введите количество чисел в массиве: "))
count = 0
array_of_numbers = []

for i in range (n):
    number = random.randint(1, 10)
    array_of_numbers.append(number)

print(array_of_numbers)

x = int(input("Введите искомое число: "))
counter = 0
for i in range(n):
    if array_of_numbers[i] == x:
        counter += 1

if counter > 0:
    print(f"Число {x} встречается {counter} раз")
else:
    print("Указанного числа нет в массиве")