'''Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)'''


my_list = [2, 5, 7, 8, 9, 10, 11, 15, 17]

min_val = 5
max_val = 11

indices = []

for index, value in enumerate(my_list):
    if min_val <= value <= max_val:
        indices.append(index)

print(indices)