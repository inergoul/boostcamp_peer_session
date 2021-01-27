import re
from itertools import permutations as p
def solution(expression):
    answer = 0
    
    # 정규표현식으로 숫자와 연산자를 list화
    expression = re.findall('[0-9]+|[-+*]', expression) 
    
    orders = ['+', '-', '*']
    for order in p(orders):
        new_expression = expression
        
        # 우선순위가 높은 순서대로 연산 반복
        for operand in order:
            stack = []
            for arg in new_expression:
                if stack and stack[-1] == operand:
                    op = stack.pop()
                    a = stack.pop()
                    stack.append(str(eval(a + op + arg)))
                else:
                    stack.append(arg)
            new_expression = stack
        answer = max(answer, abs(int(stack[0])))
    return answer