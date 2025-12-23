class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteFirstNode(last):
    if last is None:
        
        # If the list is empty
        print("List is empty")
        return None

    head = last.next

    if head == last:
        
        # If there is only one node in the list
        last = None
    else:
        
        # More than one node in the list
        last.next = head.next

    return last

def printList(last):
    if last is None:
        return

    head = last.next
    while True:
        print(head.data, end="")
        head = head.next
        if head == last.next:
            break
        print(" <-> ",end="")
    print()

if __name__ == "__main__":
    first = Node(2)
    first.next = Node(3)
    first.next.next = Node(4)

    last = first.next.next
    last.next = first

    last = deleteFirstNode(last)

    printList(last)