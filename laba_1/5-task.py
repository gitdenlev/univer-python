def calculator():
    while True:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
        operation = input("Виберіть операцію (+, -, /, *): ")

        if operation == '+':
            result = int(num1 + num2)
        elif operation == '-':
            result = int(num1 - num2)
        elif operation == '/':
            if num2 != 0:
                result = int(num1 / num2)
            else:
                print("Ділення на нуль неможливе. Спробуйте ще раз.")
                continue
        elif operation == '*':
            result = int(num1 * num2)
        else:
            print("Невідома операція. Спробуйте ще раз.")
            continue

        if result > 100 or result < 0.01:
            print(f"Результат: {result:.3e}")
        else:
            print(f"Результат: {result}")

        repeat = input("Хочете продовжити? (так/ні): ")
        if repeat.lower() != "так":
            break
calculator()