# https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if (not haystack and not needle) or (haystack and not needle):
            return 0
        elif needle not in haystack:
            return -1
        else:
            for i in range(len(haystack) - len(needle) + 1):
                if haystack[i:i + len(needle)] == needle:
                    return i


solution_obj = Solution()
index = solution_obj.strStr(haystack="hello", needle="ll")
print(index)
