class Solution:

    # time 52ms / memory 14.3MB
    def reverse1(self, x):
        is_minus = False
        if x == 0:
            return 0
        elif x < 0:
            is_minus = True
            x = -x
        num_list = []
        while x:
            a, b = divmod(x, 10)
            num_list.append(str(b))
            x = a
        num_str = "".join(num_list)
        if is_minus:
            num_str = "-" + num_str
        result = int(num_str)
        if abs(result) > pow(2,31):
            return 0
        return result


    # time 40ms / memory 14.1MB
    def reverse2(self, x):
        num_str = str(x)[::-1]
        if num_str[-1] == "-":
            num_str = "-" + num_str[:-1]            
        result = int(num_str)
        if abs(result) > pow(2,31):
            return 0
        return result


s1 = Solution()
# print(s1.reverse(-401))
# print(s1.reverse(0))
print(s1.reverse(1534236469))
