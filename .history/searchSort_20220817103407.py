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
        low = 0
        high = len(self.array) - 1
        while high >= low:
            idx = ((high - low) // 2) + low
            print(low, high, idx)
            if self.array[idx] == v:
                return idx
            elif self.array[idx] < v:
                # Explore left-side of idx
                low = idx + 1
            else:
                high = idx - 1
        return -1

    def binarySearchRec(self, v):
        return self.binarySearchAux(self.array, len(self.array), v)

    def binarySearchAux(self, array, idx, v):
        print(array, idx, v)
        if len(array) == 0:
            return False
        idx = len(array) // 2
        if array[idx] == v:
            return True
        elif array[idx] < v:
            self.binarySearchAux(array[idx + 1 :], idx, v)
        else:
            self.binarySearchAux(array[0:idx], idx, v)
