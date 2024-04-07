def loop_size(head):
    if not head or not head.next:
        return 0
    slow = head.next
    fast = head.next.next
    while slow != fast:
        if not fast or not fast.next:
            return 0
        slow = slow.next
        fast = fast.next.next
    counter = 1
    slow = slow.next
    while slow != fast:
        counter += 1
        slow = slow.next
    return counter