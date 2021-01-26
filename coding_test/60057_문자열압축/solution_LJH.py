def solution(s):
    res = 999
    if len(s)//2 + 1 == 1:
        return len(s)

    for step in range(1, len(s)//2 +1):
        ans = ''
        idx = 0
        cnt = 1
        cur = 1
        while cur:
            cur = s[idx:idx+step]
            compare = s[idx+step:idx+step*2]        
            # 같은 경우
            if cur == compare:
                cnt += 1
                idx += step

            # 다를 경우
            else:
                # 남은 글씨만처리
                if len(cur) < step:
                    ans += cur
                # 그 외
                elif cnt == 1:
                    ans += cur
                else:
                    ans += str(cnt) + cur
                    cnt = 1
                idx += step
        if len(ans) < res:
            res = len(ans)
    return res