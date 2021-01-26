from collections import deque
def solution(pb):
    '''
    전화번호 목록을 sort해준뒤 deque로 만들어준다.
    이후 dq의 길이가 1이 되기 전까지
    popleft를하여 길이가 짧은 순으로 문자열을 뽑아낸다음 남은 dq를 순회하며 뽑아낸 문자열이 남은 dq에 있는지 확인
    1개가 남을때 까지 popleft하였는데 없을때는 True를 return
    pop한 
    '''

    pb.sort()
    dq = deque(pb)
    while len(dq)!=1:
        w = dq.popleft()
        for num in dq:
            if w in num:
                return False
    return True