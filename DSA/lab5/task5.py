"""write a python program to implement a stack using an array,
linked list. Also implement the stack operations such as push,
pop, peek and also display the stack elements"""

stack = []

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        x = int(input("Enter element: "))
        stack.append(x)
        print("Pushed:", x)

    elif choice == 2:
        if len(stack) == 0:
            print("Stack Underflow")
        else:
            print("Popped:", stack.pop())

    elif choice == 3:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Top:", stack[-1])

    elif choice == 4:
        print("Stack:", stack[::-1])

    elif choice == 5:
        break

    else:
        print("Invalid choice")
