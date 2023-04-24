# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def exponentiation(user_number, power):
    if power == 0:
        return 1
    return (user_number * exponentiation(user_number, power - 1))
    
user_number = int(input("Введите число: "))
power = int(input("Введите степень, в которую хотите возвести число: "))
result_of_exponentiation = exponentiation(user_number, power)
print(f"{user_number} в степени {power} = {result_of_exponentiation}")
    
