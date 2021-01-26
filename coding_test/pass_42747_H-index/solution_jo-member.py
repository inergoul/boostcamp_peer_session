def solution(citations):
    x = sorted(citations, reverse = True)
    h=[]
    if x[0]==0:
        return 0
    else:
        for i in range(x[0]):
            for j in range(len(x)):
                if i<=x[j]:
                    if i<=j+1:
                        h.append(i)
    answer = max(h)
    return answer