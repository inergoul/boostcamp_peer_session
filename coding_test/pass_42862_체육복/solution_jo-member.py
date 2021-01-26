def solution(n, lost, reserve):
    result=0
    clo_count = [1]*n
    for i in lost:
        clo_count[i-1]-=1
    for j in reserve:
        clo_count[j-1]+=1
    print(clo_count)
    for i in range(len(clo_count)):
        if (clo_count[i]==0 and i!=0 and i!=len(clo_count)-1) and (clo_count[i+1]==2 or clo_count[i-1]==2):
            x=clo_count.index(2)
            clo_count[x]-=1
            clo_count[i]+=1
        elif i==0 and clo_count[1]==2:
            clo_count[0]=1
            clo_count[1]=1
        elif i==len(clo_count) and clo_count[i-1]==2:
            clo_count[i]=1
            clo_count[i-1]=1
    result+=clo_count.count(1)
    result+=clo_count.count(2)
    return result