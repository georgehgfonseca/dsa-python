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
    # evaluate the gain for every possible unused window size in a
    sum_a = sum(a)
    win_gain_a = {}
    for win_size_a in range(1, len(a)):
        # slide window from idx 0
        max_win_size_a_gain = 0
        for i in range(len(a) - win_size_a + 1):
            if sum_a - sum(a[i : i + win_size_a]) > max_win_size_a_gain:
                max_win_size_a_gain = sum_a - sum(a[i : i + win_size_a])
        win_gain_a[win_size_a] = max_win_size_a_gain
    # evaluate the gain for every possible unused window size in b
    sum_b = sum(b)
    win_gain_b = {}
    for win_size_b in range(1, len(b)):
        # slide window from idx 0
        max_win_size_b_gain = 0
        for i in range(len(b) - win_size_b + 1):
            if sum_b - sum(b[i : i + win_size_b]) > max_win_size_b_gain:
                max_win_size_b_gain = sum_b - sum(b[i : i + win_size_b])
        win_gain_b[win_size_b] = max_win_size_b_gain
    ans = 0
    for c in comb:
        c_gain = win_gain_a[c[0]] + win_gain_b[c[1]]
        if c_gain > ans:
            ans = c_gain
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
