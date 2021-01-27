class Solution:
    ###### STRING
    def reverse(self, x: int) -> int:
        num = int(str(x)[::-1] if x > 0 else str(x * -1)[::-1]) * (-1 if x < 0 else 1)
        return num if 2147483647 >= num and num >= -2147483647 else 0

    
    ###### MATH
    def reverse(self, x: int) -> int:
        m = -1 if x < 0 else 1
        ret = 0
        num = x * m
        while num:
            ret *= 10
            ret += (num % 10)
            num //= 10
        return ret * m if 2147483647 >= ret and ret >= -2147483647 else 0
