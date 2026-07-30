"question 4"

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n*factorial(n - 1)      

n = int(input("Enter the number of possible ways to arrange n different parcels: "))
factorial(n)
print(factorial(n))
