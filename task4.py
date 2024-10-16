def print_odd_numbers(n):
    
    for i in range(1, n + 1, 2): 
        print(i, end=" ")
    print() 


n = int(input("masukkan angka ganjil: "))
print_odd_numbers(n)