# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

number = input("Введите номер билета: ")

if len(number) == 6:                #проверка на то, что номер билета состоит из 6 цифр
    ticketNumber = int(number)
    num1 = ticketNumber // 1000     #первые 3 цифры числа
    num2 = ticketNumber % 1000      #вторые 3 цифры числа
    sum1 = 0                        #сумма первых 3 цифр
    sum2 = 0                        #сумма вторых 3 цифр
    
    while num1 > 0 and num2 > 0:
        sum1 += num1 % 10           #вычленяем по 1 цифре из числа
        num1 = num1 // 10           #уменьшаем число на 1 разряд
        sum2 += num2 % 10     
        num2 = num2 // 10
    
    print(sum1 == sum2)             #
else:
    print("Некорректный номер билета")