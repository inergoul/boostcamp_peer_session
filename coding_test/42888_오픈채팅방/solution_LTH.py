from collections import defaultdict
def solution(record):
    new_record = []
    answer = []
    uid = dict()
    check = defaultdict(int)
    for message in record:
        message = message.split()
        if len(message) == 3:
            uid[message[1]] = message[2]
        if message[0] in {'Enter', 'Leave'}:
            new_record.append(message[1])
    for user in new_record:
        if check[user] == 0:
            answer.append(f'{uid[user]}님이 들어왔습니다.')
            check[user] += 1
        else:
            check[user] -= 1
            answer.append(f'{uid[user]}님이 나갔습니다.')
    return answer