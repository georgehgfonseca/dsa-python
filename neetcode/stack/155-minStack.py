class MinStack:

    # thought about using linked lists to pop correctly, which would be quite complicated
    # looked at the smarter solution of keeping an additional min_val array
    def __init__(self):
        self.data = list()
        self.min_val = list()

    def push(self, val: int) -> None:
        self.data.append(val)
        min_value = min(val, self.min_val[-1] if self.min_val else val)
        self.min_val.append(min_value)

    def pop(self) -> None:
        self.data.pop()
        self.min_val.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min_val[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(5)
obj.push(2)
obj.pop()
print(obj.top())
print(obj.getMin())
    
