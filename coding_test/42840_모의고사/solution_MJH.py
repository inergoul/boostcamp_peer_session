from itertools import cycle

def solution(answers):
    s1 = cycle([1,2,3,4,5])
    s2 = cycle([2,1,2,3,2,4,2,5])
    s3 = cycle([3,3,1,1,2,2,4,4,5,5])
    index, result1,result2,result3 = 0,0,0,0
    for i,j,k in zip(s1,s2,s3):
        if i == answers[index]:
            result1 +=1
        if j == answers[index]:
            result2 +=1
        if k == answers[index]:
            result3 +=1
        index +=1
        if index == len(answers):
            break
    result = sorted([[result1,1],[result2,2],[result3,3]], key = lambda x: x[0], reverse=True)
    maximum = result[0][0]
    myresult = []
    for score,order in result:
        if score == maximum:
            myresult.append(order)
    return myresult