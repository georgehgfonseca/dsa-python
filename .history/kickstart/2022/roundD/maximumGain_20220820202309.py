def calcMaxGainsArray(arr, k):
    gain_left = {}
    for num_ans_left in range(0, min(len(arr), k) + 1):
        gain_left[num_ans_left] = sum(arr[:num_ans_left])
    gain_right = {}
    for num_ans_right in range(0, min(len(arr), k) + 1):
        gain_right[num_ans_right] = sum(arr[len(arr) - num_ans_right :])
    gains = {}
    for num_ans in range(0, min(len(arr), k) + 1):
        max_gain = 0
        for num_ans_left in range(0, num_ans + 1):
            num_ans_right = num_ans - num_ans_left
            gain = gain_left[num_ans_left] + gain_right[num_ans_right]
            if gain > max_gain:
                max_gain = gain
        gains[num_ans] = max_gain
    return gains


def maximumGain(a, b, k):
    # Runs in O(n^2) RE in TestSet 1
    # calculate combinations of selected elements from a and b that sums k
    comb = []
    for i in range(len(a) + 1):
        if len(b) >= k - i:
            comb.append((i, k - i))
    inv_comb = []
    for c in comb:
        if len(a) >= c[1] and len(b) >= c[0]:
            inv_comb.append((c[1], c[0]))
    comb += inv_comb
    # calculate max possible gain for every num of elements for both arrays
    gains_a = calcMaxGainsArray(a, k)
    gains_b = calcMaxGainsArray(b, k)
    # evaluate every combination and return the best gain
    ans = 0
    for c in comb:
        # (c[0]: num. of elems in a; c[1]: num. of elems in a)
        c_gain = gains_a[c[0]] + gains_b[c[1]]
        if c_gain > ans:
            ans = c_gain
    return ans


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
    # evaluate the gain for every possible unused window size in a
    sum_a = sum(a)
    win_gain_a = {}
    for win_size_a in range(0, min(len(a), k) + 1):
        # slide window from idx 0
        max_win_size_a_gain = 0
        for i in range(len(a) - win_size_a + 1):
            if sum_a - sum(a[i : i + win_size_a]) > max_win_size_a_gain:
                max_win_size_a_gain = sum_a - sum(a[i : i + win_size_a])
        win_gain_a[win_size_a] = max_win_size_a_gain
    # evaluate the gain for every possible unused window size in b
    sum_b = sum(b)
    win_gain_b = {}
    for win_size_b in range(0, min(len(b), k) + 1):
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
    file = open("ts1_input.txt", "r")
    t = file.readline()
    for test_case in range(1, t + 1):
        n = file.readline()
        a = file.readline()
        m = file.readline()
        b = file.readline()
        k = file.readline()
        # t = 1
        # for test_case in range(1, t + 1):
        #     n = 3
        #     a = [3, 1, 2]
        #     m = 4
        #     b = [2, 8, 1, 9]
        #     k = 5
        # t = int(input())
        # for test_case in range(1, t + 1):
        #     n = int(input())
        #     a = [int(x) for x in input().split(" ")]
        #     m = int(input())
        #     b = [int(x) for x in input().split(" ")]
        #     k = int(input())
        res = maximumGain(a, b, k)
        print("Case #" + str(test_case) + ": " + str(res))
