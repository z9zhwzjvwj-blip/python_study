x = 1441


def isPalindrome(x):

    if x < 0 or (x != 0 and x % 10) == 0:
        return False

    rev = 0

    while x > rev:
        last = x % 10
        x = x // 10
        rev = rev * 10 + last

    return x == rev or x == rev // 10
