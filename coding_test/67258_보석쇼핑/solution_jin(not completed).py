def solution(gems):
    # 테스트 케이스는 통과, 효율성 만족 X
    gems_num = len(set(gems))
    
    fr_num = 0
    to_num = 0
    cnt_min = len(gems)
    
    for fr in range(len(gems)-gems_num):
        shop_gems = []
        idx = fr
        cnt = 0
        while len(shop_gems) < gems_num and idx < len(gems):
            if gems[idx] not in shop_gems:
                shop_gems.append(gems[idx])
            idx += 1
            cnt += 1
        if len(shop_gems) == gems_num and cnt < cnt_min:
            cnt_min = cnt
            fr_num = fr
            to_num = idx - 1
    
    if cnt_min == len(gems):
        fr_num = 0
        to_num = len(gems) - 1
            
    return [fr_num+1, to_num+1]

print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))