stack = []
while True:
    print("1.Push")
    print("2.Pop")
    print("3.Peek")
    print("4.Display")
    print("5.Exit")

    choice = int(input("Enter your choice : "))
    if choice == 1:
        x = int(input("Enter element to pop:"))
        stack.append(x)
        print("Pushed : ", x)

    elif choice == 2:
        if len(stack) == 0:
            print("Stack underflow")
        else:
            print("Popped : ", stack.pop())

    elif choice == 3:
        if len(stack) == 0:
            print("The stack is empty")
        else:
            print("Top : ", stack[-1])

    elif choice == 4:
        print("Stack : ", stack[::-1])

    elif choice == 5:
        break
    else:
        print("Invalid choice")
