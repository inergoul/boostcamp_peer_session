def solution(s):
    
    cut_max = 0 # 줄어든 문자열의 길이의 최대값
    # num : 자르는 문자열의 단위, 최대값이 문자열 길이를 2로 나눈 몫
    for num in range(1, len(s)//2 + 1):
        string = s[num:]
        cnt = 0
        cut = 0
        unit = s[:num]
        while string:
            if unit == string[:num]:
                cnt += 1
                cut += num
                if cnt == 1:
                    cut -= 1 # 숫자가 추가되므로 줄어드는길이 -1
                if cnt == 9: # 같은 문자열 10개
                    cut -= 1
                if cnt == 99: # 같은 문자열 100개
                    cut -= 1
            else:
                cnt = 0
                unit = string[:num]
            string = string[num:]
        if cut > cut_max:
            cut_max = cut
    
    return len(s) - cut_max