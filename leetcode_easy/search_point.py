nums = [1, 3, 5, 6]
target = 3


def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    start = 0
    end = len(nums)

    while start < end:
        half = (start + end) // 2

        if nums[half] < target:
            start = half + 1
        elif nums[half] > target:
            end = half
        else:
            return half

    return end


print(searchInsert(nums, target))
