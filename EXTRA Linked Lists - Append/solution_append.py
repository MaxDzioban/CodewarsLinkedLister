class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def append(A, B):
    if A is None and B is None:
        return None
    elif A is None or B is None:
        return A if A else B
    current = A
    while current.next is not None:
        current = current.next
    current.next = B
    return A
