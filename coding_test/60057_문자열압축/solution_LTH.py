from collections import deque
def solution(s):
    answer = 1000
    for i in range(1, len(s) // 2 + 1):
        new_str = deque(s[j:j + i] for j in range(0, len(s), i))
        text = ''
        prev, cnt = new_str[0], 0
        while new_str:
            cur = new_str.popleft()
            if prev == cur:
                cnt += 1
            else:
                text += str(cnt) + prev if cnt != 1 else prev
                prev = cur
                cnt = 1
        text += str(cnt) + prev if cnt != 1 else prev
        answer = min(answer, len(text))
    return answer if answer != 1000 else 1