def solution(citations):
    sorted_citations = sorted(citations, reverse=True)
    length = len(citations)
    answer = 0

    for idx, h in enumerate(sorted_citations):
        if h >= idx+1 :
            answer = min(h, idx+1)
        else:
            break
    return answer