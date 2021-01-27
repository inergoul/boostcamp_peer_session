
## 60ms, 14.3MB
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]

'''
## 128ms, 14.3MB
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        if len(x)==0:
            return True
        elif x[0]!=x[-1]:
            return False
        else:
            return Solution().isPalindrome(x[1:-1])
'''
        