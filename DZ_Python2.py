# 1. Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27
# Вариант I

# n = input("Введите число: ")
# suma = 0 
# for digit in n:
#     if digit.isdigit():
#         suma += int(digit) 
# print("Сумма:", suma)

# Вариант II

# num = float(input("Введите число: "))
# x = len(str(num))
# Num = (num * 10 **x)
# sum = 0
# while Num > 0:
#     dig = Num % 10
#     sum = sum + dig
#     Num = Num // 10
# print(int(sum))  

# 2. Напишите программу, которая принимает на вход число N и 
# выдает набор произведений чисел от 1 до N.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]

# N = int(input("Введите число: "))
# fact=1 
# for i in range(1, N + 1):
#      fact = fact * i 
#      print(fact, end=" ")
# print()     

# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и 
# выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

# import math
# n = int(input("Введите число: "))
# array = [n]
# sum = 0
# for n in range(1, n+1):
#      a = round((1+1/n)**n)     
#      sum = (sum + a)     
#      print(a, end=", ")
# print()
# print(sum)   

# * 4. Напишите программу, которая принимает на вход 2 числа. Задайте
#  список из N элементов, заполненных числами из промежутка [-N, N]. Найдите 
# произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

# from random import randint
# a = int(input("Введите позицию первого элемента: "))
# b = int(input("Введите позицию второго элемента: "))
# N = int(input("Введите число элементов: "))
# array = [randint(-N,N) for _ in range(N)]
# print(array)
# sum = array[a-1]*array[b-1]
# print(f"Произведение чисел на позициях {a} и {b} равна {sum}")

# 5. ** Реализуйте алгоритм перемешивания списка. 
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

# import random
# n = int(input("Введите количество элементов списка: "))
# array = list(range(n))
# print(array)
# i = 0
# while i < n:
#      x = random.randint(0, n - 1)
#      array.remove(x)
#      array.append(x)
#      i += 1   
# print(array)     




