def solution(citations):
    citations.sort(reverse = True)
    for idx, citation in enumerate(citations):
        if idx + 1 == citation:
            return citation
        elif idx + 1 > citation:
            return idx
    return len(citations)