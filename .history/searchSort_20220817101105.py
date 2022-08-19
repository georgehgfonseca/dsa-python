class SearchSort:
    def __init__(self, array=[]):
        self.array = array

    def isOrdered(self):
        if len(self.array) <= 1:
            return True
        for i in range(1, len(self.array)):
            if self.array[i - 1] > self.array[i]:
                return False
        return True

    def binarySearch(self, v):
        print(len(self.array) // 2)
        if self.array[len(self.array) / 2]:
            pass
