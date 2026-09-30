s1 = "III"
s2 = "LVIII"
s3 = "MCMXCIV"


def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    pre = 0
    total = 0
    table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in reversed(s):
        if table[i] < pre:
            total = total - table[i]
        else:
            total = total + table[i]
        pre = table[i]
    return total


print(romanToInt(s1))
print(romanToInt(s2))
print(romanToInt(s3))
