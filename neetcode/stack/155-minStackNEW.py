class Node:
    def __init__(self, val = float("inf"), prev = None, prevMin = float("inf")):
        self.val = val
        self.prev = prev
        self.prevMin = min(val, prevMin)


class MinStack:

    def __init__(self):
        # dummy node
        self.topNode = Node()
        

    def push(self, val: int) -> None:
        self.topNode = Node(val, self.topNode, self.topNode.prevMin)


    def pop(self) -> None:
        popNode = self.topNode
        self.topNode = popNode.prev
       

    def top(self) -> int:
        return self.topNode.val
        

    def getMin(self) -> int:
        return self.topNode.prevMin


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(5)
obj.push(2)
obj.pop()
print(obj.top())
print(obj.getMin())
    
