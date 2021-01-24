from collections import deque

def solution(board, moves):

    move_que = deque(moves)
    doll_stack = []
    board_len = len(board)
    answer = 0

    while move_que:
        move = move_que.popleft()
        doll = 0
        for i in range(board_len):
            if board[i][move-1] != 0:
                doll = board[i][move-1]
                board[i][move-1] = 0
                break
        if doll:
            if len(doll_stack) == 0 or doll_stack[-1] != doll:
                doll_stack.append(doll)
            else:
                doll_stack.pop()
                answer += 2
    return answer