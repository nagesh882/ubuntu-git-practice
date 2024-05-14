def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
        
n = int(input("Enter the value: "))


for i in range(1,n):
    print(fibo(i), end=" ")

print("\n"*2)
