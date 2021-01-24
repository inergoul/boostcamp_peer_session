def solution(record):
    answer = []
    nick = {}
    log = []
    for x in record:
        s = x.split()
        if s[0] == "Enter" or s[0] == "Change":
            nick[s[1]] = s[2]
        if s[0] == "Enter" or s[0] == "Leave":
            log.append([s[0] == "Leave", s[1]])
    for l in log:
        if l[0]:
            answer.append(nick[l[1]] + "님이 나갔습니다.")
        else:
            answer.append(nick[l[1]] + "님이 들어왔습니다.")
    return answer
