class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def getLength(head):

    length = 0

    # Count nodes in linked list
    while head:
        length += 1
        head = head.next

    return length

def getMiddle(head):

    length = getLength(head)

    # traverse till we reach half of the length
    midIndex = length // 2
    while midIndex:
        head = head.next
        midIndex -= 1

    return head.data


if __name__ == "__main__":

    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    head.next.next.next.next.next = Node(60)

    print(getMiddle(head))