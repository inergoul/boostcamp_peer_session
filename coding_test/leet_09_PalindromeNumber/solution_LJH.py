class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        middle = len(str_x) //2
        
        for idx in range(middle+1):
            if str_x[idx] == str_x[-idx-1]:
                continue
            else:
                return False
        return True


x = '1234213'
middle = (len(str(x))) //2
tmp = Solution()
print(tmp.isPalindrome('134321'))