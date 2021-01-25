def solution(answers):
    answer = [0, 0, 0]
    s1 = list(map(int, '12345'))
    s2 = list(map(int, '21232425'))
    s3 = list(map(int, '3311224455'))
    
    for idx, a in enumerate(answers):
        if s1[idx%len(s1)] == a:
            answer[0] += 1
        if s2[idx%len(s2)] == a:
            answer[1] += 1
        if s3[idx%len(s3)] == a:
            answer[2] += 1
    max_ans = max(answer)
    res = []
    
    for idx, i in enumerate(answer):
        if i == max_ans:
            res.append(idx+1)
    return res