from collections import defaultdict

def solution(gems):
    answer = [0, len(gems) + 1]
    kind = len(list(set(gems)))
    freq = defaultdict(int)
    l = 0
    r = 0
    freq[gems[r]] += 1
    while l < len(gems) and r < len(gems):
        if len(freq) == kind:
            if (answer[1] - answer[0]) > (r - l):
                answer[1] = r + 1
                answer[0] = l + 1
            freq[gems[l]] -= 1
            if freq[gems[l]] == 0:
                freq.pop(gems[l])
            l += 1
            r = max(l, r)
        else:
            r += 1
            if r < len(gems):
                freq[gems[r]] += 1
    return answer
