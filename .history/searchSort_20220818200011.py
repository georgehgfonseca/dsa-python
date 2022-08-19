import bisect


def is_ordered(arr):
    if len(arr) <= 1:
        return True
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return False
    return True


def push(array, x):
    array.append(x)


def push_in_order(arr, x):
    # bisect.insort(array, x)
    # Lets create my own bisect.insort function
    lo = 0
    hi = len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < arr[mid]:
            hi = mid
        else:
            lo = mid + 1
    arr.insert(lo, x)

    # low = 0
    # high = len(arr) - 1
    # while high >= low:
    #     idx = (high + low) // 2
    #     if arr[idx] == x:
    #         # x already exists and a duplicate is being added
    #         arr.insert(idx, x)
    #     elif arr[idx] < x:
    #         low = idx + 1
    #     else:
    #         high = idx - 1
    # # x is a new element and is gonna be added at idx
    # if arr[idx] < x:
    #     arr.insert(idx + 1, x)
    # else:
    #     arr.insert(idx, x)


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while high >= low:
        idx = (high + low) // 2
        if arr[idx] == x:
            # v has been found
            return idx
        elif arr[idx] < x:
            # Explore left-side of idx
            low = idx + 1
        else:
            # Explore right-side of idx
            high = idx - 1
    return -1


def binary_search_rec(arr, x):
    return binary_search_aux(arr, 0, len(arr) - 1, x)


def binary_search_aux(arr, low, high, x):
    # Check base case
    if high >= low:
        idx = (high + low) // 2
        # If element is present at the middle itself
        if arr[idx] == x:
            return idx
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[idx] > x:
            return binary_search_aux(arr, low, idx - 1, x)
        # Else the element can only be present in right subarray
        else:
            return binary_search_aux(arr, idx + 1, high, x)
    else:
        # Element is not present in the array
        return -1


def bubble_sort(arr):
    # O(n^2) time-complexity O(1) space-complexity
    for i in range(len(arr)):
        swapped = False
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                swapped = True
        if not swapped:
            return


def selection_sort(arr):
    for j in range(len(arr)):
        smallest_idx = j
        for i in range(j + 1, len(arr)):
            if arr[i] < arr[smallest_idx]:
                smallest_idx = i
        arr[j], arr[smallest_idx] = arr[smallest_idx], arr[j]


def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge_sort(arr):
    # O(n log n) time-complexity O(n) space-complexity
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr) // 2
        # Dividing the array elements into 2 halves
        L = arr[:mid]
        R = arr[mid:]
        # Sorting the first and second halves
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def partition(arr, low, high):
    # Choose the rightmost element as pivot
    pivot = arr[high]
    # Pointer for greater element
    i = low - 1
    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
            # Swapping element at i with element at j
            (arr[i], arr[j]) = (arr[j], arr[i])
    # Swap the pivot element with the greater element specified by i
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
    # Return the position from where partition is done
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(arr, low, high)
        # Recursive call on the left of pivot
        quick_sort(arr, low, pi - 1)
        # Recursive call on the right of pivot
        quick_sort(arr, pi + 1, high)
