from math import ceil
def solution(progresses, speeds):
    remain = [ceil((100 - progress) / speed) for progress, speed in zip(progresses, speeds)]
    ans = []
    prev = remain[0]
    cnt = 0
    for i in remain:
        if i <= prev:
            cnt += 1
        else:
            ans.append(cnt)
            cnt = 1
            prev = i
    ans.append(cnt)
    return ans