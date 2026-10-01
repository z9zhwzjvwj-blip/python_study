nums = [-1, 0, 3, 5, 9, 12]
target = 3


def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    start = 0
    end = len(nums)
    half = 0

    while start != end:
        half = (start + end) // 2
        if target > nums[half]:
            start = start + end // 2
        elif target < nums[half]:
            end = end // 2
        else:
            return half

    return -1


print(search(nums, target))
