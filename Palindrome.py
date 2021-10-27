# https://leetcode.com/problems/palindrome-number/


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)


palindrome_obj = Solution()
print(palindrome_obj.isPalindrome(120))

