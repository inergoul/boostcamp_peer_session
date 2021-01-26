def solution(array, commands):
    answer = []
    for com in commands:
        i = com[0]
        j = com[1]
        k = com[2]
        arr = sorted(array[i-1:j])
        answer.append(arr[k-1])   
    return answer