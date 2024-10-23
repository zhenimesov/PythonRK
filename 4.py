import random

numbers = [random.randint(1, 100) for _ in range(20)]
even_count = sum(1 for x in numbers if x % 2 == 0)
odd_count = sum(1 for x in numbers if x % 2 != 0)

print(f"Список: {numbers}")
print(f"Количество чётных чисел: {even_count}")
print(f"Количество нечётных чисел: {odd_count}")
