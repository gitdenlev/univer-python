# Задача 2
import math as m
def f(x, y):
    return 1 / m.sqrt(float(x) ** 2 + float(y) ** 2)


print("Please, write numbers...")
first_num = input("Enter value a1: ")
second_num = input("Enter value a2: ")
print("The result is: ", f(first_num, second_num))
