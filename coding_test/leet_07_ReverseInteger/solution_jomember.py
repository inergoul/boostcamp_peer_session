class Solution:
    def reverse(self, x: int) -> int:
        '''
        Runtime: 28 ms
        Memory Usage: 14 MB
        '''
        x = ''.join(reversed(str(x)))

        if x[-1]=='-':
            x = -int(x[:len(x)-1])
        else: x = int(x)

        if x>pow(2,31) or x<-pow(2,31):
            return 0
        else: return x