def least_move(str1):
    mydict = {j:i for i,j in enumerate(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))}
    N = mydict[str1]
    return min(N,26-N)

def solution(name):
    mylist = [least_move(str1) for str1 in name]
    ### 방법2 : 좌우 중 0이 아닌 것에 가까운 곳으로 방향을 정하는 방법 ###
    idx2,move2,list2 = 0, 0, mylist[:]
    while True:
        list2[idx2]=0
        if all(map(lambda x: x==0, list2)):
            break
        right, left = idx2, idx2
        for _ in range(len(list2)):
            move2 +=1
            right +=1
            if list2[right] != 0:
                idx2=right
                break
            left -=1
            if list2[left] != 0:
                idx2=left
                break
                
    return move2+sum(mylist)