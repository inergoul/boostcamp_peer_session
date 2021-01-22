def solution(array, commands):
    answer = []
    for c in commands:
        start, end, find = c
        tmp = sorted(array[(start-1):end])[find-1]
        answer.append(tmp)
    return answer