'''Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X'''
import random

num = int(input('Введите количество элементов списка: '))
list = [random.randint(0, 10) for i in range(num)]
print(list)
find_num = int(input('Введите число, которое необходимо найти в списке: '))
count = 0
for i in range(len(list)):
    if list[i] == find_num:
        count += 1
print(f'Число {find_num} встречается в списке {count} раз(а)')
