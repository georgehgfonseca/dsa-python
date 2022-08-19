import itertools


def findSubsets(s, n):
    """Finds all subsets of size n"""
    return list(itertools.combinations(s, n))
    # Lets create my own combinations function
