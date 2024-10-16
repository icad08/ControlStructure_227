def print_fibonacci(n):
   
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()  # For a newline after the series

n = int(input("Masukkan nomor dalam seri Fibonacci: "))
print_fibonacci(n)
