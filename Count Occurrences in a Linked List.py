# Python program to count occurrences in
# a linked list by recursion
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def count(head, key):
    if head is None:
        return 0
      
    ans = count(head.next, key)
    
    if head.data == key:
        ans += 1
    
    return ans

# Hard coded linked list: 
# 1 -> 2 -> 1 -> 2 -> 1
head = Node(1)
head.next = Node(2)
head.next.next = Node(1)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

key = 1

print(count(head, key))