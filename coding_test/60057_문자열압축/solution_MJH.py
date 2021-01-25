def zzz(s,i):
    new_s, reduce,length =  '', 1, len(s)
    while s:
        if s[:i] == s[i:2*i]:
            reduce += 1
        else:
            if reduce==1:
                new_s += s[:i]
            else:
                new_s += f'{reduce}'+s[:i]
            reduce=1
        s = s[i:]
    return len(new_s)

def solution(s):
    if len(s)==1:
        return len(s)
    else:
        return min([zzz(s,i) for i in range( 1, int(len(s)//2)+1 )])