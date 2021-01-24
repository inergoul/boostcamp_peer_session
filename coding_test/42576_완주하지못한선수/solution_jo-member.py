def solution(participant, completion):
    '''
    참가자와 완료자의 정보를 담은 list를 받아 정렬후 순서대로 비교
    만약 index값이 같지만 value값이 다르다면 그 참가자가 완주를 못한 사람이기 떄문에 return
    만약 완료자의 list를 모두 순회하였지만 모두 참가자와 같았자면 참가자 list의 마지막이 완료하지 못한 참가자
    return 제일 끝 참가자

    '''
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if completion[i]!=participant[i]:
            return participant[i]
    return participant[-1]