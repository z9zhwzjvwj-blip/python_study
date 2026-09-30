strs1 = ["flower", "flow", "flight"]
strs2 = ["dog", "racecar", "car"]


def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    shortest = min(strs, key=len)

    for i in range(len(shortest)):
        for s in strs:
            if s[i] != shortest[i]:
                return shortest[:i]
    return shortest


print(longestCommonPrefix(strs1))
