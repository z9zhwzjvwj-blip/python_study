nums1 = [3, 2, 3]
nums2 = [2, 2, 1, 1, 1, 2, 2]


def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    return candidate


print(majorityElement(nums1))
