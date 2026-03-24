"""Task 5"""

class Node:
    """Simple class representing a node in linked list"""

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    if source is None:
        raise ValueError("Can not move first node from an empty source linked list")

    head_data = source.data
    dest_head = dest

    source = source.next
    dest = Node(head_data)
    dest.next = dest_head

    return Context(source, dest)
