import re
from itertools import permutations
def solution(expression):
    splited_op = [x for x in expression if x in '+-*']
    perms = permutations(set(splited_op))
    splited_num = re.split('[\+\-\*]',expression)
    
    answer_list = []
    for perm in perms: # perm = [+,-,*]
        new_splited_op = splited_op.copy()
        new_splited_num = splited_num.copy()
        
        for p in perm:  # p = '+'
            while p in new_splited_op:  # p 연산기호가 남아있으면
                ind = new_splited_op.index(p)
                res = str( eval( new_splited_num[ind]+new_splited_op[ind]+new_splited_num[ind+1] ) )
                new_splited_op.pop(ind)
                new_splited_num = new_splited_num[:ind] + [res] + new_splited_num[ind+2:]
                
        answer_list.append(abs(int(new_splited_num[0])))
    return max(answer_list)