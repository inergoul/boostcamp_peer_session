def solution(numbers, target):
    answer = 0
    stack = [[numbers[0],0], [-numbers[0],0]]
    
    while(len(stack)!=0):
        num, idx = stack.pop()
        if idx == len(numbers)-1 and num == target: answer+=1
        idx += 1
        if idx == len(numbers) : continue
        stack.append([num+numbers[idx], idx])
        stack.append([num-numbers[idx], idx])
    return answer