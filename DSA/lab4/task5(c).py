class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def create(self):
        n = int(input("Enter number of nodes: "))

        if n <= 0:
            print("Number of nodes must be greater than 0.")
            return

        for i in range(n):
            data = int(input(f"Enter data for node {i + 1}: "))

            new_node = Node(data)

            if self.head is None:
                self.head = new_node
                new_node.next = self.head
            else:
                temp = self.head

                while temp.next != self.head:
                    temp = temp.next

                temp.next = new_node
                new_node.next = self.head

        print("Circular Linked List created successfully.")

    def insert_beginning(self):
        data = int(input("Enter data: "))

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            new_node.next = self.head
            temp.next = new_node
            self.head = new_node

        print("Node inserted at beginning.")

    def insert_end(self):
        data = int(input("Enter data: "))

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node
            new_node.next = self.head

        print("Node inserted at end.")

    def insert_position(self):
        position = int(input("Enter position: "))
        data = int(input("Enter data: "))

        if position <= 0:
            print("Invalid position.")
            return

        new_node = Node(data)

        if position == 1:
            if self.head is None:
                self.head = new_node
                new_node.next = self.head
            else:
                temp = self.head

                while temp.next != self.head:
                    temp = temp.next

                new_node.next = self.head
                temp.next = new_node
                self.head = new_node

            print("Node inserted.")
            return

        if self.head is None:
            print("Position does not exist.")
            return

        temp = self.head

        for i in range(position - 2):
            temp = temp.next

            if temp == self.head:
                print("Position does not exist.")
                return

        new_node.next = temp.next
        temp.next = new_node

        print("Node inserted.")

    def delete_by_value(self):
        if self.head is None:
            print("Circular Linked List is empty.")
            return

        value = int(input("Enter value to delete: "))

        current = self.head
        previous = None

        while True:

            if current.data == value:

                if current == self.head and current.next == self.head:
                    self.head = None

                elif current == self.head:
                    temp = self.head

                    while temp.next != self.head:
                        temp = temp.next

                    self.head = self.head.next
                    temp.next = self.head

                else:
                    previous.next = current.next

                print("Node deleted.")
                return

            previous = current
            current = current.next

            if current == self.head:
                break

        print("Value not found.")

    def delete_first(self):
        if self.head is None:
            print("Circular Linked List is empty.")
            return

        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            self.head = self.head.next
            temp.next = self.head

        print("First node deleted.")

    def delete_last(self):
        if self.head is None:
            print("Circular Linked List is empty.")
            return

        if self.head.next == self.head:
            self.head = None
            print("Last node deleted.")
            return

        temp = self.head

        while temp.next.next != self.head:
            temp = temp.next

        temp.next = self.head

        print("Last node deleted.")

    def count(self):
        if self.head is None:
            print("Number of nodes: 0")
            return

        count = 0
        temp = self.head

        while True:
            count += 1
            temp = temp.next

            if temp == self.head:
                break

        print("Number of nodes:", count)

    def display(self):
        if self.head is None:
            print("Circular Linked List is empty.")
            return

        temp = self.head

        print("Head to Tail:", end=" ")

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(back to head)")

    def display_tail_to_head(self):
        if self.head is None:
            print("Circular Linked List is empty.")
            return

        tail = self.head

        while tail.next != self.head:
            tail = tail.next

        print("Tail to Head:", end=" ")

        current = tail

        while True:
            print(current.data, end="")

            if current == self.head:
                break

            print(" <- ", end="")

            temp = self.head

            while temp.next != current:
                temp = temp.next

            current = temp

        print(" (reached head)")

    def exit_program(self):
        print("Program ended.")


cll = CircularLinkedList()

while True:

    print("\n======================================")
    print("       CIRCULAR LINKED LIST")
    print("======================================")

    print("1. Create Linked List")
    print("2. Insert at beginning")
    print("3. Insert at end")
    print("4. Insert at specific position")
    print("5. Delete by value")
    print("6. Delete First Node")
    print("7. Delete Last Node")
    print("8. Count no of nodes")
    print("9. Display Head to Tail")
    print("10. Display Tail to Head")
    print("11. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        cll.create()

    elif choice == 2:
        cll.insert_beginning()

    elif choice == 3:
        cll.insert_end()

    elif choice == 4:
        cll.insert_position()

    elif choice == 5:
        cll.delete_by_value()

    elif choice == 6:
        cll.delete_first()

    elif choice == 7:
        cll.delete_last()

    elif choice == 8:
        cll.count()

    elif choice == 9:
        cll.display()

    elif choice == 10:
        cll.display_tail_to_head()

    elif choice == 11:
        cll.exit_program()
        break

    else:
        print("Invalid choice.")
