from collections import deque
def solution(s):
    answer = []
    for i in range(1,len(s)//2+2):
        l = [s[j:j+i] for j in range(0,len(s),i)]
        d = deque()
        temp = ''
        for x in l:
            if x in d:
                d.append(x)
            else:
                if len(d):
                    cnt = 0
                    while d:
                        y = d.popleft()
                        cnt+=1
                    if cnt ==1:
                        temp+=y
                    else:
                        temp +=str(cnt)+y
                    d.append(x)
                else:
                    d.append(x)
        cnt = 0
        while d:
            y = d.popleft()
            cnt+=1
        if cnt ==1:
            temp+=y
        else:
            temp +=str(cnt)+y
        answer.append(len(temp))
    return min(answer)