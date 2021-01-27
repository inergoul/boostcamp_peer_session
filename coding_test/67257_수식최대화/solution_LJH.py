from itertools import permutations
def calc(priority, n, expression):
    if n == 2:
        return str(eval(expression))
    if priority[n] == '*':
        res = eval('*'.join([calc(priority, n + 1, e) for e in expression.split('*')]))
    if priority[n] == '+':
        res = eval('+'.join([calc(priority, n + 1, e) for e in expression.split('+')]))
    if priority[n] == '-':
        res = eval('-'.join([calc(priority, n + 1, e) for e in expression.split('-')]))
    
    return str(res)

def solution(expression):
    answer = 0
    # 6가지 우선순위 조합 생성
    priority_list = (list(permutations(['*','-','+'], 3))) 
    print(priority_list)
    for priority in priority_list:
        res = int(calc(priority, 0, expression))
        answer = max(answer, abs(res))

    return answer