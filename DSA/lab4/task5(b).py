class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
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
            else:
                temp = self.head

                while temp.next is not None:
                    temp = temp.next

                temp.next = new_node
                new_node.prev = temp

        print("Linked List created successfully.")

    def insert_beginning(self):
        data = int(input("Enter data: "))

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        print("Node inserted at beginning.")

    def insert_end(self):
        data = int(input("Enter data: "))

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

        print("Node inserted at end.")

    def insert_position(self):
        position = int(input("Enter position: "))
        data = int(input("Enter data: "))

        if position <= 0:
            print("Invalid position.")
            return

        new_node = Node(data)

        if position == 1:
            if self.head is not None:
                new_node.next = self.head
                self.head.prev = new_node

            self.head = new_node
            print("Node inserted.")
            return

        temp = self.head

        for i in range(position - 2):
            if temp is None:
                print("Position does not exist.")
                return
            temp = temp.next

        if temp is None:
            print("Position does not exist.")
            return

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next is not None:
            temp.next.prev = new_node

        temp.next = new_node

        print("Node inserted.")

    def delete_by_value(self):
        value = int(input("Enter value to delete: "))

        temp = self.head

        while temp is not None:
            if temp.data == value:

                if temp.prev is None:
                    self.head = temp.next

                    if self.head is not None:
                        self.head.prev = None

                else:
                    temp.prev.next = temp.next

                    if temp.next is not None:
                        temp.next.prev = temp.prev

                print("Node deleted.")
                return

            temp = temp.next

        print("Value not found.")

    def delete_first(self):
        if self.head is None:
            print("Linked List is empty.")
            return

        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

        print("First node deleted.")

    def delete_last(self):
        if self.head is None:
            print("Linked List is empty.")
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        if temp.prev is None:
            self.head = None
        else:
            temp.prev.next = None

        print("Last node deleted.")

    def count(self):
        count = 0
        temp = self.head

        while temp is not None:
            count += 1
            temp = temp.next

        print("Number of nodes:", count)

    def display_forward(self):
        if self.head is None:
            print("Linked List is empty.")
            return

        temp = self.head

        print("Forward:", end=" ")

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")

    def display_backward(self):
        if self.head is None:
            print("Linked List is empty.")
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        print("Backward:", end=" ")

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.prev

        print("None")


dll = DoublyLinkedList()

while True:

    print("\n======================================")
    print("       DOUBLY LINKED LIST")
    print("======================================")

    print("1. Create Linked List")
    print("2. Insert at beginning")
    print("3. Insert at end")
    print("4. Insert at specific position")
    print("5. Delete by value")
    print("6. Delete First Node")
    print("7. Delete Last Node")
    print("8. Count no of nodes")
    print("9. Display Forward")
    print("10. Display Backward")
    print("11. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        dll.create()

    elif choice == 2:
        dll.insert_beginning()

    elif choice == 3:
        dll.insert_end()

    elif choice == 4:
        dll.insert_position()

    elif choice == 5:
        dll.delete_by_value()

    elif choice == 6:
        dll.delete_first()

    elif choice == 7:
        dll.delete_last()

    elif choice == 8:
        dll.count()

    elif choice == 9:
        dll.display_forward()

    elif choice == 10:
        dll.display_backward()

    elif choice == 11:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
