N = int(input("Введите число N: "))
product = 1

for i in range(1, N + 1):
    product *= i

print(f"Произведение чисел от 1 до {N}: {product}")
