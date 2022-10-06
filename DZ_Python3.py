# 1. Задайте список, состоящий из произвольных чисел, количество 
# задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22
# in
# 4
# out
# [4, 2, 4, 9]
# 8

# import random

# n = int(input("Введите количество элементов: "))
# array = [random.randint(1,n) for _ in range(n)]
# sum = 0
# print(array)
# i=0
# while i < n:
#     sum +=array[i]
#     i+=2
# print(sum)    


# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]
# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

# import random


# n = int(input("Введите количество элементов: "))
# array = [random.randint(1,n) for _ in range(n)]
# new_array = list()
# sum = 0
# print(array)
# for i in range(n//2):
#     sum = array[i]*array[(i+1)*-1]
#     new_array.append(sum)
# print(new_array)


# 3. Напишите программу, которая будет преобразовывать десятичное
#  число в двоичное.
# 
# in
# 88
# out
# 1011000
# in
# 11
# out
# 1011

# Вариант I

# num = int(input("Введите число для преобразования: "))
# array = []
# while num > 0:
#     array.append(str(num%2))
#     num//=2
# print(''.join(reversed(array)))

# Вариант II

# num = int(input("Введите число для преобразования: "))
# digit = 0
# sum = 0
# while num > 0:
#     for i in range(num):
#         digit = (num %2 ) * 10 ** i
#         sum += digit
#         num //= 2
# print(sum)

# 4.* Задайте список из произвольных вещественных чисел,
#  количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между
#  максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76
# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

# from random import uniform


# num = int(input("Введите число: "))
# array = list()
# for i in range(num):
#     digit = round(uniform(1, 5), 2)
#     array.append(digit)
# print(array) 
# min = 1
# max = 0
# diff = 0
# for i in range(num):
#     if (array[i]%1)<min:
#         min = round((array[i]%1),2)
#     if (array[i]%1)>max:
#         max = round((array[i]%1),2) 
# diff = round((max - min),2)
# print(f'Разница между максимальным и минимальным остатком: ', diff)             

# 5. ** Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Негафибоначчи
# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5

# def fibonachi (count):
#     array = [1, 0, 1]
#     if count < 0:
#         return "Ошибка"
#     elif count == 1:
#         print(array)
#     else:
#         i = 3
#         while i <(count * 2):
#             array.append(array[i - 1] + array[i - 2])
#             if len(array) % 4 == 0:
#                 array.insert(0, array[i] * - 1)
#             else:
#                 array.insert(0, array[i])
#             i += 2
#     print(array)  
# print('Введите число')
# fibonachi(int(input()))                        