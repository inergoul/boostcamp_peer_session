def solution(p):

    if p == '':
        return ''
    is_right = True # 올바른 괄호 문자열인가
    if p[0] == ')':
        is_right = False
    num_left = 0 # '(' 개수
    num_right = 0 # ')' 개수
    idx = 0
    for sign in p:
        idx += 1
        if sign == '(':
            num_left += 1
        else:
            num_right += 1
        if num_left == num_right:
            break
    if is_right:            
        return p[:idx] + solution(p[idx:])
    else:
        return '('+ solution(p[idx:]) + ')' + ''.join([')' if x == '(' else '(' for x in p[1:(idx-1)]])