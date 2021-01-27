'''
"(()())()"	
")("	
"()))((()"
'''

# 뒤집기
def trans(p):
    tmp = ''
    for i in p:
        if i == '(':
            tmp += ')'
        else:
            tmp += '('
    return tmp

def solution(p):
    if not p:
        return p
    tmp = 0
    flag = 1

    for idx, a in enumerate(p):
        if a == '(':
            tmp += 1
        else:
            tmp -=1
            # v 조건
            if tmp < 0:
                flag = 0 

        if tmp == 0 and flag:
            u, v = p[:idx + 1], p[idx + 1:]
            return u + solution(v)

        elif tmp == 0 and not flag:
            v, u = p[:idx + 1], p[idx + 1:]
            return '(' + solution(u) + ')' + trans(v[1:-1])