from collections import deque

def solution(progresses, speeds):
    answer = []
    dq = deque()
    for p, s in zip(progresses, speeds):
        dq.append(((100 - p) // s) + (((100 - p) % s) > 0))
    done = dq.popleft()
    cnt = 1;
    while dq:
        cur = dq.popleft()
        if done >= cur:
            cnt += 1
        else:
            answer.append(cnt)
            done = cur
            cnt = 1
    answer.append(cnt)
    return answer
