class Solution(object):
    def isPalindrome(self, x):
        s=str(x)
        j=len(s)-1
        for i in range(len(s)):
            if s[i] != s[j]:
                return False
            j-=1
        return True