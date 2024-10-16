def print_design(n):
    
    for i in range(1, n + 1):
        print((str(i) + ' ') * i)  

n = int(input("masukkan jumlah baris: "))
print_design(n)