
## 2번 # 32ms, 14.4MB
class Solution:
    def reverse(self, x: int) -> int:
        if str(x).startswith('-'):
            result=-int(''.join(reversed(list(str(-x)))))
        else:
            result=int(''.join(reversed(list(str(x)))))
        
        if -2**31<=result<=2**31:
            return result
        else:
            return 0
        
'''
## 3번 # 32ms, 14.4MB
class Solution:
    def reverse(self, x: int) -> int:
        result=''
        x=str(x)
        for i in range(len(x)-1,-1,-1):
            if x[i].isdigit():
                result += x[i]
        result=int(result)
        
        if -2**31<=result<=2**31:
            
            if x.startswith('-'):
                return (-1)*result
            else:
                return result
        else:
            return 0
        
'''

'''
## 4번 # 52ms, 14.2MB
class Solution:
    def reverse(self, x: int) -> int:
        if str(x).startswith('-'):
            
            result=-int(str(-x)[::-1])
        else:
            result=int(str(x)[::-1])
            
        if -2**31<=result<=2**31:
            return result
        else:
            return 0
        '''

