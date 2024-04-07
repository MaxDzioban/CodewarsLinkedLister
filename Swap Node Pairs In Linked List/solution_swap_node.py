class Node:
    def __init__(self, next=None):
        self.next = next
def swap_pairs(head):
    if head is None or (head.next is None):
        return head
    dummy=Node(0)
    dummy.next = head
    prev = dummy
    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next
        prev.next = second
        first.next = second.next
        second.next = first
        prev = first
    return dummy.next