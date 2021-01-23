def dfs(numbers, target, cur, idx):
    if idx == len(numbers):
        if cur == target:
            return 1
        return 0
    return dfs(numbers, target, cur + numbers[idx], idx + 1) + dfs(numbers, target, cur - numbers[idx], idx + 1)

def solution(numbers, target):
    return dfs(numbers, target, 0, 0)