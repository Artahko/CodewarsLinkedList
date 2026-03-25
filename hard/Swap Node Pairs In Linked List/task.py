"""Task 9"""

class Node:
    """Simple class representing a node in linked list"""

    def __init__(self, next = None):
        self.next = next


def swap_pairs(head):
    if head is None or head.next is None:
        return head

    probe = head

    odd_nodes = []
    even_nodes = []

    # Get even and odd nodes
    while probe is not None:
        if (len(odd_nodes) + len(even_nodes)) % 2 == 0:
            odd_nodes.append(probe)
        else:
            even_nodes.append(probe)

        probe = probe.next

    head = head.next

    swapped_nodes = []

    # Swap them
    for i in range(len(even_nodes)):
        even_nodes[i].next = odd_nodes[i]
    for i in range(len(even_nodes)-1):
        odd_nodes[i].next = even_nodes[i+1]
    # Check if even == odd
    if len(even_nodes) == len(odd_nodes):
        odd_nodes[-1].next = None
    else:
        odd_nodes[-2].next = odd_nodes[-1]

    return head
