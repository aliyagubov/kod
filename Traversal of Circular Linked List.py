# Python program to traverse a circular
# linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(curr, head):

    # return if list is empty
    if head is None:
        return
    
    print(curr.data, end=" ")
    
    if (curr.next == head):
        return
    
    print_list(curr.next, head)

if __name__ == "__main__":
  
  	# Create a hard-coded linked list
	# 11 -> 2 -> 56 -> 12
    head = Node(11)
    head.next = Node(2)
    head.next.next = Node(56)
    head.next.next.next = Node(12)

    head.next.next.next.next = head

    print_list(head, head)