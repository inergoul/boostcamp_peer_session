def solution(n, lost, reserve):
    students = [0] + [1] * n
    for i in lost:
        students[i] -= 1
    for i in reserve:
        students[i] += 1
    for i in range(1, n):
        if students[i] == 0 and students[i + 1] == 2:
            students[i] += 1
            students[i + 1] -= 1
        elif students[i] == 2 and students[i + 1] == 0:
            students[i] -= 1
            students[i + 1] += 1
    return sum([1 for i in students if i > 0])