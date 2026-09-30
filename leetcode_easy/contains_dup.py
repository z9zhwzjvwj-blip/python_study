nums1 = [1, 2, 3, 1]
nums2 = [1, 2, 3, 4]
nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]


def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if not nums:
        return False

    seen = set()

    for num in nums:
        if num in seen:
            return True

        seen.add(num)

    return False


print(containsDuplicate(nums1))
print(containsDuplicate(nums2))
print(containsDuplicate(nums3))
