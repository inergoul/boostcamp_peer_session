class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return 0
        if str(x) == str(x)[::-1]:
            return 1
        return 0
