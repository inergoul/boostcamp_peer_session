def solution(citations):
    citations.sort(reverse=True)    # 조건을 만족하는 수중 최대값이므로 내림차순
    ptr = 0  # citation 의 index
    num = citations[ptr] # h-index 후보
    while num >= 0:
        if (ptr + 1) >= num:
            return num
        elif ptr == len(citations) - 1:
            num -= 1
        else:
            if citations[ptr+1] == citations[ptr]:
                ptr += 1
            else:
                num -= 1
                citations[ptr] = num
    return num