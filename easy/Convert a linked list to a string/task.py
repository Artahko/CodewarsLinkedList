"""Task 1"""

class Node:
    """Simple class representing a node in linked list"""

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    if node == None:
        return "None"

    result = ""

    while node is not None:
        result += f"{node.data} -> "
        node = node.next

    result += "None"

    return result
