def solution(answers):
    answer = []
    hit = [0] * 3
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    thr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    m = 0
    for i in range(len(answers)):
        hit[0] += (((i % 5) + 1) == answers[i]);
        hit[1] += (two[i % len(two)] == answers[i]);
        hit[2] += (thr[i % len(thr)] == answers[i]);
        m = max(hit[0], hit[1], hit[2])
    for i in range(1, 4):
        if(hit[i - 1] == m):
            answer.append(i)
    return answer
