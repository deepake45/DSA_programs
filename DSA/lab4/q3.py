# Node of a Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Singly Linked List
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Display / Traversal
    def display(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    # 2. Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    # 3. Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    # 4. Insert at a specific position
    def insert_at_position(self, data, position):
        new_node = Node(data)

        # Insert at beginning
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head

        for _ in range(position - 2):
            if current is None:
                print("Invalid position")
                return
            current = current.next

        if current is None:
            print("Invalid position")
            return

        new_node.next = current.next
        current.next = new_node

    # 5. Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

    # 6. Delete from end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        # Only one node
        if self.head.next is None:
            self.head = None
            return

        current = self.head

        while current.next.next:
            current = current.next

        current.next = None

    # 7. Delete from a specific position
    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty")
            return

        # Delete first node
        if position == 1:
            self.head = self.head.next
            return

        current = self.head

        for _ in range(position - 2):
            if current.next is None:
                print("Invalid position")
                return
            current = current.next

        if current.next is None:
            print("Invalid position")
            return

        current.next = current.next.next

    # 8. Search for an element
    def search(self, value):
        current = self.head
        position = 1

        while current:
            if current.data == value:
                return position

            current = current.next
            position += 1

        return -1

    # 9. Count number of nodes
    def count(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next

        return count

    # 10. Update a node
    def update(self, old_value, new_value):
        current = self.head

        while current:
            if current.data == old_value:
                current.data = new_value
                return True

            current = current.next

        return False

    # 11. Reverse the linked list
    def reverse(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous

            previous = current
            current = next_node

        self.head = previous

    # 12. Find the middle node
    def find_middle(self):
        if self.head is None:
            return None

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data


# -----------------------------------
# Example Usage
# -----------------------------------

linked_list = SinglyLinkedList()

# Insert elements
linked_list.insert_end(10)
linked_list.insert_end(20)
linked_list.insert_end(30)

print("Original list:")
linked_list.display()

# Insert at beginning
linked_list.insert_beginning(5)

print("After inserting 5 at beginning:")
linked_list.display()

# Insert at position
linked_list.insert_at_position(15, 3)

print("After inserting 15 at position 3:")
linked_list.display()

# Delete beginning
linked_list.delete_beginning()

print("After deleting beginning:")
linked_list.display()

# Delete end
linked_list.delete_end()

print("After deleting end:")
linked_list.display()

# Delete at position
linked_list.delete_at_position(2)

print("After deleting position 2:")
linked_list.display()

# Search
position = linked_list.search(20)
print("Position of 20:", position)

# Count
print("Number of nodes:", linked_list.count())

# Update
linked_list.update(20, 100)

print("After updating 20 to 100:")
linked_list.display()

# Reverse
linked_list.reverse()

print("After reversing:")
linked_list.display()

# Middle
print("Middle node:", linked_list.find_middle())
