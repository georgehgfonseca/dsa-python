def recordBreaker(arr):
    if len(arr) == 1:
        return 1
    dp = arr[0]  # max until i-th index
    ans = 0
    # 1st day is record breaker
    if arr[0] > arr[1]:
        ans += 1
    # n-th day is record breaker
    for i in range(1, len(arr) - 1):
        if arr[i] > dp and arr[i] > arr[i + 1]:
            ans += 1
            dp = arr[i]
    # last day is record breaker
    if arr[-1] > dp and arr[-1] > arr[-2]:
        ans += 1
    return ans


# testCases = [
#     (1, [1]),
#     (8, [1, 2, 0, 7, 2, 0, 2, 0]),
#     (6, [4, 8, 15, 16, 23, 42]),
#     (9, [3, 1, 4, 1, 5, 9, 2, 6, 5]),
#     (6, [9, 9, 9, 9, 9, 9]),
# ]
# for t in range(len(testCases)):
#     ans = recordBreaker(testCases[t][1])
#     print("Case #" + str(t + 1) + ": " + str(ans))
t = int(input())
for t in range(0, t):
    n = int(input())
    a = [int(x) for x in input().split(" ")]
    ans = recordBreaker(a)
    print("Case #" + str(t + 1) + ": " + str(ans))
