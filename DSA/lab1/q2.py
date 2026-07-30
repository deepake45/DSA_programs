"question 2"

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

P = float(input("Enter the principal amount"))
r = float(input("Enther the annual interest rate:"))
n = int(input("Enter number of years:"))
A = P * power(1 + r, n)
compound_interest = A - P
print("final amount =", round(A, 2))
print("Compound Interest =", round(compound_interest, 2))
print(compound_interest)    
