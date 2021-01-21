'''
numbers = [1, 1, 1, 1, 1]
target = 3
return = 5
'''

# num_length = len(numbers)
# tmp = [0 for _ in range(len(numbers))]

# # 비트연산자를 활용한 부분집합 만들기
# for i in range(1 << len(numbers)):
#     for j in range(len(numbers)):
#         if i & (1 << j):
#             tmp[j] = 1
#     print(tmp)
#     tmp = [0 for _ in range(len(numbers))]


def solution(numbers, target):
    tmp = 0
    answer = 0

    # 부분집합 생성
    # [0, 0, 0, 0, 0] 부터 [1, 1, 1, 1, 1] 까지 반복해서 만든다.
    
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

# 굳이 dfs, bfs로 풀기 싫은데...?
numbers = [1, 1, 1, 1, 1]
target = 3

ans = solution(numbers, target)
print(ans)
