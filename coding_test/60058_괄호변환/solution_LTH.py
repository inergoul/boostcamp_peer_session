def solution(p):
    check = {'(':1, ')':-1}
    if not p:
        return p
    cnt, flag = 0, 0
    for idx, i in enumerate(p):
        cnt += check[i]
        if cnt < 0:
            flag = 1
        if not cnt:
            break
    u, v = p[:idx + 1], p[idx + 1:]
    if not flag:
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + u[1:-1].translate(str.maketrans('()', ')('))