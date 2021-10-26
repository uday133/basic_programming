fibo_rang = int(input("Enter Range :: "))
a = 0
b = 1
if fibo_rang == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2, fibo_rang):
        c = a + b
        a = b
        b = c
        print(c)


# Fibo with recursive function
def fibo(n):
    if n <= 1:
        return n
    else:
        return (fibo(n - 1) + fibo(n - 2))


fibo_rang = int(input("Enter Range :: "))
if fibo_rang <= 0:
    print("Enter Positive Number ")
else:
    for i in range(fibo_rang):
        print(fibo(i))
