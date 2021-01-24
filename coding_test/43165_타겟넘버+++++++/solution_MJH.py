from itertools import combinations
def solution(numbers, target):
    answer = 0
    summation = sum(numbers)
    for i in range(1,len(numbers)+1):   # 마이너스가 i개일때
        for j in list(combinations(numbers,i)):
            if target == summation - sum(j)*2:
                answer += 1
    return answer