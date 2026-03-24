"""Task 4"""

class Node:
    """Simple class representing a node in linked list"""

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def get_nth(node, index):
    if node is None:
        raise ValueError("Can not get n-th node in empty linked list")

    if index < 0:
        raise ValueError("Index out of range of linked list")

    found_node = None

    while node is not None:
        if index == 0:
            found_node = node
            break

        index -= 1
        node = node.next

    if found_node is None:
        raise ValueError("Index out of range of linked list")

    return found_node
