"""Task 7"""

class Node:
    """Simple class representing a node in linked list"""

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f"data: {self.data}"


def reverse(head):
    if head is None:
        return head

    def move_last_to_front(prev_node, node):
        if node is None:
            return

        move_last_to_front(node, node.next)

        temp_data = prev_node.data
        prev_node.data = node.data
        node.data = temp_data

    probe = head

    while probe.next is not None:
        move_last_to_front(probe, probe.next)
        probe = probe.next

    return head
