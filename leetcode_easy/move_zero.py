nums = [0, 1, 0, 3, 12]


def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    if len(nums) == 1:
        return

    read = 0
    for num in nums:
        if num != 0:
            nums[read] = num
            read += 1

    for i in range(read, len(nums)):
        nums[i] = 0


moveZeroes(nums)
print(nums)
