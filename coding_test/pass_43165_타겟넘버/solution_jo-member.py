from collections import deque
def solution(numbers, target):
    answer = 0
    d = deque()
    d.append([0,0])
    while d:
        [num,i] = d.popleft()
        if len(numbers)==i:
            if num==target:
                answer+=1
        else:
            n = numbers[i]
            d.append([num+n,i+1])
            d.append([num-n,i+1])
    return answer