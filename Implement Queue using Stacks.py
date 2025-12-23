class myQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    # Enqueue operation (costly)
    def enqueue(self, x):
        
        # Move all elements from s1 to s2
        while self.s1:
            self.s2.append(self.s1.pop())

        # Push the new item into s1
        self.s1.append(x)

        # Move everything back to s1
        while self.s2:
            self.s1.append(self.s2.pop())

    # Dequeue operation
    def dequeue(self):
        if not self.s1:
            # Queue underflow
            return  
        self.s1.pop()

    # Front operation
    def front(self):
        if not self.s1:
            return -1
        return self.s1[-1]

    # Size operation
    def size(self):
        return len(self.s1)

if __name__ == "__main__":
    q = myQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    
    print("Front:", q.front())  
    print("Size:", q.size())    
    
    q.dequeue()        
    print("Front:", q.front())  
    print("Size:", q.size())