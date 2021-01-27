def solution(name):

    diff_list = [] # 각 문자에서 상하 횟수 저장
    for cha in name:
        diff = ord(cha) - ord("A")
        diff_list.append(min(diff, 26-diff)) # 짧은 방향
    
    answer = 0
    cur = 0
    while True:
        answer += diff_list[cur]
        diff_list[cur] = 0
        if sum(diff_list) == 0:
            break
        ml = 0 # 커서 기준 왼쪽으로 가는 거리
        mr = 0 # 커서 기준 오른쪽으로 가는 거리
        while True:
            ml += 1
            if diff_list[cur - ml] != 0:
                break
        while True:
            mr += 1
            if cur + mr >= len(diff_list):
                if diff_list[cur + mr - len(diff_list)] != 0:
                    break
            else:
                if diff_list[cur + mr] != 0:
                    break
        if ml < mr: # A아닌 다른 문자가 더 빨리 나오는 쪽으로 이동
            answer += ml
            cur -= ml
        else:
            answer += mr
            cur += mr

    return answer

