def solution(input):
    diagonals = [[] for _ in range(len(input) + len(input[0]) - 1)] 

    for i in range(len(input)):
        for j in range(len(input[i])):
            diagonals[i + j].append(input[i][j])

    res = ''
    for diagonal in diagonals:
        for letter in diagonal:
            res += letter
    return diagonals

input = [
  ['a', 'b', 'c', 'd'],
  ['e', 'f', 'g', 'h'],
  ['i', 'j', 'k', 'l']
]

print(solution(input))