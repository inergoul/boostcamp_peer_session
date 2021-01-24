from collections import Counter
def solution(s):
    new_s = [sss.replace('{','').replace('}','') for sss in s.split(',')]
    return [int(c[0]) for c in sorted(Counter(new_s).items(), key = lambda x: x[1],reverse=True )]