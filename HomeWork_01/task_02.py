# Задача 2: Найдите сумму цифр трехзначного числа. 
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input("Введите целое число: "))

sum = 0
while number > 0:
    sum += number % 10          #вычленяем по 1 цифре из числа
    number = number // 10       #уменьшаем число на 1 разряд

print("Сумма цифр вашего числа", sum)