def fibonacci(n):
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

n = int(input("Введіть скільки чисел Фібоначчі вивести: "))

result = fibonacci(n)

print("Числа Фібоначчі:")
for num in result:
    print(num)
