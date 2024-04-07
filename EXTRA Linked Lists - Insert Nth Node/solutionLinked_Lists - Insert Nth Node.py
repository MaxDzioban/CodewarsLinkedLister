class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def insert_nth(head, index, data):
    if index == 0:
        new_node = Node(data)
        new_node.next = head
        return new_node
    counter = 0
    node = head
    while node is not None:
        if counter + 1 == index:
            new_node = Node(data)
            new_node.next = node.next
            node.next = new_node
            return head
        node = node.next
        counter += 1
    raise IndexError