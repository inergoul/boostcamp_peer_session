from queue import deque
def solution(progresses, speeds):
    mylist = [(100-p)//s if (100-p)%s==0 else (100-p)//s+1 for p,s in zip(progresses,speeds)]
    answer = []
    while len(mylist)>0:
        get = mylist.pop(0)
        a = 1
        if len(mylist)!=0:
            while get>=mylist[0]:
                a+=1
                mylist.pop(0)
                if len(mylist)==0:
                    break
        answer.append(a)
    return answer