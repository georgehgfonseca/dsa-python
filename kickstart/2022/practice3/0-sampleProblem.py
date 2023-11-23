def solve(kids, arr):
    total = sum(arr)
    return total - (total // kids) * kids


# tests = [(7, 3, [1, 2, 3, 4, 5, 6, 7])]
# for t in range(len(tests)):
#     ans = solve(tests[t][1], tests[t][2])
#     print("Case #" + str(t + 1) + ": " + str(ans))
t = int(input())
for t in range(0, t):
    a = [int(x) for x in input().split(" ")]
    b = [int(x) for x in input().split(" ")]
    ans = solve(a[1], b)
    print("Case #" + str(t + 1) + ": " + str(ans))
