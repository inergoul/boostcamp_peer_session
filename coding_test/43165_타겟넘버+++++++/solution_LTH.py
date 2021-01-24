def solution(numbers, target):
    return dfs(numbers, target, 0)

def dfs(numbers, target, value):
    cnt = 0
    if not numbers:
        return value == target
    cand = (-1, 1)
    for i in cand:
        cnt += dfs(numbers[1:], target, value + numbers[0] * i)
    return cnt