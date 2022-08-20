def maximumGain(a, b, k):
    # calculate combinations of selected elements from a and b that sums k
    comb = []
    for i in range(a):
        if len(b) >= k - i:
            comb.append((i, k - i))
    print(comb)
    ans = 0
    return ans


if __name__ == "__main__":
    # t = int(input())
    # for test_case in range(1, t + 1):
    #     n = int(input())
    #     a = [int(x) for x in input().split(" ")]
    #     m = int(input())
    #     b = [int(x) for x in input().split(" ")]
    #     k = int(input())
    t = 1
    for test_case in range(1, t + 1):
        n = 3
        a = [3, 1, 2]
        m = 4
        b = [2, 8, 1, 9]
        k = 5
        res = maximumGain(a, b, k)
        print("Case #" + str(test_case) + ": " + str(res))
