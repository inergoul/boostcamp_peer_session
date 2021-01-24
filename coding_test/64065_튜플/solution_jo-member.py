def solution(s):
    ans = []
    a = s.strip('{}').split('},{')
    for i in range(len(a)):
        if len(a[i])==1:
            a[i] = [int(a[i])]
        else:
            a[i] = list(map(int,a[i].split(',')))
    a = sorted(a,key = lambda x : len(x))
    ans.append(a[0][0])
    for i in range(len(a)-1):
        ans.append(list(set(a[i+1])-set(a[i]))[0])
    print(ans)
    return ans