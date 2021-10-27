# https://leetcode.com/problems/remove-element/


nums = [0, 1, 2, 2, 3, 0, 4, 2]

val = 2
count = len(nums)
for index in range(count - 1, -1, -1):
    if nums[index] == val:
        nums.remove(nums[index])
print(count, nums)
