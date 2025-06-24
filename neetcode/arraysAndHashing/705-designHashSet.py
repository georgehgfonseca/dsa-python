class ListNode:
    def __init__(self, key: int):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for _ in range(5)]

    def add(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False
    
myHashSet = MyHashSet()
myHashSet.add(1) # set = [1]
myHashSet.add(2) # set = [1, 2]
myHashSet.contains(1) # return True
myHashSet.contains(3) # return False, (not found)
myHashSet.add(2) # set = [1, 2]
myHashSet.contains(2) # return True
myHashSet.remove(2) # set = [1]
myHashSet.contains(2) # return False, (already removed)