rows = int(input("Enter the row size of the pattern"))
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print("*", end =" ")
    print()
