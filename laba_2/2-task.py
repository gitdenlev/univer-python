import numpy as np
from timeit import default_timer as timer

def matrix_product_with_loops(a1, a2):
    rows, cols = len(a1), len(a2[0])
    result = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            for k in range(len(a2)):
                result[i][j] += a1[i][k] * a2[k][j]

    return result

def matrix_product_with_numpy(a1, a2):
    return np.dot(a1, a2)

# Генеруємо випадкові матриці a1 і a2
rows_a1, cols_a1 = 3, 4
rows_a2, cols_a2 = 4, 5

a1 = np.random.rand(rows_a1, cols_a1)
a2 = np.random.rand(rows_a2, cols_a2)

# Вимірюємо час для методу з циклами for
start_time = timer()
result_loops = matrix_product_with_loops(a1, a2)
end_time = timer()
time_loops = end_time - start_time

# Вимірюємо час для методу з бібліотекою NumPy
start_time = timer()
result_numpy = matrix_product_with_numpy(a1, a2)
end_time = timer()
time_numpy = end_time - start_time

# Порівнюємо результати та виводимо час виконання
if np.array_equal(result_loops, result_numpy):
    print("Результати збігаються.")
else:
    print("Результати не збігаються.")

print(f"Час виконання (цикли for): {time_loops:.6f} сек.")
print(f"Час виконання (NumPy): {time_numpy:.6f} сек.")
