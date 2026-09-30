nums = [2, 5, 7, 15]
target = 9


def two_sums(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i


print(two_sums(nums, target))
