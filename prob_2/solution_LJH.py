def solution(numbers, target):
    tmp = 0
    answer = 0

    # 부분집합 생성
    for i in range(1 << len(numbers)):
        for j in range(len(numbers)):
            if i & (1 << j):
                tmp += numbers[j]
            else:
                tmp -= numbers[j]
        if tmp == target:
            answer += 1
        tmp = 0
    return answer