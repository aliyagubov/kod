class TwoStacks:
    def __init__(self, n):
        self.size = n
        self.arr = [0] * n
        self.top1 = n // 2 - 1  # top1 starts from the middle of the array - 1
        self.top2 = n // 2      # top2 starts from the middle of the array

    def push1(self, x):
        if self.top1 >= 0:  # Ensure there is space for stack1 (top1 should not overlap top2)
            self.top1 -= 1
            self.arr[self.top1] = x  # Insert the element
        else:
            print("Stack Overflow for stack1")

    def push2(self, x):
        if self.top2 < self.size:  # Ensure there is space for stack2 (top2 should not overlap top1)
            self.arr[self.top2] = x  # Insert the element
            self.top2 += 1
        else:
            print("Stack Overflow for stack2")

    def pop1(self):
        if self.top1 < self.size // 2 - 1:  # Ensure stack1 is not empty
            x = self.arr[self.top1]
            self.top1 += 1
            return x  # Return the element
        else:
            return -1  # Stack Underflow for stack1

    def pop2(self):
        if self.top2 > self.size // 2:  # Ensure stack2 is not empty
            self.top2 -= 1
            return self.arr[self.top2]  # Return the element
        else:
            return -1  # Stack Underflow for stack2


if __name__ == '__main__':
    ts = TwoStacks(5)
    ts.push1(2)
    ts.push1(3)
    ts.push2(4)
    print(ts.pop1(), end=' ')  
    print(ts.pop2(), end=' ')  
    print(ts.pop2(), end=' ')