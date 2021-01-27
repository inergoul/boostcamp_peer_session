from collections import defaultdict
def solution(gems):
    n = len(set(gems)) # 보석들의 종류
    bag = defaultdict(int) # 보석을 담는 가방
    answer = [len(gems), 1, len(gems)] # 최악의 경우(모든 보석이 다 다를 때) [보석수, 시작 idx, 끝 idx]
    start = 0
    for idx, gem in enumerate(gems):
        if len(bag) != n:
            bag[gem] += 1
        while len(bag) == n:
            if answer[0] > idx - start + 1: # 원래 가방에 담긴 보석 수보다 작을 때
                answer = [idx - start + 1, start + 1, idx + 1]
            bag[gems[start]] -= 1
            if not bag[gems[start]]:
                del bag[gems[start]]
            start += 1
    return answer[1:]