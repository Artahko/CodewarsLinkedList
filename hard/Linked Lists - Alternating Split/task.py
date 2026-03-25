"""Task 10"""

class Node:
    """Simple class representing a node in linked list"""

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second


def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError("Can not handle empty linked list or linked list with one node")

    probe = head
    nodes = []
    nodes1 = []
    nodes2 = []

    while probe is not None:
        nodes.append(probe)
        probe = probe.next

    # Iterate in a list
    for i, el in enumerate(nodes):
        if i % 2 == 0:
            nodes1.append(el)
        else:
            nodes2.append(el)

    linked_list1 = head
    linked_list2 = head.next

    for i, el in enumerate(nodes1[:-1]):
        el.next = nodes1[i+1]

    for i, el in enumerate(nodes2[:-1]):
        el.next = nodes2[i+1]

    nodes1[-1].next = None
    nodes2[-1].next = None

    return Context(linked_list1,linked_list2)
