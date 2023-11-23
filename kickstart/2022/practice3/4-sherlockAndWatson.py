def solve(a, b, n, k):
    # time complexity O(n^2) (too slow for TS1)
    # TLE in TestSet 1
    ans = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j and (i**a + j**b) % k == 0:
                ans += 1
    return ans % 1000000007


t = int(input())
for t in range(0, t):
    a = list(map(int, input().split(" ")))
    ans = solve(a[0], a[1], a[2], a[3])
    print(f"Case #{t + 1}: {ans}")
# tests = [(1, 1, 5, 3), (1, 2, 4, 5), (1, 1, 2, 2)]
# for t in range(len(tests)):
#     ans = solve(tests[t][0], tests[t][1], tests[t][2], tests[t][3])
#     print("Case #" + str(t + 1) + ": " + str(ans))
