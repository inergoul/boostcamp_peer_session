class Solution(object):
    def reverse(self, x):
       is_minus=True if x<0 else False
       
       x_to_string=str(abs(x))
       
       reverse_string=x_to_string[::-1]
       if is_minus == True:
           reverse_string='-'+reverse_string
       answer = int(reverse_string)
    
       if answer>=pow(2,31) or answer<-pow(2,31):
          return 0

       return answer