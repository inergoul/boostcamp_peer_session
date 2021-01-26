def solution(n, lost, reserve):
    answer = n
    students = [1] * (n + 1)
    for l in lost:
        students[l] = 0
    for r in reserve:
        students[r] += 1
    for i in range(1, n + 1):
        if students[i] == 0:
            if students[i - 1] > 1:
                students[i - 1] -= 1
                students[i] += 1
            elif i < n and students[i + 1] > 1:
                students[i + 1] -= 1
                students[i] += 1
            else:
                answer -= 1
    return answer
