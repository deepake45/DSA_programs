rows = int(input("Enter the row size for the pattern"))
for i in range(rows,0, -1):
    for j in range(1, rows + 1):
        if j == 1 or i == rows or i == j:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
