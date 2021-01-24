def solution(participant, completion):
    # 참가자와 완주자를 정렬 후 
    # 처음으로 같은 인덱스의 내용이 다르면 그 참가자 반환
    # 시간복잡도 O(NlogN) - sorted()
    par = sorted(participant)
    com = sorted(completion)
    for i in range(len(com)):
        if par[i] != com[i]:
            return par[i]
    return par[-1] # 정렬된 참가자 중 마지막이 답인 경우