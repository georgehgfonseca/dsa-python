import bisect


def isOrdered(array):
    if len(array) <= 1:
        return True
    for i in range(1, len(array)):
        if array[i - 1] > array[i]:
            return False
    return True


def push(array, x):
    array.append(x)


def pushInOrder(array, x):
    # bisect.insort(array, x)
    # Lets create my own bisect.insort function
    low = 0
    high = len(array) - 1
    while high >= low:
        idx = (high + low) // 2
        if array[idx] == x:
            # x already exists and a duplicate is being added
            array.insert(idx, x)
        elif array[idx] < x:
            low = idx + 1
        else:
            high = idx - 1
    # x is a new element and is gonna be added at idx
    if array[idx] < x:
        array.insert(idx + 1, x)
    else:
        array.insert(idx, x)


def binarySearch(array, x):
    low = 0
    high = len(array) - 1
    while high >= low:
        idx = (high + low) // 2
        if array[idx] == x:
            # v has been found
            return idx
        elif array[idx] < x:
            # Explore left-side of idx
            low = idx + 1
        else:
            # Explore right-side of idx
            high = idx - 1
    return -1


def binarySearchRec(array, x):
    return binarySearchAux(array, 0, len(array) - 1, x)


def binarySearchAux(array, low, high, x):
    # Check base case
    if high >= low:
        idx = (high + low) // 2
        # If element is present at the middle itself
        if array[idx] == x:
            return idx
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif array[idx] > x:
            return binarySearchAux(array, low, idx - 1, x)
        # Else the element can only be present in right subarray
        else:
            return binarySearchAux(array, idx + 1, high, x)
    else:
        # Element is not present in the array
        return -1


def bubbleSort(array):
    # O(n^2) time-complexity O(1) space-complexity
    for i in range(len(array)):
        swapped = False
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                swapped = True
        if not swapped:
            return


def mergeSort(array):
    # O(n log n) time-complexity O(n) space-complexity
    if len(array) > 1:
        # Finding the mid of the array
        mid = len(array) // 2
        # Dividing the array elements into 2 halves
        L = array[:mid]
        R = array[mid:]
        # Sorting the first and second halves
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
        # Checking if any element was left
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1


def partition(array, low, high):
    # Choose the rightmost element as pivot
    pivot = array[high]
    # Pointer for greater element
    i = low - 1
    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    # Return the position from where partition is done
    return i + 1


# Function to perform quicksort
def quick_sort(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
        # Recursive call on the left of pivot
        quick_sort(array, low, pi - 1)
        # Recursive call on the right of pivot
        quick_sort(array, pi + 1, high)
