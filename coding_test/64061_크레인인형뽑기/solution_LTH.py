def solution(board, moves):
    board = [[j for j in i if j] for i in map(list, zip(*board[::-1]))]
    stack = []
    cnt = 0
    for i in moves:
        if board[i - 1]:
            stack.append(board[i - 1].pop())
        while len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            cnt += 2
    return cnt