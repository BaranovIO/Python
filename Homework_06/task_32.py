# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7] min = 6, max = 10
# Вывод: [1, 9, 13, 14, 19]

list_of_numbers = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = int(input("Введите минимальное значение диапазона: "))
max_number = int(input("Введите максимальное значение диапазона: "))

list_of_indexes = []
for i in range(len(list_of_numbers)):
    if min_number <= list_of_numbers[i] <= max_number:
        list_of_indexes.append(i)

print(f"Индексы элементов в диапазоне от {min_number} и {max_number}: {list_of_indexes}")

