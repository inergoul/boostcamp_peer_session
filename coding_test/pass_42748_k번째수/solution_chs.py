def solution(array, commands):
    answer = []

    for (i,j,k) in commands:
        value = array[i-1:j]
        value = sorted(value)
        answer.append(value[k-1])
    return answer