def solution(citations):
    for h in range(min(len(citations),max(citations)), -1, -1):
        larger_h = [j for j in citations if j>=h]
        if len(larger_h)>=h and all(m<=h for m in [k for k in citations if k not in larger_h]):
            break
    return h