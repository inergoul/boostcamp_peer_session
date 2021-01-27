class Solution:
    ##### STRING
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return 0
        if str(x) == str(x)[::-1]:
            return 1
        return 0

    ##### MATH
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return 0
        ret = 0
        d = x
        while d:
            ret *= 10
            ret += (d % 10)
            d //= 10
        return (ret == x)
