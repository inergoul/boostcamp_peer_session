def solution(record):
    
    id_name = dict() # 최종 아이디 : 닉네임을 저장할 dict    
    for i in range(len(record)):
        action = record[i].split(" ")[0]
        user_id = record[i].split(" ")[1]
        if action == "Enter" or action == "Change":
            id_name[user_id] = record[i].split(" ")[2]

    answer = [] # 출력에 사용할 리스트
    for i in range(len(record)):
        action = record[i].split(" ")[0]
        user_id = record[i].split(" ")[1]
        if action == "Enter":
            answer.append(f'{id_name[user_id]}님이 들어왔습니다.')
        elif action == "Leave":
            answer.append(f'{id_name[user_id]}님이 나갔습니다.')
    return answer