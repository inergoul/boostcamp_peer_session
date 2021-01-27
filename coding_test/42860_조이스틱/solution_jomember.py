def solution(name):
    d = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    idx = []
    for letter in name:
        i = d.index(letter)
        if i>len(d)//2:
            idx.append(len(d)-i)
        else:
            idx.append(i)
    i = 0
    answer = 0
    while 1:
        answer+=idx[i]
        idx[i]=0
        if sum(idx)==0:
            return answer
        l,r = 1,1
        while idx[i-l]==0:
            l+=1
        while idx[i+r]==0:
            r+=1
        answer +=l if l<r else r
        i+= -l if l<r else r