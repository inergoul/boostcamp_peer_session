def solution(s):
    answer = []

    s_list = s[2:-2].split("},{")
    ordered_s = sorted(s_list, key=len)

    ordered_list = [x.split(",") for x in ordered_s]

    for i in range(len(ordered_list)):
        for j in range(i+1):
            if int(ordered_list[i][j]) not in answer:
                answer.append(int(ordered_list[i][j]))

    return answer

print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))