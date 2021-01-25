def solution(cacheSize, cities):
    answer = 0
    page = list()

    if not cacheSize: return len(cities) * 5
    for c in cities:
        Large_c = c.upper()
        if Large_c in page:
            idx = page.index(Large_c)
            page.pop(idx)
            page.append(Large_c)
            answer += 1
        else:
            if len(page)==cacheSize:
                page.pop(0)
                
            page.append(Large_c)
            answer += 5

    return answer