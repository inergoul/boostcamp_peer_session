def solution(p, s):
    # O(n) time
    date = [(100-p[i]) // s[i] if (100-p[i]) % s[i] == 0 \
        else (100-p[i]) // s[i] + 1 for i in range(len(p))]
    # 각 작업의 남은 일수 반환 함수
    cnt = 0
    time = 0 # 처음부터 누적 일수
    answer = []
    while date:
        if date[0] - time > 0: # 해당하는 작업이 기종료되었을 때
            if cnt > 0:
                answer.append(cnt)
            cnt = 0
            time += 1
        else:
            date.pop(0)
            cnt += 1
    answer.append(cnt)  # 마지막 남은 cnt 처리
    return answer