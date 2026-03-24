"""Task 3"""

class Node:
    """Simple class representing a node in linked list"""

    def __init__(self, data, next = None):
        self.data = data
        self.next = next


def push(head, data):
    new_node = Node(data)
    new_node.next = head

    return new_node

def build_one_two_three():
    head = Node(3)
    head = push(head, 2)
    head = push(head, 1)

    return head
