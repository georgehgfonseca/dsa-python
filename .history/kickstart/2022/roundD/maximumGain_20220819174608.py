def maximumGain(a, b, k):
    ans = 0
    for i in range(k):
        # select one (the best) task at a time
        # how to handle draws??
        best = -1
        pos = -1
        if a[0] > best:
            best = a[0]
            pos = 0
        if a[-1] > best:
            best = a[-1]
            pos = 1
        if b[0] > best:
            best = b[0]
            pos = 2
        if b[-1] > best:
            best = b[-1]
            pos = 3
        if pos == 0:
            ans += a[0]
            a.pop(0)
        elif pos == 1:
            ans += a[-1]
            a.pop()
        elif pos == 2:
            ans += b[0]
            b.pop(0)
        elif pos == 1:
            ans += b[-1]
            b.pop()
    return ans


if __name__ == "__main__":
    t = int(input())
    for test_case in range(1, t + 1):
        n = int(input())
        a = [int(x) for x in input().split(" ")]
        m = int(input())
        b = [int(x) for x in input().split(" ")]
        k = int(input())
        res = maximumGain(a, b, k)
        print("Case #" + str(test_case) + ": " + str(res))
