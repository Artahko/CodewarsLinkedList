"""Task 11"""

class Node:
    """Simple class representing a node in linked list"""

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def loop_size(node):
    slow = node.next
    fast = node.next.next

    # Look for a coliding point
    while slow != fast:
        slow = slow.next
        fast = fast.next.next

    # Look for start of the loop
    while slow != fast:
        slow = slow.next
        fast = fast.next

    starting_node = slow
    count = 1
    slow = slow.next

    # Count the lenght of the loop
    while starting_node != slow:
        count += 1
        slow = slow.next

    return count
