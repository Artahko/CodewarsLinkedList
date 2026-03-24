"""Task 2"""

class Node:
    """Simple class representing a node in linked list"""

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr == "None":
        return

    linked_list = list_repr.split(" -> ")
    nodes = [Node(int(el)) for el in linked_list[:-1]]

    for i, node in enumerate(nodes[:-1]):
        node.next = nodes[i+1]

    return nodes[0]
