# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются
# в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы
# множеств.

n = int(input("Введите размер первого множества: "))


mylist_1 = []
mylist_2 = []
list_1 = list()

for i in range(n):
    number_of_mylist_1 = int(input("Введите число - элемент множества: "))
    mylist_1.append(number_of_mylist_1)
print(f"Первое множество: {mylist_1}")

m = int(input("Введите размер второго множества: "))
for i in range(m):
    number_of_mylist_2 = int(input("Введите число - элемент множества: "))
    mylist_2.append(number_of_mylist_2)
print(f"Второе множество: {mylist_2}")

myset_1 = set(mylist_1)
myset_2 = set(mylist_2)

result_set = set.intersection(myset_1, myset_2)
result_list = sorted(list(result_set))
print(f"Числа, встречающиеся в обоих множествах: {result_list}")