from numpy import array
def solution(board, moves):
    list_list = [list(filter(lambda x: x!=0,lis[::-1])) for lis in array(board).T.tolist()]
    answer = 0
    bucket = []
    for ind in moves:
        try:
            get = list_list[ind-1].pop(-1)
        except:
            pass
        else:
            if get == 0:
                pass
            elif bucket[-1:]==[get]:
                answer+=2
                bucket.pop(-1)
            else:
                bucket.append(get)
    return answer