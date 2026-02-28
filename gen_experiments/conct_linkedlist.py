class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def concatenate(h1, h2):
    if h1 is None:
        return h2
    if h2 is None:
        return h1
    
    current = h1
    while current.next is not None:
        current = current.next

    current.next = h2
    return h1

def printLL(head):
    current = head
    while current:
        print(current.data)
        current = current.next
    print()

if __name__ == "__main__":
    h1 = Node(1)
    h1.next = Node(2)
    h1.next.next = Node(3)

    h2 = Node(4)
    h2.next = Node(5)

    concat = concatenate(h1, h2)
    printLL(concat)
