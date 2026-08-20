"""creating a node"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
node1 = Node(10)
print(node1.data)
print(node1.next)
