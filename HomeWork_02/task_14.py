# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2^k), не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input("Введите натуральное число: "))

numbers = []
i = 0
while 2 ** i <= n:
    power_of_two = 2 ** i
    numbers.append(power_of_two)
    i += 1

print(numbers)