from collections import Counter
def solution(participant, completion):
    participant = Counter(participant)
    completion = Counter(completion)
    ans = participant - completion
    return list(ans.keys())[0]