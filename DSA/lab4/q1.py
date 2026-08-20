class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
temp = head
while temp is not None:
    print(temp.data, end=" ")
    temp = temp.next
