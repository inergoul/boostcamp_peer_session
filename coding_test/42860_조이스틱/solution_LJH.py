def search(s):
    alphas = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    n = alphas.index(s)
    return min(n, 26-n)

def solution(name):
    answer = 0
    search_list = list(map(search, name))
    idx = 0
    
    # 왼쪽오른쪽 이동하는거 구해야됨
    while True:
        # 더해진 애는 더이상 조정 안해도됨
        answer += search_list[idx]
        search_list[idx] = 0
        if sum(search_list) == 0:
            break
        # 짧은방향으로 이동
        left, right = 1, 1
        while search_list[idx - left] == 0:
            left += 1
        while search_list[idx + right] == 0:
            right += 1
            
        # 진행방향 결정
        answer += left if left < right else right
        idx += -left if left < right else right
        
    return answer
    