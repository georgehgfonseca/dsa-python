import itertools


def allSubsets(numbers):
    if numbers == []:
        return [[]]
    x = allSubsets(numbers[1:])
    return x + [[numbers[0]] + y for y in x]


def findSubsets(s, n):
    """Finds all subsets of size n"""
    # return list(itertools.combinations(s, n))
    # Lets create my own combinations function
    return [x for x in allSubsets(numbers) if len(x) == n]
