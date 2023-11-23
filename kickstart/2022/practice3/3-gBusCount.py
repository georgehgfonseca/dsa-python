def solve(arr, numInt, int):
    ans = [0 for _ in range(numInt)]
    mins = [arr[i] for i in range(0, len(arr), 2)]
    maxs = [arr[i + 1] for i in range(0, len(arr), 2)]
    for i in range(len(mins)):
        for j in range(len(int)):
            if int[j] >= mins[i] and int[j] <= maxs[i]:
                ans[j] += 1
    s = str(ans[0])
    for a in range(1, len(ans)):
        s += " " + str(ans[a])
    return s


# tests = [
#     (4, [15, 25, 30, 35, 45, 50, 10, 20], 2, [15, 25]),
#     (10, [10, 15, 5, 12, 40, 55, 1, 10, 25, 35, 45, 50, 20, 28, 27, 35, 15, 40, 4, 5], 3, [5, 10, 27]),
# ]
# for t in range(len(tests)):
#     ans = solve(tests[t][1], tests[t][2], tests[t][3])
#     print("Case #" + str(t + 1) + ": " + str(ans))
t = int(input())
for t in range(0, t):
    if t != 0:
        dummy = input()
    n = int(input())
    a = [int(x) for x in input().split(" ")]
    m = int(input())
    b = []
    for _ in range(m):
        b.append(int(input()))
    ans = solve(a, m, b)
    print("Case #" + str(t + 1) + ": " + str(ans))
