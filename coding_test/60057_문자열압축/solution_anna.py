def solution(s):
    answer = len(s)
    for ss in range(1, len(s) // 2 + 1):
        words = [s[si:si + ss] for si in range(0, len(s), ss)]
        compress = 0
        cnt = 0
        bef = ""
        for w in words:
            if bef != w :
                compress += (len(str(cnt)) if cnt > 1 else 0) + len(bef)
                bef = w
                cnt = 1
            else:
                cnt += 1
        compress += (len(str(cnt)) if cnt > 1 else 0) + len(bef)
        answer = min(answer, compress)
    return answer
