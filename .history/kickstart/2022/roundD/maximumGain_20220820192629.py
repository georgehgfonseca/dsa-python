def maximumGain(a, b, k):
    # Runs in O(n^3) TLE in TestSet 1
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
    gain_a_left = {0: 0, len(a): sum(a)}
    for num_ans_left_a in range(1, len(a)):
        gain_a_left[num_ans_left_a] = sum(a[:num_ans_left_a])
    gain_a_right = {0: 0, len(a): sum(a)}
    for num_ans_right_a in range(1, len(a)):
        gain_a_right[num_ans_right_a] = sum(a[len(a) - num_ans_right_a - 1 :])

    # gain_a = {0: (0, 0), len(a): (len(0), 0)}
    # for num_ans__a in range(1, len(a)):
    return 0


def maximumGainSlow(a, b, k):
    # Runs in O(n^3) TLE in TestSet 1
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
    # improve speed: precalculate sums of every window?
    # evaluate the gain for every possible unused window size in a
    sum_a = sum(a)
    win_gain_a = {0: sum_a, len(a): 0}
    for win_size_a in range(1, len(a)):
        # slide window from idx 0
        max_win_size_a_gain = 0
        for i in range(len(a) - win_size_a + 1):
            if sum_a - sum(a[i : i + win_size_a]) > max_win_size_a_gain:
                max_win_size_a_gain = sum_a - sum(a[i : i + win_size_a])
        win_gain_a[win_size_a] = max_win_size_a_gain
    # evaluate the gain for every possible unused window size in b
    sum_b = sum(b)
    win_gain_b = {0: sum_b, len(b): 0}
    for win_size_b in range(1, len(b)):
        # slide window from idx 0
        max_win_size_b_gain = 0
        for i in range(len(b) - win_size_b + 1):
            if sum_b - sum(b[i : i + win_size_b]) > max_win_size_b_gain:
                max_win_size_b_gain = sum_b - sum(b[i : i + win_size_b])
        win_gain_b[win_size_b] = max_win_size_b_gain
    ans = 0
    for c in comb:
        # evaluate every combination
        # (c[0]: num. of used elem in a; c[1]: num. of used elem in a)
        c_gain = win_gain_a[len(a) - c[0]] + win_gain_b[len(b) - c[1]]
        if c_gain > ans:
            ans = c_gain
    return ans


if __name__ == "__main__":
    t = 1
    for test_case in range(1, t + 1):
        n = 3
        a = [3, 1, 2]
        m = 4
        b = [2, 8, 1, 9]
        k = 5
        # t = int(input())
        # for test_case in range(1, t + 1):
        #     n = int(input())
        #     a = [int(x) for x in input().split(" ")]
        #     m = int(input())
        #     b = [int(x) for x in input().split(" ")]
        #     k = int(input())
        res = maximumGain(a, b, k)
        print("Case #" + str(test_case) + ": " + str(res))
