# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target not in nums:
            nums.append(target)
        for index in range(0,len(nums)):
            if nums[index] >= target:
                return index
