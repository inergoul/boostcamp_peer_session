def solution(record):
    # 1) user_id 별로 nick_name dict 생성
    # 2) Enter / Leave / Change 세 가지 명령어가 존재
    # 3) 각 uid, 명령어에 맞게 출력list 생성 후 출력
    entrance_records = []
    user_nickname_dict = dict()
    for r in record:
        tmp = r.split()
        oper = tmp[0]
        uid = tmp[1]
        if oper != 'Leave':
            nick_name = tmp[2]
            user_nickname_dict[uid] = nick_name
        if oper != 'Change':
            entrance_records.append((oper, uid))

    answer = []
    for op, uid in entrance_records:
        tmp = ''
        if op == 'Leave':
            tmp += user_nickname_dict[uid]+"님이 나갔습니다."
        elif op == 'Enter' :
            tmp += user_nickname_dict[uid]+"님이 들어왔습니다."
        answer.append(tmp)
    
    return answer