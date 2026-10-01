word1 = "ab"
word2 = "pqrs"


def mergeAlternately(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """
    wcount = 0
    new = []

    while wcount < len(word1) and wcount < len(word2):
        new.append(word1[wcount])
        new.append(word2[wcount])
        wcount += 1

    new.append(word1[wcount:])
    new.append(word2[wcount:])

    return "".join(new)


print(mergeAlternately(word1, word2))
