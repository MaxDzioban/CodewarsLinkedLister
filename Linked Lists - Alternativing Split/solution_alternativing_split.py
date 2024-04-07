class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if not head or not head.next:
        raise ValueError
    first_head = first_tail = head
    second_head = second_tail = head.next
    current = second_tail.next if second_tail else None
    while current:
        first_tail.next = current
        first_tail = first_tail.next
        current = current.next
        if current:
            second_tail.next = current
            second_tail = second_tail.next
            current = current.next
    first_tail.next = None
    second_tail.next = None
    return Context(first_head, second_head)