"""Task 6"""

class Node:
    """Simple class representing a node in linked list"""

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f"data: {self.data}"

def sorted_insert(head, data):
    if head is None:
        return Node(data)

    probe = head.next
    prev_node = head

    # Handle insertion to first position
    if prev_node.data > data:
        head = Node(data)
        head.next = prev_node

        return head

    while True:
        # Handle insertion to tail of a list
        if probe.next is None:
            # Extra check for when data is smaller than tail
            if probe.data > data:
                prev_node.next = Node(data)
                prev_node.next.next = probe
            else:
                probe.next = Node(data)
            break

        if prev_node.data < data < probe.data:
            prev_node.next = Node(data)
            prev_node.next.next = probe

            break

        prev_node = probe
        probe = probe.next

    return head
