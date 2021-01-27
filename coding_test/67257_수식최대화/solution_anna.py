from itertools import permutations
import re

def cal(op, a, b):
    if op == '*':
        return a * b
    elif op == '+':
        return a + b
    return a - b

def calculate(prior, idx, num, op):
    if idx == 2:
        ret = num[0]
        for x in num[1:]:
            ret = cal(prior[idx], ret, x)
        return abs(ret)
    v = [num[0]]
    p = []
    for i, o in enumerate(op):
        if o == prior[idx]:
            last = v[-1]
            v.pop()
            v.append(cal(o, last, num[i + 1]))
        else:
            v.append(num[i + 1])
            p.append(o)
    return calculate(prior, idx + 1, v, p)

def solution(expression):
    answer = 0
    op = [c for c in expression if (c == '*' or c == '+' or c == '-')]
    numbers = list(map(int , re.split("[*+-]", expression)))
    
    prior = ["*", "+", "-"]
    permut = permutations(prior)
    for x in permut:
        answer = max(answer, calculate(x, 0, numbers, op))
        
    return answer
