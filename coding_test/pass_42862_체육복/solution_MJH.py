def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    common = lost&reserve
    lost = list(lost-common)
    reserve = list(reserve-common)

    for i in lost[:]:
        if i+1 in reserve and i-1 not in reserve:
            lost.remove(i)
            reserve.remove(i+1)
    for i in lost[:]:
        if i-1 in reserve and i+1 not in reserve:
            lost.remove(i)
            reserve.remove(i-1)

    if len(lost) > 0:
        print(lost)
        for i in lost[:]:
            if i+1 in reserve:
                lost.remove(i)
                reserve.remove(i+1)
        for i in lost[:]:
            if i-1 in reserve:
                lost.remove(i)
                reserve.remove(i-1)
    answer = n-len(lost)
    return answer
