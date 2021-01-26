def solution(citations):
    answer = 0
    h = 1;
    citations.sort(reverse=True)
    citations = [0] + citations
    while h < len(citations) and citations[h] != 0:
        if citations[h] >= h:
            answer = h;
        h += 1;
    return answer
