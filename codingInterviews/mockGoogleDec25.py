# find the smallest subarray that needs to be sorted so that the whole array is sorted.

# int
# big
# return = start and end indexes

# t0 = [1, 12, 14, 15, 13, 17] output = [2, 4]


# t1 = [5, 5] output = []
# t2 = [-2, -5, -3, -1, 0] output = [0 ,2]
# t3 = [1, 3,* 2, 4, 5, 8, 7, 6, 9] output = [1, 7]


# t4= [1,3,5,6,2,3,4] ->???  output = [1,6]


# arr       = [1,3,5,6,2,3,4]
# sortedArr = [1,2,3,3,4,5,6]
# i         =              *
# l         = 1
# r         = 6
from typing import List


def findSmallestUnsortedSubarray(arr: List[int]) -> List[int]:
    sortedArr = sorted(arr)
    l, r = -1, -1
    for i in range(len(sortedArr)):
        if sortedArr[i] != arr[i]:
            l = i
            break

    if l == -1:
        return []

    for i in range(len(sortedArr) - 1, -1, -1):
        if sortedArr[i] != arr[i]:
            r = i
            break

    return [l, r]


def findSmallestUnsortedSubarray2(arr: List[int]) -> List[int]:
    l, r = -1, -1
    unsorted = -1
    # finding start index
    for i in range(len(arr) - 1):  # 2
        if arr[i] > arr[i + 1]:
            unsorted = i + 1
            break

    if unsorted == -1:
        return []

    min = arr[unsorted]
    for i in range(unsorted + 1, len(arr)):
        if min > arr[i]:
            unsorted = i
            min = arr[i]

    for i in range(len(arr) - 1):
        if arr[i] > arr[unsorted]:
            l = i
            break

    # finding end index
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] < arr[i - 1]:
            unsorted = i - 1
            break

    max = arr[unsorted]
    for i in range(unsorted - 1, -1, -1):
        if max < arr[i]:
            unsorted = i
            max = arr[i]

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] < arr[unsorted]:
            r = i
            break

    return [l, r]


testCases = [
    ([1, 2, 4, 5, 3, 7], [2, 4]),
    ([5, 5], []),
    ([-2, -5, -3, -1, 0], [0, 2]),
    ([1, 3, 2, 4, 5, 8, 7, 6, 9], [1, 7]),
    ([1, 3, 5, 6, 2, 3, 4], [1, 6]),
]

for t in testCases:
    print(findSmallestUnsortedSubarray2(t[0]))
    assert findSmallestUnsortedSubarray2(t[0]) == t[1], "Wrong answer"
