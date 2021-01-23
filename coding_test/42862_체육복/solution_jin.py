def solution(n, lost, reserve):
    clo_num = [1] * n # 각 학생이 가진 체육복의 수를 저장하는 리스트
    # 도난당한 학생은 -1, 여벌 있는 학생은 +1
    for stu_num in lost:
        clo_num[stu_num - 1] -= 1
    for stu_num in reserve:
        clo_num[stu_num - 1] += 1
    # 뒤에 친구가 앞으로 전달
    for i in range(n-1):
        if clo_num[i] == 0 and clo_num[i+1] == 2:
            clo_num[i] = clo_num[i+1] = 1
    # 앞에 친구가 뒤로 전달
    for i in range(1, n):
        if clo_num[i] == 0 and clo_num[i-1] == 2:
            clo_num[i] = clo_num[i-1] = 1
    return n - clo_num.count(0)