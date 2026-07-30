"question 1"

def countdown(n):
    if n > 0:
        print(n)
        countdown(n - 1)
n = int(input("Enter the countdown time:"))
countdown(n)
print("rocket launches!!")
