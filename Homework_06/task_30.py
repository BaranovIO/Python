# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: 
# an = a1+(n-1)*d.
# Каждое число вводится с новой строки.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

first_element = int(input("Введите первый элемент арифметической прогрессии: "))
delta = int(input("Введите разность арифметической прогрессии: "))
amount = int(input("Введите количество элементов арифметической прогрессии: "))


for i in range(amount):
    element_of_progression = first_element + i * delta
    print(element_of_progression, end = " ")



