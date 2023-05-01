'''Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.'''

num_a = int(input('Введите число A: '))
num_b = int(input('Введите степень B: '))
def recursive(a, b):
    if b == 0:
        return 1
    else:
        return a * recursive(a, b - 1)

print(f'Число {num_a} в степени {num_b} = {recursive(num_a, num_b)}')

