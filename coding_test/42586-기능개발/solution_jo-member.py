def solution(progresses, speeds):
    '''
    
    '''
    t,answer,d_stack = [], [], []
    c=0
    x = list(map(lambda x,y :[x,y],progresses,speeds ))
    for i in x:
        time = 0
        while i[0]<100:
            i[0]+=i[1]
            time +=1
        t.append(time)
    print(t)
    for i in t:
        b=0
        if len(d_stack)==0:
            d_stack.append(i)
        elif i>max(d_stack):
            while len(d_stack)!=0:
                d_stack.pop()
                b+=1
            answer.append(b)
            d_stack.append(i)
        elif i<=max(d_stack):
            d_stack.append(i)
    while len(d_stack)!=0:
        d_stack.pop()
        c += 1
    answer.append(c)
        
    return answer