import itertools


def imageLabeler(n, m, a):
    a.sort()
    ans = 0
    for i in range(m - 1):
        ans += a[n - 1 - i]
    ans += (a[(n - m + 1) // 2] + a[(n - m) // 2]) / 2
    return ans


if __name__ == "__main__":
    t = int(input())
    for test_case in range(1, t + 1):
        line1 = [int(x) for x in input().split(" ")]  # Number of regions and categories
        line2 = [int(x) for x in input().split(" ")]  # Array of values
        res = imageLabeler(line1[0], line1[1], line2)
        print("Case #" + str(test_case) + ": " + str(res))
