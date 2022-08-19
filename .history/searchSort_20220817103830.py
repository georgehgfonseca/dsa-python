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
            idx = (high + low) // 2
            print(low, high, idx)
            if self.array[idx] == v:
                return idx
            elif self.array[idx] < v:
                # Explore left-side of idx
                low = idx + 1
            else:
                # Explore right-side of idx
                high = idx - 1
        return -1

    def binarySearchRec(self, v):
        return self.binarySearchAux(self.array, 0, len(self.array) - 1, v)

    def binarySearchAux(arr, low, high, x):
        # Check base case
        if high >= low:
            mid = (high + low) // 2
            # If element is present at the middle itself
            if arr[mid] == x:
                return mid
            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif arr[mid] > x:
                return binarySearchAux(arr, low, mid - 1, x)
            # Else the element can only be present in right subarray
            else:
                return binarySearchAux(arr, mid + 1, high, x)
        else:
            # Element is not present in the array
            return -1

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
