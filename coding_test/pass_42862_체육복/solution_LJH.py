def find_near(lost, reserve):
    tmp = [[] for _ in range(len(lost))]
    lost_copy = lost[:]
    reserve_copy = reserve[:]    
    zero, one = 0, 0

    for idx, l in enumerate(lost):
        if (l-1) in reserve_copy:
            tmp[idx].append(-1)
        if (l+1) in reserve:
            tmp[idx].append(1)
        
        # 빌릴 대상이 없는 경우
        if len(tmp[idx]) == 0:
            lost_copy.remove(l)
            zero += 1

        # 한명한테만 빌릴 수 있는 경우(그냥 빌림)
        elif len(tmp[idx]) == 1:
            lost_copy.remove(l)
            reserve_copy.remove(l + tmp[idx][0])
            one += 1
        # 두명(양쪽)한테 빌릴 수 있는 경우는 일단 왼쪽에서 빌려야지(왼쪽부터 서칭하니까)
        else:
            lost_copy.remove(l)
            reserve_copy.remove(l-1)
            one += 1
    return lost_copy, reserve_copy, zero, one

def solution(n, lost, reserve):
    # 중복제거
    real_lost = list(set(lost) - set(reserve))
    real_reserve = list(set(reserve) - set(lost))
    new_lost, new_reserve, zero, one = find_near(real_lost, real_reserve)
    ans = n - len(new_lost) - zero

    return ans
    
'''
n   lost    reserve   return
------------------------------
5	[2, 4]	[1, 3, 5]	5
5	[2, 4]  [3]	        4
3	[3]	    [1]	        2
'''