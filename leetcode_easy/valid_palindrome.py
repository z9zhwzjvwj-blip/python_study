s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = " "


def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    left = 0
    right = len(s) - 1

    while left < right:
        if not s[left].isalnum():
            left += 1
            continue

        if not s[right].isalnum():
            right -= 1
            continue

        if s[left].lower() != s[right].lower():
            print(s[left].lower(), " vs ", s[right].lower())
            return False

        left += 1
        right -= 1

    return True


print(isPalindrome(s1))
print(isPalindrome(s2))
print(isPalindrome(s3))
