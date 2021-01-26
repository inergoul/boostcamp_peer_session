def solution(record):
    d = {}
    answer = []
    for i in record:
        l = i.split(' ')
        if l[0]=='Enter':
            d[l[1]] =l[2]
        elif l[0] =='Change':
            d[l[1]]=l[2]
    for j in record:
        l = j.split(' ')
        if l[0]=='Enter':
            answer.append(f'{d[l[1]]}님이 들어왔습니다.')
        elif l[0]=='Leave':
            answer.append(f'{d[l[1]]}님이 나갔습니다.')
    return answer