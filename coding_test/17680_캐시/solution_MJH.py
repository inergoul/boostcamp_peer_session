def solution(cacheSize, cities):
    if cities==[]:
        return 0
    if cacheSize==0:
        return 5*len(cities)
    cities = [c.lower() for c in cities]
    answer = 5
    ind = 1
    current_cache = cities[:ind]
    while ind<=len(cities)-1:
        if len(current_cache)<cacheSize:
            if cities[ind] in current_cache:    # cache_hit
                answer += 1
                current_cache.remove(cities[ind])
            else:   # cache_miss
                answer += 5
            current_cache.append(cities[ind])
    
        else : # 캐시허용크기인 경우 pop 혹은 remove 필수
            if cities[ind] in current_cache:    # cache_hit
                answer += 1
                current_cache.remove(cities[ind])
            else:   # cache_miss
                answer += 5
                current_cache.pop(0)
            current_cache.append(cities[ind])
        ind += 1
    return answer