"""nums = [10, 20, 30, 40, 50]

print(nums[0])
print(nums[-1])
print(len(nums))

nums.append(60)

print(nums)"""

nums = [3, 7, 2, 9, 4]

"""for num in nums:
    if num >= 5:
        print(num)"""

for i, num in enumerate(nums):
    print(i, num)


def find_max(nums):
    max_nums = nums[0]

    for num in nums:
        if num > max_nums:
            max_num = num

    return max_num


nums = [3, 8, 2, 10, 5]

answer = find_max(nums)

print(answer)
