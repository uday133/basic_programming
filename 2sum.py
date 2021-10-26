# https://leetcode.com/problems/two-sum/


# Best Approach
# Complexity O(n) because of the 1 loop
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_list = []
        for i, n in enumerate(nums):
            temp = target - n
            if temp in num_list:
                return [i, nums.index(temp)]
            else:
                num_list.append(n)
                
# Worst Approach
# Complexity O(n^2) Because of the 2 ineer loop
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i,j]
