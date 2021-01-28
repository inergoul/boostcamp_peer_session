class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            answer = -int(str(x)[:0:-1])        
        else:
            answer = int(str(x)[1::-1])
            
        if x > pow(2,31) or x < -pow(2,31):
            return 0
        else: 
            return answer

tmp = Solution()
print(tmp.reverse(120))
print(tmp.reverse(-321))