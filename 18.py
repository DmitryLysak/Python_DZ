''' Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X'''
import random

num = int(input('Введите количество элементов списка: '))
list = [random.randint(0, 1000) for i in range(num)]
print(list)
ind_num = int(input('Введите число: '))
index_element = 0
min_element = abs(ind_num - list[0])
for i in range(1, num):
    find_element = abs(ind_num - list[i])
    if find_element < min_element:
        min_element = find_element
        index_element = i
print(f'Самый близкий по величине элемент к заданному числу {list[index_element]}')

