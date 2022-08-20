import itertools


def imageLabeler(n, m, a):
    for i in range(1, m + 1):
        print(list(itertools.combinations(a, i)))
        for j in list(itertools.combinations(a, i)):
            
    # assignments = []
    # curr = []
    # for i in range(len(a)):
    #     for j in range(len(m)):
    #         curr.append(j+1)

    print(n, m, a)
    return 10


if __name__ == "__main__":
    t = 1  # int(input())
    for test_case in range(1, t + 1):
        line1 = [int(x) for x in "3 2".split(" ")]  # Number of regions and categories
        line2 = [int(x) for x in "11 24 10".split(" ")]  # Array of values
        res = imageLabeler(line1[0], line1[1], line2)
        print("Case #" + str(test_case) + ": " + str(res))
