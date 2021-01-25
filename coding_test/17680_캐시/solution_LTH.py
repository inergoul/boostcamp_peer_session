def solution(cacheSize, cities):
    cities = map(lambda x:x.lower(), cities)
    cache = []
    answer = 0
    for city in cities:
        if city in cache:
            answer += 1
            cache.pop(cache.index(city))
            cache.append(city)
        else:
            answer += 5
            cache.append(city)
        if len(cache) > cacheSize:
            cache.pop(0)
    return answer