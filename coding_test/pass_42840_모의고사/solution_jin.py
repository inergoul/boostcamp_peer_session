def solution(answers):
    
    l = len(answers)
    ans_1 = [x%5 + 1 for x in range(l)]
    ans_2 = []
    for i in range(l):
        if i % 2 == 0:
            ans_2.append(2)
        elif i % 8 == 1:
            ans_2.append(1)
        elif i % 8 == 3:
            ans_2.append(3)
        elif i % 8 == 5:
            ans_2.append(4)
        else:
            ans_2.append(5)   
    ans_3 = []
    for i in range(l):
        if (i//2) % 5 == 0:
            ans_3.append(3)
        if (i//2) % 5 == 1:
            ans_3.append(1)
        if (i//2) % 5 == 2:
            ans_3.append(2)
        if (i//2) % 5 == 3:
            ans_3.append(4)
        if (i//2) % 5 == 4:
            ans_3.append(5)
            
    score_1 = 0
    score_2 = 0
    score_3 = 0
    
    for i in range(l):
        if ans_1[i] == answers[i]:
            score_1 += 1
        if ans_2[i] == answers[i]:
            score_2 += 1
        if ans_3[i] == answers[i]:
            score_3 += 1
    
    score_list = [score_1,score_2,score_3]
    max_score = max(score_list)
    
    return sorted([i+1 for i,num in enumerate(score_list) if num == max_score])