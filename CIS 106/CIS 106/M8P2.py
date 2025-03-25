a, b = 0, 1
print("First 20 Fibonacci Numbers:")

for _ in range(20):
    print(a, end=" ")
    a, b = b, a + b
