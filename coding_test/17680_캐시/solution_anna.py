from collections import deque

def solution(cacheSize, cities):
    answer = 0
    used = deque(maxlen = cacheSize)
    for c in cities:
        if c.upper() in used:
            used.remove(c.upper())
            answer += 1
        else:
            answer += 5
        used.append(c.upper())
                
    return answer
