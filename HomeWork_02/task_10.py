# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

import random
number_of_coins = int(input("Введите количество монет: "))

coins = []
for i in range (number_of_coins):
    side_of_coin = random.randint(0, 1) # генерируем случайное положение монетки - орёл или решка
    coins.append(side_of_coin)
print(coins)

counter_of_tails = 0    #счётчик монет, повёрнутых решкой
counter_of_eagles = 0   #счётчик монет, повёрнутых орлом
for i in coins:
    if i == 0:
        counter_of_tails += 1 
    else:
        counter_of_eagles += 1 #Была мысль также просто посчитать количество решек и отнять его от общего количества монет, чтобы получить количество орлов.

if counter_of_tails <= counter_of_eagles:
    print(f"Необходимо перевернуть {counter_of_tails} монет(-ы)") 
elif counter_of_tails == 0 or counter_of_eagles == 0:
    print("Монеты не нужно переворачивать")
else:
    print(f"Необходимо перевернуть {counter_of_eagles} монет(-ы)")
