def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """

    start = 1
    end = n
    while start < end:
        half = (start + end) // 2
        if isBadVersion(half):
            end = half
        else:
            start = half + 1
    return end
