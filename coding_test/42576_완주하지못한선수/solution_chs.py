from collections import defaultdict

def solution(participant, completion):
    answer = ''

    new_list = defaultdict(lambda: 0)
    for name in participant:
        new_list[name] +=1
    
    for name in completion:
        new_list[name] -=1
    
    for key,value in new_list.items():
        if value == 1:
            answer = key
            break

    return answer