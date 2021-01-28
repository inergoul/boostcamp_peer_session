class Solution:
    def isPalindrome(self, x: int) -> bool:
        origin = str(x)
        reverse = origin[::-1]
        return origin == reverse