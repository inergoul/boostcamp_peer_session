class Solution:
    def reverse(self, x: int) -> int:
        num = int(str(x)[::-1] if x > 0 else str(x * -1)[::-1]) * (-1 if x < 0 else 1)
        return num if 2147483647 >= num and num >= -2147483647 else 0
