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

    print("Linked List created successfully.")

    # 2. Insert at Beginning
    def insert_beginning(self, data):

        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

        print("Node inserted successfully.")

    # 3. Insert at End
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            print("Node inserted successfully.")
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

        print("Node inserted successfully.")

    # 4. Insert at Specific Position
    # Position starts from 1
    def insert_at_position(self, data, position):

        if position < 1:
            print("Invalid position.")
            return

        new_node = Node(data)

        # Insert at position 1
        if position == 1:
            new_node.next = self.head
            self.head = new_node

            print("Node inserted successfully.")
            return

        temp = self.head

        # Move to the node before the required position
        for i in range(position - 2):

            if temp is None:
                print("Invalid position.")
                return

            temp = temp.next

        if temp is None:
            print("Invalid position.")
            return

        new_node.next = temp.next
        temp.next = new_node

        print("Node inserted successfully.")

    # 5. Delete by Value
    def delete_by_value(self, value):

        if self.head is None:
            print("Linked List is empty.")
            return

        # If first node contains the value
        if self.head.data == value:
            self.head = self.head.next

            print("Node deleted successfully.")
            return

        temp = self.head

        while temp.next is not None:

            if temp.next.data == value:
                temp.next = temp.next.next

                print("Node deleted successfully.")
                return

            temp = temp.next

        print("Value not found.")

    # 6. Delete First Node
    def delete_first(self):

        if self.head is None:
            print("Linked List is empty.")
            return

        deleted_value = self.head.data

        self.head = self.head.next

        print("First node deleted:", deleted_value)

    # 7. Delete Last Node
    def delete_last(self):

        if self.head is None:
            print("Linked List is empty.")
            return

        # Only one node
        if self.head.next is None:
            deleted_value = self.head.data

            self.head = None

            print("Last node deleted:", deleted_value)
            return

        temp = self.head

        while temp.next.next is not None:
            temp = temp.next

        deleted_value = temp.next.data

        temp.next = None

        print("Last node deleted:", deleted_value)

    # 8. Count Number of Nodes
    def count_nodes(self):

        count = 0
        temp = self.head

        while temp is not None:
            count += 1
            temp = temp.next

        print("Number of nodes:", count)

    # 9. Display / Traverse
    def display(self):

        if self.head is None:
            print("Linked List is empty.")
            return

        temp = self.head

        print("Linked List:")

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# ==========================================
# MAIN PROGRAM
# ==========================================
sll = singlyLinkedList()

while True:

    print("\n======================================")
    print("       SINGLY LINKED LIST")
    print("======================================")

    print("1. Create Linked List")
    print("2. Insert at beginning")
    print("3. Insert at end")
    print("4. Insert at specific position")
    print("5. Delete by value")
    print("6. Delete First Node")
    print("7. Delete Last Node")
    print("8. Count no of nodes")
    print("9. Display / Traverse")
    print("10. Exit")

    print("======================================")

    ch = int(input("Enter your choice: "))

    if ch == 1:

        sll.create()

    elif ch == 2:

        data = int(input("Enter data: "))

        sll.insert_beginning(data)

    elif ch == 3:

        data = int(input("Enter data: "))

        sll.insert_end(data)

    elif ch == 4:

        data = int(input("Enter data: "))

        position = int(input("Enter position (starting from 1): "))

        sll.insert_at_position(data, position)

    elif ch == 5:

        value = int(input("Enter value to delete: "))

        sll.delete_by_value(value)

    elif ch == 6:

        sll.delete_first()

    elif ch == 7:

        sll.delete_last()

    elif ch == 8:

        sll.count_nodes()

    elif ch == 9:

        sll.display()

    elif ch == 10:

        print("Exiting program...")
        break

    else:

        print("Invalid choice. Please enter a number between 1 and 10.")
