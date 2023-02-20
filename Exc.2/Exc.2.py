# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
import random

# определяем случайное трехзначное число 
number = random.randrange(100, 1000)

def SumOfNumbers (num):
    sum = 0
    
        # Простой вариант решения задачи
        # sum = sum + num % 10 + (num // 10) % 10 + (num // 100) % 10

        # Более полный вариант
    while num > 0:
        x = num % 10
        sum = sum + x
        num = num // 10
    return sum  
           

print('Искомое число равно:')
print(number)
sumOfNum = SumOfNumbers(number)
print("Сумма чисел равна:")
print(sumOfNum)

