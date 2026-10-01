nums1 = [3, 0, 1]
nums2 = [0, 1]
nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]


def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0

    missing = sum(range(1, len(nums) + 1))

    for num in nums:
        missing -= num

    return missing


print(missingNumber(nums1))
print(missingNumber(nums2))
print(missingNumber(nums3))
