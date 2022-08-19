import itertools


def allSubsets(array):
    if array == []:
        return [[]]
    x = allSubsets(array[1:])
    return x + [[array[0]] + y for y in x]


def findSubsets(array, n):
    """Finds all subsets of size n"""
    # return list(itertools.combinations(array, n))
    # Lets create my own combinations function
    return [x for x in allSubsets(array) if len(x) == n]
