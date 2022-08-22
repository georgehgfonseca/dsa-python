def touchbarTyping(a, b):
    # runs in O(n+m) WA for TestSet 2
    # handle trivial case
    if len(a) == 1:
        return 0
    # compute the set of positions for each key
    key_pos = {}
    for pos in range(len(b)):
        if b[pos] not in key_pos:
            key_pos[b[pos]] = [pos]
        else:
            key_pos[b[pos]] += [pos]
    F = [[0 for _ in range(len(b))] for _ in range(len(a))]
    for x in range(len(a)):
        for y in range(len(b)):
            minVal = float("inf")
            for j in key_pos[y]:
                if F[x - 1][j] + abs(y - j) < minVal:
                    minVal = F[x - 1][j] + abs(y - j)
            F[x][y] = minVal
    return 0


def touchbarTypingSingleKey(a, b):
    # runs in O(n+m) WA for TestSet 2
    # handle trivial case
    if len(a) == 1:
        return 0
    # hashmap of the position of each key
    key_pos = {}
    for pos in range(len(b)):
        key_pos[b[pos]] = pos
    # compute the answer
    ans = 0
    for i in range(len(a) - 1):
        ans += abs(key_pos[a[i]] - key_pos[a[i + 1]])
    return ans


file = open("C:/Users/George/Downloads/test_set_1/ts1_input.txt", "r")
t = int(file.readline())
for test_case in range(1, t + 1):
    n = int(file.readline())
    a = [int(x) for x in file.readline().split(" ")]
    m = int(file.readline())
    b = [int(x) for x in file.readline().split(" ")]
    # t = 1
    # for test_case in range(1, t + 1):
    #     n = 5
    #     a = [1, 1, 1]
    #     m = 3
    #     b = [2, 1]
    # t = int(input())
    # for test_case in range(1, t + 1):
    #     n = int(input())
    #     a = [int(x) for x in input().split(" ")]
    #     m = int(input())
    #     b = [int(x) for x in input().split(" ")]
    res = touchbarTyping(a, b)
    print("Case #" + str(test_case) + ": " + str(res))
