from collections import deque

def non_zero(deque):
    while deque:
        tmp = deque.popleft()
        if tmp:
            deque.appendleft(tmp)
            break
    return deque

def solution(board, moves):
    # 회전시켜서 생각하면 편함
    rotate_board = []
    
    for i in zip(*board):
        rotate_board.append(deque(i))
    
    rotate_board_non_zero = list(map(non_zero, rotate_board))
    # moves순서대로 왼쪽부터 뽑으면 됨.
    cnt = 0
    stack = [0]
    for m in moves:
        current_board = rotate_board_non_zero[m-1]
        if current_board:
            tmp = current_board.popleft()
            if stack[-1] == tmp:
                stack.pop()
                cnt += 1
            else:
                stack.append(tmp)
                        
    return cnt * 2