def maximumGain(a, b, k):
    ans = 0
    temp = a + b
    print(temp)
    for i in range(k):
        # select one (the best) task at a time
        # how to handle draws??
        best = -1
        pos = []
        best = max(a[0], a[-1], b[0], b[-1])
        cand = []
        if a[0] == best:
            cand.append(1)
        if a[-1] == best:
            cand.append(2)
        if b[0] == best:
            cand.append(3)
        if b[-1] == best:
            cand.append(4)
        if len(cand) 
        
            
        for j in range(4):
            if a[0] > best


        if a[0] > best:
            best = a[0]
            pos = 0
        if a[-1] > best:
            best = a[-1]
            pos = 1
        elif a[-1] == best:
            # which next element is better?


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
        elif pos == 3:
            ans += b[-1]
            b.pop()
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
