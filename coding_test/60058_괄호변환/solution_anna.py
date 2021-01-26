def divide(s):
    for i in range(1, len(s) + 1):
        if s[:i].count('(') == s[:i].count(')'):
            return [s[:i], s[i:]]
    return [s, ""]


def right(s):
    bracket = 0
    for c in s:
        if c == ')':
            if bracket:
                bracket -= 1
            else:
                return 0
        else:
            bracket += 1
    if bracket:
        return 0
    return 1


def recursive(w, u, v):
    if not w or right(w):
        return w
    u, v = divide(w)
    if right(u):
        return u + recursive(v, "", "")
    else:
        return "(" + recursive(v, "", "") + ")" + "".join(['(' if c == ')' else ')' for c in u[1:-1]]);
    
    
def solution(p):
    return recursive(p, "", "")
