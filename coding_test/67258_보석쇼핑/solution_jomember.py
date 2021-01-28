def solution(gems):
    '''
    단순히 list를 순회해서는 효율성을 통과 못하는것 같습니다...
    dict를 사용하면 될거 같긴한데.. 모르겠네요 ㅠㅠ
    '''
    gem = set(gems)
    answer = []
    for i in range(len(gems)-1):
        for j in range(i,len(gems)):
            bag = set(gems[i:j+1])
            if len(gem-bag)==0:
                answer.append([i+1,j+1])
    a = sorted(answer,key = lambda x: (x[1]-x[0],x[0]))
    return a[0]