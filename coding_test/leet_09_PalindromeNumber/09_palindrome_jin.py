class Solution:

    # 문자열 변환후 역순으로 뒤집은 것과 비교
    # time : 60ms // memory : 14.1MB
    def isPalindrome1(self, x):
        
        if x < 0:
            return False
        rev_x = str(x)[::-1]
        if rev_x == str(x):
            return True
        else:
            return False


    # 문자열 변환을 쓰지 않기 위해 list에 넣고 앞쪽 인덱스와 뒤쪽 인덱스 비교
    # time : 72ms // memory : 14.3MB
    def isPalindrome2(self, x):
        
        if x < 0:
            return False
        if x == 0:
            return True
        num_list = []
        while x:
            a, b = divmod(x, 10)
            num_list.append(b)
            x = a
        for i in range(len(num_list) // 2):
            if num_list[i] != num_list[-(i+1)]:
                return False
        return True

s1 = Solution()
print(s1.isPalindrome1(10))
print(s1.isPalindrome2(10))