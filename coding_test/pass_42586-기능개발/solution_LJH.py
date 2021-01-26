import math
from collections import deque

def solution(progresses, speeds):
    days = deque([])
    for p, s in zip(progresses, speeds):
        day = math.ceil((100-p)/s)
        days.append(day)
    
    tmp_max = days.popleft()
    answer = [1]
    
    while days:
        tmp = days.popleft()
        if tmp > tmp_max:
            tmp_max = tmp
            answer.append(1)
        else:
            answer[-1] += 1
            
    return answer