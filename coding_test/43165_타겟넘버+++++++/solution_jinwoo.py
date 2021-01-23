from collections import deque

def solution(numbers, target):
    # time : O(2^N) 완전탐색
    num_que = deque(numbers)
    waynum = dict()
    # key : num, value : num 까지 가기위한 방법의 수 dict 만듬
    waynum[0] = 1

    while num_que:
        num = num_que.popleft()
        # numbers에서 왼쪽 숫자를 하나 연산할 때마다 waynum에 해당하는 dict를 만듬
        temp_dict = dict()
        for key in waynum.keys():
            if (key + num) not in temp_dict.keys():
                temp_dict[key + num] = waynum[key]
            else:
                temp_dict[key + num] += waynum[key]
            if (key - num) not in temp_dict.keys():
                temp_dict[key - num] = waynum[key]
            else:
                temp_dict[key - num] += waynum[key]
        waynum = temp_dict

    return waynum[target]