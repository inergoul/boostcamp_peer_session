def solution(answers):
    n=len(answers)
    answer = []
    f = [1,2,3,4,5]*2000
    s = [2,1,2,3,2,4,2,5]*1250
    t = [3,3,1,1,2,2,4,4,5,5]*1000
    first,second,third= f[0:n],s[0:n],t[0:n]
    c,d,e = 0, 0, 0
    for i in range(n):
        if answers[i]==first[i]:
            c+=1
        if answers[i]==second[i]:
            d+=1
        if answers[i]==third[i]:
            e+=1
    result = [c,d,e]
    maxi = max(result)
    answer=[i+1 for i,x in enumerate(result) if x==maxi]
    answer.sort()
    return answer