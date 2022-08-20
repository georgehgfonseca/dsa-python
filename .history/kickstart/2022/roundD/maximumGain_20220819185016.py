def maximumGain(a, b, k):
    # calculate combinations of selected elements from a and b that sums k
    comb = []
    for i in range(len(a)):
        if len(b) >= k - i:
            comb.append((i, k - i))
    inv_comb = []
    for c in comb:
        if len(a) >= c[1] and len(b) >= c[0]:
            inv_comb.append((c[1], c[0]))
    comb += inv_comb
    ans = 0
    for c in comb:
        comb_max_gain = 0
        # slide window of left-out elements
        win_size_a = len(a) - c[0]
        if win_size_a == 0:
            comb_max_gain += sum(a)
        # TODO
        win_size_b = len(b) - c[1]
        print(c, win_size_a, win_size_b)
    # print(comb)
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
