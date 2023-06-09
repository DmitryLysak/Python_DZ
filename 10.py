'''Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть'''

n = int(input('Введите количество монет: '))
orel = 0
reshka = 0
for i in range(n):
    x = int(input('Положите монету, введите -> орел:1 или решка:0 -> '))
    if x != 1 and x != 0:
        print('ошибка ввода, перезапустите программу')
        exit()
    if x == 1:
        orel += 1
    else:
        reshka += 1
if orel == 0 or reshka == 0:
    print(f'все {n} монет(ы) лежат одинаковой стороной, переворачивать монеты не нужно')
elif orel == reshka:
    print(f'Количество орлов и решек одинаково, по {orel} штук(е)')
elif orel < reshka:
    print(f'Переверните {orel} монет(у) с орла на решку')
else:
    print(f'Переверните {reshka} монет(у) с решки на орла')

