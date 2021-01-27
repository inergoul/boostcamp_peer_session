## 효율성 실패한 코드입니다

def solution(gems):
    need = set(gems)
    answer_list = []
    for ind in range(len(gems)):
        ind_list = []
        gem_set = set()
        for i in range(ind,len(gems)):
            ind_list.append(i)
            gem_set |= {gems[i]}
            if gem_set==need:
                break
        if ind==0:
            answer_list = [ind_list[0]+1,ind_list[-1]+1,ind_list[-1]-ind_list[0]]
        
        elif gem_set == need:
            length = ind_list[-1]-ind_list[0]
            if answer_list[-1]>length:
                answer_list =  [ind_list[0]+1,ind_list[-1]+1,length]
    return answer_list[0:2]