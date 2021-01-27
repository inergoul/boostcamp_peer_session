class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        Runtime: 44 ms
        Memory Usage: 14.1 MB
        '''
        reversed_x = ''.join(reversed(str(x)))
        if reversed_x==str(x):
            return True
        else: return False