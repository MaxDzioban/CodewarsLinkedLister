class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def length(node):
    counter=0
    while node is not None:
        counter+=1
        node = node.next
    return counter
def count(node, data):
    counter=0
    while node is not None:
        if node.data == data:
            counter+=1
        node = node.next
    return counter