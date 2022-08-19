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
        return self.binarySearchAux(self.array, len(self.array), v)

    def binarySearchAux(self, array, idx, v):
        print(array, idx, v)
        idx = len(array) // 2
        if array[idx] == v:
            return True
        elif array[idx] < v:
            self.binarySearchAux(array[idx + 1 :], idx, v)
        else:
            self.binarySearchAux(array[0:idx], idx, v)
