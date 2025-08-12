# costumerOrders = [(1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1), (2, 1, 2), ..., (5, 5, 5)]
# packageSizes = [(1, 1, 1), (2, 2, 2), ..., (6, 6, 6)] 1000s up to 10
# len(costumerOrders) = 100
# 49 -> -1
# 51 -> 1
# maxPackages = 1

def canAssign(order, package) -> Bool:
    if order[0] > package[0] or order[1] > package[1] or order[2] > package[2]:
        return False
    return True
    

def assignPackages(costumerOrders: List[Tuple], packageSizes: List[Tuple], maxPackages: int):
    matches = []
    assignments = []

    for order in costumerOrders:
        minSlackIdx = -1
        minSlack = float("inf")
        orderMatches = set()
        for i, package in enumerate(packageSizes):
            if canAssign(order, package):
                slack = (package[0] - order[0]) + (package[1] - order[1]) + (package[2] - order[2])
                orderMatches.add(i)
                if slack < minSlack:
                    minSlackIdx = i
                    minSlack = slack

        assigments.append(i)
        matches.append(orderMatches)
    
    usedPackages = set(assignments)

    while usedPackages > maxPackages:
        # get the package with least assignments and try to assign a new one to each of its previous assignments
        packageSizeToRemvove = #TODO index(min(assignments))
        usedPackages.remove(packageSizeToRemvove)
        for i, assignment in enumerate(assignments):
            if assignment == packageSizeToRemvove:
                # assign another match
                for match in orderMatches[i]:
                    if match in usedPackages:
                        # pick the any match TODO
                        assignments[i] = match

    return assignments # []