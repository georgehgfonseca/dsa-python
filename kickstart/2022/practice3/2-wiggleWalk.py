def wiggleWalk(arr, s):
    # TLE on TestSet 2
    R, C, sR, sC = arr[1], arr[2], arr[3] - 1, arr[4] - 1
    visited = {}
    visited[(sR, sC)] = True
    currR = sR
    currC = sC
    for i in range(len(s)):
        if s[i] == "N":
            while (currR, currC) in visited:
                currR -= 1
        elif s[i] == "S":
            while (currR, currC) in visited:
                currR += 1
        elif s[i] == "W":
            while (currR, currC) in visited:
                currC -= 1
        elif s[i] == "E":
            while (currR, currC) in visited:
                currC += 1
        visited[(currR, currC)] = True
    return str(currR + 1) + " " + str(currC + 1)


def wiggleWalkMLE(arr, s):
    R, C, sR, sC = arr[1], arr[2], arr[3] - 1, arr[4] - 1
    visited = [[False for _ in range(C)] for _ in range(R)]
    visited[sR][sC] = True
    currR = sR
    currC = sC
    for i in range(len(s)):
        if s[i] == "N":
            while visited[currR][currC]:
                currR -= 1
        elif s[i] == "S":
            while visited[currR][currC]:
                currR += 1
        elif s[i] == "W":
            while visited[currR][currC]:
                currC -= 1
        elif s[i] == "E":
            while visited[currR][currC]:
                currC += 1
        visited[currR][currC] = True
    return str(currR + 1) + " " + str(currC + 1)


# testCases = [
#     ([5, 3, 6, 2, 3], "EEWNS"),
#     ([4, 3, 3, 1, 1], "SESE"),
#     ([11, 5, 8, 3, 4], "NEESSWWNESE"),
# ]
# for t in range(len(testCases)):
#     ans = wiggleWalk(testCases[t][0], testCases[t][1])
#     print("Case #" + str(t + 1) + ": " + str(ans))
t = int(input())
for t in range(0, t):
    a = [int(x) for x in input().split(" ")]
    s = input()
    ans = wiggleWalk(a, s)
    print("Case #" + str(t + 1) + ": " + str(ans))
