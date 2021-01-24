def solution(array, commands):
    ans = []
    for i, j, k in commands:
        ans.append(sorted(array[i - 1:j])[k - 1])
    return ans