def solution(phone_book):
    sorted_pb = sorted(phone_book, key=len)
    shortest = 30
    # 가장 짧은 번호 찾기
    for idx, p_num in enumerate(sorted_pb):
        if idx == 0:
            shortest = len(p_num)
        else:
            if len(p_num) > shortest:
                break
    
    # 짧은 애들 / 나머지로 구분
    shortest_pnums = sorted_pb[:idx]
    not_shortest_pnums = sorted_pb[idx:]
    
    # 짧은애가 들어가있으면 False
    for s_pnum in shortest_pnums:
        for ns_pnum in not_shortest_pnums:
            if ns_pnum[:len(s_pnum)] == s_pnum:
                return False
            
    return True