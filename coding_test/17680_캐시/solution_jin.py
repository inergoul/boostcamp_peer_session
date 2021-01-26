from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache_que = deque(maxlen=cacheSize)
    city_que = deque([x.lower() for x in cities]) # 대소문자 구분 안하므로
    while city_que:
        city = city_que.popleft()
        if city in cache_que:
            cache_que.remove(city)
            answer += 1
        else:
            answer += 5
        cache_que.append(city)
        # 최대 크기가 고정되면 알아서 넘치면 popleft() 실행됨
    return answer