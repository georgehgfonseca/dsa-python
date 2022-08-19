def imageLabeler(n, m, a):
    print(n, m, a)
    return 10


n = 1
tests = [("3 2", "")]


if __name__ == "__main__":
    t = 1  # int(input())
    for test_case in range(1, t + 1):
        line1 = [int(x) for x in "3 2".split(" ")]  # Number of regions and categories
        line2 = [int(x) for x in "11 24 10".split(" ")]  # Array of values
        res = imageLabeler(line1[0], line1[1], line2)
        print("Case #" + str(test_case) + ": " + str(res))
