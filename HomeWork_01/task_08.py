# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите число долек шоколадки по длине: "))
m = int(input("Введите число долек шоколадки по ширине: "))
k = int(input("Какое количество долек шоколадки хотите отломить одим разломом? "))

if k > n * m:
    print("Вы хотите отломить долек больше, чем есть в шоколадке")

elif k == n * m:
    print("Это целая шоколадка")

if k % n == 0 or k % m == 0:
    print("Вы можете отломить столько долек")

else:
    print("Нельзя отломить столько долек")