from itertools import permutations
import re

def oper(a,b,o):
    if o=='+':
        return a+b
    elif o=='-':
        return a-b
    else: return a*b
    

def solution(expression):
    answer = []
    #정규식을 사용할수도 있지만 아직 익숙치 않아서 다시 일단 이렇게 구현했지만 정규식으로 바꿔볼 예정이다
    l = []
    tmp = ''
    
    for i in expression+' ':
        if i in '1234567890':
            tmp+=i
        else:
            l.append(int(tmp))
            tmp = ''
            l.append(i)
    l = l[:-1]
    p = list(permutations('-+*',3))
    
    for a,b,c in p:
        cpy = l[:]
        if a in cpy:
            while a in cpy:
                i = cpy.index(a)
                tmp = oper(cpy[i-1],cpy[i+1],a)
                cpy = cpy[:i-1]+[tmp]+cpy[i+2:]
                
        if b in cpy:
            while b in cpy:
                i = cpy.index(b)
                tmp = oper(cpy[i-1],cpy[i+1],b)
                cpy = cpy[:i-1]+[tmp]+cpy[i+2:]
                
        if c in cpy:
            while c in cpy:
                i = cpy.index(c)
                tmp = oper(cpy[i-1],cpy[i+1],c)
                cpy = cpy[:i-1]+[tmp]+cpy[i+2:]
                
        answer.append(abs(cpy[0]))
    return max(answer)