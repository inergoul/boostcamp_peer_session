# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    sorted_p = sorted(participant)
    sorted_c = sorted(completion) + [0] # 길이가 다르기때문에 마지막에 맞춰줌
    answer = 0
    
    for p, c in zip(sorted_p, sorted_c):
        if p != c:
            answer = p
            break
            
    return answer