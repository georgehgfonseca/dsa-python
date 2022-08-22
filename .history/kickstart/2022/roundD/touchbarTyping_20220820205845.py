def touchbarTyping(a, b):
    return 0


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
