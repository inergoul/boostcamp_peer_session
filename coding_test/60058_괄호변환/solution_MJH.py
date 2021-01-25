def alright(u):
    l,r=0,0
    for i in u:
        if i=='(':
            l+=1
        else:
            r+=1
        if r>l:
            return False
    return True

def solution(p):
    if alright(p):
        return p
    else:
        p = list(p)
        l,r = 0,0
        u=''
        while p:
            if p[0]=='(':
                l+=1
            else:
                r+=1
            u += p.pop(0)
            if l==r:
                break
        v = ''.join(p)
        if alright(u):
            return u+solution(v)
        else:
            answer = '(' + solution(v) + ')'
            for y in u[1:-1]:
                if y == '(':
                    answer+=')'
                else:
                    answer+='('
            return answer