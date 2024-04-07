class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(s):
    if s == "None":
        return None
    if not s:
        return None
    values = s.split(" -> ")
    head = Node(int(values[0]))
    current = head
    for val in values[1:]:
        if val != "None":
            current.next = Node(int(val))
            current = current.next
    return head 