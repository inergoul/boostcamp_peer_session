from collections import deque
def split_str_idx(p):
    cnt1 = 0
    cnt2 = 0
    for i in range(len(p)):
        if p[i] =='(': cnt1+=1
        else: cnt2+=1
        if cnt1==cnt2:
            return i

def is_paired(p):
    stk = deque()
    for s in p:
        if s=='(':
            stk.append('(')
        else:
            if len(stk)!=0 and stk.popleft()=='(':
                continue
            else:
                return False
    if len(stk)!=0:
        return False
    else: return True          
    
def solution(p):
    answer = ''
    if p=='':
        return p
    idx = split_str_idx(p)
    u = p[:idx+1]
    v = p[idx+1:]
    if is_paired(u):
        answer = u+solution(v)
    else:
        answer+='('
        answer+=solution(v)
        answer+=')'
        u = u[1:-1]
        s = ''
        for i in u:
            if i=="(":
                s+=')'
            else:
                s+='('
        answer+=s
    return answer