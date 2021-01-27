def solution(name):
    n = len(name)
    answer = idx = 0
    remain = [1 if 'A' == name[i] else 0 for i in range(n)]
    
    while 1:
        left = right = 1
        answer += min(ord(name[idx]) - ord('A'), ord('A') + 26 - ord(name[idx])) # ord: 아스키코드 변환
        remain[idx] = 1 # 완료된 문자는 1로 변경
        
        while remain[idx - left if idx >= left else idx + n - left]:
            left += 1
            if left >= n: # 자기 자신으로 돌아오면 반환(더 이상 바꿀게 없는 경우)
                return answer
            
        while remain[idx + right if idx < n - right else idx - n + right]:
            right += 1
            
        if left < right:
            idx = idx - left if idx >= left else idx + n - left
        else:
            idx = idx + right if idx < n - right else idx - n + right
            
        answer += min(left, right)