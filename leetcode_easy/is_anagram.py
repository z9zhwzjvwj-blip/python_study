s1 = "anagram"
t1 = "nagaram"
s2 = "rat"
t2 = "car"


def isAnagram(s, t):
    if len(s) != len(t) or len(s):
        return False

    freq = {}

    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    for ch in t:
        if ch not in freq:
            return False
        else:
            freq[ch] -= 1

    return all(value == 0 for value in freq.values())


print(isAnagram(s1, t1))
print(isAnagram(s2, t2))
