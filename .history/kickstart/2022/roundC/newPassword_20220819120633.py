def change_pass(password):
    sp_char = False
    digit = False
    upper = False
    lower = False
    for letter in password:
        if letter == "#" or letter == "@" or letter == "*" or letter == "&":
            sp_char = True
        if letter.isdigit():
            digit = True
        if letter.isupper():
            upper = True
        if letter.islower():
            lower = True
        if len(password) >= 7 and sp_char and digit and upper and lower:
            return password
    if not sp_char:
        password += "#"
    if not digit:
        password += "0"
    if not upper:
        password += "A"
    if not lower:
        password += "a"
    while len(password) < 7:
        password += "a"
    return password


if __name__ == "__main__":
    t = int(input())
    for test_case in range(1, t + 1):
        n = int(input())  # Size of password
        password = str(input())  # Input password
        res = change_pass(password)
        print("Case #" + str(test_case) + ": " + str(res))
