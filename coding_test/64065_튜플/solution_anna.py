def solution(s):
    answer = []
    arrays = []
    arr = []
    si = 1
    for i in range(1, len(s) - 1):
        if s[i] == '{':
            si = i
        if s[i] == '}':
            arr.append(s[si + 1:i])
    for a in arr:
        arrays.append([int(num) for num in a.split(',')])
    arrays.sort(key = len)
    for i in arrays:
        for j in i:
            if j not in answer:
                answer.append(j)
    return answer
