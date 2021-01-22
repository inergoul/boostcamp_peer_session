from collections import deque

def solution(numbers, target):

    num_que = deque(numbers)
    waynum = dict()
    waynum[0] = 1

    while num_que:
        num = num_que.popleft()
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
    print(waynum)

    return
