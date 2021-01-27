from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen=cacheSize)
    cities = list(map(lambda x:x.lower(), cities))

    for city in cities:
        if city in cache:
            cache.remove(city)
            answer += 1
        else:
            answer += 5
        cache.append(city)
    return answer