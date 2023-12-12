from timeit import default_timer as timer
import numpy as np

N = 1000  # Розмір масивів

# Створення масива заповненого нулями
a1 = np.zeros(N)
# Створення масива заповненого одиницями
a2 = np.ones(N)
# Масив який зберігає результат
result = np.zeros(N)

print("a) Складання массивів напряму в циклі:")
start = timer()  # Запуск таймера
for i in range(N):
    result[i] = a1[i] + a2[i]
end = timer()  # Зупинка таймера
print(f"Час виконання: {(end - start):.3e} с")

# Швидке складання
print("b) Складання за допомогою numpy:")
start = timer()  # Запуск таймера
result = a1 + a2
end = timer()  # Зупинка таймера
print(f"Час виконання: {(end - start):.3e} с")