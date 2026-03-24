"""Task 8"""

class Node:
    """Simple class representing a node in linked list"""

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def remove_duplicates(head):
    if head is None:
        return

    prev_probe = head
    probe = head.next

    while probe is not None:
        if prev_probe.data == probe.data:
            prev_probe.next = probe.next
            probe = probe.next

            continue

        prev_probe = probe
        probe = probe.next

    return head
