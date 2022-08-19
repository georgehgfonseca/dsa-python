import bisect


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

    def push(self, x):
        self.array.append(x)

    def pushInOrder(self, x):
        bisect.insort(self.array, x)
        # Lets create my own bisect.insort function
        # low = 0
        # high = len(self.array) - 1
        # while high >= low:
        #     idx = (high + low) // 2
        #     if self.array[idx] == x:
        #         # x already exists and a duplicate is being added
        #         self.array.insert(idx, x)
        #     elif self.array[idx] < x:
        #         low = idx + 1
        #     else:
        #         high = idx - 1
        # # x is a new element and is gonna be added at idx
        # if self.array[idx] < x:
        #     self.array.insert(idx + 1, x)
        # else:
        #     self.array.insert(idx, x)

    def binarySearch(self, x):
        low = 0
        high = len(self.array) - 1
        while high >= low:
            idx = (high + low) // 2
            if self.array[idx] == x:
                # v has been found
                return idx
            elif self.array[idx] < x:
                # Explore left-side of idx
                low = idx + 1
            else:
                # Explore right-side of idx
                high = idx - 1
        return -1

    def binarySearchRec(self, x):
        return self.binarySearchAux(self.array, 0, len(self.array) - 1, x)

    def binarySearchAux(self, arr, low, high, x):
        # Check base case
        if high >= low:
            idx = (high + low) // 2
            # If element is present at the middle itself
            if arr[idx] == x:
                return idx
            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif arr[idx] > x:
                return self.binarySearchAux(arr, low, idx - 1, x)
            # Else the element can only be present in right subarray
            else:
                return self.binarySearchAux(arr, idx + 1, high, x)
        else:
            # Element is not present in the array
            return -1

    # def binarySearchAux(self, array, idx, v):
    #     print(array, idx, v)
    #     if len(array) == 0:
    #         return False
    #     idx = len(array) // 2
    #     if array[idx] == v:
    #         return True
    #     elif array[idx] < v:
    #         self.binarySearchAux(array[idx + 1 :], idx, v)
    #     else:
    #         self.binarySearchAux(array[0:idx], idx, v)
