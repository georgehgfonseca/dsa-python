def touchbarTyping(a, b):
    # handle trivial case
    if len(a) == 1:
        return 0
    # compute the position of each key
    key_pos = {}
    for key in a:
        if key not in key_pos:
            for pos in b:
                if b[pos] == key:
                    key_pos[key] = pos
    # compute the min dist for each pair of keys
    dists = {}
    for key1 in key_pos.keys():
        for key2 in key_pos.keys():
            dists[(key1, key2)] = abs(key1 - key2)
    ans = 0
    for i in range(len(a) - 1):
        ans += dists[(a[i], a[i + 1])]
    return ans


t = 1
for test_case in range(1, t + 1):
    n = 5
    a = [1, 2, 3, 2, 1]
    m = 3
    b = [1, 2, 3]
    # t = int(input())
    # for test_case in range(1, t + 1):
    #     n = int(input())
    #     a = [int(x) for x in input().split(" ")]
    #     m = int(input())
    #     b = [int(x) for x in input().split(" ")]
    #     k = int(input())
    res = touchbarTyping(a, b)
    print("Case #" + str(test_case) + ": " + str(res))

# file = open("ts2_input.txt", "r")
# t = int(file.readline())
# for test_case in range(1, t + 1):
#     n = int(file.readline())
#     a = [int(x) for x in file.readline().split(" ")]
#     m = int(file.readline())
#     b = [int(x) for x in file.readline().split(" ")]
#     k = int(file.readline())
# t = 1
# for test_case in range(1, t + 1):
#     n = 3
#     a = [3, 1, 2]
#     m = 4
#     b = [2, 8, 1, 9]
#     k = 5
