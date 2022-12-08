# 22. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# my var
# new_list = [int(x) for x in input('Введите список из нескольких чисел через пробел: ').split()]
# print(new_list)
# summ = 0
# for i in range(1, len(new_list), 2):
#     summ += new_list[i]
# print(summ)

# var 2 (метод тот же, только задаем случайный список)
# from random import randint
# some_list = [randint(1, 10) for _ in range(5)]
# summa = 0
# print(some_list)
# for idx in range(1, len(some_list), 2):
# 	summa += some_list[idx]
# print(summa)

# ______________________________________________________________________________
# 23. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# my var
# inc_list = [int(x) for x in input('Введите список из нескольких чисел через пробел: ').split()]
# print(inc_list)
# res_list = []
# res_list_len = len(inc_list) // 2
# for i in range(res_list_len):
#     res_list.append(inc_list[i] * inc_list[-1 * (i + 1)])
# if len(inc_list) % 2 != 0:
#     res_list.append(inc_list[res_list_len] ** 2)
# print(res_list)

# var 2 (задаем рандомно, и решение одним перебором)
# from random import randint
# some_list = [randint(1, 10) for _ in range(5)]
# new_list = []
# print(some_list)
# for i in range(0, (len(some_list) - 1) // 2 + 1):
#     new_list.append(some_list[i] * some_list[len(some_list) - 1 - i])
# print(new_list)

# __________________________________________________________________________
# 24. Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# my var
# inc_list = [float(x) for x in input('Введите список из нескольких вещественных чисел через пробел: ').split()]
# print(inc_list)
# dec_list = []
# for i in range(len(inc_list)):
#     if inc_list[i] % 1 != 0:
#         dec_list.append(inc_list[i] % 1)
# print(round(max(dec_list) - min(dec_list), 2))

# var 2 (с семинара, интересный ввод, но мое решение изящнее)
# some_list = [float(input()) for _ in range(int(input()))]
# minn = 1
# maxx = 0
# for el in some_list:
#     if el % 1 < minn and el % 1 != 0:
#         minn = el % 1
#     else:
#         if el % 1 > maxx:
#             maxx = el % 1
# print(maxx - minn)

# var 3 (strings)
# some_list = [input() for _ in range(int(input()))]
# minn = 1
# maxx = 0
# for el in some_list:
#     if '.' in el:
#         if float('0.' + el.split('.')[1]) < minn:
#             minn = float('0.' + el.split('.')[1])
#         else:
#             if float('0.' + el.split('.')[1]) > maxx:
#                 maxx = float('0.' + el.split('.')[1])
# print(maxx - minn)

# var 4 (от Рината тяжелый, но генерация интересная))
# import math
# import random
# n = int(input('Введите размер списка: '))
# lst = [math.floor(random.random() * random.randint(1, 100) * 100) / 100 for _ in range(n)]
# print(f'Сгенерированный список случайных чисел от 0 до {n - 1}: {lst}')
# min_fract, max_fract = 100., .0
# for num in lst:
#     fract = math.floor((num - int(num)) * 100) / 100
#     if fract < min_fract:
#         min_fract = fract
#     if fract > max_fract:
#         max_fract = fract
#
# print(f'Максимальная дробная часть: {max_fract}, минимальная дробная часть: {min_fract}, их разность: {max_fract - min_fract}')

# ________________________________________________________________________
# 25. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# my var
# n = int(input('Введите десятичное число: '))
# res_bin = ''
# while n > 0:
#     res_bin = str(n % 2) + res_bin
#     n = n // 2
# print(res_bin)

# var 2
# n = int(input())
# print(bin(n)[2:])
# our_str = ''
# while n != 0:
#     our_str = str(n % 2) + our_str
#     n //= 2
# print(our_str)

# ________________________________________________________________________________________
# 26. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# my var
# n = int(input('Введите границу списка Фибоначчи: '))
# fib_start = 0
# fib_next = 1
# list_Fibonacci = [0, fib_next]
# for i in range(n - 1):
#     fib_start, fib_next = fib_next, fib_start + fib_next
#     list_Fibonacci.append(fib_next)
# start_fib = 1
# fib_prev = 0
# i = 0
# for i in range(n):
#     start_fib, fib_prev = fib_prev, start_fib - fib_prev
#     list_Fibonacci.insert(0, fib_prev)
# print(list_Fibonacci)

# var 2
# k = int(input())
# some_list = [0] * (2 * k + 1)
# some_list[k + 1] = 1
# for i in range(k + 2, 2 * k + 1):
#     some_list[i] = some_list[i - 1] + some_list[i - 2]
# for i in range(k - 1, -1, -1):
#     some_list[i] = some_list[i + 2] - some_list[i + 1]
# print(some_list)

