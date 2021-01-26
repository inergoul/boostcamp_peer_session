def solution(record):
    answer = []
    Id_Name_dict = dict()

    for s in record:
        string_list = s.split()        
        if string_list[0] == "Enter" or string_list[0] == "Change":
            Id_Name_dict[string_list[1]] = string_list[2]

    for s in record:        
        string_list = s.split()
        if(string_list[0] == "Enter"):
            Id = string_list[1]
            answer.append(f"{Id_Name_dict[Id]}님이 들어왔습니다.")
        elif(string_list[0] == "Leave"):
            Id = string_list[1]
            answer.append(f"{Id_Name_dict[Id]}님이 나갔습니다.")
    return answer