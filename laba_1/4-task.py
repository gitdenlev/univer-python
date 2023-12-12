# Задача 4
import math as m


def f(x, y):
    return 1 / m.sqrt(float(x) ** 2 + float(y) ** 2)


work = True

while work:
    print("Hello!")
    first_value = input("Enter a1: ")
    second_value = input("Enter a2: ")

    try:
        result = f(first_value, second_value)
        print("The result is", result)
    except ValueError:
        print("Invalid input. Please enter numerical values for a1 and a2.")

    str_ans = input("Continue work? (y/n): ")

    if str_ans.lower() in ["n", "no"]:
        work = False
    elif str_ans.lower() not in ["y", "yes"]:
        print("I didn't understand your answer. Please, enter y, n, yes, or no")

print("Goodbye!")