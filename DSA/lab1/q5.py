"question 5"

def fibbanocci(n):
    if n == 0 or n == 1:
        return 1
    return fibbanocci(n - 1) + fibbanocci(n - 2)
n = int(input("Enter the number of fibbanocci terms"))
fibbanocci(n)
print(fibbanocci(n))
