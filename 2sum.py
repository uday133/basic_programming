# https://leetcode.com/problems/two-sum/


# Best Approach
# Complexity O(n) because of the 1 loop
class BestSolution:
    def twoSum(self, nums, target):
        """
            target : input type : Integer
            nums : input type : List
            Return : Return Type : List
        """
        num_list = []
        for i, n in enumerate(nums):
            temp = target - n
            if temp in num_list:
                return [i, nums.index(temp)]
            else:
                num_list.append(n)


# Worst Approach
# Complexity O(n^2) Because of the 2 ineer loop
class WorstSolution:
    def twoSum(self, nums, target):
        """
            target : input type : Integer
            nums : input type : List
            Return : Return Type : List
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]


target = 9
nums = [2, 7, 11, 10]
best_solution_obj = BestSolution()
indexes = best_solution_obj.twoSum(nums, target)
print("Best Solution Output ::", indexes)
worst_solution_obj = WorstSolution()
indexes = worst_solution_obj.twoSum(nums, target)
print("Worst Solution Output ::", indexes)
