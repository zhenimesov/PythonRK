import numpy as np

array = np.random.randint(1, 101, size=(4, 4))
array_sum = np.sum(array)

print(f"Двумерный массив 4x4:\n{array}")
print(f"Сумма всех элементов массива: {array_sum}")
