from collections import deque

def solution(name):
    dq = deque()
    dq.append([(["A"] * len(name)), 0, 0])
    while dq:
        s, m, i = dq.popleft()
        m += min(abs(ord(name[i]) - ord(s[i])), (26 - (max(ord(name[i]), ord(s[i])) - 97) + (min(ord(name[i]), ord(s[i])) - 97)))
        ns = s[:]
        ns[i] = name[i]
        if ''.join(ns) == name:
            return m
        dq.append([ns, m + 1, (i + 1) % len(name)])
        dq.append([ns, m + 1, (len(name) - 1 if i == 0 else i - 1)])
    return -1
